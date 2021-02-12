text = open("string.txt", "r")
count = 0

for i in text:
    for j in i.split():
        print(j)
        count += 1

print(count)
text.close()