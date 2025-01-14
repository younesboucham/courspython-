
#IMAGE_NAME=my-python-application
#PORT : 5000
#.PHONY : run test 
#all : build test run 


#"build:
#echo "Building the project ..."
#Name:
#echo "$(IMAGE_NAME)"

#test:
#echo "Running tests ..."

#run:
#python app.py
#echo "Runnig the application ..."
# Variables
PYTHON = python3
PIP = pip3
APP_FILE = app.py
TEST_FILE = test.py
REQUIREMENTS = requirements.txt

# Commandes Make

# Initialisation du projet (installation de virtualenv et création de l'environnement virtuel)
init:
	$(PIP) install virtualenv
	virtualenv venv
	@echo "Environnement virtuel créé."

# Installation des dépendances
install: init
	venv/bin/$(PIP) install -r $(REQUIREMENTS)
	@echo "Dépendances installées."

# Build du projet (containerisation avec Docker)
build:
	docker build -t health-calculator-service .
	@echo "Image Docker construite."

# Lancer l'application Flask en utilisant Docker
run:
	docker run -p 5000:5000 health-calculator-service
	@echo "Application lancée à l'adresse http://localhost:5000"

# Exécution des tests unitaires
test:
	venv/bin/$(PYTHON) -m unittest $(TEST_FILE)
	@echo "Tests unitaires exécutés."

# Test API via curl (par exemple pour l'IMC et le TMB)
test_api:
	@echo "Test API BMI"
	curl -X POST "http://localhost:5000/bmi" -H "Content-Type: application/json" -d '{"height": 1.75, "weight": 70}'
	@echo "\nTest API BMR"
	curl -X POST "http://localhost:5000/bmr" -H "Content-Type: application/json" -d '{"height": 175, "weight": 70, "age": 25, "gender": "male"}'

# Supprimer l'environnement virtuel
#clean:
#rm -rf venv
#@echo "Environnement virtuel supprimé."

	# Tâche principale pour tout exécuter dans l'ordre
all: install build run 
	@echo "Tout a été exécuté avec succès."
