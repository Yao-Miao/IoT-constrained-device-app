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
import programmingtheiot.common.ConfigConst as ConfigConst

class BaseActuatorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, actuatorType: int = ActuatorData.DEFAULT_ACTUATOR_TYPE, simpleName: str = "Actuator", actuatorName = ConfigConst.NOT_SET):
		"""
		Initialization of class.
		Create an instance of BaseActuatorSimTask
		"""
		self.actuatorType = actuatorType
		self.simpleName = simpleName
		self.latestAd = ActuatorData(name=actuatorName)
		
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
		self.latestAd.setCommand(ActuatorData.COMMAND_ON)
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
		self.latestAd.setCommand(ActuatorData.COMMAND_OFF)
		return True
	
	def getActuatorType(self):
		"""
		Get the ActuatorType of the instance
		
		@return str
		"""
		return self.actuatorType
	
	def getLatestActuatorResponse(self) -> ActuatorData:
		"""
		Get the LatestActuatorResponse of the instance
		
		@return ActuatorData
		"""
		return self.latestAd
	
	def getSimpleName(self) -> str:
		"""
		Get the SimpleName of the instance
		
		@return str
		"""
		return self.simpleName
	
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
			self.latestAd._handleUpdateData(data)
		
		self.latestAd.setAsResponse()
		return True
	
	def getActuatorTypeName(self):
		"""
		Get the ActuatorTypeName of the instance
		
		@return str
		"""
		if self.actuatorType == 1:
			return 'HVAC'
		if self.actuatorType == 2:
			return 'HUMIDIFIER'
		return 'Unknown'
		
		