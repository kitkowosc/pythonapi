from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}, {"id": 3, "name": "Company Three"}, {"id": 4, "name": "Company Four"}]
cats = [{"id": 1, "name": "Cat One"}, {"id": 2, "name": "Cat Two"}, {"id": 3, "name": "Cat Three"}, {"id": 4, "name": "Cat Four"}, {"id": 5, "name": "DOG"}]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/cats', methods=['GET'])
def get_cats():
  return json.dumps(cats)

if __name__ == '__main__':
    api.run()