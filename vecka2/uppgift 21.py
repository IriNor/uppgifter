"""Skapa funktioner som:

1)  Kvadrerar ett tal n, kalla funktionen square
exempel:
square(1) -> 1
square(2) -> 4
square(3) -> 9
square(4) -> 16
2) Räknar ut omkretsen på en cirkel givet radien r
circumference(2) -> 12.5664
3) Räknar ut radien på en cirkel givet omkretsen
radius(12.5664) -> 2
4) Räknar ut fakultet för ett tal n
Fakultet är produkten av alla tal från 1 till talet n, skrivs i matematiken med ett !, exempel:
5! som är 1*2*3*4*5 = 120
3! är 1*2*3 = 6
Den engelska termen för fakultet är factorial så det är ett lämpligt funktionsnamn"""

def square(n: int)->int:
    return n*n


def circle_omkretsen(n: int)-> int:
    p = 3.14159
    return 2 * p * n


def circle_radien(n: int) -> int:
    p = 3.14159
    c_o = 12.56636
    return c_o / p / n

if __name__ == '__main__':
    print(square(1))
    print(square(2))
    print(square(3))
    print(square(4))
    print(circle_omkretsen(2))
    print(circle_radien(2))

factorial = 1
n = input("Skriv ett nummer: ")

if int(n) >= 1:
    for i in range(1, int(n)+1):
        factorial = factorial * i

if __name__ == '__main__':
 print("! av ", n, " är : ", factorial)