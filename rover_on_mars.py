class plateau: #starting platform 
	def __init__(self, x_coordinate = "", y_coordinate = "", rover = ""):
		self.x_coordinate = x_coordinate
		self.y_coordinate = y_coordinate
		self.rover = [] #quantity of rovers in a list
	def createRovers(self,quantity):
		for i in range(quantity):
			self.rover.append(rover()) #creating rovers and appending to list 
class rover:
	def __init__(self, x_coordinate = "", y_coordinate = "", orientation = ""):
		self.x_coordinate = x_coordinate
		self.y_coordinate = y_coordinate
		self.orientation = orientation
	def movement(self, movementInstructions, plateau): 
		for instruction in movementInstructions: #the movement of the commands in the text file.
			if instruction == 'M': #move one 
				if self.orientation== 'N': 
					self.y_coordinate += 1
				elif self.orientation == 'E':
					self.x_coordinate += 1
				elif self.orientation == 'S':
					self.y_coordinate -= 1
				elif self.orientation == 'W':
					self.x_coordinate -= 1
			elif instruction == 'L' or 'R':
				positionCalculator(instruction, self) #list of positions clockwise 
			if self.x_coordinate > plateau.x_coordinate:
				self.x_coordinate = plateau.x_coordinate
			if self.x_coordinate < 0:
				self.x_coordinate = 0 #north 
			if self.y_coordinate > plateau.y_coordinate:
				self.y_coordinate = plateau.y_coordinate
			if self.y_coordinate < 0:
				self.y_coordinate = 0
def positionCalculator(instruction, rover):
	position = ['N','E','S','W']
	if instruction == 'L':
		index = position.index(rover.orientation)
		if index == 0:
			rover.orientation = 'W'
		else:
			rover.orientation = position[index-1]
	elif instruction == 'R':
		index = position.index(rover.orientation)
		if index == 3:
			rover.orientation = 'N'
		else:
			rover.orientation = position[index+1]
def readInput():
	try:
		data = open('test.txt', 'r')
		dataInput = []
		if data.mode == 'r':
			for line in data:
				dataInput.append(line.replace('\n', ''))
		data.close()
		if len(dataInput) > 0:
			return dataInput
	except:
		print('File could not be found, check if test.txt and rover.py is in the same folder or directory')
def createPlateau(plateau, dataInput,rovers):
	plateau = plateau(int(dataInput[0][0]), int(dataInput[0][2]))
	plateau.createRovers(rovers)
	return plateau
def startRover(plateau):
	counter = 1
	for rover in plateau.rover:
		rover.x_coordinate = int(dataInput[counter][0])
		rover.y_coordinate = int(dataInput[counter][2])
		rover.orientation = dataInput[counter][4]
		rover.movement(dataInput[counter+1], plateau)
		counter += 2
		print(str(rover.x_coordinate) + ' ' + str(rover.y_coordinate) + ' ' + rover.orientation)
dataInput = readInput()
if dataInput:
	plateau = createPlateau(plateau, dataInput, (len(dataInput) - 1) // 2)
	startRover(plateau)
