import datetime 
from email_validator import validate_email, EmailNotValidError
def check_valid_name(
    field,
    field_name,
    lower_bound,
    upper_bound,
    
    ):
    
    if len(field) < lower_bound:
        raise ValueError(
            f"{field_name} Must have {lower_bound} character"
        )
    
    elif len(field) > upper_bound:
        raise ValueError(
            f"{field_name} Can not have more than {upper_bound} character"
        )
    
    
def is_valid_us_date(date_string):
    try:
        # %m = month, %d = day, %Y = 4-digit year
        datetime.datetime.strptime(date_string, "%m/%d/%Y")
    except :
        raise ValueError (
            f"Provide Date In Month/Date/Year format"
        )
        
def validate_bd_number(phone_number: str) -> bool:
    """Validates if a phone number is a 11-digit Bangladeshi mobile number starting with 01.
    
    Raises ValueError if criteria are not met.
    """
    # Remove any accidental leading/trailing whitespace
    clean_number = phone_number.strip()

    # Check all conditions in a clean if-else structure
    if not clean_number.isdigit():
        is_valid = False
    elif not clean_number.startswith("01"):
        is_valid = False
    elif len(clean_number) != 11:
        is_valid = False
    else:
        is_valid = True

    # Raise an error with the specific criteria if validation fails
    if not is_valid:
        raise ValueError(
            f"Invalid phone number: '{phone_number}'.\n"
            "A valid number must follow these criteria:\n"
            "- Must consist only of numbers (digits 0-9).\n"
            "- Must start exactly with '01'.\n"
            "- Must be exactly 11 digits long."
        )

    return True
        

def validate_gender(gender: str) -> bool:
    """Validates that the input gender is strictly 'male', 'female', or 'intersex'.
    
    Raises ValueError if the input does not match these criteria.
    """
    # Define the allowed lowercase categories
    valid_genders = ["male", "female", "intersex"]

    # Check if the input perfectly matches one of the valid options
    if gender in valid_genders:
        is_valid = True
    else:
        is_valid = False

    # Raise an error with explicit criteria if validation fails
    if not is_valid:
        raise ValueError(
            f"Invalid gender input: '{gender}'.\n"
            "The gender must follow these criteria:\n"
            "- Must be provided completely in lower case.\n"
            "- Must be exactly one of these options: 'male', 'female', or 'intersex'."
        )

    return True


def email_validator(email):
    try:
        validate_email(email)
    except:
        raise EmailNotValidError 

def validate_blood_group(blood_group: str) -> bool:
    """Validates that the input is a valid blood group.
    
    Raises ValueError if the input is not in the allowed list.
    """
    blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    
    # Remove any accidental spaces
    clean_bg = blood_group.strip()

    if clean_bg in blood_groups:
        is_valid = True
    else:
        is_valid = False

    if not is_valid:
        # Formats the list into a clean string for the error message
        allowed_options = ", ".join(blood_groups)
        raise ValueError(
            f"Invalid blood group: '{blood_group}'.\n"
            "The blood group must match one of these criteria:\n"
            f"- Must be exactly one of these options: {allowed_options}."
        )

    return True


def validate_religion(religion: str) -> bool:
    """Validates that the input is a valid religion category.
    
    Raises ValueError if the input is not in the allowed list.
    """
    religions = ["Islam", "Hinduism", "Buddhism", "Christianity", "Atheist", "Other"]
    
    # Remove any accidental spaces
    clean_religion = religion.strip()

    if clean_religion in religions:
        is_valid = True
    else:
        is_valid = False

    if not is_valid:
        # Formats the list into a clean string for the error message
        allowed_options = ", ".join(religions)
        raise ValueError(
            f"Invalid religion: '{religion}'.\n"
            "The religion must match one of these criteria:\n"
            f"- Must match the exact capitalization of these options: {allowed_options}."
        )

    return True