from flask import Flask,request,render_template,jsonify
from utilities import Loan_prediction
import config
import pickle

app=Flask(__name__)
@app.route("/")
def app_home():
    return render_template('index.html')

@app.route("/prediction" ,methods=["post"])
def get_loan():
    data=request.form
    Gender=data['Gender']
    Married=data['Married']
    Dependents=float(data['Dependents'])
    Education=data['Education']
    Self_Employed=data['Self_Employed']
    ApplicantIncome=float(data['ApplicantIncome'])
    CoapplicantIncome=float(data['CoapplicantIncome'])
    LoanAmount=float(data['LoanAmount'])
    Loan_Amount_Term=float(data['Loan_Amount_Term'])
    Credit_History=float(data['Credit_History'])
    Property_Area=data['Property_Area']

    instance=Loan_prediction(Gender,Married ,Dependents, Education ,Self_Employed ,ApplicantIncome ,CoapplicantIncome ,LoanAmount ,Loan_Amount_Term ,Credit_History ,Property_Area)
    loan=instance.predict_loan()

    return render_template('index.html', Result=loan)

if __name__=="__main__":
    app.run(debug=True,port=config.PORT, host=config.HOST)

