

from datetime import datetime
import calendar

heute = datetime.now()
geburt = input("Bitte geben Sie Ihren Geburtsdatum (in diesem Foramt: TT.MM.JJJJ) ein: ")
geburt= datetime.strptime(geburt, "%d.%m.%Y")
#print(geburt)
alter_j = heute.year - geburt.year
alter_m = heute.month - geburt.month
alter_t = heute.day - geburt.day

# falls minus tage erzeugt: heute.day < geburt.day
if alter_t < 0:
    alter_m -= 1
    let_monat = heute.month - 1 or 12
    jahr_for_month = heute.year if heute.month != 1 else heute.year -1
    tage = calendar.monthrange(jahr_for_month, let_monat)[1]
    alter_t += tage

# falls minus Monate erzeugt: heute.month < geburt.month
if alter_m < 0:
    alter_j -= 1
    alter_m += 12


print(f"\n\nSie sind {alter_j} Jahre und {alter_m} Monate und {alter_t} Tage alt!")
