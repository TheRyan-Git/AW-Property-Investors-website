from flask import *


app=Flask(__name__)

@app.route("/")
def main_page():
  return render_template('index.html')



def terms_service():
  return render_template('terms_service.html')



if __name__ == "__main__":
    app.run(debug=True)


#Skeleton code for Flask keep on working on this....
