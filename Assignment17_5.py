def ChkPrime(no):
    for i in range(2,no):
        if no % i == 0:
            print("Not prime")
            return
    print("Prime")

def main():
    num = int(input("Enter a number :"))
    ChkPrime(num)

if __name__ == "__main__":
    main()