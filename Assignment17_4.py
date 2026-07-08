def factor(no):
    sum= 0
    for i in range(1,no):
        if no % i == 0:
            sum = sum + i 
    return sum

def main():
    num = int(input("Enter a number"))
    ret = factor(num)
    print("Sum of number is :",ret)

if __name__ == "__main__":
    main()