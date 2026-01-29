s = input("Enter a String: ")

def reverse(s):
    length = len(s) - 1
    result = ""
    while length >= 0:
        result += s[length]
        length -= 1
    print("Reversed : ", result)
    
reverse(s)
