import decisions

options = float(input("What is the number of options "))
total = float(input("What is the total amount ")) 
ratio = decisions.get_options_ratio(options, total)
rating = decisions.get_faculty_rating(ratio)

print(rating)
#
