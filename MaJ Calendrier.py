import re

events = []
calendar_sentences = ["haut à gauche","haut à droite","bas à gauche","bas à droite"]

for i in range(4):
  print("-----------------------------------------------------")
  print("Informations de la case en " + calendar_sentences[i] + ".")
  print("-----------------------------------------------------")
  date = input("Veuillez entrer une date (au format jj/mm/aaaa) : ")
  while not date:
    print("La date est obligatoire.")
    date = input("Veuillez entrer une date (au format jj/mm/aaaa) : ")

  lieu = input("Veuillez entrer un lieu : ")
  while not lieu:
    print("Le lieu est obligatoire.")
    lieu = input("Veuillez entrer un lieu : ")

  titre = input("Veuillez entrer un titre : ")
  while not titre or len(titre) > 50:
    if not titre:
      print("Le titre est obligatoire.")
    else:
      print("Le titre ne doit pas dépasser 50 caractères.")
    titre = input("Veuillez entrer un titre : ")

  commentaire = input("Veuillez entrer un commentaire : ")
  while not commentaire:
    print("Le commentaire est obligatoire.")
    commentaire = input("Veuillez entrer un commentaire : ")
  print("")

  event = {"date": date, "lieu": lieu, "titre": titre, "commentaire": commentaire}
  events.append(event)

# Ouvrez le fichier HTML et lisez-le en tant que chaîne de caractères
with open("index.html", "r") as f:
    html = f.read()

# Remplacez le contenu de la balise ayant l'ID "mon_id" par la valeur de votre variable
html_modifie = re.sub('<div[^>]*id="case_haut_gauche"[^>]*>.*</div>', f'<div class="calendar-thumb" id="case_haut_gauche"><span class="calendar-date">{events[0]["date"]}<br>{events[0]["lieu"]}</span><h3 class="calendar-title">{events[0]["titre"]}</h3><h5 class="calendar-comment">{events[0]["commentaire"]}</h5></div>', html)

# Enregistrez le fichier HTML modifié
with open("index.html", "w") as f:
    f.write(html_modifie)

print("Les informations ont été envoyées à votre site internet.") 
print("Il devrait être mis à jour dans peu de temps.")
input("Appuyez sur Entrée pour fermer le programme...")