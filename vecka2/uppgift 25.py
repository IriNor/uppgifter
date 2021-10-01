"""1. Skriv en funktion som "vänder" en textsträng baklänges - utan att använda "reverse" (eller [::-1])!
Använd istället strängar eller listor, och en for-loop.
T.ex. "12345" blir "54321".

2. Skriv en funktion som tar in en textsträng, och returnerar antalet stora bokstäver i strängen.

3. Skriv en funktion som avgör om ett tal ligger mellan två andra tal.
t.ex.
inrange(value=1, min=2, max=3) blir False eftersom 1 ligger utan för 2 till 3.
inrange(value=10, min=0, max=100) blir True eftersom 10 ligger mellan 0 och 100."""


def listan(minlista):
    str = ""
    for i in minlista:
        str = i + str
    return str
minlista = "Det Här är En bra Dag!"

if __name__ == '__main__':
    print("rätt ord är ", end="")
    print(minlista)
    print(len(minlista), "bokstaver i en mening")

    print("andra är ", end="")
    print(listan(minlista))
    print(sum(map(str.isupper, minlista)))
    print(sum(map(str.islower, minlista)))

def range_s()->int:


    if __name__ == '__main__':
        range_s()
