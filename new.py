from flask import *


app=Flask(__name__)

@app.route("/")
def main_page():
  return render_template('hello.html')


if __name__ == "__main__":
    app.run()


#Skeleton code for Flask keep on working on this....
