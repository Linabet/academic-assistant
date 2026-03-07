# 💻 Academic Assistants – Chatbot FAQ Multilingue

**Academic Assistants** est un projet de fin d’études (PFE) qui consiste à développer un chatbot FAQ intelligent et multilingue capable de répondre aux questions des étudiants concernant les informations académiques. Le système utilise le traitement automatique du langage naturel (NLP) et une FAQ trilingue (Français, Arabe et Darija).

---

## 🎯 Contexte du projet

Dans les établissements académiques, les étudiants posent souvent les mêmes questions concernant les stages, les inscriptions, les absences, les examens ou les documents administratifs.

Ce projet vise à créer un assistant académique intelligent capable de comprendre les questions et fournir automatiquement des réponses pertinentes.

---

## ✨ Fonctionnalités

- 🤖 Chatbot FAQ intelligent  
- 🌍 Support multilingue (Français / Arabe / Darija)  
- 🧠 Utilisation du NLP et Deep Learning  
- 📊 Analyse des questions les plus fréquentes  
- 💾 Enregistrement automatique des questions  
- 🌐 Interface web avec Flask  

---

## 🏗️ Architecture du projet

academic-assistants/

app/  
│  
├── database/  
│   └── faq.json  

├── logs/  
│   └── questions.csv  

├── static/  
│   └── style.css  

├── templates/  
│   ├── base.html  
│   └── index.html  

├── admin.py  
├── main.py  
├── models.py  
└── utils.py  

README.md  
requirements.txt  

---

## ⚙️ Installation et utilisation

Mettre pip à jour :

pip install --upgrade pip

Installer les dépendances nécessaires :

pip install Flask pandas scikit-learn sentence-transformers gpt4all

Lancer l'application :

python main.py

---

## 💬 Exemple de questions

Je cherche un stage  
Wash kayn bourse ?  
Comment m'inscrire ?  
أين أجد الوثائق ؟  
Exam de passage  

---

## 📊 Analyse des questions

Toutes les questions posées sont enregistrées dans :

app/logs/questions.csv

Ces données permettent d’identifier les questions les plus fréquentes afin d’améliorer le chatbot.

---

## 🛠️ Technologies utilisées

Python  
Flask  
sentence-transformers  
scikit-learn  
pandas  

---

