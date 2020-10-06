# Если номер дома четный, то к следующему (нечетному) идти 1 минуту, а к предыдущему (нечетному) 0 минут.
# Если номер дома нечетный, то к следующему (четному) дома идти 0 минут, а к предыдущему (четному) 1 минуту.

a = int(input('Дом #1: '))
b = int(input('Дом #2: '))

n_list = list(range(a, b+1))

if (a <= 0) or (b <= 0):
    print('error')
elif (a == b):
    n = 0
    print(int(abs(n)))
else:
    if (a % 2 == 0):
        # Дом A четный
        if (b % 2 == 0):
            # Дом B четный
            n = (b - a) / 2
            print(int(abs(n)))
        elif (b % 2 == 1):
            # Дом B нечетный
            n = (b - a) // 2 + 1
            print(int(abs(n)))
    elif (a % 2 == 1):
        # Дом А нечетный
        if (b % 2 == 0) or (b % 2 == 1):
            # Дом B четный или нечетный
            if (b < a):
                if (b % 2 == 0):
                    # Дом B четный
                    n = (b - a) // 2
                    print(int(abs(n)))
                elif (b % 2 == 1):
                    # Дом B нечетный
                    n = (b - a) // -2
                    print(int(abs(n)))
            elif (b == n_list[1]):
                n = 0
                print(int(abs(n)))
            else:
                n = (b - a) // 2
                print(int(abs(n)))
