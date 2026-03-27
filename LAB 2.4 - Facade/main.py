import random


class Generator:
    def generate(self, n):
        return [random.randint(1, 9) for _ in range(n)]


class Splitter:
    def split(self, matrix):
        size = len(matrix)
        result = []

        # read
        for row in matrix:
            result.append(row)

        # veerud
        for col in range(size):
            column = []
            for row in range(size):
                column.append(matrix[row][col])
            result.append(column)

        # peadiagonaal
        main_diag = []
        for i in range(size):
            main_diag.append(matrix[i][i])
        result.append(main_diag)

        # kõrvaldiagonaal
        other_diag = []
        for i in range(size):
            other_diag.append(matrix[i][size - 1 - i])
        result.append(other_diag)

        return result


class Verifier:
    def verify(self, lists):
        sums = [sum(lst) for lst in lists]
        return all(s == sums[0] for s in sums)


class MagicSquareGenerator:
    def __init__(self):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size):
        while True:
            # 1. genereeri arvud
            numbers = self.generator.generate(size * size)

            # 2. tee maatriks
            matrix = []
            for i in range(size):
                row = numbers[i * size:(i + 1) * size]
                matrix.append(row)

            # 3. split
            parts = self.splitter.split(matrix)

            # 4. kontroll
            if self.verifier.verify(parts):
                return matrix

gen = MagicSquareGenerator()
square = gen.generate(3)

for row in square:
    print(row)