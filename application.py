from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder

#model import
gbm = pickle.load(open("models/gradient_boosting.pkl","rb"))
le = pickle.load(open("models/label_encoder.pkl","rb"))
sc = pickle.load(open("models/scaler.pkl","rb"))

#Flask app
application = Flask(__name__)
app = application
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/startup_info")
def startup_info():
    return render_template("startup_info.html")


@app.route("/predict_data", methods=["GET","POST"])
def prediction():
    if request.method == "POST":
        # Get all the data from the form
        funding_rounds = float(request.form.get("funding_rounds"))
        funding_total_usd = float(request.form.get("funding_total_usd"))
        milestones = float(request.form.get("milestones"))
        category_code = request.form.get("category_code")
        has_angel = int(request.form.get("has_angel", 0))  # default to 0 if not checked
        has_roundA = int(request.form.get("has_roundA", 0))  # default to 0 if not checked
        has_roundB = int(request.form.get("has_roundB", 0))  # default to 0 if not checked
        has_roundC = int(request.form.get("has_roundC", 0))  # default to 0 if not checked
        has_roundD = int(request.form.get("has_roundD", 0))  # default to 0 if not checked
        is_top500 = int(request.form.get("is_top500"))

        # Create a DataFrame from the input data
        data = pd.DataFrame({
            "funding_rounds": [funding_rounds],
            "funding_total_usd": [funding_total_usd],
            "milestones": [milestones],
            "category_code": [category_code],
            "has_angel": [has_angel],
            "has_roundA": [has_roundA],
            "has_roundB": [has_roundB],
            "has_roundC": [has_roundC],
            "has_roundD": [has_roundD],
            "is_top500": [is_top500]
        })

        # Scale the numerical columns
        columns_to_scale = ["funding_rounds", "funding_total_usd", "milestones"]
        data[columns_to_scale] = sc.transform(data[columns_to_scale])

        # Encode the categorical column
        data["category_code"] = le.transform(data["category_code"])

        # Make predictions
        result = gbm.predict(data)
        if result[0]==0:
            result = "closed"
        else:
            result = "acquired"

        return render_template("predict.html", result=result)
    else:
        return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)
