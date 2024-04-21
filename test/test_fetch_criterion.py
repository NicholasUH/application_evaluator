import unittest
import src.criteria.criminal_records
from src.fetch_criterion import fetch_criterion
import src.criteria.employment

class FetchCriterionTest(unittest.TestCase):
    def test_fetch_criterion_employment_status(self):        
        self.assertEqual(fetch_criterion('employment'), src.criteria.employment.evaluate_application)
    
    def test_fetch_criterion_criminal_record(self):
        self.assertEqual(fetch_criterion('criminal_records'), src.criteria.criminal_records.evaluate_application)
        