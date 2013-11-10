from flask import Flask, redirect, url_for
import json
import os
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

  return json.dumps([{
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
    ])

def _now():
  return time.time();
