def reverseRecursion(given_string):
    stringLen = len(given_string)
    if stringLen == 1:
        return given_string
    else:
        return reverseRecursion(given_string[1:]) + given_string[0]


givenstring = input('Enter inverted word/s = ')
print('The modified given word/s = ', reverseRecursion(givenstring))






