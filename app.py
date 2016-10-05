from flask import Flask, render_template, request, json

app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html') #modifying the main method to render template
if __name__ == "__main__":
    app.run()
@app.route('/showSignUp')
def showSignUp():
    return render_template('singup.html')
@app.route('/signUp',methods=['POST'])
def signUp():
    #read the posted values from the UI
    _name =request.form['inputName']
    _email = request.form['inputEmail']
    _password =request.form['inputpassword']

    #validate the received values
    if _name and _email and _password:
        return json.dumps({'html': '<span> All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span> Enter the Required fields</span>'})

