import sys

coef =[int(sys.argv[i]) for i in range(1, 4, 1)]
D = (coef[1] ** 2 - 4 * coef[0] * coef[2])**0.5

print(int((-coef[1] - D) / (2 * coef[0])))
print(int((-coef[1] + D) / (2 * coef[0])))