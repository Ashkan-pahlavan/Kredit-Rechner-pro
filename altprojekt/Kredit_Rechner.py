import os
import tkinter as tk
os.system('cls')

def kradit_rechner():
    try:
        print("           ***   wilkommen zum kredit rechner program :)   *** ")
        kredit = float(input("Geben  Sie hier ein wie viel Kredit Sie benötigen: "))
        zahlung = float(input("wie viel können Sie monatlich bezahlen : "))
        zinse = float(input("geben Sie den jährlichen Zinsen Ihrer Bank ein : "))
        monatlichezinsen = []
        übrigKredit = []
        nettoZahlung = []
        while True:
            zinsen = ((kredit * zinse) / 100) / 12
            if zahlung > zinsen:
                if kredit > zahlung:
                    nettoZ = zahlung - zinsen
                    restschuld = kredit - nettoZ
                    kredit = restschuld
                    monatlichezinsen.append(round(zinsen,1))
                    übrigKredit.append(round(kredit,1))
                    nettoZahlung.append(round(nettoZ,1))
                else:
                    restzahlung = kredit 
                    zzz = sum(monatlichezinsen)
                    z = len(übrigKredit)
                    print(f"sie sollen {z + 1} Monaten weiter bezahlen")
                    print(f" * Ihre letzte Zahlung wird {round(restzahlung,2)} € ")
                    print(f"es wird {round(z / 12,1)} Jahre dauern")
                    print(f"Sie bezahlen insgesamt {round(zzz)} € Zinsen ")
                    user_input1 = input("wollen Sie wissen wie viel  zahlen Sie an Zinsen monatlich? : j/n " )
                    if user_input1 == "j":
                        counter_list1 = list(enumerate(monatlichezinsen, 1))
                        print(counter_list1)
                    else:
                        print("nächte Frage")
                    user_input2 = input("wollen Sie wissen wie viel  zahlen Sie Netto jeden Monat? : j/n " )
                    if user_input2 == "j":
                        counter_list2 = list(enumerate(nettoZahlung, 1))
                        print(counter_list2)
                    else:
                        print("letzte Frage")
                    user_input3 = input("wollen Sie wissen wie viel vom Kredit Netto monatlich übrig bleibt? : j/n " )
                    if user_input3 == "j":
                        counter_list3 = list(enumerate(übrigKredit, 1))
                        print(counter_list3)
                    else:
                        print("danke für Ihre Nachfrage, viel spass mit Kredit :)")
                        break
                    print("           ***   danke für Ihre Nachfrage, viel spass mit Kredit :)   ***")
                    break
            else:
                print("Sie sollen mehr monatlich zahlen so ist es leider nicht Gültig(probieren es bitte nochmal!)")
                break
    except ValueError: 
        print("Eingabe nicht Gültig, bitte geben Sie nur ein Zahl !")
        kradit_rechner()


kradit_rechner()