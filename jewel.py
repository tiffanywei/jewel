from flask import Flask, redirect, url_for, request
import json
import time


app = Flask(__name__)

class Column:
  PERSON = 'person'
  AMOUNT = 'amount'
  TIMESTAMP = 'timestamp'
  MEMO = 'memo'

@app.route('/')
def index():
  return redirect(url_for('static', filename='jewel.html'))
  
@app.route('/test_records.json')
def test_records():
  # TODO: Remove sleep.
  time.sleep(1)

  records = [{
    Column.PERSON: 'vlad',
    Column.AMOUNT: 50,
    Column.TIMESTAMP: _now(),
    Column.MEMO: '"services"'},
    {
    Column.PERSON: 'juliet',
    Column.AMOUNT: 100,
    Column.TIMESTAMP: _now(),
    Column.MEMO: 'shoes'},
    {
    Column.PERSON: 'juliet',
    Column.AMOUNT: -50,
    Column.TIMESTAMP: _now(),
    Column.MEMO: 'food'}
    ]
  return json.dumps(records)

@app.route('/tab/all')
def all_records_for_user():
  # TODO: Retrieve all RecordLogs for user. See recordlog.py.
  return json.dumps([])


@app.route('/tab/<int:other_user_id>')
def records_with(other_user_id):
  # TODO: Use actual other_user_id + User class.
  pass

@app.route('/create_record', methods=['POST'])
def create_record():
  # TODO: validate form.
  RECORD_FIELDS = ['transaction_type', 'secondary_user', 'amount', 'memo']
  record = {}
  for field in RECORD_FIELDS:
    record[field] = request.form[field]

  # TODO: Use real time from form.

  record['primary_user'] = _get_current_user_id()

  _build_path_to_record_log(record)

def _build_path_to_record_log(record):
  # TODO: Find/create user.

  transaction = Transaction(record['transaction_type'], record['primary_user'], record['secondary_user'])
  rl = RecordLog(transaction.get_debtor(), transaction.get_creditor(), record['amount'], record['memo'])
  rl.store()

def _now():
  return time.time()

# TODO: Actually get the currently logged in user.
def _get_current_user_id():
  return '3'
