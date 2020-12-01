#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.BaseIotData import BaseIotData
import programmingtheiot.common.ConfigConst as ConfigConst

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
	


	
	def __init__(self, actuatorType: int = DEFAULT_ACTUATOR_TYPE, name = ConfigConst.NOT_SET, d = None):
		"""
		Constructor.
		
		@param d Defaults to None. The data (dict) to use for setting all parameters.
		It's provided here as a convenience - mostly for testing purposes. The utility
		in DataUtil should be used instead.
		"""
		super(ActuatorData, self).__init__(name = name, d = d)
		
		self.isResponse = False
		self.actuatorType = actuatorType
		
		if d:
			self.command = d['command']
			self.stateData = d['stateData']
			self.value = d['curValue']
			self.actuatorType = d['actuatorType']
		else:
			self.command = self.DEFAULT_COMMAND
			self.stateData = None
			self.value = self.DEFAULT_VAL
			self.actuatorType = actuatorType
	
		
	def getActuatorType(self):
		"""
		Get the ActuatorType of the instance
		
		@return str
		"""
		return self.actuatorType	
	
	def getCommand(self) -> int:
		"""
		Get the Command of the instance
		
		@return int
		"""
		return self.command
	
	def getStateData(self) -> str:
		"""
		Get the StateData of the instance
		
		@return str
		"""
		return self.stateData
	
	def getValue(self) -> float:
		"""
		Get the Value of the instance
		
		@return float
		"""
		return self.value
	
	def isResponseFlagEnabled(self) -> bool:
		"""
		Get the ResponseFlag of the instance
		
		@return bool
		"""
		return self.isResponse
	
	def setCommand(self, command: int):
		"""
		Set the Command of the instance
		"""
		self.command = command
	
	def setAsResponse(self):
		"""
		Set the ResponseFlag of the instance
		"""
		self.responseFlag = True
		
	def setStateData(self, stateData: str):
		"""
		Set the StateData of the instance
		"""
		self.stateData = stateData
	
	def setValue(self, val: float):
		"""
		Set the value of the instance
		"""
		self.value = val
		
	def _handleUpdateData(self, data):
		"""
		update the instance
		"""
		self.command = data.command
		self.stateData = data.stateData
		self.value = data.value
		
		