# Putu Bayu Baskara
# 1808561022

# func prime number checker
def prime_check():
    print("PRIME NUMBER CHECKER")
    num = int(input("Input Number : "))
    # number must > 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")
    # if number < 1 || == 1
    else:
        print(num, "is not a prime number")


# func factorial of a number
def factorial_numb():
    print("FACTORIAL OF A NUMBER")
    i = 1
    n = 1
    num = int(input("Input Number : "))

    if num < 0:
        print("Number must > 0")
    elif num == 0:
        print("0! = 1")
    else:
        while i <= num:
            n = n*i
            if i < num:
                print(i, 'x', i+1)
            i = i+1
        print("-------------------")
        hasil = str(num)+'! = '+str(n)
        print(hasil)


# func find GCD of two numbers Using Euclidian Algorithm
def gcd_numb(x, y):
    print("GCD OF TWO NUMBERS")
    while(y):
        x, y = y, x % y
        gcd_v = x
    return gcd_v


# func main program
def main():
    print("============================")
    print("1. Prime Number Checker")
    print("2. Factorial of a Number")
    print("3. Find GCD of Two Numbers")
    pilih = int(input("Input (1/2/3) : "))
    print("============================")

    if pilih == 1:
        # call func prime number checker
        prime_check()
    elif pilih == 2:
        # call func factorial numb
        factorial_numb()
    elif pilih == 3:
        # call func GCD numb
        num1 = int(input("Input 1st Number : "))
        num2 = int(input("Input 2nd Number : "))
        gcd = gcd_numb(num1, num2)
        print("-------------------")
        print("The GCD is", gcd)
    else:
        print("Not Available!Choose Again")


# run main programs
main()
