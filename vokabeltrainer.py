import csv
import random

class Vokabeltrainer:
    def __init__(self, datei):
        self.datei = datei
        self.vokabeln = []
        self.falsche_vokabeln = {}
        self.lade_vokabeln()

    def lade_vokabeln(self):
        with open(self.datei, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            self.vokabeln = [row for row in reader]

    def abfrage(self):
        richtige = 0
        falsche = 0
        for latein, deutsch in random.sample(self.vokabeln, len(self.vokabeln)):
            antwort = input(f"Übersetze: {latein} -> ")
            if antwort.strip().lower() == deutsch.lower():
                print("Richtig!")
                richtige += 1
            else:
                print(f"Falsch! Die richtige Antwort ist: {deutsch}")
                falsche += 1
                self.falsche_vokabeln[latein] = deutsch

        self.ergebnis(richtige, falsche)

    def ergebnis(self, richtige, falsche):
        gesamt = richtige + falsche
        prozent = (richtige / gesamt) * 100
        print(f"\nDu hast {richtige} von {gesamt} richtig ({prozent:.2f}%).")
        print("Falsche Vokabeln werden erneut abgefragt.")
        self.falsche_abfrage()

    def falsche_abfrage(self):
        if not self.falsche_vokabeln:
            print("Alle Vokabeln sind richtig beantwortet!")
            return

        for latein, deutsch in self.falsche_vokabeln.items():
            antwort = input(f"Nochmal: {latein} -> ")
            if antwort.strip().lower() == deutsch.lower():
                print("Richtig!")
            else:
                print(f"Falsch! Die richtige Antwort ist: {deutsch}")

if __name__ == "__main__":
    trainer = Vokabeltrainer("vokabeln.csv")
    trainer.abfrage()

