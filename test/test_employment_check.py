import unittest
import sys
sys.path.append('src')
from status import Status
from application import Application
from criteria.employment import evaluate_application

class EmployementCheckTest(unittest.TestCase):
    def test_check_employement_pass(self):
        applicant = Application(True)
        self.assertEqual(evaluate_application(applicant), (Status.PASS, "Applicant has had previous employment."))
        
    def test_check_employement_fail(self):
        applicant = Application(False)
        self.assertEqual(evaluate_application(applicant), (Status.FAIL, "Applicant has no previous employment"))
        