# capsule.py

max_capsule = int(input())

if (max_capsule < 0):
    print('error')
else:
    if (max_capsule % 2 == 0):
        result = max_capsule / 2
        print(int(result))
    elif (max_capsule % 2 == 1):
        result = max_capsule / 2
        print(int(result + 1))
