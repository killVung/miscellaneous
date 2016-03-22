import sys
from bs4 import BeautifulSoup
import pprint
from bs4 import UnicodeDammit
import json
from firebase import firebase

firebase = firebase.FirebaseApplication('https://scorching-heat-4336.firebaseio.com/',None)
def buildDict(id,courseID,courseCode,courseName):
	result = {}
	result['id'] = id
	result['courseID'] = courseID + courseCode
	# result['codeCode'] = courseCode
	result['courseName'] = courseName

	#Upload to Firebase
	firebase.put('allCourses',result['courseID'],result['courseName'])

	return result

'''
Some courses have TCCN code on it
'''
def removeTCCN(courseName):
	if "TCCN" in courseName:
		courseName = courseName.split('.')[1]		
		return courseName
	else:
		# print(courseName)
		return courseName

i = 1
coursesList = []
for s in sys.stdin:	
	soup = BeautifulSoup(open(s[:-1]),'html')
	# dammit = UnicodeDammit(soup.h5.string)
	# print(dammit.unicode_markup)
	for courses in soup.find_all('h5'):
		#Expected either Course ID. Course name, or Course ID, Course ID, .., Course Name
		course = courses.string 
		#Skip Courses with multple Course ID for now
		finalCourse = {}
		if "," not in course:
			courseID = course.split(' ')[0]
			courseName = course.split(' ')[1:]						
			# print(courseID.split('\xa0')) #THX	
			# print(' '.join(courseName))

			if len(courseID.split('\xa0')) == 3:
				newCourseID = ' '.join(courseID.split('\xa0')[0:2]).replace(' ','')				
				newCourseCode = ' '.join(courseID.split('\xa0')[2]).replace(' ','')[0:-1].replace('.','')
				newCourseName = removeTCCN(' '.join(courseName))
				# print(newCourseID)
				# print(newCourseCode)
				# print(' '.join(courseName))				
				finalCourse = buildDict(i,newCourseID,newCourseCode,newCourseName)

			else:
				newCourseID = ' '.join(courseID.split('\xa0')[0]).replace(' ','')				
				newCourseCode = ' '.join(courseID.split('\xa0')[1]).replace(' ','').replace('.','')				
				newCourseName = removeTCCN(' '.join(courseName))
				# print(newCourseName)			
				# print(newCourseID)					
				# print(newCourseCode)
				# print(' '.join(courseName))
				finalCourse = buildDict(i,newCourseID,newCourseCode,newCourseName)								

			i += 1
			coursesList.append(finalCourse)
	print(pprint.pprint(coursesList))
with open('UTAustinCourses.json', 'w') as data_file:
	json.dump(coursesList,data_file)



	# print('\n')
	
