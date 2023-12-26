import pandas as pd
import numpy as np
import json
import pickle
import config

class Loan_prediction():
    def __init__(self,Gender,Married ,Dependents, Education ,Self_Employed ,ApplicantIncome ,CoapplicantIncome ,LoanAmount ,Loan_Amount_Term ,Credit_History ,Property_Area):
        self.Gender=Gender
        self.Married=Married
        self.Dependents=Dependents
        self.Education=Education
        self.Self_Employed=Self_Employed
        self.ApplicantIncome=ApplicantIncome
        self.CoapplicantIncome=CoapplicantIncome
        self.LoanAmount=LoanAmount
        self.Loan_Amount_Term=Loan_Amount_Term
        self.Credit_History=Credit_History
        self.Property_Area=Property_Area

    def load_model(self):
        with open(config.model_file_path,'rb') as f1:
            self.model=pickle.load(f1)

        with open(config.project_data_file,'r') as f2:
            self.project_data=json.load(f2)
    def predict_loan(self):
        self.load_model()

        series=pd.Series(np.zeros(len(self.project_data['columns'])),index=self.project_data['columns'])
        series['Gender']=self.project_data['Gender'][self.Gender]
        series['Married']=self.project_data['Married'][self.Married]
        series['Dependents']=self.Dependents
        series['Education']=self.project_data['Education'][self.Education]
        series['Self_Employed']=self.project_data['Self_Employed'][self.Self_Employed]
        series['ApplicantIncome']=self.ApplicantIncome
        series['CoapplicantIncome']=self.CoapplicantIncome
        series['LoanAmount']=self.LoanAmount
        series['Loan_Amount_Term']=self.Loan_Amount_Term
        series['Credit_History']=self.Credit_History
        series['Property_Area']=self.project_data['Property_Area'][self.Property_Area]

        pred_output=self.model.predict([series])[0]
        
        if pred_output==1:
            pred_output='Congratulations! Your Loan is Approved'
        elif pred_output==0:
            pred_output='Loan is Rejected'

        return pred_output
