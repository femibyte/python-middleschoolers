
from math import log, sqrt

errMsg = "Bad input argument"

def check_input(s):
    """Check if string is a number
    # This function should return True if x is a number, False if not
    # This function should use a try-except block as shown in th video 
    # https://www.youtube.com/watch?v=KdMAj8Et4xk
    Replace pass below with working code
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

def do_basic_arithmetic(func):
    """"
    This function should do the following:

    1. Prompt the user for needed inputs x and y
    2. Check if the inputs are numeric and return error message if not
        by calling the check_input function implemented above
    3. Calculate and return the result for a basic arithmetic calculation : 
         add, subtract, multiply, divide
    Note that the add, subtract, multiply, divide functions are no longer needed
    since we now have a check_input function


    """

    x_input = input("Enter x:")
    y_input = input("Enter y:")

    if not check_input(x_input) or not check_input(y_input):
        return errMsg
    x = float(x_input)
    y=float(y_input)
    if func=='A':
        return x+y
    elif func=='M':
        return x*y
    elif func=='S':
        return x-y 
    else:
        try:
            return x/y
        except:
            return errMsg


def do_square_or_sqrt(func):
    """
        This function should do the following:
        1. Prompt the user for needed input(s)
        2. Check if the inputs are numeric and return error message if not
        by calling the check_input function implemented above
        3. Calculate and return the result depending on whether the square or square root
           function was specified


    """
    x_input = input("Enter x:")
    if not check_input(x_input):
        return errMsg
    x= float(x_input)
    if func=='X':
        return x*x
    else:
        try:
            return sqrt(x)
        except:
            return errMsg


def do_exp_or_log(func):
    """
        This function should do the following:
        1. Prompt the user for needed input(s)
        2. Check if the inputs are numeric and return error message if not
          by calling the check_input function implemented above
        3. Calculate and return the result depending on whether the exponent or logarithm
           function was specified
           

    """
    if func=='E':
        num_input = input("Enter num:")
        idx_input = input("Enter index:")

        if not check_input(num_input) or not check_input(idx_input):
            return errMsg

        num = float(num_input)
        idx = float(idx_input)
 
        return num ** idx
    else:
        num_input = input("Enter num:")
        base_input = input("Enter base:")

        if not check_input(num_input) or not check_input(base_input):
            return errMsg

        num = float(num_input)
        base = float(base_input)
        try:
            return log(num, base)
        except:
            return errMsg


def get_input_and_calculate():
    """
    Fill in missing parts of the code below
    1. Check if the letter entered corr. to an arithmetic function
    2.  Check if the letter entered corr. to an square or square root
    3.  Check if the letter entered corr. to an exponent or logarithmic function

    """
    input_prompt = """Select operation by letter:
                        Addition       : A
                        Subtraction    : S
                        Multiplication : M
                        Division       : D
                        Square         : X
                        Square Root    : Y
                        Logarithm      : L
                        Exponential    : E
                        Sine           : B
                        Cosine         : C
                        Tangent        : T
                        ArcSine        : F
                        ArcCosine      : G
                        ArcTangent     : H
                        Quit           : Q
                    """
    func = input(input_prompt)
    if func in ['A', 'S','M', 'D']:
        return do_basic_arithmetic(func)
    elif func in ['X', 'Y']:
        return do_square_or_sqrt(func)
    elif func in ['E', 'L']:
        return do_exp_or_log(func)
    elif func in ['B','C','T','F','G','H']:
        return do_trigonometric(func)
    elif func == 'Q':
        return "Bye"
    else:
        return errMsg


from math import sin, cos, tan, asin, acos, atan, radians, degrees

def calc_sin(angle):
  return sin(radians(angle))
  
def calc_cos(angle):
  return cos(radians(angle))

def calc_tan(angle):
  return tan(radians(angle))

def calc_arcsin(value):
  return degrees(asin(value))
  
def calc_arccos(value):
  return degrees(acos(value))

def calc_arctan(value):
  return degrees(atan(value))

def do_trigonometric(func):
    val = input("Enter value:")
    if not check_input(val):
        return errMsg
    value = float(val)
    
    try:
        if func == 'B':
            return calc_sin(value)
        elif func == 'C':
            return calc_cos(value)
        elif func == 'T':
            return calc_tan(value)
        elif func == 'F':
            return calc_arcsin(value)
        elif func == 'G':
            return calc_arccos(value)
        elif func == 'H':
            return calc_arctan(value)
    except:
        return errMsg

def main():
    res = None
    while res!= "Bye":
        res = get_input_and_calculate()
        print("{}".format(res))




if __name__ == "__main__":
    main()


"""Useful links

Calculating exponential values

https://www.educative.io/edpresso/calculating-the-exponential-value-in-python

Calculating logarithm

https://www.w3schools.com/python/ref_math_log.asp


https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float

Try except for check_input:

https://www.youtube.com/watch?v=KdMAj8Et4xk

Watch from 0 up to 5:35

Follow along and try out the code using repl.it

"""