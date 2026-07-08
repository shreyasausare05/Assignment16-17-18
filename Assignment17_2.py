def pattern(no):
    for i in range(no):
        for j in range(no):
            print("*", end="")
        print()
def main():
    num = int(input("Enter a number :"))
    pattern(num)

if __name__ == "__main__":
    main()