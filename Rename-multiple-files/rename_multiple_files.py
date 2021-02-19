import os


def main():
	counter = 1
	for file in os.listdir(path + "\\"):
	    file_extension = os.path.splitext(file)[1]
	    new_name = "mah_" + str(counter) + file_extension
	    source = path + "\\" + file
	    destination = path + "\\" + new_name
	    os.rename(source, destination)
	    counter += 1
	print("All files renamed successfully...")


if __name__ == '__main__':
	main()