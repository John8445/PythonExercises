def allPrimesUpTo(num):
    #The general algorithm is as follows

    if num <= 1:
        return ['no Prime numbers']
    
    listOfPrimes =[]

    #iterate from 2 to num
    for number in range(2, num):
        #iterate from 2 to squareroot of num. remember the range function expects type int so ensure that you cast
        for factor in range(2, int(num ** 0.5) + 1):
            #if the remainder of number % factor is 0 it is not prime
            if number % factor == 0:
                break
        else:
            #Code to execute when the loop completes all iterations without encountering a break
            #since the number never hit a break that means we went through every number and found a remainder and therefore it is prime
            listOfPrimes.append(number)

    return listOfPrimes

try:
    # Get user input and convert it to an integer
    user_input = input("Enter an integer: ")
    user_input_int = int(user_input)

    #check primes up to user input
    print(allPrimesUpTo(user_input_int))

except ValueError:
    # If the user input cannot be converted to an integer, a ValueError will be raised
    print("Invalid input. Please enter an integer.")