days = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
d = int(input("Skriv en siffra från 1 till 7 >>>"))
if d < 1 or d > 7:
    print("Kan skrivas siffror från 1 till 7")
else:
    print(f"dagen {d} är {days[d-1]}")
