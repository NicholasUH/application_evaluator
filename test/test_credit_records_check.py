import unittest
import sys
sys.path.append('src')
from status import Status
from application import Application
from criteria.credit_records import evaluate_application

class CreditRecordsCheckTest(unittest.TestCase):
    def test_check_credit_records_pass(self):
        applicant = Application(credit_records=True)
        self.assertEqual(evaluate_application(applicant), (Status.PASS, "Applicant has a good credit record."))
        
    def test_check_credit_records_fail(self):
        applicant = Application(credit_records=False)
        self.assertEqual(evaluate_application(applicant), (Status.FAIL, "Applicant has a bad credit record."))
