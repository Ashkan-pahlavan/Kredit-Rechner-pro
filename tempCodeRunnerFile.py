        return render_template(
            'result.html',
            fehlender_wert=f"{fehlender_wert:,.2f}",
            fehlender_wert_text=fehlender_wert_text,
            jahre=jahre,
            rest_monate=rest_monate,
            total_zahlung=f"{total_zahlung:,.2f}",
            total_zinsen=f"{total_zinsen:,.2f}",
            monatliche_zinszahlung=f"{monatliche_zinszahlung:,.2f}",
        )