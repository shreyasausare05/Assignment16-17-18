import MarvellousNum1

def listprime(arr):
    sum = 0

    for i in arr:
        if MarvellousNum1.ChkPrime(i):
            sum = sum +i
        
    return sum

def main():
    size = int(input("Enter number of elements :"))

    data = []

    print("Enetr elements :")
    for i in range(size):
        value = int(input())
        data.append(value)

    result = listprime(data)

    print("Addition of prime number is :",result)

if __name__ == "__main__":
    main()