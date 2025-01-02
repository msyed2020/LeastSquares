# The purpose of this program is to demonstrate the Principle of Least Squares Algorithm. Run via 'python3 leastsquare.py'

def leastSquare(n: int, x: list, y: list):
    # Sum of squared errors (SSE): (y[i] - (a * x[i] + b))^2 for i in range(n)

    # Through partial derivatives, we can assume a = Cov(x,y) / Var(x)

    x_bar = sum(x) / len(x)
    y_bar = sum(y) / len(y)

    cov = 0
    var = 0
    
    # Cov calculation
    for i in range(n):
        eq = (x[i] - x_bar) * (y[i] - y_bar)
        cov += eq
    
    # Var calculation
    for i in range(n):
        eq = (x[i] - x_bar) * (x[i] - x_bar)
        var += eq
    
    a = cov / var

    b = y_bar - (a * x_bar)

    # SSE Calculation
    sse = 0
    for i in range(n):
        eq = (y[i] - (a * x[i] + b)) * (y[i] - (a * x[i] + b))
        sse += eq
    return "a: " + str(a) + ", b: " + str(b) + ", SSE: " + str(sse)

print(leastSquare(3, [1,2,3], [2,4,6]))