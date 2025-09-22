from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import pickle
import os

# -----------------------------
# Load trained end-to-end pipeline (preprocessing + model)
# -----------------------------
pipeline = pickle.load(open("pipeline.pkl", "rb"))

app = Flask(__name__)

# Fields expected by the pipeline (must include all columns used in training)
FORM_FIELDS = [
    "Ticket ID",
    "Customer Name",
    "Customer Email",
    "Customer Age",
    "Customer Gender",
    "Product Purchased",
    "Ticket Type",
    "Ticket Status",
    "Resolution",
    "Ticket Priority",
    "Ticket Channel",
    "First Response Time",
    "Time to Resolution",
    "Ticket Subject",
    "Ticket Description",
    "Date of Purchase"   # optional (used for time features)
]

# -----------------------------
# Helper: Build Input DataFrame
# -----------------------------
def build_input_df(form):
    row = {}
    for f in FORM_FIELDS:
        key = f.replace(" ", "_").lower()
        val = form.get(key, "")

        # Convert empty string → NaN
        if val == "":
            row[f] = np.nan
        else:
            row[f] = val

    # Convert numeric fields
    for nf in ["Customer Age", "First Response Time", "Time to Resolution", "Ticket ID"]:
        if nf in row and pd.notna(row[nf]):
            try:
                row[nf] = float(row[nf])
            except:
                row[nf] = np.nan  # if conversion fails

    return pd.DataFrame([row])

# -----------------------------
# Routes
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    prediction_text, proba_text = "", ""

    if request.method == "POST":
        try:
            input_df = build_input_df(request.form)

            # Predict class (0–4 → add +1 for rating)
            pred = pipeline.predict(input_df)[0]
            prediction_text = f"Predicted Satisfaction: {int(pred) + 1} / 5"

            # Probabilities
            if hasattr(pipeline.named_steps["clf"], "predict_proba"):
                proba = pipeline.predict_proba(input_df)[0]
                proba_text = ", ".join([f"{i+1}★: {p:.2f}" for i, p in enumerate(proba)])

        except Exception as e:
            prediction_text = f"⚠️ Error: {e}"

    return render_template("index.html", prediction=prediction_text, proba=proba_text)

# Allow downloading trained model
@app.route("/download-model")
def download_model():
    path = "pipeline.pkl"
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "pipeline.pkl not found.", 404

# Allow downloading metrics (if saved)
@app.route("/download-metrics")
def download_metrics():
    path = "metrics.txt"
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "metrics.txt not found.", 404

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
