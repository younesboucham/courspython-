from flask import Flask, render_template, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route pour calculer l'IMC (BMI), en utilisant la méthode POST
@app.route('/bmi', methods=['POST'])
def bmi():
    # Récupération des données JSON envoyées avec la requête POST
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')

    # Vérification si les paramètres 'height' et 'weight' sont fournis
    if not height or not weight:
        return jsonify({"error": "Les paramètres 'height' et 'weight' sont requis"}), 400

    # Calcul de l'IMC
    bmi_value = calculate_bmi(height, weight)

    # Retour du résultat sous forme de JSON
    return jsonify({"bmi": bmi_value})

# Route pour calculer le TMB (BMR), en utilisant la méthode POST
@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()

    # Récupération des paramètres 'height', 'weight', 'age', et 'gender'
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
    return jsonify({"bmr": bmr_value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
