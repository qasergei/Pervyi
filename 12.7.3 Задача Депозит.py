money = int(input("Какую сумму вы хотели бы положить на депозит?"))
m = (round(money/100))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
tkb = (int(m*(per_cent['ТКБ'])))
skb = (int(m*(per_cent['СКБ'])))
vtb = (int(m*(per_cent['ВТБ'])))
sber = (int(m*(per_cent['СБЕР'])))
L = (list((tkb, skb, vtb, sber)))
print("Годовой процент по депозиту составит:", (list(("ТКБ:", (tkb)) + ("СКБ:", (skb)) + ("ВТБ:", (vtb)) + ("СБЕР:", (sber)))))
max = max(L)
print("Максимальная сумма, которую вы можете заработать:", (max))