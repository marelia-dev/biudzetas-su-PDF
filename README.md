# Biudžetas su PDF

**Programa asmeniniam / šeimos biudžeto valdymui su PDF ataskaitomis**

Paprasta ir patogi konsolinė Python programa, leidžianti vesti pajamas ir išlaidas, peržiūrėti balansą bei generuoti gražias PDF ataskaitas. Duomenys saugomi naudojant `pickle`.

## Galimybės

- Pridėti pajamas ir išlaidas
- Peržiūrėti operacijų žurnalą
- Skaičiuoti balansą
- Generuoti PDF ataskaitą
- Duomenų išsaugojimas tarp programos paleidimų (`pickle`)
- Paprastas meniu pagrindu veikiantis interfeisas
- Galimybė sukompiliuoti į `.exe` failą (PyInstaller)

## Technologijos

- **Python 3**
- `pickle` (duomenų serializacija)
- PDF generavimas (`reportlab` / `fpdf`)
- PyInstaller (`.exe` kūrimui)

## Kaip paleisti

```bash
# 1. Klonuoti repozitoriją
git clone https://github.com/marelia-dev/biudzetas-su-PDF.git
cd biudzetas-su-PDF

# 2. Paleisti programą
python biudzetas.py
