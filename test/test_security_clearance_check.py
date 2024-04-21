import unittest
import sys
sys.path.append('src')
from status import Status
from application import Application
from criteria.security_clearance import evaluate_application

class SecurityClearanceCheckTest(unittest.TestCase):
    def test_check_security_clearance_pass(self):
        applicant = Application(security_clearance=True)
        self.assertEqual(evaluate_application(applicant), (Status.PASS, "Applicant has security clearance."))
        
    def test_check_security_clearance_fail(self):
        applicant = Application(security_clearance=False)
        self.assertEqual(evaluate_application(applicant), (Status.FAIL, "Applicant has no security clearance."))
        