import unittest
import sys
sys.path.append('src')
from status import Status
from evaluate_application import process_application
from application import Application

class ApplicantTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
    
    def test_application_with_no_criteria(self):
        self.assertEqual(process_application(Application()), (Status.PASS, "Nothing to check"))

    def test_application_with_previous_employment(self):
        applicant = Application()
        employment_check = lambda applicant : (Status.PASS, "Applicant has had previous employment")  
        
        self.assertEqual(process_application(Application(), employment_check), (Status.PASS, "Applicant has had previous employment"))
        
    def test_application_no_previous_employment(self):
        applicant = Application()
        employment_check = lambda applicant: (Status.FAIL, "Applicant has no previous employment")
        
        self.assertEqual(process_application(Application(), employment_check), (Status.FAIL, "Applicant has no previous employment"))
        
    def test_application_with_previous_employment_no_criminal_records(self):
        applicant = Application()
        employment_check = lambda applicant : (Status.PASS, "Application has had previous employment.")
        criminal_record_check = lambda applicant : (Status.PASS, "Application has had no criminal records.")

        self.assertEqual(process_application(Application(), employment_check, criminal_record_check), (Status.PASS, "Application has had previous employment. Application has had no criminal records."))

    def test_application_no_previous_employment_no_criminal_records(self):
        applicant = Application()
        employment_check = lambda applicant : (Status.FAIL, "Application has no previous employment.")
        criminal_record_check = lambda applicant : (Status.PASS, "Application has had no criminal records.")

        self.assertEqual(process_application(Application(), employment_check, criminal_record_check), (Status.FAIL, "Application has no previous employment. Application has had no criminal records."))

    def test_application_no_previous_employment_has_criminal_records(self):
        applicant = Application()
        employment_check = lambda applicant : (Status.PASS, "Application has had previous employment.")
        criminal_record_check = lambda applicant : (Status.FAIL, "Application has criminal records.")

        self.assertEqual(process_application(Application(), employment_check, criminal_record_check), (Status.FAIL, "Application has had previous employment. Application has criminal records."))
