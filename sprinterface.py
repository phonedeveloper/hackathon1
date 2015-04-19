from flask import Flask, request
from flask import render_template
from config import config
import requests
from requests import session
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/')
def login_form():
  return render_template('login.html')

@app.route('/login', methods = ['POST'])
def do_login():
  username = request.form['username']
  password = request.form['password']
  payload = '{"userName":"' + username + '","password":"' + password + '"}'
  headers = {'Accepts-Encoding':'application-json'}
  auth = {config['securedb_user'], config['securedb_pass']}
  response = requests.post(config['securedb_authenticate_url'], 
                      data=json.dumps(payload),
                      auth=(config['securedb_user'], config['securedb_pass']),
                      headers={'Accept-Encoding':'application-json'})
                    
  if (response.status_code != 200):
    print response.status_code
    print response.content
    return render_template('login_failed.html')
  else:
    return "woot!" # response.content

# for another hackathon friend
@app.route('/test_score')
def test_score():
  return render_template('score.html')

# for another hackathon friend
@app.route('/set_score', methods = ['POST'])
def set_score():
  score = request.form['score']
  f = open('score','w')
  f.write(str(score))
  f.close()
  return score

# for another hackathon friend
@app.route('/get_score')
def get_score():
  f = open('score','r')
  score = f.read()
  f.close()
  return '{"score":"' + str(score) + '"}'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
