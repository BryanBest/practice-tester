import pickle
import os
clear = lambda: os.system('cls')

class Test:
	def __init__(self, name, answers):
		self.name = name
		self.answers = answers

testList = []

try:
	savedFile = open("save", "rb")
	testList = pickle.load(savedFile)
	savedFile.close()
except:
	print("No save detected.")

def runTest(test):
	clear()
	print("\n==========Running Test '{0}'==========".format(test.name))
	print("Input the answer to each question and hit Enter.\n")
	index = 1
	answers = []
	report = []
	for ques in test.answers:
		answers.append(input("Question {0}: ".format(index)))
		index += 1
	answerIndex = 0
	print("\n==========The Test has ended==========")
	print("Listed below are the answers you gave, followed by the correct answer if you got it wrong.\n")
	for answer in answers:
		if answer == test.answers[answerIndex]:
			report.append("Question {0}: {1} (Correct)".format(answerIndex+1,answer))
		else:
			report.append("Question {0}: {1} (Incorrect - Answer was '{2}')".format(answerIndex+1, answer, test.answers[answerIndex]))
		answerIndex+=1
	for x in report:
		print(x)
	input("\nHit enter to continue\n")

def startup():
	print("\n==========Welcome to PracticeTester. Please select an option.==========\n")
	if len(testList) == 0:
		print("1. Create New Test\n")
	else:
		optionNum = 1
		for x in testList:
			print("{0}. {1}".format(optionNum, testList[optionNum-1].name))
			optionNum = optionNum + 1
		print("{0}. Create New Test".format(optionNum))
		print("{0}. Delete Test\n".format(optionNum+1))
	while True:
		choice = input("Enter a number: ")
		try:
			choice = int(choice)
			break;
		except:
			print("Please input a valid number.")
			
	if choice == len(testList)+1:
		testName = input("\nName your Test: ")
		testAnswers = []
		questionNum = 1		
		while True:
			print("\nEnter the answer to question {0}, then hit Enter. Input 'stop' to stop.\n".format(questionNum))
			answer = input("Answer: ")
			if answer.lower() == "stop":
				break;
			else:
				testAnswers.append(answer)
				questionNum = questionNum+1
		testList.append(Test(testName, testAnswers))
		saveFile = open("save", "wb")
		pickle.dump(testList, saveFile)
		saveFile.close()
	elif choice == len(testList)+2:
		print("\nPlease select a Test to delete\n")
		optionNum = 1
		for x in testList:
			print("{0}. {1}".format(optionNum, testList[optionNum-1].name))
			optionNum = optionNum + 1
		while True:
			deleteNum = input("\nEnter a number: ")
			try:
				deleteNum = int(deleteNum)
				break;
			except:
				print("Please input a valid number.")
		while True:
			try:
				del testList[deleteNum-1]
				saveFile = open("save", "wb")
				pickle.dump(testList,saveFile)
				saveFile.close()
				break;
			except:
				print("\nPlease pick a valid Test\n")
		startup()
	else:
		try:
			testToTake = testList[choice-1]	
		except:
			print("\n==========ERROR: Please pick a valid Test==========\n")
		runTest(testToTake)
	startup()


	


	
startup()