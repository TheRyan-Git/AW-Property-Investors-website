from flask import *

app=Flask(__name__)


@app.route("/contact")

def contact_us():
  # return file name here
  return render_template("contactus.html")
