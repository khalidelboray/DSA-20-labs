

def locate_loop(string,chr):
    indexes = []
    for i in range(0,len(string)):
        if string[i] == chr:
            indexes.append(i)
    return indexes

print(locate_loop("Hello Thereo","o"))