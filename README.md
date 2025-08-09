# Spam Detection Web Application

A web-based **Spam vs. Ham classification system** built with **Flask** and integrated with **Firebase Realtime Database**.  
This application analyzes long text inputs, detects whether they are **malicious (SPAM)** or **legitimate (HAM)**, and stores the results for future analysis.  

---
## Authors
- Name	                                    Role
- **Angel Eduardo Larios Torres**	        Developer
- **Francisco Javier de Luna Reyes**	    Developer
- **Fatima Monserrat Hurtado Carmona**    Developer
- **Tania Erato Aguayo Salgado**	        Developer
---
## Features

- **Spam Detection** using keyword-based and pattern analysis.
- **Classification Output**: Clearly labels text as **SPAM** or **HAM**.
- **Firebase Integration**: Stores text, classification result, and timestamp.
- **User-Friendly Interface** with clean and responsive design.
- **Real-Time Logging** for tracking submissions.


## Tech Stack

- **Python** + **Flask** — Web framework for backend logic.
- **Firebase Realtime Database** — Data storage.
- **HTML / CSS** — Frontend design.
- **Custom Spam Detection Model** — Implements keyword and pattern recognition.

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/AngelLarios23/DetectorSpam-Ham.git
cd SpamDetectionApp

# Install dependencies
pip install flask
pip install firebase-admin
pip install pandas scikit-learn nltk

# Run the application
python app.py

# En el buscar:
http://127.0.0.1:5000

