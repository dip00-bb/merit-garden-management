class FeesRepository:
    def __init__(self, database):
        self.database = database
        self.connection=self.database.connect()
        self.cursor=self.connection.cursor()
        
    def create_fees(
        self,
        fees_model
        ):
        
        
        query = """
            INSERT INTO student_fee (

            student_id, 
            admission_fee, 
            monthly_fee,
            academic_year,
            total_fee
            
            )
            
            VALUES (?, ?, ?, ?, ?)
        """
        
        total_fee=(fees_model.monthly_fee*12)+fees_model.admission_fee
        
        params = (
            fees_model.student_id,
            fees_model.admission_fee,
            fees_model.monthly_fee,
            fees_model.academic_year,
            total_fee
        )
        self.cursor.execute(query, params)
        self.connection.commit()
        
    # def find_fees_information(self,roll,class_,year):
    #     query="""
    #         SELECT * FROM student_fee
    #     """
        