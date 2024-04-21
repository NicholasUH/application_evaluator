from dataclasses import dataclass

@dataclass
class Application:
    employment: bool = False
    criminal_records: bool = False
    credit_records: bool = False
    security_clearance: bool = False
