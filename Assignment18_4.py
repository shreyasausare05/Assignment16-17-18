def frequency(arr,no):
    count = 0
    for i in arr:
        if i == no:
            count += 1
    return count

def main():
    size = int(input("Enter a number of Elements :"))

    data = []

    print("Enter Elements :")
    for i in range(size):
        value = int(input())
        data.append(value)
    
    search = int(input("Enter a number to search :"))
    result = frequency(data,search)
    print("Frequency of",search,"is :",result)

if __name__ == "__main__":
    main()