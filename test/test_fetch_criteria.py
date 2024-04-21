import unittest
from src.fetch_criteria import fetch_criteria
import src.criteria.employment
import src.criteria.criminal_records

class TestFetchCriteria(unittest.TestCase):
    def test_fetch_criteria_includes_employment(self):
        self.assertIn('employment', fetch_criteria())
        
    def test_fetch_criteria_includes_criminal_record(self):
        self.assertIn('criminal_records', fetch_criteria())
