"""1. Skriv en funktion som beräknar maximum (=största värdet) av tre tal (utan att använda max()!)
2. Skriv en funktion som summerar alla tal i en lista. Inbyggda funktionen sum() ska ej användas
3. Skriv en funktion som räknar ut produkten (=multiplikation av alla tal) av en lista av heltal"""

def max_tal(x:int, y: int, z: int) -> int:

    if x > y and x > z:
        return x
    elif z > y and z > x:
        return z
    else:
        return y


if __name__ == '__main__':
    assert max_tal(3, 2, 5) == 5
    assert max_tal(45, 5, 34) == 45



