#zadanie 3
temp = input("Podaj produkty oddzielone przecinkiem (bez spacji):\n ")
s_list = temp.split(",")
s_set = set(s_list)
s_dict = dict()
for product in s_set:
    try:
        price = float(input("Podaj cene produktu <" + product + ">:"))
        if price < 0:
            raise ValueError    
    except ValueError:
        price = 0
    s_dict.update( {product.upper() : price} )

print(s_dict)

s_sum = 0
for value in s_dict.values():
    s_sum += value
if s_sum > 100:
    print("Suma wartosci produktow: " + str(s_sum) + "\nNie mozesz zakupic wszystkich z wymienionych produkow")
