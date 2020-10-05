# guests.py

w = int(input('w: '))
t = int(input('t: '))

coord_1 = 0 # первая координатa x
coord_2 = 0 # вторая координата y 
time = 0 # общее время
# t = t + 1

final = coord_1, coord_2, time

while True:
    # 1 шаг
    coord_2 = coord_2 + w
    time = time + w
    if time > t:
        coord_2 = coord_2 - w
        break
    else:
        # 2 шаг
        coord_1 = coord_1 + 1
        time = time + 1
        if time > t:
            coord_1 = coord_1 - 1
            break
        else:
            # 3 шаг
            coord_2 = coord_2 - w
            time = time + w
            if time > t:
                coord_2 = coord_2 + w
                break
            else:
                # 4 шаг
                coord_1 = coord_1 + 1
                time = time + 1
                if time > t:
                    coord_1 = coord_1 - 1
                    break
                # else:
                    # continue

        
print('(' + str(coord_1) + ', ' + str(coord_2) + ')')
