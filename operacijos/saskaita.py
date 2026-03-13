import pickle

from operacijos.sukurti_pdf_ataskaita import SukurtiPdfAtaskaita
from operacijos.pajamos import Pajamos
from operacijos.islaidos import Islaidos


class Saskaita:
    def __init__(self):
        self.zurnalas = self.nuskaityti()

    def irasyti(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def nuskaityti(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def prideti_pajamas(self):
        while True:
            try:
                suma_str = input("Suma: ").strip()
                if not suma_str:
                    print("Suma negali buti tuscia!")
                    continue

                suma = int(suma_str)
                siuntejas = input("Siuntėjas: ").strip()
                if not siuntejas:
                    print("Siuntejas negali buti tuscias!")
                    continue

                info = input("Papildoma informacija: ").strip()

                pajamos = Pajamos(suma, siuntejas, info)
                self.zurnalas.append(pajamos)
                self.irasyti()
                print("Pajamos pridetos sekmingai!")
                break

            except ValueError:
                print("Klaida: suma turi buti sveikasis skaicius! Bandykite dar karta.")
            except Exception as e:
                print(f"Klaida: {e}. Bandykite dar karta.")

    def prideti_islaidas(self):
        while True:
            try:
                suma_str = input("Suma: ").strip()
                if not suma_str:
                    print("Suma negali buti tuscia!")
                    continue

                suma = int(suma_str)
                isigyta = input("Įsigyta prekė/paslauga: ").strip()
                if not isigyta:
                    print("Isigyta preke/paslauga negali buti tuscia!")
                    continue

                info = input("Papildoma informacija: ").strip()

                islaidos = Islaidos(suma, isigyta, info)
                self.zurnalas.append(islaidos)
                self.irasyti()
                print("Islaidos pridetos sekmingai!")
                break

            except ValueError:
                print("Klaida: suma turi buti sveikasis skaicius! Bandykite dar karta.")
            except Exception as e:
                print(f"Klaida: {e}. Bandykite dar karta.")

    def paskaiciuoti_balansa(self):
        if not self.zurnalas:
            print("Zurnale nera irasu.")
            return

        print("\nZurnalo irasai:")
        print("-" * 70)
        print(f"{'Nr.':<4} {'Tipas':<12} {'Nuo/Uz ka':<20} {'Suma':<12} {'Info':<20}")
        print("-" * 70)

        balansas = 0

        for nr, irasas in enumerate(self.zurnalas, 1):
            tipas = "PAJAMOS" if isinstance(irasas, Pajamos) else "ISLAIDOS"
            is_ko = irasas.siuntejas if isinstance(irasas, Pajamos) else irasas.isigyta
            suma_zenklu = f"+{irasas.suma}" if isinstance(irasas, Pajamos) else f"-{irasas.suma}"
            info = irasas.info if irasas.info else "-"

            print(f"{nr:<4} {tipas:<12} {is_ko:<20} {suma_zenklu:<12} {info:<20}")

            if isinstance(irasas, Pajamos):
                balansas += irasas.suma
            else:
                balansas -= irasas.suma

        print("-" * 70)
        print(f"Bendras balansas: {balansas} €")


saskaita = Saskaita()