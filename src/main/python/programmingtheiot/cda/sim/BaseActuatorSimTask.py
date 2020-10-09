#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import random

from programmingtheiot.data.ActuatorData import ActuatorData

class BaseActuatorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, actuatorType: int = ActuatorData.DEFAULT_ACTUATOR_TYPE, simpleName: str = "Actuator"):
		"""
		Initialization of class.
		Create an instance of BaseActuatorSimTask
		"""
		self.__actuatorType = actuatorType
		self.__simpleName = simpleName
		self.__latestAd = ActuatorData()
		
	def activateActuator(self, val: float) -> bool:
		"""
		Activate the Actuator
		
		@return bool
		"""
		logging.info("---> Emulating %s actuator ON:", str(self.getActuatorTypeName()))
		print('*******')
		print('* O N *')
		print('*******')
		print(self.getActuatorTypeName() + ' VALUE -> ' + str(val))
		self.__latestAd.setCommand(ActuatorData.COMMAND_ON)
		return True
		
	def deactivateActuator(self) -> bool:
		"""
		Deactivate the Actuator
		
		@return bool
		"""
		logging.info("---> Emulating %s actuator OFF: ", str(self.getActuatorTypeName()))
		print('*******')
		print('* OFF *') 
		print('*******')
		self.__latestAd.setCommand(ActuatorData.COMMAND_OFF)
		return True
	
	def getActuatorType(self):
		"""
		Get the ActuatorType of the instance
		
		@return str
		"""
		return self.__actuatorType
	
	def getLatestActuatorResponse(self) -> ActuatorData:
		"""
		Get the LatestActuatorResponse of the instance
		
		@return ActuatorData
		"""
		return self.__latestAd
	
	def getSimpleName(self) -> str:
		"""
		Get the SimpleName of the instance
		
		@return str
		"""
		return self.__simpleName
	
	def updateActuator(self, data: ActuatorData) -> bool:
		"""
		Update the Actuator
		
		@return bool
		"""
		if data:
			if data.getCommand() == ActuatorData.COMMAND_ON :
				self.activateActuator(data.getValue())
			else :
				self.deactivateActuator()
			self.__latestAd._handleUpdateData(data)
		
		self.__latestAd.setAsResponse()
		return True
	
	def getActuatorTypeName(self):
		"""
		Get the ActuatorTypeName of the instance
		
		@return str
		"""
		if self.__actuatorType == 1:
			return 'HVAC'
		if self.__actuatorType == 2:
			return 'HUMIDIFIER'
		return 'Unknown'
		
		