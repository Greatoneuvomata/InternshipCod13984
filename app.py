# this is were you import flask
from flask import Flask, request, redirect, url_for, render_template

# this is were you stage your app
app = Flask(__name__)

#this is were you define your route
@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/signup', methods=['POST','GET'])
def Signup():
    if request.method == 'POST':
        Username = request.form.get('Username')
        Password = request.form.get('Password')
        Adress = request.form.get('Adress')
        Phone_Number = request.form.get('Phone_Number')
        Gender = request.form.get('Gender')
       
        new_username={"Username,": Username,
        "Password":Password,    
        "Adress":Adress,
        "Phone_Number":Phone_Number,
        "Gender":Gender} 
        print(new_username)
       
        
    return render_template('index.html')

@app.route('/')
def homepage():
    return render_template('Welcome.html')

if __name__ == "__main__":
    app.run(debug=True)
    # this is the bottom of your flask app it should always be at the end