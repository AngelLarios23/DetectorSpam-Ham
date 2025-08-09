# Spam Detection Web Application

A web-based **Spam vs. Ham classification system** built with **Flask** and integrated with **Firebase Realtime Database**.  
This application analyzes long text inputs, detects whether they are **malicious (SPAM)** or **legitimate (HAM)**, and stores the results for future analysis.  

## 📂 Firebase Credentials

> ⚠️ **Security Warning:** This file contains sensitive credentials. Do not expose it in public repositories.  
> If shared for testing, regenerate the keys in Firebase afterward.

[📄 Download `firebase_key.json` from Google Drive](https://drive.google.com/file/d/1LdXOCYRiM6ecDiclqtjQkdlLbn8PvpMb/view?usp=sharing)

---

## 📑 Documentation

You can view the full project documentation here:  
[📄 Project Documentation (Google Docs)](https://docs.google.com/document/d/1n-4EqS5wcB4ico2QtksCL2H0mSyCZqj9/edit?usp=sharing&ouid=105826322858886379246&rtpof=true&sd=true)


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
cd  DetectorSpam-Ham

# Install dependencies
pip install flask
pip install firebase-admin
pip install pandas scikit-learn nltk

# Run the application
python app.py

# En el buscar:
http://127.0.0.1:5000

