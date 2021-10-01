import json

with open('massadata.json') as file:
    massadata = json.load(file)
print(len(massadata["entries"]))


def main():
    summa = 0
    for item in massadata['entries']:
        summa += item['total']
        print(summa)
#print(sum([delsum['entries']for delsum in massadata ['entries']]))

if __name__ == '__main__':
    main()