from status import Status

def evaluate_application(application):
    return (Status.PASS, "Applicant has security clearance.") if application.security_clearance else \
        (Status.FAIL, "Applicant has no security clearance.")
