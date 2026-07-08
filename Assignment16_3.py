def add(no1,no2):
    return no1 + no2

def main():
    num1 = int(input("Enter a first number :"))
    num2 = int(input("Enter a second number :"))

    ret = add(num1,num2)
    print("Addition is :",ret)

if __name__ == "__main__":
    main()