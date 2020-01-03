def outerFunction(aParameterValue):
    # SETS SOME FACTOR OF THE FINAL RESULT
    print(f"Setting x as {aParameterValue}")

    def innerFunction(anotherParameterValue):
        # THE INNER FUNCTION SETS THE FINAL RESULT
        print(f"Setting y as {anotherParameterValue}")
        finalResult = aParameterValue + anotherParameterValue + 3
        print(f"Final function: x is {aParameterValue} , y is {anotherParameterValue}, constant is 3")
        return finalResult

    return innerFunction


def function_modder(originalFunction):
    #  WILL ADD SOME ADDITIONAL FUNCTIONALITY TO A FUNCTION THAT IS PASSED TO IT BEFORE CALLING IT
    # IN THIS CASE, ADDING TWO PRINT STATEMENTS BEFORE AND AFTER CALLING THE FUNCTION
    def modifiedFunction(x):
        print(f"Before calling function {originalFunction.__name__}")
        print(f"Paramater passed into inner function: {x}")

        # HERE , WE ARE STILL CALLING THE ORIGINAL FUNCTION (BUT WE ARE DOING OTHER STUFF ABOVE AND BELOW IT AS WELL)
        originalFunction(x)

        print(f"After calling function {originalFunction.__name__}")
        # A MODIFIED FUNCTION IS RETURNED THAT STILL DOES THE ORIGINAL STUFF THE FUNCTION WAS MADE TO SO WITH SOME ADDITIONAL STUFF

        # **NOTE THAT A DECORATOR FUNCTION RETURNS A FUNCTION
    return modifiedFunction


@function_modder
# PUTTING OUR_DECORATOR HERE MEANS THAT WE ARE PASSING THE FUNCTION BELOW INTO  THE DECORATOR
# Summarizing we can say that a decorator in Python is a callable Python object that is used to modify a function, method or class definition.
# The original object, the one which is going to be modified, is passed to a decorator as an argument.
def food(x):
    print(f"Function: Food. Paramater passed: {x}")

 def memoize(originalFunction):
    memo = {}

    def modifiedFunction(x):
        if x not in memo:
            # NO SAVED RESULTS FOR RUNNING THE ORIGINAL FUNCTION WITH THIS PARAMETER X
            # SAVE PARAMETER AND RESULT OF RUNNING THE ORIGINAL FUNCTION WITH THIS PARAMETER AS A KEY VALUE PAIR
            memo[x] = originalFunction(x)

        # MODIFIED FUNCTION RETURNS WHAT ORIGINAL FUNCTION WOULD HAVE RETURNED
        return memo[x]

    # HERE, WE RETURN A MODIFIED VERSION OF THE ORIGINAL FUNCTION
    return modifiedFunction
