price = []
bil = int(input("Сколько билетов вы желаете приобрести"))
for i in range(1, bil + 1):
    age = int(input(f"Возраст посетителя для билета № {i}"))
    print(age)
    if age < 18:
        price.append(0)
    elif 18 <= age <= 25:
        price.append(990)
    else:
        price.append(1390)
if bil > 3:
    s = sum(price) - sum(price) * 0.1
    print("Общая стоимость билетов, с учетом скидки:", s)
else:
    a = sum(price)
    print("Общая стоимость билетов:", a)
