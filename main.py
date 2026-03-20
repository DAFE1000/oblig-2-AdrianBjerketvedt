import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar


def main():
    x_values = np.linspace(0, 10, 100)
    max_result = maximum()
    max_x = max_result.x
    max_y = f(max_x)

    plot(x_values, max_x, max_y)


def f(x):
    return np.exp(-x/4) * np.arctan(x)


def maximum():
    return minimize_scalar(lambda x: -f(x), bounds=(-10, 10), method='bounded')


def plot(x_values, max_x, max_y):
    plt.plot(x_values, f(x_values))
    plt.title('Plot of f(x) = e^(-x/4) * arctan(x)')
    plt.plot(max_x, max_y, 'ro')
    plt.legend(['f(x)', f'Maximum at x={max_x:.2f}, y={max_y:.2f}'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
