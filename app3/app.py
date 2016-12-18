
from flask import Flask, jsonify
from flask import request
from model import db
from model import createdb
from model import Expenses
from sqlalchemy.exc import IntegrityError
import json


app = Flask(__name__)
createdb()
db.create_all()
@app.route('/')
def index():
	return 'Flask and Mysql Working\n'

@app.route('/v1/expenses/<int:expense_id>', methods= ['GET', 'PUT', 'DELETE'])
def expense(expense_id):
    
    db_obj = Expenses.query.filter_by(id=expense_id).first_or_404()
    if request.method == 'GET':
        return jsonify({'id' : one.id,
                           'name': one.name,
                           'email': one.email,
                           'category': one.category,
                           'description': one.description,
                           'link': one.link,
                           'estimated_costs': one.estimated_costs,
                           'submit_date': one.submit_date,
                           'status': one.status,
                           'decision_date': one.decision_date
                        })

    if request.method == 'PUT':
        data = json.loads(request.data)
        upd = Expense_data.query.filter_by(id=num).first()
        upd
        upd.estimated_costs = data['estimated_costs']
        db.session.commit()
        return 'Data Updated',202
    if request.method == 'DELETE':
         dele = Expense_data.query.filter_by(id=num).first()
        dele
        db.session.delete(dele)
        db.session.commit()
        return 'Data Deleted',204

@app.route('/v1/expenses', methods=['POST'])

def post_expense():
    try:
        json_obj = request.get_json(force=True)
        one = Expenses(id=json_obj['id'], name=json_obj['name'], email=json_obj['email'], category=json_obj['category'],
                        description=json_obj['description'], link=json_obj['link'],
                        estimated_costs=json_obj['estimated_costs'], submit_date=json_obj['submit_date'],
                        status="Pending", decision_date= "")
        db.session.add(one)
        db.session.flush()
        db.session.commit()

        return jsonify({'id': one.id,
                        'name': one.name,
                        'email': one.email,
                        'category': one.category,
                        'description': one.description,
                        'link': one.link,
                        'estimated_costs': one.estimated_costs,
                        'submit_date': one.submit_date,
                        'status': one.status,
                        'decision_date': one.decision_date
                        }), 201
    except IntegrityError as e:
        db.session.rollback()
        return json.dumps({'status': False}, e)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=5003)

