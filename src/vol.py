# python3 -m venv mon_environnement
# source mon_environnement/bin/activate
# deactivate
# pip freeze > requirements.txt
# pip install -r requirements.txt
import pycountry

countries = [country.name for country in pycountry.countries]
print(countries)
