# Expression vs Statement

## Expression
- Any section of codes that **evaluates to a value.**
- Can be horizontal
- ex) 5 * 5

## Statement
- A line of codes that performs some actions
- Only vertical
- ex) `print` `assignment`

## Expression Statement
`print 5*5`

```js
// Expression bodies
  var odds = evens.map(v => v + 1);
  var nums = evens.map((v, i) => v + i);

  // Statement bodies
  nums.forEach(v => {
    if (v % 5 === 0)
      fives.push(v);
  });
```
