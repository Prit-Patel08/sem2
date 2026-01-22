def func(a, b, c):
    mn = min(a,b,c)
    mx = max(a,b,c)
    print("Largest:", mx)
    print("Smallest", mn)

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))

small(x, y, z)
