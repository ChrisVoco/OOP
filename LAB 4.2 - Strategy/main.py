import cmath


class DiscriminantStrategy:
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b * b - 4 * a * c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = b * b - 4 * a * c
        if d < 0:
            return float('nan')
        return d


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        d = self.strategy.calculate_discriminant(a, b, c)

        # Kui diskriminant on NaN → tagasta kaks NaN-i
        if d != d:  # NaN kontroll
            return (complex(float('nan'), float('nan')),
                    complex(float('nan'), float('nan')))

        sqrt_d = cmath.sqrt(d)

        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)

        return (x1, x2)
    
# Näide 1
solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
print(solver.solve(1, 10, 16))
# ((-2+0j), (-8+0j))


# Näide 2
solver = QuadraticEquationSolver(RealDiscriminantStrategy())
print(solver.solve(1, 4, 5))
# (nan+nanj, nan+nanj)


# Näide 3
solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
print(solver.solve(1, 4, 5))
# kompleksarvud