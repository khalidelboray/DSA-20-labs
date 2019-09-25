
num = int(input(" Input start number : "))
final = []
for i in range(1,num + 1):
    table = []
    for k in range(1,i+1):
        table.append(i*k)
    final.append(table)    
print(final) 