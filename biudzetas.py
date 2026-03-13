from operacijos.saskaita import saskaita
from operacijos.sukurti_pdf_ataskaita import SukurtiPdfAtaskaita
import traceback

def gauti_skaiciu(pranesimas: str) -> int:
    while True:
        try:
            ivestis = input(pranesimas).strip()
            if not ivestis:
                print("Iveskite skaiciu!")
                continue
            return int(ivestis)
        except ValueError:
            print("Klaida: iveskite sveikaji skaiciu!")

while True:
    veiksmas = gauti_skaiciu(
        "\n1 - peržiūrėti zurnala\n"
        "2 - pridėti pajamas\n"
        "3 - pridėti išlaidas\n"
        "4 - balansas\n"
        "5 - sukurti pdf ataskaita\n"
        "0 - išeiti\n"
        "→ "
    )
    match veiksmas:
        case 1:
            if not saskaita.zurnalas:
                print("Zurnale nera irasu")
            else:
                print("\nZurnalo irasai:")
                for nr, irasas in enumerate(saskaita.zurnalas, 1):
                    print(f"{nr}. {irasas}")
        case 2:
            saskaita.prideti_pajamas()
        case 3:
            saskaita.prideti_islaidas()
        case 4:
            saskaita.paskaiciuoti_balansa()
        case 5:
            failo_pavad = input("Įveskite PDF failo pavadinimą (arba Enter — saskaitos_ataskaita.pdf): ").strip()
            if not failo_pavad:
                failo_pavad = "saskaitos_ataskaita.pdf"
            elif not failo_pavad.lower().endswith(".pdf"):
                failo_pavad += ".pdf"
            SukurtiPdfAtaskaita.sukurti(saskaita, failo_pavad)
        case 0:
            print("Viso gero!")
            break
        case _:
            print("Tokio pasirinkimo nera!")

