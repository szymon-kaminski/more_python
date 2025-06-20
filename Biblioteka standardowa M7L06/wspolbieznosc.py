print("Przykład 1")

import time

def pobierz_dane():
    print("Pobieram dane...")
    time.sleep(3)
    print("Dane pobrane")
    return "Dane"

def main():
    wynik = pobierz_dane()
    print("Zrobiłem coś po pobraniu:", wynik)

if __name__ == "__main__":
    main()


print("Przykład 2")

import asyncio

async def pobierz_dane():
    print("Pobieram dane...")
    await asyncio.sleep(3)
    print("Dane pobrane")
    return "DANE"

async def main():
    wynik = await pobierz_dane()
    print("Zrobiłem coś po pobraniu", wynik)

asyncio.run(main())


print("Przykład 3")

import asyncio

async def zadanie(n):
    print(f"Zadanie {n} startuje")
    await asyncio.sleep(2)
    print(f"Zadanie {n} kończy")

async def main():
    await asyncio.gather(
        zadanie(1),
        zadanie(2),
        zadanie(3)
    )

asyncio.run(main())


print("Przykład 4")

import asyncio

async def fetch_data(id):
    print(f"[{id}] Start pobierania")
    await asyncio.sleep(1)
    print(f"[{id}] Dane pobrane")
    return f"Dane-{id}"

async def main():
    wyniki = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print("Wszystkie wyniki:", wyniki)

asyncio.run(main())