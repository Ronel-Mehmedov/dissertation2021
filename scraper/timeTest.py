from datetime import datetime

str = "April 04, 2021"

date_object = datetime.strptime(str, '%B %d, %Y')
print(date_object)