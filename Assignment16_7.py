def ChkTrue(no):
    if no % 5 == 0:
        print("True")
    else:
        print("False")

def main():
    num = int(input("Enter a number :"))
    ChkTrue(num)

if __name__ == "__main__":
    main()