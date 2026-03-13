from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime
from operacijos.pajamos import Pajamos
from operacijos.islaidos import Islaidos


class SukurtiPdfAtaskaita:
    @staticmethod
    def sukurti(saskaita, failo_pavadinimas="saskaitos_ataskaita.pdf"):
        if not saskaita.zurnalas:
            print("Zurnale nėra irašų — PDF nesukurtas.")
            return

        c = canvas.Canvas(failo_pavadinimas, pagesize=letter)
        width, height = letter

        # font Helvetica
        c.setFont("Helvetica-Bold", 16)
        c.drawString(1 * inch, height - 1 * inch, "Saskaitos Zurnalas")
        c.setFont("Helvetica", 12)
        c.drawString(1 * inch, height - 1.3 * inch, f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Lentele
        y = height - 2 * inch
        c.setFont("Helvetica-Bold", 12)
        c.drawString(1 * inch, y, "Nr.")
        c.drawString(1.5 * inch, y, "Tipas")
        c.drawString(2.8 * inch, y, "Nuo/Uz ka")
        c.drawString(5.0 * inch, y, "Suma")
        c.drawString(6.0 * inch, y, "Info")
        y -= 0.3 * inch
        c.line(1 * inch, y + 0.15 * inch, 7.5 * inch, y + 0.15 * inch)

        # uzpildom lentele
        balansas = 0
        c.setFont("Helvetica", 10)
        for nr, irasas in enumerate(saskaita.zurnalas, 1):
            y -= 0.25 * inch
            tipas = "PAJAMOS" if isinstance(irasas, Pajamos) else "ISLAIDOS"
            is_ko = irasas.siuntejas if isinstance(irasas, Pajamos) else irasas.isigyta
            if isinstance(irasas, Pajamos):
                suma = f"+{irasas.suma:.2f} €"
                balansas += irasas.suma
            else:
                suma = f"-{irasas.suma:.2f} €"
                balansas -= irasas.suma

            info = irasas.info if irasas.info else "-"

            c.drawString(1 * inch, y, str(nr))
            c.drawString(1.5 * inch, y, tipas)
            c.drawString(2.8 * inch, y, is_ko[:30])
            c.drawString(5.0 * inch, y, suma)
            c.drawString(6.0 * inch, y, info[:30])

            if y < 1 * inch:
                c.showPage()
                y = height - 1 * inch

        # resultatas
        y -= 0.5 * inch
        c.setFont("Helvetica-Bold", 12)
        c.drawString(1 * inch, y, f"Bendras balansas: {balansas:.2f} €")

        c.save()
        print(f"PDF ataskaita sukurta: {failo_pavadinimas}")