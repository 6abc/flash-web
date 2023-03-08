from sqlalchemy import create_engine, text
import os 

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string, 
  connect_args=
  {
  "ssl": 
  {
     "ssl_ca": "/etc/ssl/cert.pem"
  }})

# def load_jobs_from_db():
#   with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     jobs = []
#     for row in result.all():
#       # jobs.append(row._mapping)
#       jobs.append(dict(row))
#     return jobs

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, title, location, salary, currency, responsibilities, requirements FROM jobs"))
        jobs = []
        for row in result.fetchall():
            job_dict = {}
            job_dict['id'] = row.id
            job_dict['title'] = row.title
            job_dict['location'] = row.location
            job_dict['salary'] = row.salary
            job_dict['currency'] = row.currency
            job_dict['responsibilities'] = row.responsibilities
            job_dict['requirements'] = row.requirements
            jobs.append(job_dict)
        return jobs