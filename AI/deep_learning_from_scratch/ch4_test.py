import numpy as np
import matplotlib.pylab as plt
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(x_batch, t_batch)

def function_1(x):
    return 0.01 * (x**2) + 0.1 * x

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)

plt.plot(x, y)
plt.show()

from functions import numerical_diff

print(numerical_diff(function_1, 5))

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(len(x)):
        temp_val = x[idx]

        x[idx] = temp_val + h
        fxh1 = f(x)

        x[idx] = temp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = temp_val

    return grad

def gradient_decent(f, init_x, lr=0.01, steps=100):
    x = init_x

    for i in range(steps):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x

def function_2(x):
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0, 4.0])
print(numerical_gradient(function_2, np.array([3.0, 4.0])))
print(gradient_decent(function_2, init_x, lr=10))

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) # 정규분포로 초기화

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

def f(W):
    return net.loss(x, t)

net = simpleNet()

x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)

dW = numerical_gradient(f, net.W)
print(dW)
