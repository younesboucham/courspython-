from flask import Flask, render_template, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi')
def bmi():
    # ici va le code pour calculer l'IMC
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')
    if not height or not weight:
        return jsonify({"error": "Les paramètres 'height' et 'weight' sont requis"}), 400
    bmi_value = calculate_bmi(height, weight)
    return jsonify({"bmi": bmi_value})
    #return "test"
    # pass

@app.route('/bmr', methods=['POST'])
def bmr():
    # ici va le code pour calculer le TMB
    data = request.get_json()

    # Récupération des paramètres 'height', 'weight', 'age', et 'gender' depuis les données JSON
    height = data.get('height')  # en centimètres
    weight = data.get('weight')  # en kilogrammes
    age = data.get('age')        # en années
    gender = data.get('gender')  # 'male' ou 'female'

    # Vérification si les paramètres sont fournis
    if not height or not weight or not age or not gender:
        return jsonify({"error": "Les paramètres 'height', 'weight', 'age', et 'gender' sont requis"}), 400

    # Calcul du TMB
    bmr_value = calculate_bmr(height, weight, age, gender)
    
    # Retour du résultat sous forme de JSON
    #return jsonify({"bmr": bmr_value})
    return f"<h1>Votre TMB est {bmr_value:.2f} calories par jour</h1>"
    #pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)