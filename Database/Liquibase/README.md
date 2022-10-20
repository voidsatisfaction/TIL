# Liquibase

- 의문
- 개요
- 체크섬이 꼬일 경우

## 의문

## 개요

### Precondition

```xml
<!--
onError: precondition 통과 여부를 조사하는 동안 에러가 났을때
onFail: precondition 통과하지 못했을 경우
-->
<preConditions  onFail="WARN"> <!-- 실패했을 시, 어떤 동작을 할지(CONTINUE, HALT, MARK_RAN, WARN) -->
    <!-- 아래 두 조건이 and로 엮여있어서, 두 조건이 만족해야지만 해당 changeSet을 실행시킨다 -->
    <dbms  type="oracle"  />
    <runningAs  username="SYSTEM"  />
</preConditions>
```

- 개요
  - DB의 상태에 따라서 업데이트의 실행을 컨트롤 하기 위한 태그

## 체크섬이 꼬일 경우

```xml
<!-- from -->
<changeSet id="1" author="example">
   <addColumn tableName="my_table">
       <column name="my_column" type="INT"/>
   </addColumn>
</changeSet>

<!-- to -->
<!-- 체크섬이 변화함 -->
<!-- 에러발생 -->
<!--
Validation Failed:
 1 change sets check sum
com/example/changelog.xml::1::example was: 8:63f82d4ff1b9dfa113739b7f362bd37d but is now: 8:b4fd16a20425fe377b00d81df722d604
-->
<changeSet id="1" author="example">
   <addColumn tableName="my_table">
       <column name="my_column" type="BIGINT"/>
   </addColumn>
</changeSet>
```

체크섬 처리 예시

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
        xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
            http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.1.xsd">
    <changeSet id="0306" author="dongguri">
        <validCheckSum>8:aab6c840c52115aa6ba04ed72f9e2820</validCheckSum>
        <preConditions onFail="MARK_RAN">
            <not>
                <columnExists tableName="taxi_settlement_info" columnName="company_funds_expenditure_id"/>
            </not>
            <not>
                <columnExists tableName="tmoney_settlement_record" columnName="company_funds_expenditure_id"/>
            </not>
            <not>
                <foreignKeyConstraintExists foreignKeyTableName="taxi_settlement_info" foreignKeyName="fk_taxi_settlement_info_company_funds_expenditure" />
            </not>
            <not>
                <indexExists tableName="tmoney_settlement_record" indexName="idx_tmoney_settlement_record_12"/>
            </not>
        </preConditions>
        <addColumn tableName="taxi_settlement_info">
            <column name="company_funds_expenditure_id" afterColumn="payment_extra_type" type="VARCHAR(16)">
                <constraints
                        nullable="true"
                        foreignKeyName="fk_taxi_settlement_info_company_funds_expenditure"
                        referencedTableName="company_funds_expenditure"
                        referencedColumnNames="id"
                        deleteCascade="false"
                />
            </column>
        </addColumn>
        <addColumn tableName="tmoney_settlement_record">
            <column name="company_funds_expenditure_id" afterColumn="payment_extra_type" type="VARCHAR(16)">
                <constraints nullable="true"/>
            </column>
        </addColumn>
        <createIndex tableName="tmoney_settlement_record" indexName="idx_tmoney_settlement_record_12">
            <column name="company_funds_expenditure_id"/>
        </createIndex>
    </changeSet>
</databaseChangeLog>

```

- 체크섬
  - 개요
    - 현재 changelog vs db에서 실제로 적용된 내용, 위의 둘을 탐지하기 위해, `DATABASECHANGELOG` 테이블에 changeset을 저장함
      - changelog와 db적용된것 사이의 변경점이 있는지 파악
      - 각 changeset은 id / author/ filepath로 unique하게 구분됨
    - changeset의 내용으로 해시를 만들어서 내용이 변경되었는지 체크(md5)
      - 일부 제외
        - SQL문 내부를 제외한 whitespace, linebreaks의 수정
        - precondition의 수정
        - *context의 수정*
        - *label의 수정*
        - *validCheckSum* 세팅 추가
        - 커멘트의 수정
- 문제가 생겼을 시 대처
  - Revert and roll forward
    - 이미 문제가 생긴건 그대로 놔두고, 새로 changeSet을 파서 적용시키기
  - Valid checksum tag
    - `<validCheckSum>8:b4fd16a20425fe377b00d81df722d604</validCheckSum>`
      - 8:b4fd16a20425fe377b00d81df722d604를 알맞는 cehckSum으로 간주하자
        - 이미 DB의 DATABASECHANGELOG테이블에 존재하는 체크섬이 다른 값이어도 여기 설정한 값이 맞는거라고 설정하기
  - Manually modify
    - 직접 수정해주고, 체크섬 무시하도록 하기
