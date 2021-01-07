#zadanie 2
import matplotlib.pyplot as plt

numbers=[]
while True:
    n = input("(aby wyjsc wprowadz slowo 'exit')\nPodaj dowolna liczbe: ")
    if n == 'exit':
        break
    try:
        n_f = float(n)
        numbers.append( n_f )
    except ValueError:
        print("Podales <" + str(len(numbers)) + "> liczb. Dalej sie nie bawie")
        break

for number in numbers:
    print(number)
if len(numbers) > 3:
    plt.plot( numbers, 'r.' )
    plt.show()

