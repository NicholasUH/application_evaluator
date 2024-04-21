from status import Status

def evaluate_application(application):
    return (Status.PASS, "Applicant has a good credit record.") if application.credit_records else \
        (Status.FAIL, "Applicant has a bad credit record.")
