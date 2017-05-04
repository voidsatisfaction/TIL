## 구현

### Permutation

```scheme
(define (remove x lst)
  (cond
    ((null? lst) '())
    ((eq? x (car lst))(remove x (cdr lst)))
    (else (cons (car lst) (remove x (cdr lst))))))

; 길이 지정 없는 permutation
(define (permute lst)
  (cond
    ((= (length lst) 1)(list lst))
    (else (apply append (map (lambda (i) (map (lambda (j)(cons i j))
                                            (permute (remove i lst))))lst)))))

; 길이 지정이 있는 permutation
(define (permute-size size l)
  (cond
    ((= size 0) '(()))
    ((= (length l) 1) (list l))
    (else (apply append (map (lambda (i) (map (lambda (j) (cons i j))
                                              (permute-size (- size 1) (remove i l)))) l)))))
```

### Combination

```scheme
(define (combi-improved l)
  (if (null? l)
      '(())
      (append (combi-improved (cdr l)) (map (lambda (j) (cons (car l) j)) (combi-improved (cdr l))))))
```

함수형 프로그래밍의 아름다움으로 구현했다.
