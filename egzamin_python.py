#zadanie 1
import math

def circle(r):
    return math.pi*r*r

def triangle(a,h):
    return a*h/2

def rectangle(a,b=-1):
    if b == -1:
        return a*a
    return a*b


def fields():
    figures=["kolo", "trojkat", "prostokat", "kwadrat"]
    fig_dict=dict()
    for i in range(4):
        fig_dict.update( {i+1 : figures[i]} )

    choice=-1
    print(fig_dict)
    while True:
        try:
            choice=int(input("Podaj nr figury: "))
        except ValueError:
            print("Bledna wartosc")
        if choice not in range(1,5):
            print("Bledny wybor - wybierz dostepny nr!")
            continue
        else:
            print("Wybrano " + fig_dict[choice])
            break

    n1, n2 = -1, -1
    if choice == 1:
        try:
            n1=float(input("Podaj promien: "))
            if n1 < 0:
                raise ValueError
            print("Pole figury <" + fig_dict[choice] + "> o podanych wartosciach wynosi " + str(circle(n1)))
        except ValueError:
            print("Podano niewlasciwa wartosc!")
    elif choice == 2:
        try:
            n1=float(input("Podaj dl podstawy: "))
            n2=float(input("Podaj wysokosc: "))
            if n1 < 0 or n2 < 0:
                raise ValueError
            print("Pole figury <" + fig_dict[choice] + "> o podanych wartosciach wynosi " + str(triangle(n1, n2)))
        except ValueError:
            print("Podano niewlasciwa wartosc!")
    elif choice == 3:
        try:
            n1=float(input("Podaj dl pierwszego boku: "))
            n2=float(input("Podaj dl drugiego boku: "))
            if n1 < 0 or n2 < 0:
                raise ValueError
            print("Pole figury <" + fig_dict[choice] + "> o podanych wartosciach wynosi " + str(rectangle(n1, n2)))
        except ValueError:
            print("Podano niewlasciwa wartosc!")
    elif choice == 4:
        try:
            n1=float(input("Podaj dl boku: "))
            if n1 < 0:
                raise ValueError
            print("Pole figury <" + fig_dict[choice] + "> o podanych wartosciach wynosi " + str(rectangle(n1)))
        except ValueError:
            print("Podano niewlasciwa wartosc!")


while True:
    fields()


