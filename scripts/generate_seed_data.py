import os
import sys

app_root_path = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))
sys.path.append(app_root_path)

from models.recordlog import RecordLog
from models.userpair import UserPair

def main():
	r1 = RecordLog('Primary Godzilla', 'Best Husk', 50, 'hugs')
	r2 = RecordLog('Mr. Butters', 'Gyolfreh', 1000, 'cuddles')
	r3 = RecordLog('Best Husk', 'Gyolfreh', 400, 'haircut')
	r4 = RecordLog('Primary Godzilla', 'Mr. Butters', 10, 'head scratches')
	r5 = RecordLog('Gyolfreh', 'Best Husk', 90, 'food')
	r6 = RecordLog('Toast', 'Best Husk', 50, 'hugs')
	r7 = RecordLog('Primary Godzilla', 'Toast', 70, 'furniture')
	record_list = [r1, r2, r3, r4, r5, r6, r7]
	for record in record_list:
		record.redis_store()
	up1 = UserPair('Best Husk', 'Gyolfreh')
	print up1.redis_get_record_log_keys()
	up1_record_logs = [RecordLog.redis_fetch_record_log(rl_key) for rl_key in up1.redis_get_record_log_keys()]
	print up1_record_logs

main()