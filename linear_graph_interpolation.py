# Data visualization - line graph linear interpolation.

# Sample input:
time_series = [
    {'x': 1, 'y': 1.25},
    {'x': 5, 'y': 2.25},
    {'x': 10, 'y': 1},
    {'x': 20, 'y': 2.12}
]
#
#
# Corresponding output (the gaps in the X values are filled in for each integer X via linear interpolation):
# output = [
#   { x: 1, y: 1.25 }, <-- same as input
#   { x: 2, y: 1.5 },
#   { x: 3, y: 1.75 },
#   { x: 4, y: 2 },
#   { x: 5, y: 2.25 }, <-- same as input
#   { x: 6, y: 2 },
#   { x: 7, y: 1.75 },
#   { x: 8, y: 1.5 },
#   { x: 9, y: 1.25 },
#   { x: 10, y: 1 }, <-- same as input
#   .
#   .
#   .
# ]

# Write a method that accepts a timeseries (as above - an array of dictionaries) and outputs a new array with the
# same format as the sample output.


def linear_interpolation(time_series):
    """
    Takes as input a set of (x_i, y_i) points and use linear interpolations
    between the input points to give an estimate of the y values for all
    integer values of x between the input points.
    :param time_series: an array containing input points. Each input point
    is a dictionary of the form {'x': 1, 'y': 1.25}.
    :return: an array containing the input values along with the predicted values
    for every integer value of x.
    """
    output = []
    # Iterate over the input points :
    for i in range(len(time_series) - 1):
        # Take the two points that we want to interpolate between :
        point = time_series[i]
        next_point = time_series[i + 1]
        # Compute the slope of the affine function between those two points :
        slope = (next_point['y'] - point['y']) / (next_point['x'] - point['x'])
        # Compute the constant of the affine function :
        c = point['y'] - point['x'] * slope
        # Add every integer value of x between the 2 points along with the corresponding y value :
        for x in range(point['x'], next_point['x']):
            output.append({'x': x, 'y': x * slope + c})
    output.append({'x': time_series[-1]['x'], 'y': time_series[-1]['y']})
    return output


print(linear_interpolation(time_series))
