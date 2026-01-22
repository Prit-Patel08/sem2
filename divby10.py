def odd_even(n):
    if (n % 10 == 0):
        print("number is divisible by 10")
    else:
        print("number is not divisible by 10")

x = int(input("Enter a number: "))
odd_even(x)
