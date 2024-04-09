import unittest
from src.status import Status
from src.evaluate_applicant import process_applicant
from src.applicant import Application

class ApplicantTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
    
    def test_applicant_with_no_criteria(self):
        self.assertEqual(process_applicant(Application()), (Status.PASS, "Nothing to check"))
        