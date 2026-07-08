from functools import reduce
addition = lambda no1,no2 : no1 + no2

def main():
    data = list(map(int,input("Enter numbers :").split()))

    print("Input data is :",data)
    print("Number of elements in list is :",len(data))

    fdata = reduce(addition,data)
    print("sum of all elements",fdata)

if __name__ =="__main__":
    main()