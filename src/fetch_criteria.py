import os

def fetch_criteria(criteria_path='src/criteria'):
    return [os.path.splitext(file)[0] for file in os.listdir(criteria_path) if file.endswith('.py')]
