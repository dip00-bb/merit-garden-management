class FeesModel:
    def __init__(
        self,
        student_id, 
        admission_fee, 
        monthly_fee,
        academic_year
    ):
        self.student_id = student_id
        self.admission_fee = admission_fee
        self.monthly_fee = monthly_fee
        self.academic_year = academic_year