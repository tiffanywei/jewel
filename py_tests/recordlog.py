from models.recordlog import RecordLog

rl = RecordLog('debtor', 'creditor', 1337, '"services"')
print rl.to_json()
rl.store()

up = rl.get_user_pair()
print up.get_record_logs()
