#Write Binary.python to read an integer as an Input, convert to Binary using toBinary function and perform the following functions.
#i. Swap nibbles and find the new number.
#ii. Find the resultant number is the number is a power of 2.
#A nibble is a four-bit aggregation, or half an octet. There are two nibbles in a byte.
#Given a byte, swap the two nibbles in it. For example 100 is to be represented as 01100100 in a byte (or 8 bits). The two nibbles are (0110) and (0100). If we swap the two nibbles, we get 01000110 which is 70 in decimal.

def swapNibbles(x):
    print((x & 0x0F) << 4 | (x & 0xF0) >> 4)
x = 100
swapNibbles(x)
def bin(num):
    if(num >=1):
        bin(num//2)
    print(num % 2, end="")
num=100
bin(num)
