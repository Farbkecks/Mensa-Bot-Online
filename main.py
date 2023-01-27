from flask import Flask
from Meals import Meals
import datetime
import locale

app = Flask("Mensa Bot")
ids = {1: 101, 2: 105, 3: 111}


def generate_site(mensa):
    def headline(s):
        return f"<b>{s}</b><br>"

    def generate_string(date, day=None):
        def generate_substring(meals):
            result = ""
            for meal in meals:
                result += f"{meal.name}:<i>{meal.price}€</i> {meal.tag}<br>"
            return result

        string = ""
        meals = Meals(ids[mensa], date)
        if meals.main_meal == []:
            return ""

        if day == None:
            string += f"<h1>Mensa {mensa} am {date.strftime('%d.%m.%Y')} ({date.strftime('%A')})</h1>"
        else:
            string += f"<h1>Mensa {mensa} am {date.strftime('%d.%m.%Y')} ({day})</h1>"
        string += headline("Hauptgericht")
        string += generate_substring(meals=meals.main_meal)
        string += headline("Beilage")
        string += generate_substring(meals=meals.supplement_meal)
        string += headline("Nachtisch")
        string += generate_substring(meals=meals.dessert_meal)
        string += "<hr><br><br><br><br>"
        return string

    string = "<br><br>"
    today = datetime.date.today()
    for day in range(6):
        string += generate_string(today + datetime.timedelta(days=day))

    return string


@app.route("/")
def index():
    return generate_site(1) + generate_site(3) + generate_site(2)


app.run(host="0.0.0.0", port=81)
# app.run(host="localhost", port=8080)
# print(generate_site(1) + generate_site(2))
