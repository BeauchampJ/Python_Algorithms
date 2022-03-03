def f(x): #Define a function
    return x**4-8*x+3


def falseposition(xl, xu, es): #Impliment false position algorithm
    xr = xl
    it = 0
    es = es / 100  # Changes percent to decimal
    ea = 100
    if f(xl) == 0:
        raise ValueError("Lower limit was a root!")
    elif f(xu) == 0:
        raise ValueError("Upper limit was a root!")
    while ea > es:
        xrold = xr
        xr = xu - ((f(xu) * (xl - xu)) / (f(xl) - f(xu)))  # False position formula
        it += 1
        if not xr == 0:
            ea = (abs((xr - xrold) / xr)) * 100
        if f(xu) * f(xr) < 0:
            xl = xr
        elif f(xl) * f(xr) < 0:
            xu = xr
        else:
            ea = 0
    fx = f(xr)
    root = xr
    if root == float("inf"):
        raise ValueError("Function either doesn't cross zero or has two zeros in your bounds")

#Print to console the results
    print(f"The root value is {root}")
    print(f"Function value at root is {fx}")
    print(f"Approximate relative error is {ea}")
    print(f"Number of iterations is {it}")

#Get users inputs
xl = float(input("Lower bound: "))
xu = float(input("Upper bound: "))
es = float(input("Estimated error: "))

falseposition(xl, xu, es)
