"""
Umsetzung der Superdepp-Aufgabe mittels Python
24.03.26 IGy25
"""

def main() -> None:
    #Lokale Variablen
    smsListe:[str] = ["SuperDepp =1", "superdepp= 3", "sUperdepp 5", "superdepp = 7", "superdepp = 9"
"superdepp= 3", "Superdepp=7", "SUPERDEPP=7", "suppendepp=11", "hupersep= b", "superdepp=a", "sUperdep=c", "superdepp==7",
"superdepp-9", "superdepp 3", "superdepp..7", "pupersepp=7", "SUPERdepp= 3", "superDEPP= 5", "SUPERDEPP= 7", "SUPERDEPP= 9",
"SUPERDEPP= 7", "SUPERDEPP= 9", "SuPeRdEpP=9"]
    anzahlSmsListe: int = len(smsListe)
    smsOK:[str] = []
    anzahlSmsOK: int = 0
    prozentSmsOK: float = 0.0

    ausgabe:str = "Auswertung Superdepp\n" + 20 * "*"
    ausgabe += f"\nerhaltene SMS: {smsListe}\nmit {anzahlSmsListe} Eintragen"
    ausgabe += f"\ngültige SMS: {sms0K}\nmit {anzahlSmsOK} Einträgen"
    ausgabe += f"\ngültige SMS \[\%\]{prozentSmsOK}"


    print(ausgabe)



# Einstiegspunkt Hauptprogramm
if __name__ == '__main__':
    main()