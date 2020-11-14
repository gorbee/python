w = input().split(" ") # ЗП за месяц
c = input().split(" ") # стоимость продажи сыворотки
r = input().split(" ") # количесвто проданных миллилитров сыворотки

w1 = w[0]
w2 = w[1]
w3 = w[2]

c1 = c[0]
c2 = c[1]
c3 = c[2]

r1 = r[0]
r2 = r[1]
r3 = r[2]

w1 = int(w1)
w2 = int(w2)
w3 = int(w3)

c1 = int(c1)
c2 = int(c2)
c3 = int(c3)

r1 = int(r1)
r2 = int(r2)
r3 = int(r3)

income1 = c1 * r1 - w1
income2 = c2 * r2 - w2
income3 = c3 * r3 - w3

list_income = []
list_income.append(income1)
list_income.append(income2)
list_income.append(income3)

final_list_income = []

if (income1 <= 0) and (income2 <= 0) and (income3 <= 0):
    final_list_income.append('0')
elif (income1 > income2) and (income1 > income3):
    final_list_income.append('1')
elif (income2 > income1) and (income2 > income3):
    final_list_income.append('2')
elif (income3 > income1) and (income3 > income2):
    final_list_income.append('3')
elif (income1 == income2) and (income1 == income3):
    final_list_income.append('1')
    final_list_income.append('2')
    final_list_income.append('3')
elif (income1 == income2):
    final_list_income.append('1')
    final_list_income.append('2')
elif (income1 == income3):
    final_list_income.append('1')
    final_list_income.append('3')
elif (income2 == income3):
    final_list_income.append('2')
    final_list_income.append('3')
else:
    print('error')

len_final_list_income = len(final_list_income)

if len_final_list_income == 1:
    print(final_list_income[0])
elif len_final_list_income == 2:
    final_list_income = sorted(final_list_income)
    final_list_income1 = final_list_income[0]
    if (final_list_income1 == '0'):
        print(0)
    else:
        print(final_list_income[0], final_list_income[1])
elif len_final_list_income == 3:
    final_list_income = sorted(final_list_income)
    final_list_income1 = final_list_income[0]
    if (final_list_income1 == '0'):
        print(0)
    else:
        print(final_list_income[0], final_list_income[1], final_list_income[2])
else:
    print('error')
