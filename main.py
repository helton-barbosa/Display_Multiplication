number = int(input('Escolha um número inteiro: '))
count = 1

while count < 11:
    value = number * count
    print(f'{number} x {count} = {value}')
    count += 1
