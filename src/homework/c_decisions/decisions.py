 def get_options_ratio(option, total):
    if total == 0:
        print("Invalid: Total cannot be zero")
        return 0  
    return option / total

def get_faculty_rating(ratio):
    if ratio >= 0.9 and ratio < 1:
        return "Excellent"
    elif ratio >= 0.8 and ratio < 0.9:
        return "Very Good"
    elif ratio >= 0.7 and ratio < 0.8:
        return "Good"
    elif ratio >= 0.6 and ratio < 0.7:
        return "Needs Improvement"
    elif ratio >= 0 and ratio < 0.6:
        return "Unacceptable"
    else:
        return "Invalid"
