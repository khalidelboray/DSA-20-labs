length = int(input("Input number : "))
for i in range(0,length+1):
    print(' ' * (length - i), end = '')
    print('*' * i )
