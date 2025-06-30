from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

from samp import lookup,infor
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///main.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=["GET", "POST"])
def main():

     return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
         username = request.form.get("username")
         password = request.form.get("password")

         if not username:
             return render_template("login.html",msg="Please Enter Username")
         if not password:
             return render_template("login.html",msg="Please Enter Password")

         opass = db.execute("SELECT username FROM users WHERE username=?",username)
         if not opass:
             return render_template("login.html",msg="Incorrect Username")
         opass = db.execute("SELECT password,id FROM users WHERE username=?",username)
         print(opass[0]["password"],password,"if")

         if opass[0]["password"] == password:
            print(opass[0]["password"],password,"if")
            session["user_id"] = opass[0]["id"]
            return render_template("compare.html")
         else:
            print(opass,password,"else")
            return render_template("login.html",msg="Incorrect password")
    else:
      return render_template("login.html")

@app.route("/logout")
def logout():


    session.clear()

    return redirect("/")


@app.route("/signup", methods=["GET", "POST"])
def signup():
     if request.method == "POST":
         username = request.form.get("name")
         password = request.form.get("password")

         if not request.form.get("username"):
             return render_template("login.html",msg="Please Enter Username")
         if not request.form.get("password"):
             return render_template("login.html",msg="Please Enter Password")

         rows = db.execute("SELECT * FROM users WHERE username = ?", username)

         if (len(rows) != 0):
            return render_template("signup.html",msg="The username already exists.")

         confirmation = request.form.get("confirmation")
         if password == confirmation:

            db.execute("INSERT INTO users(username,password) VALUES(?,?)",username, password)
            return redirect("/")

         else:
              return render_template("signup.html",msg="Both Passwords don't match")


     else:
         return render_template("signup.html")



@app.route("/compare", methods=["GET", "POST"])
def compare():
      if request.method == "POST":
        stock1 = request.form.get("stock1")
        stock2 = request.form.get("stock2")
        lookup(stock1,stock2)



        return render_template("compare1.html")

      else:
         return render_template("compare.html")


@app.route("/compare1", methods=["GET", "POST"])
def compare1():

    return render_template("compare.html")


@app.route("/info", methods=["GET", "POST"])
def info():

            name1 = request.form.get("stock1")
            name2 = request.form.get("stock2")
            result1 =infor(name1)
            result2 =infor(name2)

            return render_template("info.html",info1=result1,info2=result2,name1=name1,name2=name2)




