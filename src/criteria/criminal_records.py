from status import Status

def evaluate_application(application):
    return (Status.FAIL, "Applicant has criminal records.") if application.criminal_records else \
        (Status.PASS, "Applicant has no criminal records.")
