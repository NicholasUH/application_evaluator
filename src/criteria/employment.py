from status import Status

def evaluate_application(application):
    return (Status.PASS, "Applicant has had previous employment.") if application.employment else \
        (Status.FAIL, "Applicant has no previous employment")
