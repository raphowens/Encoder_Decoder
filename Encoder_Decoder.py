# Author: 766431

# File: Day2_Encoder_Decoder.py


print("""
        **********************************************
                     ENCODER  & DECODER
        **********************************************
        """)

##ord()>>> to convert character to ASCII value
##chr()>>> to convert ASCII value  to character


print("""
        **********************************************
                           ENCODER
        **********************************************
        """)


def Encoder(text, shift):
    '''Returns the encoded input, taking into consideration
        the number of text shifts

    >>> Encoder('abcde123',1)
    original input: abcde123, shift: 1, result: bcdef234

    >>> Encoder('raphael000',2)
    original input: raphael000, shift: 2, result: tcrjcgn222
    '''

    output = ''
    for char in text:

        if ord(char) in range(48, 58):
            output += chr((ord(char) - 48 + shift) % 10 + 48)

        elif char.islower():
            output += chr((ord(char) - 97 + shift) % 26 + 97)

        elif char.isupper():
            output += chr((ord(char) - 65 + shift) % 26 + 65)

    print(f'original input: {text}, shift: {shift}, result: {output}')


Encoder('bruttonetto312', 1)

if __name__ == "__main__":
    # run the doctest cases:
    print(">>> doctest >>>")
    import doctest

    doctest.testmod()
    print("<<< doctest <<<")

print("""
        **********************************************
                           DECODER
        **********************************************
        """)


def Decoder(text, shift):
    """
    Returns the decoded input, taking into consideration
    the number of text shifts

    >>> Decoder('bnmj098',2)
    original input: bnmj098, shift: 2, result: zlkh876

    >>> Decoder('owens',2)
    original input: owens, shift: 2, result: muclq
    """

    output = ''
    for char in text:

        if ord(char) in range(48, 58):
            output += chr((ord(char) - 48 - shift) % 10 + 48)

        elif char.islower():
            output += chr((ord(char) - 97 - shift) % 26 + 97)

        elif char.isupper():
            output += chr((ord(char) - 65 - shift) % 26 + 65)

    print(f'original input: {text}, shift: {shift}, result: {output}')


Decoder('astalavisata098', 2)

if __name__ == "__main__":
    # run the doctest cases:
    print(">>> doctest >>>")
    import doctest

    doctest.testmod()
    print("<<< doctest <<<")

print("""
        **********************************************
                           ENCODER (INPUT)
        **********************************************
        """)


def Encoder(text=None, shift=None):
    '''Returns the encoded input, taking into consideration
        the number of text shifts'''

    if text == None and shift == None:
        text = str(input('Original Input: '))
        shift = int(input('How many places to shift: '))

    output = ''
    for char in text:

        if ord(char) in range(48, 58):
            output += chr((ord(char) - 48 + shift) % 10 + 48)

        elif char.islower():
            output += chr((ord(char) - 97 + shift) % 26 + 97)

        elif char.isupper():
            output += chr((ord(char) - 65 + shift) % 26 + 65)

    print(f'original input: {text}, result: {output}')


Encoder(text=None, shift=None)

print("""
        **********************************************
                           DECODER (INPUT)
        **********************************************
        """)


def Decoder(text=None, shift=None):
    """
    Returns the decoded input, taking into consideration
    the number of text shifts

    """

    if text == None and shift == None:
        text = str(input('Original Input: '))
        shift = int(input('How many places to shift: '))

    output = ''
    for char in text:

        if ord(char) in range(48, 58):
            output += chr((ord(char) - 48 - shift) % 10 + 48)

        elif char.islower():
            output += chr((ord(char) - 97 - shift) % 26 + 97)

        elif char.isupper():
            output += chr((ord(char) - 65 - shift) % 26 + 65)

    print(f'original input: {text}, result: {output}')


Decoder(text=None, shift=None)

##def Encoder(text = None,shift = None):
##
##    nums = '0123456789'
##    lowers = 'abcdefghijklmnopqrstuvwxyz'
##    uppers = lowers.upper()
##
##    if text == None and shift == None:
##        text=str(input('Original Input: '))
##        shift=int(input('How many places to shift: '))
##
##    output= ''
##    for char in text:
##
##        if char in '0123456789':
##            output += nums[(nums.index(char) + shift) % 10]
##
##        elif char.islower():
##            output += lowers[(lowers.index(char) + shift) % 26]
##
##        elif char.isupper():
##            output += uppers[(uppers.index(char) + shift) % 26]
##
##    print(f'original input:{text}, result: {output}')
##
##Encoder(text = None,shift = None)


input('...')

'''
print("""
        **********************************************
                           ENCODER
        **********************************************
        """)


def Encoder(textE = None,shift = None):

    if textE == None and shift == None:
        textE=str(input('Original Input: '))
        shift=int(input('How many places to shift: '))

    outputE= ' '
    for char in textE:

        print(char, ord(char), ord(char)+shift, chr(ord(char)+shift))
        outputE += chr(ord(char)+shift)       
    print(f'original input: {textE}, result: {outputE}')

Encoder(textE = None,shift = None)

print("""
        **********************************************
                           DECODER
        **********************************************
        """)

def Decoder(textD = None,shift = None):

    if textD == None and shift == None:
        textD=str(input('Original Input: '))
        shift=int(input('How many places to shift: '))

    outputD= ' '
    for char in textD:

         print(char, ord(char), ord(char)-shift, chr(ord(char)-shift))
         outputD += chr(ord(char)-shift)       
    print(f'original input: {textD}, result: {outputD}')

Decoder(textD = None,shift = None)

'''











































