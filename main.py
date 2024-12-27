from flask import Flask, json
import psycopg2
import os

#companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}, {"id": 3, "name": "Company Three"}, {"id": 4, "name": "Company Four"}]
#cats = [{"id": 1, "name": "Cat One"}, {"id": 2, "name": "Cat Two"}, {"id": 3, "name": "Cat Ryszarth"}, {"id": 4, "name": "Cat Four"}, {"id": 5, "name": "DOG"}]

api = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_SERVER'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    return conn

@api.route('/companies', methods=['GET'])
def get_companies():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('SELECT id, name FROM companies')
  companies = cur.fetchall()
  cur.close()
  conn.close()
  return json.dumps(companies)

#@api.route('/cats', methods=['GET'])
#def get_cats():
#  return json.dumps(cats)

if __name__ == '__main__':
    api.run()