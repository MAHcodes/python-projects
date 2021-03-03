<<<<<<< HEAD
import os


def main():
	counter = 1
	for file in os.listdir(path + "\\"):
		file_extension = os.path.splitext(file)[1]
		new_name = name  + str(counter) + file_extension
		source = path + "\\" + file
		destination = path + "\\" + new_name
		os.rename(source, destination)
		counter += 1
	print("All files renamed successfully...")


if __name__ == '__main__':
	path = input("Enter folder path: ")
	name = input("Enter files name: ")
=======
import os


def main():
	counter = 1
	for file in os.listdir(path + "\\"):
		file_extension = os.path.splitext(file)[1]
		new_name = name  + str(counter) + file_extension
		source = path + "\\" + file
		destination = path + "\\" + new_name
		os.rename(source, destination)
		counter += 1
	print("All files renamed successfully...")


if __name__ == '__main__':
	path = input("Enter folder path: ")
	name = input("Enter files name: ")
>>>>>>> d3f1690f946524ddeb7f2e06bcc8d641a3d42416
	main()