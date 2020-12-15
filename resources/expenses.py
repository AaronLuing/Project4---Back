import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

# First argument is blueprints name
# Second argument is it's import_name
# Third argument is the url_prefix so we dont have to
# prefix all our apis
expense = Blueprint('expenses', 'expense')

@expense.route('/', methods=["GET"])
def get_expenses():
  try:
    expenses = [model_to_dict(expense) for expense in models.Expense.select()]
    print(expenses)
    return jsonify(data=expenses, status={"code": 200, "message":"Success"})
  except models.DoesNotExist:
    return jsonify(data={}, status={"code":401, "message":"Error getting resources"})


@expense.route('/', methods=["POST"])
def create_expenses():
  payload = request.get_json()
  print(payload)
  expense = models.Expense.create(**payload)
  expense_dict = model_to_dict(expense)
  return jsonify(data=expense_dict, status={"code": 201, "message": "Success"})

