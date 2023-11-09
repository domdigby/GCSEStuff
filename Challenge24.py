def line_draw(num_space, num_x):
    """
    Write a function that takes two numbers.
    The first number indicates the number of
    spaces that should be displayed and the
    second indicates the number of Xs that
    should be displayed. These should both
    be displayed on the same line.
    :param num_space: The number of spaces to be displayed
    :param num_x: The number of Xs to be displayed
    :return: A string of spaces then Xs
    """
    line = chr(32) * num_space + chr(88) * num_x
    return line


def picture_x(pic):
    """
    A function that makes repeated calls
    to line_draw function and to draw a picture with Xs.
    :param pic: An integer 2D array of lines and spaces/Xs per line
    :return:
    """
    for line in pic:
        print(line_draw(line[0], line[1]))


# Wavy line
picture = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [3, 4], [2, 3], [1, 2], [0, 1], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [3, 4], [2, 3], [1, 2], [0, 1]]
picture_x(picture)
