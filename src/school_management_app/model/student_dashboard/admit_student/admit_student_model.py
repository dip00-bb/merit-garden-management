from ....utilitis import check_valid_name
from ....utilitis import is_valid_us_date
class AdmitStudentModel:

    def __init__(
        self,
        student_name="",
        mother_name="",
        father_name="",
        date_of_birth="",
        gender="",
        phone_number="",
        whats_app_number="",
        email="",
        blood_group="",
        religion="",

        present_division="",
        present_district="",
        present_upazila="",
        present_address="",

        permanent_division="",
        permanent_district="",
        permanent_upazila="",
        permanent_address="",

        to_admit="",
        group_name="",
        opt_sub="",
        previous_school=""
    ):
        # ---------------------------------
        # Personal Information
        # ---------------------------------
        
        check_valid_name(student_name,"Student Name",3,15)
        check_valid_name(mother_name,"Mother Name",3,15)
        check_valid_name(father_name,"Father Name",3,15)        
        is_valid_us_date(date_of_birth)
        
        
        self.student_name = student_name
        self.mother_name = mother_name
        self.father_name = father_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone_number = phone_number
        self.whats_app_number = whats_app_number
        self.email = email
        self.blood_group = blood_group
        self.religion = religion

        # ---------------------------------
        # Present Address
        # ---------------------------------
                


        
        self.present_division = present_division
        self.present_district = present_district
        self.present_upazila = present_upazila
        self.present_address = present_address

        # ---------------------------------
        # Permanent Address
        # ---------------------------------

        self.permanent_division = permanent_division
        self.permanent_district = permanent_district
        self.permanent_upazila = permanent_upazila
        self.permanent_address = permanent_address

        # ---------------------------------
        # Admission Information
        # ---------------------------------

        self.to_admit = to_admit
        self.group_name = group_name
        self.opt_sub = opt_sub
        self.previous_school = previous_school
