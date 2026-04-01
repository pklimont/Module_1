from dataclasses import dataclass
from typing import List

@dataclass
class Produkt:
    nazwa: str
    cena_za_kg: float
    ilosc_kg: float = 1.0

    def wartosc(self) -> float:
        return self.cena_za_kg * self.ilosc_kg


class Koszyk:
    def __init__(self, produkty: List[Produkt]):
        self._produkty = produkty

    def suma(self) -> float:
        return sum(p.wartosc() for p in self._produkty)

    def produkty(self) -> List[Produkt]:
        return self._produkty


class GeneratorRaportu:
    def generuj(self, koszyk: Koszyk) -> str:
        linie = ["RAPORT ZAKUPÓW SERÓW:\n"]

        for p in koszyk.produkty():
            linie.append(
                f"{p.nazwa:15} {p.ilosc_kg:.0f} kg × {p.cena_za_kg:.2f} zł = {p.wartosc():.2f} zł"
            )

        linie.append(f"\nŁĄCZNA KWOTA: {koszyk.suma():.2f} zł")
        return "\n".join(linie)


# Tworzenie obiektów produktów
produkty = [
    Produkt("Roquefort", 12.50),
    Produkt("Stilton", 11.24),
    Produkt("Brie", 9.30),
    Produkt("Gouda", 8.55),
    Produkt("Edam", 11.00),
    Produkt("Parmezan", 16.50),
    Produkt("Mozzarella", 14.00),
    Produkt("Ser owczy", 122.32),
]

# Użycie
koszyk = Koszyk(produkty)
raport = GeneratorRaportu().generuj(koszyk)

print(raport)

