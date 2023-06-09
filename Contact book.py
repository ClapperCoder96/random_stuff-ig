choose = input("Would you like to add a contact or search for one? \n(please enter either 'add' or 'search')\n")
name = ""
num = 0
if choose == 'add':
	name = input("Name: ")
	num = int(input("Number:"))

	with open("miniproj.txt", "a",) as f:
		f.write("\n")
		f.write("NAME: " + name + " NUMBER: " + str(num))

elif choose == "search":
	who = input("Enter the name of the person you are looking for: ")
	with open(r'miniproj.txt', 'r') as fp:
		lines = fp.readlines()
		for row in lines:
			word = who
			if row.find(word) != -1:
				print(row)
			else:
				print("Sorry, that name is not in our directory. . .")
		
