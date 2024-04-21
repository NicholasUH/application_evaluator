from importlib import import_module

def fetch_criterion(criterion, path = 'src.criteria'):
    criterion_module = import_module(f'{path}.{criterion}') 
    
    return getattr(criterion_module, 'evaluate_application')
