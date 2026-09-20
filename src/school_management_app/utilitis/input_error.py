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
        


def email_validator(email):
    try:
        validate_email(email)
    except:
        raise EmailNotValidError 

def validate_image(image_data):

    if len(image_data)<=0:
        raise ValueError(
            f"Image field can not be empty"
        )
        
    if type(image_data) is not bytes:
        raise ValueError(
            f"It is not a valid Image"
        )