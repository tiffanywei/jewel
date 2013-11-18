import sys
import os

app_root_path = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))
sys.path.append(app_root_path)
print sys.path

import recordlog
