import tkinter as tk
from tkinter import messagebox


def berechne_kredit():
    try:
        kredit = float(entry_kredit.get())
        zahlung = float(entry_monatlich.get())
        zinse = float(entry_zinsen.get())

        if zahlung <= 0 or kredit <= 0 or zinse <= 0:
            messagebox.showerror("Fehler", "Bitte geben Sie gültige positive Werte ein.")
            return

        monatliche_zinsen = []
        übrig_kredit = []
        netto_zahlung = []
        ergebnis = []

        while True:
            zinsen = ((kredit * zinse) / 100) / 12
            if zahlung > zinsen:
                if kredit > zahlung:
                    netto_z = zahlung - zinsen
                    restschuld = kredit - netto_z
                    kredit = restschuld
                    monatliche_zinsen.append(round(zinsen, 2))
                    übrig_kredit.append(round(kredit, 2))
                    netto_zahlung.append(round(netto_z, 2))
                else:
                    restzahlung = kredit
                    zzz = sum(monatliche_zinsen)
                    monate = len(übrig_kredit) + 1
                    jahre = round(monate / 12, 1)

                    ergebnis.append(f"Restzahlung: {round(restzahlung, 2)} €")
                    ergebnis.append(f"Dauer: {jahre} Jahre ({monate} Monate)")
                    ergebnis.append(f"Gesamtzinsen: {round(zzz, 2)} €")

                    ergebnis_anzeige(ergebnis, monatliche_zinsen, netto_zahlung, übrig_kredit)
                    break
            else:
                messagebox.showerror(
                    "Fehler", "Die monatliche Zahlung reicht nicht aus, bitte erhöhen Sie den Betrag."
                )
                break
    except ValueError:
        messagebox.showerror("Fehler", "Bitte geben Sie gültige Zahlen ein.")


def ergebnis_anzeige(ergebnis, monatliche_zinsen, netto_zahlung, übrig_kredit):
    ergebnis_fenster = tk.Toplevel(root)
    ergebnis_fenster.title("Kredit Ergebnis")
    ergebnis_fenster.geometry("400x400")
    ergebnis_fenster.configure(bg="#ecf0f1")

    for zeile in ergebnis:
        tk.Label(ergebnis_fenster, text=zeile, bg="#ecf0f1", font=("Helvetica", 12)).pack(pady=5)

    def details_anzeigen(titel, daten):
        detail_fenster = tk.Toplevel(ergebnis_fenster)
        detail_fenster.title(titel)
        detail_fenster.geometry("400x400")
        detail_fenster.configure(bg="#ecf0f1")

        for index, wert in enumerate(daten, 1):
            tk.Label(detail_fenster, text=f"Monat {index}: {wert}", bg="#ecf0f1", font=("Helvetica", 10)).pack(pady=2)

    tk.Button(
        ergebnis_fenster,
        text="Monatliche Zinsen anzeigen",
        command=lambda: details_anzeigen("Monatliche Zinsen", monatliche_zinsen),
        bg="#2980b9",
        fg="white",
        font=("Helvetica", 10),
    ).pack(pady=5)

    tk.Button(
        ergebnis_fenster,
        text="Nettozahlungen anzeigen",
        command=lambda: details_anzeigen("Nettozahlungen", netto_zahlung),
        bg="#27ae60",
        fg="white",
        font=("Helvetica", 10),
    ).pack(pady=5)

    tk.Button(
        ergebnis_fenster,
        text="Übrige Kredite anzeigen",
        command=lambda: details_anzeigen("Übrige Kredite", übrig_kredit),
        bg="#e67e22",
        fg="white",
        font=("Helvetica", 10),
    ).pack(pady=5)


# Hauptfenster
root = tk.Tk()
root.title("Kreditrechner")
root.geometry("500x500")
root.configure(bg="#2c3e50")

tk.Label(root, text="Kredit Rechner", bg="#2c3e50", fg="white", font=("Helvetica", 16)).pack(pady=20)

# Eingabefelder
tk.Label(root, text="Kreditsumme (€):", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack(pady=5)
entry_kredit = tk.Entry(root, font=("Helvetica", 12))
entry_kredit.pack(pady=5)

tk.Label(root, text="Monatliche Zahlung (€):", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack(pady=5)
entry_monatlich = tk.Entry(root, font=("Helvetica", 12))
entry_monatlich.pack(pady=5)

tk.Label(root, text="Jährlicher Zinssatz (%):", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack(pady=5)
entry_zinsen = tk.Entry(root, font=("Helvetica", 12))
entry_zinsen.pack(pady=5)

# Berechnungsknopf
tk.Button(
    root, text="Berechnen", command=berechne_kredit, bg="#27ae60", fg="white", font=("Helvetica", 14)
).pack(pady=20)

root.mainloop()
