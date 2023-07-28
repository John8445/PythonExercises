def encodeString(stringVal):
    #use list to store our data
    encodedList = []
    #variable for when the string has changed
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        #if previous character isnt the smae as the the cur value
        if prevChar != char:
            #add a new key value pair using tuple
            encodedList.append((prevChar, count))
            #reset the count of the current char
            count = 0
        #set prevchar to current char before next iteration of the loop
        prevChar = char 
        #increment count to reflect how many times we see a number pop up
        count += 1
    #lastly append the last set of values
    encodedList.append((prevChar, count))
    return encodedList 
   

def decodeString(encodedList):
    decodedStr = ''

    for item in encodedList:
        #multiply the letter times the count
        decodedStr = decodedStr + item[0] * item[1]
    
    return decodedStr