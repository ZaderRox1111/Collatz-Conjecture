import random

def main():
    for i in range(10):
        print(' ')
        num = random.randint(0,100000000000000000000000000000000000000000000000000000000)
        print(num)
        collatz(num)
 

#checks to see if a number is even or odd
def check(number):
    return number % 2 == 0


def collatz(number):
    #print(number)
    #if the number is even, divide by 2, if odd multpily by 3 and add 1; go until it equals 1
    if number != 1:
        if check(number) == True:
            number = number / 2
            collatz(number)
        else:
            number = number * 3 + 1
            collatz(number)
    else:
        print('goes to 1')


main()
