import numpy
from scipy import stats
import os
import sys

def dataIn(var):
    data = input("Ingrese los datos de la variable {} (separados con comas): ".format(var))
    return numpy.array(data.split(", "), dtype=float)

def main():
    y = dataIn("y")
    x = dataIn("x")

    if len(y) != len(x):
        os.system("clear")
        print("\nError: x y y deben tener la misma cantidad de datos.\n")
        sys.exit()

    os.system("clear")

    print("x = ", x)
    print("y = ", y)

    m, b, r, _, _ = stats.linregress(x, y)

    print("\nm = %f" %(m))
    print("b = %f" %(b))
    print("r = %f\n" %(r))

if __name__ == '__main__':
    main()
