from flask import Flask, redirect, url_for, request
import json
import time

from models.recordlog import RecordLog
from models.userpair import UserPair
from models.userpairsforuser import UserPairsForUser

app = Flask(__name__)
app.debug = True

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
  current_user = _get_current_user_id()
  upfu = UserPairsForUser(current_user)
  # TODO: paginate record logs.
  record_log_keys = []
  for user_pair in upfu.redis_get_user_pairs().values():
    record_log_keys.extend(user_pair.redis_get_record_log_keys())
  record_logs = [RecordLog.redis_fetch_record_log(rl_key).to_json() for rl_key in record_log_keys]
  return "[%s]" % ','.join(record_logs)


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
  rl.redis_store()

def _now():
  return time.time()

# TODO: Actually get the currently logged in user.
def _get_current_user_id():
  # see generate_seeed_data.py
  return 'Best Husk'
