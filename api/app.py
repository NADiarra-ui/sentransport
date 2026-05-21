import json
from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)

# Charger les données depuis le fichier JSON
with open("lignes_ddd.json", "r") as f:
    lignes = json.load(f)

@app.route("/")
def accueil():
    return jsonify({
        "message": "Bienvenue sur l'API SenTransport !",
        "endpoints": ["/lignes", "/lignes/<id>"]
    })

@app.route("/lignes")
def get_lignes():
    return jsonify(lignes)

@app.route("/lignes/<int:ligne_id>")
def get_ligne(ligne_id):
    ligne = next((l for l in lignes if l["id"] == ligne_id), None)
    if ligne is None:
        return jsonify({"erreur": "Ligne non trouvee"}), 404
    return jsonify(ligne)

@app.route("/arrets")
def get_arrets():
    tous_les_arrets = []
    for ligne in lignes:
        tous_les_arrets.extend(ligne["listeArrets"])
    # set pour enlever les doublons, puis retour à une liste
    arrets_uniques = list(set(tous_les_arrets))
    # On trie pour un affichage plus propre (optionnel)
    arrets_uniques.sort()
    return jsonify(arrets_uniques)

@app.route("/stats")
def get_stats():
    total_lignes = len(lignes)
    
    total_arrets = sum(ligne["arrets"] for ligne in lignes)
    
    # Trouver la ligne avec le maximum d'arrêts
    ligne_max = max(lignes, key=lambda l: l["arrets"])
    ligne_plus_arrets = ligne_max["numero"]
    
    return jsonify({
        "total_lignes": total_lignes,
        "total_arrets": total_arrets,
        "ligne_plus_arrets": ligne_plus_arrets
    })

@app.route("/lignes/recherche")
def recherche_lignes():
    q = request.args.get("q", "")
    if q == "":
        return jsonify({"erreur": "Paramètre q manquant"}), 400
    
    q_lower = q.lower()
    resultats = []
    for ligne in lignes:
        if q_lower in ligne["depart"].lower() or q_lower in ligne["arrivee"].lower():
            resultats.append(ligne)
    
    return jsonify(resultats)

if __name__ == "__main__":
    app.run(debug=True, port=5000)