# Array class is defined here

class Array:
    def __init__(self, list):
        self.list = list
        for row in list:
            if len(row) != len(list[0]):
                raise ValueError("All rows must have the same number of columns")
        self.rows = len(list)
        self.cols = len(list[0])
        return
    def at(self, row, col):
        return self.list[row][col]
    def set(self, row, col, value):
        self.list[row][col] = value
        return
    def display(self):
        for row in self.list:
            print(row)
        return
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match")
        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(other.cols):
                result[i].append(0)
                for k in range(self.cols):
                    result[i][j] += self.list[i][k] * other.list[k][j]
        # print("Multiplied")
        return Array(result)
    
