cash = int(input("Введите сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# список процентных ставок и банков
protcent = list(per_cent.values())
banks = list(per_cent.keys())
# доход в каждом банке
TKB = round(protcent[0]/100 * cash, 2)
CKB = round(protcent[1]/100 * cash, 2)
VTB = round(protcent[2]/100 * cash, 2)
SBER = round(protcent[3]/100 * cash, 2)
# возможный доход
deposit = [TKB, CKB, VTB, SBER]
print("Возможный доход:", deposit)
# найс трай
# print("Возможный доход:" banks[0], deposit[0], banks[1], deposit[1], banks[2], deposit[2], banks[3], deposit[3],)
# максимальный доход
index_max = deposit.index(max(deposit))
print("Максимальная сумма, которую вы можете заработать - в банке ", banks[index_max], "под процент",
      protcent[index_max], " сумму ", max(deposit))
