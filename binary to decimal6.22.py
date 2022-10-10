def into_decimal(data):
    decimal = 0
    j = 0
    while data != 0:
        decimal += int(data%10)*int(pow(2,j))
        j += 1
        data = data / 10
    return decimal
def into_octal(data):
    return oct(into_decimal(data))
data = input('Binary data :')
ch = input('Enter either D/O : ')
if ch=='D' or ch=='d':
    print('Decimal form :',into_decimal(int(data)))
elif ch=='O' or ch=='o':
    print('Octal form :',into_octal(int(data)))
