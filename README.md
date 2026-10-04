# Fulfillment Hub

A Streamlit prototype for XYZ's e-commerce fulfillment operations.

## Features
- Operations dashboard
- Order status tracking
- Priority-order visibility
- Main/Overflow inventory visibility
- Inventory transfer requests
- Exception logging and resolution
- Courier/staging readiness view
- Process documentation

## Run locally on Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown by Streamlit, normally `http://localhost:8501`.

## Notes
This take-home uses dummy CSV data and Streamlit session state. It does not claim live courier, marketplace, payment, or warehouse-system integrations.
