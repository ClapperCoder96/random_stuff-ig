#This is a contact book program where you can store names with numbers into a txt file and use the search function to pull it up

choose = input("Would you like to add a contact or search for one? \n (please enter either 'add' or 'search')\n")
name = ""
num = 0
if choose == 'add':
	name = input("Name: ")
	num = int(input("Number:"))
	print("NAME:", name, "NUMBER:", num)
	#make your own txtfile. miniproj.txt is MY file, and you need to create a file in your files app which has a txt file of any name.
	with open("miniproj.txt", "a",) as f:
		f.write("\n")
		f.write(name + " " + str(num))

elif choose == "search":
	who = input("Enter the name of the person you are looking for: ")
	if who == name:
		print("NAME:" + name + "NUMBER:" + str(num))
	
