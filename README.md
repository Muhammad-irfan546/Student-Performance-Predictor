# Student Performance Predictor

A Streamlit app that loads a trained Gradient Boosting model and predicts a
student's performance score from study habits.

## Files

- `app.py` — the Streamlit app
- `gradient_boosting_model.pkl` — your trained model
- `requirements.txt` — dependencies for Streamlit Cloud

The model expects these 5 inputs (already wired up in the app):

- Hours Studied
- Previous Scores
- Extracurricular Activities (Yes/No)
- Sleep Hours
- Sample Question Papers Practiced

## Step 1 — Put all files in one folder

```
gb-streamlit-app/
├── app.py
├── requirements.txt
└── gradient_boosting_model.pkl
```

## Step 2 — Upload to GitHub

1. Go to https://github.com/Muhammad-irfan546
2. Click **New repository** → name it (e.g. `student-performance-app`) → Create
3. Click **Add file → Upload files**
4. Drag in all 3 files above
5. Click **Commit changes**

Or via terminal:

```bash
git init
git add .
git commit -m "Add Gradient Boosting Streamlit app"
git branch -M main
git remote add origin https://github.com/Muhammad-irfan546/student-performance-app.git
git push -u origin main
```

## Step 3 — Deploy on Streamlit Cloud


1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click **New app**
4. Select your repo, branch `main`, and set main file path to `app.py`
5. Click **Deploy**

Your app will be live at a URL like:

https://student-performance-predictor-c6cwuzoh62jkfre8nrbtcu.streamlit.app/

## Note on scikit-learn version

Your model was trained with scikit-learn 1.6.1. `requirements.txt` pins
this exact version so the model loads correctly on Streamlit Cloud —
don't remove that pin.
