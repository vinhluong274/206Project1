#Vinh Luong
#vinhbl@umich.edu
#GITHUB USERNAME: vinhluong274
#GITHUB REPO LINK: https://github.com/vinhluong274/206Project1

import os
import filecmp
from datetime import datetime, date
import math

def getData(file):
#Input: file name

#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.
	csv = open(file, 'r')
	stringList = [] #list to store each line's data
	dictList = {} #dictionary to be appended to final list
	headers = [] #list of first line/headers
	listItems = [] #final list

	headerString = csv.readline()
	headers = headerString.strip("\n").split(",")
	for header in headers:
		dictList[header] = 0

	for line in csv:
		stringList = line.strip("\n").split(",")
		listItems.append({
			"First": stringList[0],
			"Last": stringList[1],
			"Email": stringList[2],
			"Class": stringList[3],
			"DOB": stringList[4]
			})

	return(listItems)


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	data_sorted = sorted(data, key=lambda item: item[col])
	d = data_sorted[0]
	FullName = d["First"] + ' ' + d["Last"]
	return FullName



#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
#need to use items() on dictionaries, but also count number of instances
#freshman, sophomore, etc appear.
	tupsList = []
	for i in data:
		tup = sorted(i.items())
		for x in tup:
			tupsList.append(x)

	Freshman = tupsList.count(('Class', 'Freshman'))
	Sophomore = tupsList.count(('Class',"Sophomore"))
	Junior = tupsList.count(('Class',"Junior"))
	Senior = tupsList.count(('Class',"Senior"))
	finalList = [('Senior', Senior), ('Junior', Junior), ('Freshman', Freshman), ('Sophomore', Sophomore)]
	finalList = sorted(finalList, key=lambda x : x[1], reverse=True)
	return finalList


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

#creates a list of tuples containing all of the dictionary objects
	tupsList = []
	for i in a:
		tup = sorted(i.items())
		for x in tup:
			tupsList.append(x)

#if the tuple includes the element DOB, add the date to a list
	dobList = []
	for t in tupsList:
		for item in t:
			if "DOB" in item:
				dobList.append(t[1])

#Split the date into a list and append the middle item (the date) to a list
	dayList = []
	for date in dobList:
		d = date.split("/")
		dayList.append(d[1])

#Check to see how many counts are present in the list and cast as an int
	numberCounts = 0
	commonDay = 0
	for number in dayList:
		counts = dayList.count(number)
		if counts > numberCounts:
			numberCounts = counts
			commonDay = number
	return int(commonDay)


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

#creates a list of tuples containing all of the dictionary objects
	tupsList = []
	for i in a:
		tup = sorted(i.items())
		for x in tup:
			tupsList.append(x)

#if the tuple includes the element DOB, add the date to a list
	dobList = []
	for t in tupsList:
		for item in t:
			if "DOB" in item:
				dobList.append(t[1])
	#create list of ages, strips age into datetime format and adds it to list
	ages = []
	for date in dobList:
		dt = datetime.strptime(date, "%m/%d/%Y")
		age = ((datetime.today() - dt).days/365)
		ages.append(age)

#create var for total, add all age, divide by length of list (total # of ages)
	total = 0
	for old in ages:
		total += old
	avg = total/(len(ages))
	avg = math.floor(avg)

	return avg


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
#sorts data based on col and creates list of tuples
	data_sorted = sorted(a, key=lambda item: item[col])
	f = open(fileName, "w")
	tuples = []
	for i in data_sorted:
		tuples.append(sorted(i.items()))

#Iterates through list of tuples and gets data appends data to line variable
#Writes line to file with an additional comma and line break
	for x in tuples:
		fName = x[3][1]
		lName = x[4][1]
		Email = x[2][1]
		line = fName + "," + lName + "," + Email
		f.write(line)
		f.write("\n")



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
