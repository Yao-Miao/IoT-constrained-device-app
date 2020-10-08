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
		self.__actuatorType = actuatorType
		self.__simpleName = simpleName
		self.__latestAd = ActuatorData()
		
	def activateActuator(self, val: float) -> bool:
		logging.info("---> The Actuator just send an \"ON\" Command, the value is " + str(val))
		self.__latestAd.setCommand(ActuatorData.COMMAND_ON)
		return True
		
	def deactivateActuator(self) -> bool:
		logging.info("---> The Actuator just send an \"OFF\" Command. ")
		self.__latestAd.setCommand(ActuatorData.COMMAND_OFF)
		return True
		
	def getLatestActuatorResponse(self) -> ActuatorData:
		return self.__latestAd
	
	def getSimpleName(self) -> str:
		pass
	
	def updateActuator(self, data: ActuatorData) -> bool:
		if data:
			if data.getCommand() == ActuatorData.COMMAND_ON :
				self.activateActuator(data.getValue())
			else :
				self.deactivateActuator()
			self.__latestAd._handleUpdateData(data)
		
		self.__latestAd.setAsResponse()
		return True
		
		