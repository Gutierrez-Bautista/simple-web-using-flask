def validate_integer(val):
    try:
        val = int(val)
        return True, "200"
    except ValueError:
        return False, 'Not An Integer'

def validate_positive_integer(val):
    try:
        val = int(val)
        return (True, "200") if val > 0 else (False, "Not A Positive Integer")
    except ValueError:
        return False, 'Not An Integer'