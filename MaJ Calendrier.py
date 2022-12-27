import re
import subprocess

nbCadreCalendrier = 4
events = []
calendar_sentences = ["haut à gauche","haut à droite","bas à gauche","bas à droite"]
calendar_div_ids = ["case_haut_gauche", "case_haut_droite", "case_bas_gauche", "case_bas_droite"]

# Pull le projet
subprocess.run(["git", "pull"])

for i in range(nbCadreCalendrier):
  print("-----------------------------------------------------")
  print("Informations de la case en " + calendar_sentences[i] + ".")
  print("-----------------------------------------------------")
  date = input("Veuillez entrer une date : ")
  while not date:
    print("La date est obligatoire.")
    date = input("Veuillez entrer une date : ")

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

# Ouverture du fichier HTML et lecture de ce dernier en tant que chaîne de caractères
with open("index.html", "r") as f:
  html = f.read()

# Itération sur chaque élément de la liste events
for i in range(nbCadreCalendrier):
  # Remplacement du contenu des balises
  nouvelle_balise = f'<div class="calendar-thumb" id="{calendar_div_ids[i]}"><span class="calendar-date">{events[i]["date"]}<br>{events[i]["lieu"]}</span><h3 class="calendar-title">{events[i]["titre"]}</h3><h5 class="calendar-comment">{events[i]["commentaire"]}</h5></div>'
  html = re.sub(f'<div class=\"calendar-thumb\" id=\"case_haut_gauche\">.*</div>', nouvelle_balise, html)

# Enregistrement du fichier HTML modifié
with open("index.html", "w") as f:
    f.write(html)

# Commit et push les modifications
# subprocess.run(["git", "add", "."])
# subprocess.run(["git", "commit", "-m", "Commit automatique de màj du calendrier"])
# subprocess.run(["git", "push"])

print("Les informations ont été envoyées à votre site internet.") 
print("Il devrait être mis à jour dans peu de temps.")
input("Appuyez sur Entrée pour fermer le programme...")