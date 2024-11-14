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

## How to Run the Backend Locally

### Prerequisites
Before running the backend, make sure you have the following installed:
1. **Python 3.7 or above**.
2. **pip** (Python package manager).

---

### Steps to Run Locally
Follow these steps to test the backend locally:

1. **Clone this Repository**:
   - Open a terminal and run:
     ```bash
     git clone https://github.com/alexisMarceau1/CreditRisk_backend.git
     ```

2. **Navigate to the Project Directory**:
   - Move into the repository folder:
     ```bash
     cd CreditRisk_backend
     ```

3. **Install Required Dependencies**:
   - Use the following command to install the necessary Python libraries:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the FastAPI Server**:
   - Start the server by running:
     ```bash
     uvicorn api:app --reload
     ```
   - You will see output in the terminal with a URL such as:
     ```
     http://127.0.0.1:8000
     ```

5. **Access the API**:
   - Open your browser or an API testing tool (like Postman) and go to:
     - API Home: `http://127.0.0.1:8000`
     - API Documentation: `http://127.0.0.1:8000/docs`

6. **Test Predictions**:
   - Use the `/prediction/{client_id}` endpoint to query predictions for specific clients. For example:
     - Good Client: `http://127.0.0.1:8000/prediction/100057`
     - Average Client: `http://127.0.0.1:8000/prediction/100074`
     - Bad Client: `http://127.0.0.1:8000/prediction/100038`

---

### Example Predictions

Here are example queries and responses for testing the backend:

1. **Good Client (ID: 100057)**:
   - URL:
     ```bash
     http://127.0.0.1:8000/prediction/100057
     ```
   - Example Response:
     ```json
     {
         "prediction": 0,
         "proba": 0.92
     }
     ```

2. **Average Client (ID: 100074)**:
   - URL:
     ```bash
     http://127.0.0.1:8000/prediction/100074
     ```
   - Example Response:
     ```json
     {
         "prediction": 0,
         "proba": 0.60
     }
     ```

3. **Bad Client (ID: 100038)**:
   - URL:
     ```bash
     http://127.0.0.1:8000/prediction/100038
     ```
   - Example Response:
     ```json
     {
         "prediction": 1,
         "proba": 0.15
     }
     ```

---

## Files
- **`api.py`**:
  - Contains the main logic for the API, including routes for prediction.
- **`LGBMClassifier.pkl`**:
  - Pre-trained LightGBM model for credit scoring.
- **`test_df.parquet`**:
  - Sample test dataset for validating predictions.
- **`requirements.txt`**:
  - Dependencies for running the backend.

---

This backend provides a robust and transparent way to serve machine learning predictions for credit risk analysis. Feel free to contribute or suggest improvements!
