'''
Task: Print out numbers 1 - 100, however if number is divisible by 3, print
"fizz", if divisible by 5 print "buzz", and if divisible by 3 AND 5, print
"fizzbuzz".

Assumptions:
    - We are not concerned with input validation and that the input
    to the function will be an integer greater than 0.

    - We will print out numbers starting at 1, and will include the limit.

'''


def fizzbuzz(n):
    '''
    This function takes in one argument, n. We will print numbers 1 through n,
    replacing "fizz", "buzz", and "fizzbuzz" where appropriate.
    '''
    for i in range(n + 1)[1:]:
        if i % 15 == 0:  # if n is divisible by 3 and 5 print 'fizzbuzz'
            print("fizzbuzz")
        elif i % 5 == 0:  # check if divisible by 5
            print("buzz")
        elif i % 3 == 0:  # check if divisible by 3
            print("fizz")
        else:
            print(i)  # Otherwise, print the number


fizzbuzz(100)
