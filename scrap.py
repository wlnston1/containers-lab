month=input("Enter the month of the season").lower()
day=int("Enter the day of the month")

if month in ('dec', 'jan', 'feb'):
    if day >= 21:
        season = "Winter"
    else:
        season = "Fall"
elif month == 'mar':
    if day >= 20:
        season = "Spring"
    else:
        season = "Winter"


print("{} {} is in {}".format(month.capitalize(), day, season))