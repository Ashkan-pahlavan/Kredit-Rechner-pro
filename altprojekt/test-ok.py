import tkinter as tk
from tkinter import messagebox, Toplevel, Label


def zeige_ergebnis(title, fehlender_wert, fehlender_wert_text, monate, total_zahlung, total_zinsen, monatliche_zinszahlung):
    """نمایش نتیجه در یک پنجره جداگانه با اطلاعات کامل و رنگ‌ها."""
    ergebnis_fenster = Toplevel()
    ergebnis_fenster.title(title)
    ergebnis_fenster.geometry("450x500")
    ergebnis_fenster.configure(bg="#2c3e50")

    # عنوان نتیجه
    Label(ergebnis_fenster, text="🌟 Ergebnis", bg="#2c3e50", fg="#f1c40f", font=("Helvetica", 18, "bold")).pack(pady=20)

    # پارامتر محاسبه شده
    Label(ergebnis_fenster, text=f"🔍 {fehlender_wert_text}:", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack()
    Label(ergebnis_fenster, text=f"{round(fehlender_wert, 2)}", bg="#2c3e50", fg="#e74c3c", font=("Helvetica", 14, "bold")).pack(pady=10)

    # مدت زمان
    Label(ergebnis_fenster, text="⏳ Laufzeit:", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack()
    Label(ergebnis_fenster, text=f"{round(monate)} Monate", bg="#2c3e50", fg="#1abc9c", font=("Helvetica", 14, "bold")).pack(pady=10)

    # کل پرداخت‌ها
    Label(ergebnis_fenster, text="💰 Gesamtbetrag der Zahlungen:", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack()
    Label(ergebnis_fenster, text=f"{round(total_zahlung, 2)} €", bg="#2c3e50", fg="#3498db", font=("Helvetica", 14, "bold")).pack(pady=10)

    # کل سود
    Label(ergebnis_fenster, text="💸 Gesamtbetrag der Zinsen:", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack()
    Label(ergebnis_fenster, text=f"{round(total_zinsen, 2)} €", bg="#2c3e50", fg="#e74c3c", font=("Helvetica", 14, "bold")).pack(pady=10)

    # سهم ماهانه سود
    Label(ergebnis_fenster, text="📈 Monatlicher Anteil der Zinszahlung:", bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack()
    Label(ergebnis_fenster, text=f"{round(monatliche_zinszahlung, 2)} €", bg="#2c3e50", fg="#f39c12", font=("Helvetica", 14, "bold")).pack(pady=10)

    # دکمه بستن
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

        # تبدیل ورودی‌ها به عدد
        kredit = float(kredit) if kredit else None
        zahlung = float(zahlung) if zahlung else None
        zinse = float(zinse) if zinse else None
        monate = int(monate) if monate else None

        # بررسی حداقل سه ورودی
        eingaben = [kredit, zahlung, zinse, monate]
        if eingaben.count(None) > 1:
            messagebox.showerror("Fehler", "Bitte geben Sie mindestens drei Werte ein.")
            return

        # نرخ سود ماهانه
        monatlicher_zinssatz = zinse / 100 / 12 if zinse else None

        fehlender_wert = None
        fehlender_wert_text = ""

        # محاسبات
        if kredit is None:
            kredit = zahlung * monate / (1 + monatlicher_zinssatz * monate)
            fehlender_wert = kredit
            fehlender_wert_text = "Kreditsumme (€)"
        elif zahlung is None:
            zahlung = kredit * monatlicher_zinssatz + kredit / monate
            fehlender_wert = zahlung
            fehlender_wert_text = "Monatliche Zahlung (€)"
        elif zinse is None:
            zinse = ((zahlung * monate / kredit) - 1) * 12 * 100 / monate
            fehlender_wert = zinse
            fehlender_wert_text = "Jährlicher Zinssatz (%)"
        elif monate is None:
            monate = kredit / (zahlung - kredit * monatlicher_zinssatz)
            fehlender_wert = monate
            fehlender_wert_text = "Anzahl der Monate"

        total_zahlung = zahlung * monate
        total_zinsen = total_zahlung - kredit
        monatliche_zinszahlung = total_zinsen / monate

        zeige_ergebnis("Berechnung abgeschlossen", fehlender_wert, fehlender_wert_text, monate, total_zahlung, total_zinsen, monatliche_zinszahlung)

    except ValueError:
        messagebox.showerror("Fehler", "Bitte geben Sie gültige Zahlen ein.")
    except ZeroDivisionError:
        messagebox.showerror("Fehler", "Ungültige Eingabe. Division durch Null ist nicht erlaubt.")


# رابط کاربری اصلی
root = tk.Tk()
root.title("Kreditrechner mit fehlendem Faktor")
root.geometry("500x700")
root.configure(bg="#2c3e50")

# عنوان اصلی
tk.Label(root, text="💳 Kredit Rechner", bg="#2c3e50", fg="#f1c40f", font=("Helvetica", 24, "bold")).pack(pady=20)

# فیلدهای ورودی با ایموجی و استایل
fields = [
    ("💰 Kreditsumme (€):", entry_kredit := tk.Entry(root, font=("Helvetica", 12))),
    ("💵 Monatliche Zahlung (€):", entry_monatlich := tk.Entry(root, font=("Helvetica", 12))),
    ("📊 Jährlicher Zinssatz (%):", entry_zinsen := tk.Entry(root, font=("Helvetica", 12))),
    ("⏳ Anzahl der Monate:", entry_monate := tk.Entry(root, font=("Helvetica", 12))),
]

for label_text, field in fields:
    tk.Label(root, text=label_text, bg="#2c3e50", fg="white", font=("Helvetica", 12)).pack(pady=5)
    field.pack(pady=5)

# دکمه محاسبه
tk.Button(
    root, text="📈 Berechnen", command=berechne_kredit, bg="#27ae60", fg="white", font=("Helvetica", 14, "bold")
).pack(pady=20)

# توضیحات
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
