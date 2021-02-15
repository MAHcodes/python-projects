def prime():
    n = int(input("Enter a number: "))
    is_prime = True
    for i in range(2, n//2):
        if n % i != 0:
            continue
        else:
            is_prime = False
            break

    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

if __name__ == "__main__":
    prime()