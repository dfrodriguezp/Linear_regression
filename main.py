import numpy
from scipy import stats
from matplotlib import pyplot
import os
import sys

def dataIn(var):
    data = input("Ingrese los datos de la variable {} (separados con comas): ".format(var))
    return numpy.array(data.split(", "), dtype=float)

def main():
    # y = dataIn("y")
    # x = dataIn("x")

    y = numpy.arange(200, 700, 100)
    x = numpy.array([0.1556, 0.2181, 0.2767, 0.4058, 0.4576])

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

    newX = numpy.linspace(min(x), max(x), 100)
    newY = m * newX + b

    pyplot.figure()
    pyplot.scatter(x, y, label="Raw data")
    pyplot.plot(newX, newY, label="Linear regression")
    pyplot.xlabel("$x$", fontsize=20)
    pyplot.ylabel("$y$", fontsize=20)
    pyplot.legend(loc="best")
    pyplot.grid()
    pyplot.savefig("graph.pdf")
    pyplot.show()
    pyplot.close()

if __name__ == '__main__':
    main()
