import csv

data = open("olx-cars.csv")
data_read = csv.reader(data)
filtered = open("filtered.csv", "w")
filtered_write = csv.writer(filtered)


for row in data_read:
    try:
        if (len(row[1]) < 7 or row[1] == "1,000 $") and (row[2][:9] == "Yesterday" or row[2][:5] == "Today"):
            filtered_write.writerow(row)
    except:
        pass
print("Done")

data.close()
filtered.close()