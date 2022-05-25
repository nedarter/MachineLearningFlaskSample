from ast import In
from flask import Flask, request, render_template

import pickle

app = Flask(__name__)

#We need the get / post here to allow us to initially load the page, 
#and also to handle our form data
@app.route("/", methods=["GET", "POST"])
def index(): 

    #if the method is post, we have user entered data play with
    if request.method == "POST":
        #The numbers within form (Pregnancies, Glucose, etc... ) match to the "name" property
        #in the input elements of our form
        Pregnancies = request.form["Pregnancies"]
        Glucose = request.form["Glucose"]
        BloodPressure = request.form["BloodPressure"]
        SkinThickness=request.form["SkinThickness"]
        Insulin=request.form["Insulin"]
        BMI=request.form["BMI"]
        DiabetesPedigreeFunction=request.form["DiabetesPedigreeFunction"]
        Age=request.form["Age"]

        #Setting up all of the user input variables to pass into the model
        guess = [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]

        #we use pickle here to load the model from the file
        model = pickle.load( open( "model.p", "rb" ) )

        #Run the model
        p = model.predict(guess)

    #If the method is not post, we just set all of our values to 0
    else: 
        Pregnancies = 0
        Glucose = 0
        BloodPressure = 0
        SkinThickness=0
        Insulin=0
        BMI=0
        DiabetesPedigreeFunction=0
        Age=0
        p = ""
    
    #We pass all of the values (default to 0's or the user input) back to the page. This way
    #the values are entered back into the page when the user hits submit
    return render_template("index.html",
                            P = p, 
                            Pregnancies = Pregnancies,
                            Glucose = Glucose,
                            BloodPressure = BloodPressure,
                            SkinThickness=SkinThickness,
                            Insulin=Insulin,
                            BMI=BMI,
                            DiabetesPedigreeFunction=DiabetesPedigreeFunction,
                            Age=Age)


app.run(debug=True)