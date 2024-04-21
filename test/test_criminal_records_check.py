import unittest
import sys
sys.path.append('src')
from status import Status
from application import Application
from criteria.criminal_records import evaluate_application

class CriminalRecordsCheckTest(unittest.TestCase):
    def test_check_criminal_records_pass(self):
        applicant = Application(criminal_records=False)
        self.assertEqual(evaluate_application(applicant), (Status.PASS, "Applicant has no criminal records."))
        
    def test_check_criminal_records_fail(self):
        applicant = Application(criminal_records=True)
        self.assertEqual(evaluate_application(applicant), (Status.FAIL, "Applicant has criminal records."))
        