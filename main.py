from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

# IN OUR EXAMPLE WE LABLED IT AS [main.py]
main = Flask(__name__)

# IN OUR EXAMPLE WE LABLED IT AS [main.py]
@main.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Ashish')

@main.route("/api/jobs")
def api_info():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

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
