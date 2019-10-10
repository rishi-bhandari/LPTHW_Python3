from sys import argv

script, filename = argv

txt = open(filename)

print("Which file do you want to open? {}".format(filename))
print(txt.read())
txt.close()


#####################################
#print("Type the filename again:")
#file_again = input("> ")
#txt_again = open(file_again)
#print(txt_again.read())
#####################################





#####################################
#filename = input("Enter File name:")
#txt = open(filename)
#print(txt.read())
#####################################