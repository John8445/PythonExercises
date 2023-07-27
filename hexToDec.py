
#dictionary as a look up table
hexNumbers =  {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
}

user_input = input("Enter a Hexadecimal number: ")
decNum = 0
digit = 0
isHex = True

for i in range(len(user_input) - 1, -1, -1):

    if user_input[i] in hexNumbers:
        #first get the power of 16 needed for the digit
        pow = 16 ** digit
        decNum += pow * hexNumbers[user_input[i]]
        digit += 1
    else:
        print(f'{user_input} is not a hex number')
        isHex = False
        break

if isHex:
    print(f'The hexadecimal number in decimal is {decNum}')


#with out giving me any code or the answer is my solution correct? if not then only give me hints