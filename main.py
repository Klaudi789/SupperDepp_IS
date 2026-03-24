"""
Umsetzung der Superdepp-Aufgabe mittels Python
24.03.26 IGy25
"""

def main() -> None:
    #Lokale Variablen
    smsListe:[str] = ["SuperDepp =1", "superdepp= 3", "uperdepp=3", "sUperdepp 5", "superdepp = 7", "superdepp     =9"
"superdepp=    3", "Superdepp=7", "SUPERDEPP=7", "suppendepp=11", "hupersep= b", "superdepp=a", "sUperdep=c", "superdepp==7",
"superdepp-9", "superdepp 3", "superdepp..7", "pupersepp=7", "SUPERdepp= 3", "superDEPP= 5", "SUPERDEPP= 7", "SUPERDEPP= 9",
"SUPERDEPP= 7", "SUPERDEPP= 9", "SuPeRdEpP=11"]
    anzahlSmsListe: int = len(smsListe) #Anzahl abgegebener Stimmen
    smsOK:[str] = [] # leere Liste für güötige SMS-Einträge
    anzahlSmsOK: int = 0 # Anzahl gültiger Stimmen
    prozentSmsOK: float = 0.0 # Prozentsatz gültiger Stimmen
    kandidatenStimmenListe:[int] = [0,0,0,0,0,0,0,0,0,0,] # für 10 Kandidaten
    platzierungsListe:[int] = [] # leere Platzierungsliste

    # *********** Verarbeitung nach Syntaxgraph zu SupperDepp-Stimmen *****************
    for sms in smsListe:
        #Prüfung auf genau ein =-Zeichen
        if sms.count("=") ==1:
            if "superdepp" in sms.lower(): # Prüfung, dass Superdepp enthalten ist, egal ob Groß- oder Kleinschreibung
                teile = sms.split("=")
                if teile[1].strip().isdigit():
                    zahl:int = int(teile[1].strip())
                    if zahl >= 1 and zahl <=10:
                        smsOK.append(sms) # gültige SMS in Liste hinzufügen
                        kandidatenStimmenListe[zahl-1] += 1 # Kandidatenstimme hinzufügen

    anzahlSmsOK = len(smsOK) # ermittle Anzahl der gültigen Stimmen
    prozentSmsOK = anzahlSmsOK*100/anzahlSmsListe


    # Ausgabetext erstellen
    ausgabeText:str = "Auswertung Superdepp\n" + 20 * "*"
    ausgabeText += f"\nerhaltene SMS: {smsListe}\nmit {anzahlSmsListe} Eintragen"
    ausgabeText += f"\ngültige SMS: {smsOK}\nmit {anzahlSmsOK} Einträgen"
    ausgabeText += f"\ngültige SMS {prozentSmsOK} %"
    ausgabeText += f"\nKandidateiste mit Stimmenanzahl: {kandidatenStimmenListe}"
    ausgabeText += f"\nPlatzierungsliste mit Kandidatennummern: {platzierungsListe}"




    # Ausgabe
    print(ausgabeText)


# Einstiegspunkt Hauptprogramm
if __name__ == '__main__':
    main()