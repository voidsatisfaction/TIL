# Eveluation Loop

## 의문

## 개요

- Code objects
  - 개요
    - 오브젝트 s.t AST로부터 파싱된 bytecode형태의 discrete 연산의 리스트를 포함
    - code object는 input이 있어야 실행이 가능
      - input은 local, global 변수의 형태로 받아들여짐(Value Stack에서 다뤄짐)
  - 생성되는 장소
    - `.pyc` file
    - compiler
- evaluation loop
  - 개요
    - `Stack Frame` 기반 시스템에 의하여 bytecode instruction을 실행
      - bytecode instruction == code object 인지?
      - code object를 frame object로 변환

example of stack frame

```
Traceback (most recent call last):
  File "example_stack.py", line 8, in <module> <--- Frame
    function1()
  File "example_stack.py", line 5, in function1 <--- Frame
    function2()
  File "example_stack.py", line 2, in function2 <--- Frame
    raise RuntimeError
RuntimeError
```

- stack frame
  - 개요
    - 함수 사이에 변수가 반환되는 것과 함수들이 호출되는 것을 가능하게 하는 데이터 타입
      - arguments, local variables을 포함한 상태 정보를 갖음
  - 특징
    - 다양한 runtime에서 사용되는 데이터 타입
    - 모든 함수 호출시에 생성되며, 순서대로 stacked됨

큰 그림

![](./images/ch6/evaluation_loop1.png)

*interpreter & evaluation loop & thread의 관계를 한눈에 보면 좋겠다.*

*각 스레드마다 하나의 evaluation loop가 존재하는 것인지? 그렇다면 gil이 없으면 한번에 여러 개의 evaluation loop를 돌릴 수 있다는 얘기인데?*

- 중요 개념
  - interpreter는 evaluation loop의 컨테이너
  - interpreter는 적어도 하나의 스레드를 갖음
    - 각 스레드는 thread state를 갖음
  - evaluation loop은 code object를 받아서 frame object의 시리즈로 변환함
    - frame object는 스레드와 link 되어야 함
    - frame stack에서 frame object가 실행 됨
    - 변수는 value stack에서 참조됨
  - *다수의 파이썬 스레드가 동작하는 경우, 각 thread 이벤트루프에 code object를 어떻게 보내줄 수 있는가?*
- Thread State
  - 개요
    - 스레드의 상태를 나타내는 자료구조
    - 30개 이상의 속성을 갖고 있음
  - Type
    - ID
    - linked-list s.t 다른 thread state들을 갖는
    - interpreter state s.t 해당 스레드가 생성된
    - currently executing frame
    - current recursion depth
    - exception currently being handled
    - async exception currently being handled
    - stack of exceptions
      - e.g) raise within an exception block
    - GIL counter
    - async generator counters
    - ...
- Constructing Frame Objects
  - Frame Object
    - 개요
      - **code object안에 있는 명령을 실행하기에 필요한 런타임 데이터를 포함하는 오브젝트**
        - local variables, global variables, builtin modules 등으로 이루어져 있음
        - **code object는 이미 컴파일 타임에 결정된 것들**
    - Type
      - `f_back`
        - Pointer to the previous in the stack, or NULL if first frame
      - `f_code`
        - Code Object to be executed
        - `f_code.co_code`
          - 함수의 바이트코드 바이너리
        - `f_code.co_consts`
          - 함수 내에서 사용된 상수들
        - `f_code.co_varnames`
          - 함수에서 사용된 지역변수 이름들
        - `f_code.co_names`
          - 함수내에서 사용된 전역변수 이름들
      - `f_builtins`
      - `f_globals`
      - `f_locals`
      - `f_valuestack`
        - Pointer to last local
      - `f_stacktop`
      - `f_trace`
      - `f_trace_lines`
      - `f_trace_-`
      - `opcodes`
      - `f_gen`
      - `f_lasti`
        - last instruction
      - `f_lineno`
      - `f_iblock`
      - `f_executing`
      - `f_blockstack`
      - `f_localsplus`

### Frame Object Initialization API

관련 코드는 `Python/clinic/ceval.c`에 존재함

- `PyEval_EvalCode()`
  - 개요
    - code object를 평가하기 위한 entry point
- `_PyEval_EvalCode()`
  - 개요
    - interpreter loop과 frame object의 행위에 대한 내용이 담겨있음
      - CPython 인터프리터 디자인 원칙이 담겨있음
- `_PyFrame_New_NoTrack(tstate, co, globals, locals)`
  - 개요
    - 프레임 오브젝트를 새로 생성함

```c
# Python/clinic/ceval.c

PyObject *
_PyEval_EvalCode(PyThreadState *tstate,
           PyObject *_co, PyObject *globals, PyObject *locals,
           PyObject *const *args, Py_ssize_t argcount,
           PyObject *const *kwnames, PyObject *const *kwargs,
           Py_ssize_t kwcount, int kwstep,
           PyObject *const *defs, Py_ssize_t defcount,
           PyObject *kwdefs, PyObject *closure,
           PyObject *name, PyObject *qualname)
{
  /* Create the frame */
  PyFrameObject *f = _PyFrame_New_NoTrack(tstate, co, globals, locals);
  if (f == NULL) {
      return NULL;
  }
  PyObject **fastlocals = f->f_localsplus;
  PyObject **freevars = f->f_localsplus + co->co_nlocals;

  ...

  retval = _PyEval_EvalFrame(tstate, f, 0);
}

static inline PyObject*
_PyEval_EvalFrame(PyThreadState *tstate, PyFrameObject *f, int throwflag)
{
    return tstate->interp->eval_frame(tstate, f, throwflag);
}

// 위의 interp->eval_frame(tstate, f, throwflag) 의 호출은
// 아래의 _PyEval_EvalFrameDefault() 메서드의 호출과 같음

PyObject* _Py_HOT_FUNCTION
_PyEval_EvalFrameDefault(PyThreadState *tstate, PyFrameObject *f, int throwflag)
{
  /* Start of code */

  /* push frame */
  if (_Py_EnterRecursiveCall(tstate, "")) {
      return NULL;
  }

  tstate->frame = f;

  co = f->f_code;
  names = co->co_names;
  consts = co->co_consts;
  fastlocals = f->f_localsplus;
  freevars = f->f_localsplus + co->co_nlocals;

  first_instr = (_Py_CODEUNIT *) PyBytes_AS_STRING(co->co_code);

  next_instr = first_instr;
  if (f->f_lasti >= 0) {
      assert(f->f_lasti % sizeof(_Py_CODEUNIT) == 0);
      next_instr += f->f_lasti / sizeof(_Py_CODEUNIT) + 1;
  }
  stack_pointer = f->f_valuestack + f->f_stackdepth;
  /* Set f->f_stackdepth to -1.
   * Update when returning or calling trace function.
     Having f_stackdepth <= 0 ensures that invalid
     values are not visible to the cycle GC.
     We choose -1 rather than 0 to assist debugging.
   */
  f->f_stackdepth = -1;
  f->f_state = FRAME_EXECUTING;

main_loop:
    for (;;) {
    fast_next_opcode:
        f->f_lasti = INSTR_OFFSET();

        if (PyDTrace_LINE_ENABLED())
            maybe_dtrace_line(f, &instr_lb, &instr_ub, &instr_prev);

        /* line-by-line tracing support */

        if (_Py_TracingPossible(ceval2) &&
            tstate->c_tracefunc != NULL && !tstate->tracing) {
            int err;
            /* see maybe_call_line_trace
               for expository comments */
            f->f_stackdepth = stack_pointer-f->f_valuestack;

            err = maybe_call_line_trace(tstate->c_tracefunc,
                                        tstate->c_traceobj,
                                        tstate, f,
                                        &instr_lb, &instr_ub, &instr_prev);
            /* Reload possibly changed frame fields */
            JUMPTO(f->f_lasti);
            stack_pointer = f->f_valuestack+f->f_stackdepth;
            f->f_stackdepth = -1;
            if (err)
                /* trace function raised an exception */
                goto error;
        }

        /* Extract opcode and argument */

        NEXTOPARG();
    dispatch_opcode:
        switch (opcode) {
          /* BEWARE!
             It is essential that any operation that fails must goto error
             and that all operation that succeed call [FAST_]DISPATCH() ! */

          case TARGET(NOP): {
              FAST_DISPATCH();
          }

          case TARGET(LOAD_FAST): {
              PyObject *value = GETLOCAL(oparg);
              if (value == NULL) {
                  format_exc_check_arg(tstate, PyExc_UnboundLocalError,
                                       UNBOUNDLOCAL_ERROR_MSG,
                                       PyTuple_GetItem(co->co_varnames, oparg));
                  goto error;
              }
              Py_INCREF(value);
              PUSH(value);
              FAST_DISPATCH();
          }

          case TARGET(LOAD_CONST): {
              PREDICTED(LOAD_CONST);
              PyObject *value = GETITEM(consts, oparg);
              Py_INCREF(value);
              PUSH(value);
              FAST_DISPATCH();
          }

          case TARGET(STORE_FAST): {
              PREDICTED(STORE_FAST);
              PyObject *value = POP();
              SETLOCAL(oparg, value);
              FAST_DISPATCH();
          }

          case TARGET(POP_TOP): {
              PyObject *value = POP();
              Py_DECREF(value);
              FAST_DISPATCH();
          }

          case TARGET(RETURN_VALUE): {
              retval = POP();
              assert(f->f_iblock == 0);
              assert(EMPTY());
              f->f_state = FRAME_RETURNED;
              f->f_stackdepth = 0;
              goto exiting;
          }

          ...
        }
  ...
error:
    /* Log traceback info. */
    PyTraceBack_Here(f);

    if (tstate->c_tracefunc != NULL) {
        /* Make sure state is set to FRAME_EXECUTING for tracing */
        f->f_state = FRAME_UNWINDING;
        call_exc_trace(tstate->c_tracefunc, tstate->c_traceobj,
                       tstate, f);
    }
exit_eval_frame:
    if (PyDTrace_FUNCTION_RETURN_ENABLED())
        dtrace_function_return(f);
    _Py_LeaveRecursiveCall(tstate);
    tstate->frame = f->f_back;

    return _Py_CheckFunctionResult(tstate, NULL, retval, __func__);
}
```

- CPython 일부 함수 설명
  - `Py_INCREF(value)`
    - value object의 reference count를 1 증가시킴
  - `PUSH(value)`
    - value object를 value stack에 push함
  - `NEXTOPARG()`
    - next instruction을 `word`라는 변수에 할당
    - `opcode`, `oparg` 라는 변수에 각각 opcode와 oparg를 할당
    - `next_instr++`
  - `FAST_DISPATCH()`
    - fast_next_opcode 로 넘어감
