# CreditRisk Backend

This repository contains the backend code for the **CreditRisk** project, designed to serve machine learning predictions for loan default probabilities. The backend was implemented using **FastAPI** to provide a lightweight and efficient API interface for the deployed LightGBM model.

---

## Features
- **Machine Learning Model**:
  - The backend serves a pre-trained **LightGBM Classifier** stored in the `LGBMClassifier.pkl` file.
  - Predicts the probability of loan default based on client features.

- **API Endpoints**:
  - Accepts JSON inputs containing client data.
  - Returns predictions with detailed probability scores.

- **Testing**:
  - Includes a sample test dataset (`test_df.parquet`) for local verification of the API's functionality.

---

## Technical Stack
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Model**: LightGBM (pre-trained)
- **Data Format**: Parquet and JSON
- **Environment**:
  - Dependencies are listed in `requirements.txt`.
  - Designed for deployment on **Heroku** using a `Procfile`.

---

## How to Use
As the project is no longer deployed, the backend cannot currently be tested online. However, to use locally:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/CreditRisk_backend.git

