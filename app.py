from flask import Flask, render_template
from flask.json import jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'jmeno': 'Martin Boril',
    'pohlavi': 'muz',
    'klub': 'SK ZDARAK',
  },
  {
    'id':2,
    'jmeno': 'Vojta Boril',
    'pohlavi': 'muz',
    'klub': 'SK kentico'

  },
  {  
  'id':3,
  'jmeno': 'Lukas Boril',
  'pohlavi': 'muz',
  'klub': 'SK gympl'

  }  
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)