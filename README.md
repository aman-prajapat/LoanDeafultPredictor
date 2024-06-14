WebApp Link
https://loandeafultpredictor.streamlit.app/



To create a `README.md` file for your Streamlit Loan Prediction Model application, you can use the following template:

```markdown
# Loan Prediction Model Application

This Streamlit application predicts loan approval based on user-provided input parameters using a machine learning model. The model predicts whether a loan application will be approved or rejected based on factors such as annual income, loan amount, loan term, CIBIL score, residential assets, number of dependents, and employment status.

## Requirements

- Python 3.6 or higher
- Required libraries: `streamlit`, `joblib`

## Installation

1. Clone this repository.
2. Install the required libraries using `pip`:
   ```bash
   pip install streamlit joblib
   ```

## Usage

To run the application, execute the following command in your terminal:
```bash
streamlit run app.py
```

### Application Interface

- **Employment Status:** Select whether the applicant is employed or unemployed.
- **Number of Dependent Members:** Number of dependent family members (0 to 10).
- **Annual Income:** Annual income of the applicant (minimum value 0).
- **Loan Amount:** Amount of loan requested (minimum value 0).
- **Loan Term (year):** Duration of the loan in years (1 to 20 years).
- **CIBIL Score:** Credit score of the applicant (300 to 900).
- **Residential Assets:** Value of residential assets owned by the applicant (minimum value 0).

### Predicting Loan Approval

- After entering the required information, click on the **Predict** button.
- The model predicts whether the loan application is **Approved** or **Rejected** based on the input provided.

### Model Details

- **Machine Learning Model:** Logistic Regression model trained on historical loan data.
- **Data Preprocessing:** Features are scaled using a pre-trained scaler model (`LoanPredictionPickleModel`) before prediction.

## Example

Here's a sample screenshot of the Loan Prediction Model application:

![Loan Prediction Model](loan_prediction_app.png)
