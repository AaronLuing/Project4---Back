import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import login_required, current_user

expense = Blueprint('expenses', 'expense')

# Index route
@expense.route('/', methods=["GET"])
# @login_required
def get_expenses():
  try:
    # expenses = [model_to_dict(expense) for expense in current_user.expense]
    expenses = [model_to_dict(expense) for expense in models.Expense.select()]
    print(expenses)
    return jsonify(data=expenses, status={"code": 200, "message":"Success"})
  except models.DoesNotExist:
    return jsonify(data={}, status={"code":401, "message":"Error getting resources"})

# New route
@expense.route('/', methods=["POST"])
def create_expenses():
  payload = request.get_json()
  print(payload)
  payload['profile'] = current_user.id

  new_expense = models.Expense.create(**payload)
  expense_dict = model_to_dict(new_expense)
  return jsonify(data=expense_dict, status={"code": 201, "message": "Success"})

# Individual Show route
@expense.route('/<id>', methods=["GET"])
def get_one_expense(id):
  print(id, 'reserved_word?')
  expense = models.Expense.get_by_id(id)
  print(expense.__dict__)
  return jsonify(data=model_to_dict(expense), status={"code": 200, "message":"Success"})

# Update route
@expense.route('/<id>', methods=["PUT"])
def update_expense(id):
  payload = request.get_json()
  query = models.Expense.update(**payload).where(models.Expense.id==id)
  query.execute()
  return jsonify(data=model_to_dict(models.Expense.get_by_id(id)), status={"code": 200, "message": "resource updated successfully"})

# Delete route
@expense.route('/<id>', methods=["DELETE"])
def delete_expense(id):
  query = models.Expense.delete().where(models.Expense.id==id)
  query.execute()
  return jsonify(data='deleted', status={"code": 200, "message": "deletion successful"})