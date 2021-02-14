def palindrome():
    if text == text[::-1]:
        print(text + " is palindrome")
    else:
        print(text + " is not palindrome")


if __name__ == "__main__":
    text = input("Enter a string: ").lower()
    palindrome()