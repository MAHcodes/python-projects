def reverse_string():
    text = input("Enter text to reverse: ")
    rev_text = ""
    getlen = len(text)

    while len(rev_text) != getlen:
        rev_text += text[-1]
        text = text[:-1]
    print(rev_text)