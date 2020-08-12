with open("C:\\Users\\Latitude\\Desktop\\Cyrus\\Python Trainng Bootcamp\\Python Scripts\\Sampletext.txt", mode = "a") as myfile1:
	myfile1.write("\nThis is the fourth line.")
with open("C:\\Users\\Latitude\\Desktop\\Cyrus\\Python Trainng Bootcamp\\Python Scripts\\Sampletext.txt", mode = "r") as myfile1:
	print(myfile1.readlines())