from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # دریافت ورودی‌ها از فرم
        kredit = float(request.form.get('kredit', 0)) if request.form.get('kredit') else None
        zahlung = float(request.form.get('zahlung', 0)) if request.form.get('zahlung') else None
        zinse = float(request.form.get('zinse', 0)) if request.form.get('zinse') else None
        monate = int(request.form.get('monate', 0)) if request.form.get('monate') else None

        if [kredit, zahlung, zinse, monate].count(None) > 1:
            return render_template('result.html', error="Bitte mindestens drei Werte eingeben!")

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

        # تبدیل مدت زمان به سال و ماه
        jahre = int(monate // 12)  # فقط بخش صحیح سال‌ها
        rest_monate = int(monate % 12)  # فقط بخش صحیح ماه‌ها

        return render_template(
            'result.html',
            fehlender_wert=f"{fehlender_wert:.2f}",
            fehlender_wert_text=fehlender_wert_text,
            jahre=jahre,
            rest_monate=rest_monate,
            total_zahlung=f"{total_zahlung:.2f}",
            total_zinsen=f"{total_zinsen:.2f}",
            monatliche_zinszahlung=f"{monatliche_zinszahlung:.2f}",
        )
    except ValueError:
        return render_template('result.html', error="Bitte gültige Zahlen eingeben!")
    except ZeroDivisionError:
        return render_template('result.html', error="Division durch Null ist nicht erlaubt!")

if __name__ == "__main__":
    app.run(debug=True)
