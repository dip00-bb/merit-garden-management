import datetime 
def check_valid_name(
    field,
    field_name,
    lower_bound,
    upper_bound,
    
    ):
    
    if len(field) < lower_bound:
        print(f"{field_name} Must have {lower_bound} character")
        raise ValueError(
            f"{field_name} Must have {lower_bound} character"
        )
    
    elif len(field) > upper_bound:
        print(f"{field_name} Can not have more than {upper_bound} character")
        raise ValueError(
            f"{field_name} Can not have more than {upper_bound} character"
        )
    
    
def is_valid_us_date(date_string):
    try:
        # %m = month, %d = day, %Y = 4-digit year
        datetime.strptime(date_string, "%m/%d/%Y")
        return True
    except ValueError:
        return False