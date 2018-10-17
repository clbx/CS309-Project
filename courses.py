import csv
import re

# Python script to read course data and put it into sql queries


data = []

# Get all of our data in
with open('ScrapedCourses.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Now to parse the raw csv
print(data[0])


# INPUT
# 0 - Course ID [36390]
# 1 - Course Code, also contains Department [AC 101 - -BU - - A]
# 2 - Name of Class [INTRODUCTION TO ACCOUNTING]
# 3 - Instructor [Miller, Jared]
# 4 - Status [Open]
# 5 - Seats Open/Total [35/35]
# 6 - Time offered & Room [MWF (12:30pm-1:40pm) H 215]
# 7 - Credits

# See README for Output design

newdata = []

#Course ID
newdata.append(data[0][0])



m = re.search(r'([^\s]+)',data[0][1]) # Regex to get everything before the space
newdata.append(m.group())
m = re.search(r'\s(.*)',data[0][1]) # Regex to get everything after spaces
newdata.append(m.group())
newdata.append(data[0][2])
m = re.search(r'^(.+?),',data[0][3])
newdata.append(m.group()[:-1]) #TODO: Fix me im bad



print(newdata)
#for i in range(len(data)):