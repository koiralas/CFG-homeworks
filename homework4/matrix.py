def matrix_finder(matrix, target):
    x = -1
    y = -1
    for index_x in range(len(matrix)):
        for index_y in range(len(matrix[index_x])):
            if matrix[index_x][index_y] == target:
                x = index_x
                y = index_y

    return [x, y]


matrix = [[1, 4, 7, 12, 15, 1000],
          [2, 5, 19, 31, 32, 1001],
          [3, 8, 24, 33, 35, 1002],
          [40, 41, 42, 44, 45, 1003],
          [99, 100, 103, 106, 128, 1004]
          ]

print(matrix_finder(matrix, 44))