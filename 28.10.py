"""
Jednoduchá ruleta v Pythone (funguje v termináli / PyCharme).

Pravidlá:
- Môžeš staviť na:
    1) číslo (0–36)
    2) farbu: 'cervena' alebo 'cierna'
    3) 'parne' alebo 'neparne'
- Výhry:
    - číslo → 35:1
    - farba → 1:1
    - parne/neparne → 1:1
"""

import random
import time

# Červené a čierne čísla podľa európskej rulety
CERVENE = {1, 3, 5, 7, 9, 12, 14, 16, 18,
           19, 21, 23, 25, 27, 30, 32, 34, 36}
CIERNE = {2, 4, 6, 8, 10, 11, 13, 15, 17,
          20, 22, 24, 26, 28, 29, 31, 33, 35}


def roztoct_ruletu():
    cislo = random.randint(0, 36)
    if cislo == 0:
        farba = 'zelena'
    elif cislo in CERVENE:
        farba = 'cervena'
    else:
        farba = 'cierna'
    return cislo, farba


def ruleta():
    bank = 100
    print("🎰 Vitaj v rulete! Máš 100 $.")

    while bank > 0:
        print(f"\nTvoj aktuálny bank: {bank} $")
        try:
            stavka = int(input("Zadaj výšku stávky (0 pre koniec): "))
        except ValueError:
            print("❌ Zadaj číslo.")
            continue

        if stavka == 0:
            print("👋 Koniec hry. Ďakujeme za hranie!")
            break
        if stavka > bank or stavka < 0:
            print("❌ Neplatná stávka.")
            continue

        print("\nTyp stávky:")
        print("1 - Číslo (0-36)")
        print("2 - Farba (cervena / cierna)")
        print("3 - Párne / Nepárne")
        typ = input("Vyber (1/2/3): ")

        if typ == '1':
            try:
                volba = int(input("Zvoľ číslo (0-36): "))
                if not (0 <= volba <= 36):
                    raise ValueError
            except ValueError:
                print("❌ Zadaj číslo 0–36.")
                continue

        elif typ == '2':
            volba = input("Zvoľ farbu (cervena/cierna): ").lower()
            if volba not in ['cervena', 'cierna']:
                print("❌ Neplatná farba.")
                continue

        elif typ == '3':
            volba = input("Párne alebo nepárne? (parne/neparne): ").lower()
            if volba not in ['parne', 'neparne']:
                print("❌ Neplatná voľba.")
                continue
        else:
            print("❌ Neplatná voľba.")
            continue

        print("\n🎡 Roztočenie rulety...")
        time.sleep(1.5)
        cislo, farba = roztoct_ruletu()
        print(f"➡️ Výsledok: {cislo} ({farba})")

        vyhra = 0

        # vyhodnotenie výsledku
        if typ == '1':
            if cislo == volba:
                vyhra = stavka * 35
                print(f"💰 Trafené číslo! Vyhrávaš {vyhra} $.")
            else:
                print("❌ Netriafol si číslo.")

        elif typ == '2':
            if farba == volba:
                vyhra = stavka
                print(f"✅ Trafená farba! Vyhrávaš {vyhra} $.")
            else:
                print("❌ Netriafol si farbu.")

        elif typ == '3':
            if cislo == 0:
                print("❌ Padla nula – prehrávaš.")
            elif (cislo % 2 == 0 and volba == 'parne') or (cislo % 2 == 1 and volba == 'neparne'):
                vyhra = stavka
                print(f"✅ Trafené! Vyhrávaš {vyhra} $.")
            else:
                print("❌ Zle, prehrávaš.")

        # aktualizácia banku
        bank += vyhra - stavka

        if bank <= 0:
            print("\n💸 Prehral si všetky peniaze! Hra končí.")
            break

    print("\n🎲 Ďakujeme za hranie rulety!")


if __name__ == '__main__':
    ruleta()
