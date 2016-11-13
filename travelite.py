from flask import Flask, render_template, request, jsonify
import flask
from nearAtt import vacationPlans
from flights import get_flights

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def static_page():
  if request.method == 'POST':
    budget = request.form['budget']
    people = request.form['people']

    data = get_flights('SFO', '2016-12-01--2016-12-30', budget)
    # return jsonify(data)
    package = vacationPlans(data)
    return render_template('form_handle.html', flights=data, activites=package)
  return render_template('index.html')

@app.route('/trips', methods = ['POST'])
def trips():
  return 'success'


if __name__ == '__main__':
    app.run(debug=True)