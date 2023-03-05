from flask import Flask, render_template, jsonify

# IN OUR EXAMPLE WE LABLED IT AS [main.py]
main = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bangaluru, India',
  'salary': 'Rs. 10,00,000.00'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,00,000.00'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
  'salary': 'Rs. 12,00,000.00'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Francisco, USA',
  'salary': '$ 120,000.00'
}]


# IN OUR EXAMPLE WE LABLED IT AS [main.py]
@main.route("/")
def hello_world():
  return render_template('home.html', jobs_list=JOBS, company_name='Ashish')


@main.route("/api/jobs")
def api_info():
  return jsonify(JOBS)


#_______________________________________________________________________
# Save it as [hello.py] or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.
# $ flask --app hello run
#  * Serving Flask app 'hello'

# Application Discovery Behavior
# As a shortcut, if the file is named app.py or wsgi.py, you don’t have to use --app. See Command Line Interface for more details.
#_______________________________________________________________________

# IN OUR EXAMPLE WE LABLED IT AS [main.py]
if __name__ == "__main__":
  main.run(host='0.0.0.0', debug=True)
