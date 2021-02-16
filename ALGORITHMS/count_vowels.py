def count_vowels():
    vowels = ["o", "u", "a", "e", "i"]
    text = input("Enter text: ")
    count = 0
    txt_vwls = ""

    for i in text:
        if i in vowels:
            count += 1
            txt_vwls += i + ", "
        for u in txt_vwls:
            u.join(txt_vwls)

    print(f"The text contains: {count} vowels, here they are: {txt_vwls[:-2]}")

if __name__ == "__main__":
	count_vowels()