from flask import Flask, request
from flask import render_template
from config import config
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/')
def login_form():
  return render_template('login.html')

@app.route('/login', methods = ['POST'])
def do_login():
  data = request.form
  username = request.form['username']
  password = request.form['password']
  payload = {'userName': username, 'password': password}
  response = requests.post(config['securedb_authenticate_url'], 
                          auth=(config['securedb_user'], 
                          config['securedb_pass']), 
                          data=payload)
  if (response.status_code != 200):
    print response.status_code
    return render_template('login_failed.html')
  else:
    return "woot!" # response.content

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
