# Créé par chark, le 25/03/2025 en Python 3.7
# Code à utiliser avec le langage Python
import webbrowser
zoom='16' # Faire des essais avec différentes valeurs
latitude=55.75025 # Expliquer comment vous trouvez  ce résultat
longitude=37.6205 # Expliquer comment vous trouvez  ce résultat
webbrowser.open("https://www.openstreetmap.org/#map=" + zoom + " / " + str ( latitude )
+ "/ " + str ( longitude))        # Observer dans l'URL les paramètres
