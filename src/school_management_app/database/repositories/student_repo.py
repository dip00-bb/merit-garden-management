class StudentRepository:

    def __init__(self, database):
        self.database = database
        self.connection=self.database.connect()
        self.cursor=self.connection.cursor()
    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def create_student(self, student):
        query = """
            INSERT INTO students (
                student_name,
                student_image,
                mother_name,
                father_name,
                date_of_birth,
                gender,
                phone_number,
                whats_app_number,
                email,
                blood_group,
                religion,

                present_division,
                present_district,
                present_upazila,
                present_address,

                permanent_division,
                permanent_district,
                permanent_upazila,
                permanent_address,

                to_admit,
                current_class,
                admission_fee,
                monthly_fee,
                class_roll,
                group_name,
                optional_subject,
                previous_school,
                
                admitted_year,
                academic_year,
                student_status

                
            )
            VALUES (
                ?, ?, ?, ?, 
                ?, ?, ?, ?,  
                ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?,?
            
            )
        """
        
        roll_query = """
        SELECT COALESCE(MAX(CAST(class_roll AS INTEGER)), 0) + 1
        FROM students
        WHERE academic_year = ?
        AND to_admit = ?
            """
        class_roll=  self.cursor.execute(roll_query,(
            student.academic_year,student.to_admit
        )).fetchone()[0]
        

        params = (
            student.student_name,
            student.student_image,
            student.mother_name,
            student.father_name,
            student.date_of_birth,
            student.gender,
            student.phone_number,
            student.whats_app_number,
            student.email,
            student.blood_group,
            student.religion,

            student.present_division,
            student.present_district,
            student.present_upazila,
            student.present_address,

            student.permanent_division,
            student.permanent_district,
            student.permanent_upazila,
            student.permanent_address,

            student.to_admit,
            student.current_class,    
            student.admission_fee,
            student.monthly_fee,
            class_roll,        
            student.group_name,
            student.opt_sub,
            student.previous_school,
            
            
            student.admitted_year,
            student.academic_year,
            student.student_status,

        )
        self.cursor.execute(query, params)
        self.connection.commit()



    # ---------------------------------------------------------
    # READ - GET ONE STUDENT
    # ---------------------------------------------------------

    def get_student_by_id(self, student_id):

        query = """
            SELECT *
            FROM students
            WHERE id = ?
        """

        return self.database.fetch_one(
            query,
            (student_id,)
        )

    # ---------------------------------------------------------
    # READ - GET ALL STUDENTS
    # ---------------------------------------------------------

    def get_all_students(self):

        query = """
            SELECT *
            FROM students
            ORDER BY id DESC
        """

        return self.database.fetch_all(query)

    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update_student(self, student_id, student):

        query = """
            UPDATE students
            SET
                student_name = ?,
                mother_name = ?,
                father_name = ?,
                date_of_birth = ?,
                gender = ?,
                phone_number = ?,
                whats_app_number = ?,
                email = ?,
                blood_group = ?,
                religion = ?,

                present_division = ?,
                present_district = ?,
                present_upazila = ?,
                present_address = ?,

                permanent_division = ?,
                permanent_district = ?,
                permanent_upazila = ?,
                permanent_address = ?,

                to_admit = ?,
                group_name = ?,
                optional_subject = ?,
                previous_school = ?,

                updated_at = CURRENT_TIMESTAMP

            WHERE id = ?
        """

        params = (
            student["student_name"],
            student["mother_name"],
            student["father_name"],
            student["date_of_birth"],
            student["gender"],
            student["phone_number"],
            student["whats_app_number"],
            student["email"],
            student["blood_group"],
            student["religion"],

            student["present_division"],
            student["present_district"],
            student["present_upazila"],
            student["present_address"],

            student["permanent_division"],
            student["permanent_district"],
            student["permanent_upazila"],
            student["permanent_address"],

            student["to_admit"],
            student["group_name"],
            student["optional_subject"],
            student["previous_school"],

            student_id
        )

        return self.database.execute(query, params)

    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------

    def delete_student(self, student_id):

        query = """
            DELETE FROM students
            WHERE id = ?
        """

        return self.database.execute(
            query,
            (student_id,)
        )

    # ---------------------------------------------------------
    # SEARCH
    # ---------------------------------------------------------

    def search_students(self, keyword):

        query = """
            SELECT *
            FROM students
            WHERE
                student_name LIKE ?
                OR phone_number LIKE ?
                OR whats_app_number LIKE ?
                OR email LIKE ?
            ORDER BY id DESC
        """

        search_pattern = f"%{keyword}%"

        params = (
            search_pattern,
            search_pattern,
            search_pattern,
            search_pattern
        )

        return self.database.fetch_all(
            query,
            params
        )