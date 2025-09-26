from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)


user=""
mot=""


def choix_ligne():
    """
    """
    fichier = open("dictionnaire.txt")
    lignes = fichier.readlines()
    nombre_aleatoire=random.randint(0, len(lignes))
    ligne=lignes[nombre_aleatoire]
    return ligne

def choix_mot():
    mot_brut=choix_ligne()
    mot=mot_brut.split(";")[0]
    return mot    



@app.route('/', methods=['GET', 'POST'])
def home():
    global user, mot
    if request.method == 'POST':
        user=request.form["nom"]
        return redirect(url_for("jouer"))
    else:
        return render_template('home.html')
    
@app.route('/play', methods=['GET', 'POST'])
def jouer():
    print(choix_mot())
    return render_template("play.html", nom_joueur=user)



