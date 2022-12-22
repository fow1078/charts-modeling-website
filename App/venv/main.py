import os
from flask import Flask, request, redirect, render_template
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="../templates", static_folder="../static")


@app.route('/', methods=['POST', 'GET'])
def index(): 
  return render_template('index.html')


port = int(os.environ.get('PORT', 5555))

if __name__ == "__main__":
  app.run(port=port, debug=True) #Изменить с true на false когда закончим