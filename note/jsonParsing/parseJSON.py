import sys
import json

def buildDict(id,courseNumber,courseName):
	result = {}
	result['id'] = id
	result['code'] = courseNumber
	result['name'] = courseName
	return result

courses = []
for i in range(88):
	line = input()
	# print(line.split(' ')[0])
	courseNumber = line.split(' ')[0]
	# print(' '.join(courseName))
	courseName = line.split(' ')[1:]
	# print(courseNumber + " " + ' '.join(courseName))
	course = buildDict(i,courseNumber,' '.join(courseName)[0:-1])
	courses.append(course)

with open('UTCSCourses.json', 'w') as data_file:
	json.dump(courses,data_file)