# Flatten의 구현

```js
Array.prototype.flatten = function() {
  return this.reduce(function(a,b){
    if(b instanceof Array) {
      return a.concat(b.flatten());
    } else  {
      return a.concat(b);
    }
    }, []);
};
```

역시 함수형 프로그래밍은 섹시하다.
