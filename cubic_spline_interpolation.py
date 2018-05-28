# Natural cubic spline interpolation
import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

"""
time_series = [
    {'x': 0, 'y': 0},
    {'x': 1, 'y': 0.5},
    {'x': 2, 'y': 2},
    {'x': 3, 'y': 1.5}
]
"""

time_series = [
    {'x': 1, 'y': 1.25},
    {'x': 5, 'y': 2.25},
    {'x': 10, 'y': 1},
    {'x': 20, 'y': 2.12}
]
"""

time_series = [
    {'x': 0, 'y': 0},
    {'x': 5, 'y': 10},
    {'x': 10, 'y': 7},
    {'x': 15, 'y': 4},
    {'x': 20, 'y': 6},
    {'x': 25, 'y': 8},
    {'x': 30, 'y': 6}
]
"""


def delta_x(i):
    return time_series[i + 1]['x'] - time_series[i]['x']


def x(i):
    return time_series[i]['x']


def y(i):
    return time_series[i]['y']


def cubic_spline(time_series):
    """
    Takes as input a set of (x_i, y_i) points and uses cubic splines interpolation
    between the input points to give an estimate of the y values for all
    integer values of x between the input points.
    :param time_series: between the input points.
    :param time_series: an array containing input points. Each input point
    is a dictionary of the form {'x': 1, 'y': 1.25}.
    :return: an array containing the input values along with the predicted values
    for every integer value of x.
    """
    n = len(time_series) - 1

    # Construction of the matrix containing the coefficients
    coefficients = []
    for k in range(0, n - 1):
        coefficients.append([0 for _ in range(0, n - 1)])
        if k != 0:
            coefficients[k][k - 1] = delta_x(k) / delta_x(k + 1)

        coefficients[k][k] = 2 * (x(k + 2) - x(k) / delta_x(k + 1))

        if k != n - 2:
            coefficients[k][k + 1] = 1

    # Construction of the right hand side of the system
    b = []
    for k in range(0, n - 1):
        b.append(6 * (y(k + 2) - y(k + 1)) / (delta_x(k + 1) ** 2) - (y(k + 1) - y(k)) / (delta_x(k + 1) * delta_x(k)))

    # Solve the system to get the M_i values
    M = np.linalg.solve(coefficients, b)
    M = np.append(0, M)
    M = np.append(M, 0)

    # Use the M values to evaluate the polynomials for every integer value of x
    output = []
    # For every polynomial
    for i in range(len(time_series) - 1):
        for x_j in range(x(i), x(i + 1)):
            # Evaluate the polynomial, using expression (3.14)
            y_j = M[i] / 6 * ((x(i + 1) - x_j)**3 / delta_x(i) - delta_x(i) * (x(i + 1) - x_j)) + M[i + 1] / 6 * \
                  ((x_j - x(i)) ** 3 / delta_x(i) - delta_x(i) * (x_j - x(i))) + y(i) * (x(i + 1) - x_j) / \
                  delta_x(i) + y(i + 1) * (x_j - x(i)) / delta_x(i)
            output.append({'x': x_j, 'y': y_j})
    output.append({'x': x(len(time_series) - 1), 'y': y(len(time_series) - 1)})

    return output


res = cubic_spline(time_series)
print(res)
