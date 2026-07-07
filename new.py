# IMPORTING
from flask import Flask, render_template, request
import os # for importing path




# INTERACTION
web = Flask(__name__)

picfolder = os.path.join("static")
web.config["UPLOAD_FOLDER"] = picfolder


# MAPPING
@web.route("/")
@web.route("/register")

# INPUTS
def homepage():
    pic = os.path.join(web.config["UPLOAD_FOLDER"], "dhurandhar2.jpeg")
    return render_template("register.html", user_image = pic)

@web.route("/second")
# INPUTS
def second():
    return render_template("second.html")

# MAPPING
@web.route("/confirmation" , methods = ["POST","GET"])

def register():
    if request.method == "POST":
        n = request.form.get("name")
        c = request.form.get("city")
        p = request.form.get("phonenumber")
        return render_template("confirm.html", name = n, city = c, phonenumber = p)
# MAIN
if __name__ == "__main__":
    web.run(debug=True)
    


