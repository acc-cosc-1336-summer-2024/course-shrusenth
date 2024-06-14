def get_options_ratio(option, total):
  if total == 0:
    print("Invalid: Total cannot be zero")
return option / total

def get_faculty_rating(ratio):
  if (ratio >= 0.9 and ratio < 1):
        return "Excellent"
    elif(ratio < 0.9 and ratio >= 0.8):
      return "Very Good"
    elif(ratio <.8 and ratio >= .7):
      return "Good"
    elif(ratio <.7 and ratio >= .6):
        return "Needs Improvement"
    elif(ratio <.6 and ratio >= 0):
      return "Unnacceptable"
else:
return "Invalid"


