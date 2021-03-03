def Armstrong(num):
    sum = 0
    for i in str(num):
        i = int(i)
        sum += i*i*i
    print(f"{num} is Armstrong number") if sum == num else print(f"{num} is not Armstrong number")

if __name__ == '__main__':
    Armstrong(int(input("Enter number: ")))