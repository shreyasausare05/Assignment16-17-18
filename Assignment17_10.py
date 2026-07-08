def sumdigit(no):
    sum = 0
    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10
    return sum

def main():
    num = int(input("Enter a number :"))
    result = sumdigit(num)
    print("Sum of digits is :", result)

if __name__ == "__main__":
    main()