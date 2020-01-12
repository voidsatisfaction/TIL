import numpy as np

# activation functions
def step_function(x):
    y = x > 0
    return y.astype(np.int)

def sigmoid(x):
    return np.array(1/(1+np.exp(-x)))

# output functions
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c) # escape overflow
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

# loss functions
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t):
    # 정답 레이블이 원-핫 인코딩인 경우
    if y.ndim == 1:
        t = t.reshape(1, t.size) # 1차원 np.array인 경우, 2차원 행렬로 변환(행이 하나임)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    delta = 1e-7
    # y, t 는 행렬형식으로 input데이터가 올 것이므로, + 연산을 사용해서 간단하게 계산 가능
    # 또한, np.sum()은 행렬의 모든 원소를 다 더해줌
    return -np.sum(t * np.log(y + delta)) / batch_size

# numerical diff
def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h))/ (2*h)

# numerical_gradient
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.shape[0]):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad

# def numerical_gradient(f, x):
#     h = 1e-4 # 0.0001
#     grad = np.zeros_like(x)
#
#     it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
#     while not it.finished:
#         idx = it.multi_index
#         tmp_val = x[idx]
#         x[idx] = float(tmp_val) + h
#         fxh1 = f(x) # f(x+h)
#
#         x[idx] = tmp_val - h
#         fxh2 = f(x) # f(x-h)
#         grad[idx] = (fxh1 - fxh2) / (2*h)
#
#         x[idx] = tmp_val # 값 복원
#         it.iternext()
#
#     return grad

if __name__ == '__main__':
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

    print(mean_squared_error(np.array(y), np.array(t)))
    print(cross_entropy_error(np.array(y), np.array(t)))

    a = np.array([[1,2,3]])
    b = np.array([[1,2,3]])
    print(a.shape)
    print(a+b)
    print(np.sum(a+b))
