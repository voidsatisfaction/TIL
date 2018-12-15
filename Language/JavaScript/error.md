# Error

- 정의

## 정의

- 에러 오브젝트 `new Error()`
- 프로퍼티
  - `message`
    - 에러의 내용
  - `stack`
    - 메시지 + 어디서 에러가 났는지

## 서버에서의 에러 핸들링

### 에러 오브젝트

```js
export class CustomError extends Error {
  constructor(code = 'GENERIC', status = 500, ...params) {
    super(...params)

    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, CustomError)
    }

    this.code = code
    this.status = status
  }
}
```

### 라우팅

- 에러가 던져지면 하나의 라우터가 모든 에러를 처리하도록 함
  - `NODE_ENV`에 따라서 에러메시지를 보여주거나 보여주지 않거나 커스터마이징

```js
const express = require('express')
const router = express.Router()
const CustomError = require('../CustomError')

router.use(async (req, res) => {
    try {
        const route = require(`.${req.path}`)[req.method]

        try {
            const result = route(req) // We pass the request to the route function
            res.send(result) // We just send to the client what we get returned from the route function
        } catch (err) {
            /*
            This will be entered, if an error occurs inside the route function.
            */
            if (err instanceof CustomError) {
                /*
                In case the error has already been handled, we just transform the error
                to our return object.
                */

                return res.status(err.status).send({
                    error: err.code,
                    description: err.message,
                })
            } else {
                console.error(err) // For debugging reasons

                // It would be an unhandled error, here we can just return our generic error object.
                return res.status(500).send({
                    error: 'GENERIC',
                    description: 'Something went wrong. Please try again or contact support.',
                })
            }
        }
    } catch (err) {
        /*
        This will be entered, if the require fails, meaning there is either
        no file with the name of the request path or no exported function
        with the given request method.
        */
        res.status(404).send({
            error: 'NOT_FOUND',
            description: 'The resource you tried to access does not exist.',
        })
    }
})

module.exports = router
```
