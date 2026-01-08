import sys

# LEGACY CODE: 1998 PAYROLL CALCULATOR
# No comments, weird variable names, logic mixed with print statements
def c(h, r):
    x = 0
    # Overtime logic hardcoded
    if h > 40:
        x = (40 * r) + ((h - 40) * (r * 1.5))
    else:
        x = h * r
    
    # Weird "Manager Bonus" legacy rule
    if x > 1000:
        x = x + 50 # Add $50 bonus for high earners (undocumented)
    
    return int(x)

if __name__ == "__main__":
    # Expects inputs: Hours, Rate
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        print(c(a, b))
    except:
        print("ERROR")