

def locate_loop(string,chr):
    indexes = []
    for i in range(0,len(string)):
        if string[i] == chr:
            indexes.append(i)
    return indexes

string = input(" Input your string : ")
char =  input( " Input char to look for : ")
indexes = locate_loop(string,char)
print(" Found {} at {}".format(char,indexes))