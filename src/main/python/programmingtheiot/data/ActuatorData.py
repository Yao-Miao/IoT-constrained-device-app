#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.BaseIotData import BaseIotData

class ActuatorData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_COMMAND = 0
	COMMAND_OFF = DEFAULT_COMMAND
	COMMAND_ON = 1

	# for now, actuators will be 1..99
	# and displays will be 100..1999
	DEFAULT_ACTUATOR_TYPE = 0
	
	HVAC_ACTUATOR_TYPE = 1
	HUMIDIFIER_ACTUATOR_TYPE = 2
	LED_DISPLAY_ACTUATOR_TYPE = 100
	


	def __init__(self, actuatorType = DEFAULT_ACTUATOR_TYPE, d = None):
		"""
		Initialization of class.
		Create an instance of ActuatorData
		"""
		super(ActuatorData, self).__init__(d = d)
		
		# The private member in the class
		# add by Yao Miao
		self.__actuatorType = actuatorType
		self.__command = self.DEFAULT_COMMAND
		self.__stateData = ""
		self.__value = 0.0
		self.__responseFlag = False
	
		
	def getActuatorType(self):
		"""
		Get the ActuatorType of the instance
		
		@return str
		"""
		return self.__actuatorType	
	
	def getCommand(self) -> int:
		"""
		Get the Command of the instance
		
		@return int
		"""
		return self.__command
	
	def getStateData(self) -> str:
		"""
		Get the StateData of the instance
		
		@return str
		"""
		return self.__stateData
	
	def getValue(self) -> float:
		"""
		Get the Value of the instance
		
		@return float
		"""
		return self.__value
	
	def isResponseFlagEnabled(self) -> bool:
		"""
		Get the ResponseFlag of the instance
		
		@return bool
		"""
		return self.__responseFlag
	
	def setCommand(self, command: int):
		"""
		Set the Command of the instance
		"""
		self.__command = command
	
	def setAsResponse(self):
		"""
		Set the ResponseFlag of the instance
		"""
		self.__responseFlag = True
		
	def setStateData(self, stateData: str):
		"""
		Set the StateData of the instance
		"""
		self.__stateData = stateData
	
	def setValue(self, val: float):
		"""
		Set the value of the instance
		"""
		self.__value = val
		
	def _handleUpdateData(self, data):
		"""
		update the instance
		"""
		self.__command = data.__command
		self.__stateData = data.__stateData
		self.__value = data.__value
		
		