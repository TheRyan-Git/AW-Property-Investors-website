from flask import *


app=Flask(__name__)

@app.route("/")
def main_page():
  return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


#Skeleton code for Flask keep on working on this....
