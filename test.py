import tkinter as tk
from tkinter import messagebox, Toplevel, Label


def zeige_ergebnis(title, monate, total_zahlung, total_zinsen, monatliche_zinszahlung):
    """Öffnet ein separates Fenster für die Ergebnisanzeige."""
    ergebnis_fenster = Toplevel()
    ergebnis_fenster.title(title)
    ergebnis_fenster.geometry("400x400")
    ergebnis_fenster.configure(bg="#2c3e50")

    # Titel
    Label(ergebnis_fenster, text="🌟 Ergebnis", bg="#2c3e50", fg="#f1c40f", font=("Helvetica", 18, "bold")).pack(pady=20)

    # Laufzeit
    Label(ergebnis_fenster, text=f"📅 Die berechnete Laufzeit beträgt:", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack()
    Label(ergebnis_fenster, text=f"{monate} Monate", bg="#2c3e50", fg="#1abc9c", font=("Helvetica", 14, "bold")).pack(pady=10)

    # Gesamtbetrag der Zahlungen
    Label(ergebnis_fenster, text="💰 Gesamtbetrag der Zahlungen:", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack()
    Label(ergebnis_fenster, text=f"{round(total_zahlung, 2)} €", bg="#2c3e50", fg="#3498db", font=("Helvetica", 14, "bold")).pack(pady=10)

    # Gesamtbetrag der Zinsen
    Label(ergebnis_fenster, text="💸 Gesamtbetrag der Zinsen:", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack()
    Label(ergebnis_fenster, text=f"{round(total_zinsen, 2)} €", bg="#2c3e50", fg="#e74c3c", font=("Helvetica", 14, "bold")).pack(pady=10)

    # Monatlicher Anteil der Zinszahlung
    Label(ergebnis_fenster, text="📈 Monatlicher Anteil der Zinszahlung:", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack()
    Label(ergebnis_fenster, text=f"{round(monatliche_zinszahlung, 2)} €", bg="#2c3e50", fg="#f39c12", font=("Helvetica", 14, "bold")).pack(pady=10)

    # Schließen-Knopf
    tk.Button(
        ergebnis_fenster,
        text="Schließen",
        command=ergebnis_fenster.destroy,
        bg="#e74c3c",
        fg="white",
        font=("Helvetica", 12, "bold"),
    ).pack(pady=20)


def berechne_kredit():
    try:
        kredit = entry_kredit.get()
        zahlung = entry_monatlich.get()
        zinse = entry_zinsen.get()
        monate = entry_monate.get()

        # Konvertiere Eingaben zu Zahlen, falls vorhanden
        kredit = float(kredit) if kredit else None
        zahlung = float(zahlung) if zahlung else None
        zinse = float(zinse) if zinse else None
        monate = int(monate) if monate else None

        # Prüfe, ob mindestens drei Eingaben vorhanden sind
        eingaben = [kredit, zahlung, zinse, monate]
        if eingaben.count(None) > 1:
            messagebox.showerror("Fehler", "Bitte geben Sie mindestens drei Werte ein.")
            return

        # Berechnung
        if kredit is None:
            kredit = zahlung * monate / (1 + (zinse / 100 / 12) * monate)
            total_zahlung = zahlung * monate
            total_zinsen = total_zahlung - kredit
            monatliche_zinszahlung = total_zinsen / monate
            zeige_ergebnis("Berechnung abgeschlossen", monate, total_zahlung, total_zinsen, monatliche_zinszahlung)
        elif zahlung is None:
            zahlung = kredit / monate + (kredit * (zinse / 100 / 12))
            total_zahlung = zahlung * monate
            total_zinsen = total_zahlung - kredit
            monatliche_zinszahlung = kredit * (zinse / 100 / 12)
            zeige_ergebnis("Berechnung abgeschlossen", monate, total_zahlung, total_zinsen, monatliche_zinszahlung)
        elif zinse is None:
            zinse = ((zahlung * monate / kredit) - 1) * 12 * 100 / monate
            total_zahlung = zahlung * monate
            total_zinsen = total_zahlung - kredit
            monatliche_zinszahlung = total_zinsen / monate
            zeige_ergebnis("Berechnung abgeschlossen", monate, total_zahlung, total_zinsen, monatliche_zinszahlung)
        elif monate is None:
            monate = kredit / zahlung * (1 + (zinse / 100 / 12))
            total_zahlung = zahlung * monate
            total_zinsen = total_zahlung - kredit
            monatliche_zinszahlung = total_zinsen / monate
            zeige_ergebnis("Berechnung abgeschlossen", monate, total_zahlung, total_zinsen, monatliche_zinszahlung)

    except ValueError:
        messagebox.showerror("Fehler", "Bitte geben Sie gültige Zahlen ein.")
    except ZeroDivisionError:
        messagebox.showerror("Fehler", "Ungültige Eingabe. Division durch Null ist nicht erlaubt.")


# Hauptfenster
root = tk.Tk()
root.title("Kreditrechner mit fehlendem Faktor")
root.geometry("500x700")
root.configure(bg="#2c3e50")

tk.Label(root, text="Kredit Rechner", bg="#2c3e50", fg="#f1c40f", font=("Helvetica", 20, "bold")).pack(pady=20)

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

tk.Label(root, text="Anzahl der Monate:", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack(pady=5)
entry_monate = tk.Entry(root, font=("Helvetica", 12))
entry_monate.pack(pady=5)

# Berechnungsknopf
tk.Button(
    root, text="Berechnen", command=berechne_kredit, bg="#27ae60", fg="white", font=("Helvetica", 14)
).pack(pady=20)

# Hinweis
tk.Label(
    root,
    text="Bitte mindestens drei der oben genannten Felder ausfüllen.\nDer fehlende Wert wird berechnet.",
    bg="#2c3e50",
    fg="white",
    font=("Helvetica", 10),
    wraplength=400,
    justify="center",
).pack(pady=20)

root.mainloop()
