file = open('Codingal.txt','r')
print(file.read())
file.close()

file = open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(5))   #will read character not lines
file.close()

file = open('Codingal.txt','a')
file.write("\n\n Hi! This is written by Maahekaan ")
file.close()