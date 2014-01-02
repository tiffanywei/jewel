import sys
import os
import unittest

app_root_path = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))
sys.path.append(app_root_path)

# import test files here.
from recordlog import TestRecordLog

if __name__ == '__main__':
    unittest.main()
