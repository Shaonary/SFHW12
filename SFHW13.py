
# ticket_q = int(input('введите кол-во билетов '))
# age = [int(input('введите возраст ')) for i in range(ticket_q)]
# summa = 0
# for years in age:
#     if years < 18:
#         summa += 0
#     elif 18 <= years < 25:
#         summa += 990
#     elif years >= 25:
#         summa += 1390
# # summa = (count_1*0 + count_2*990 + count_3*1390)
# if ticket_q > 3:
#     print(summa*0.9)
# else:
#     print(summa)

ticket_q = int(input('Введите кол-во билетов: '))       # вводим кол-во билетов
if ticket_q <= 0:                                       # если билетов 0 или отрицательное значение завершение программы
    raise SystemExit("Укажите верное значение!")
age = [int(input('Введите возраст гостя '+str(i+1)+" ")) for i in range(ticket_q)] # вводим возраст каждого гостя
summa = 0                                               # счетчик суммы билетов
for years in age:                                       # цикл, в котором рассчитывается стоимость билетов,
    if years in range(18, 25):                          # в зависимости от возраста гостя
        summa += 990
        print("Билет для студентов 990")
    elif years >= 25:
        summa += 1390
        print("Взрослый билет 1390")
    elif years in range(0, 18):
        print("Детские билеты бесплатно")
    else:
        raise SystemExit("Указан неверный возраст")     # если возраст отрицательный завершение программы
if ticket_q > 3:                                        # если билетов больше трех скидка 10%
    summa = summa*0.9
    print("Общая скидка 10%")
print("Итого:", summa)
