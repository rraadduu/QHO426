#Open file for reading
f = open("song.txt")
#Print full content
#print(f.read())
#Read line by line
#Print a line
#print(f.readline())#first line
#print(f.readline())#second line...same code
#Grabing content of a txt file and return it as a list...act by index
lista = f.readlines()
print(lista)
f.close()

#open for writing..apend
g = open("song.txt", "a")
#g.write("\nAnd it's everlasting, infinitye\n")
g.writelines(["It goes on and on, you can't measure it\n", "Can't quench your love"])
g.close()