#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.data.ActuatorData import ActuatorData

from programmingtheiot.cda.sim.HumidifierActuatorSimTask import HumidifierActuatorSimTask
from programmingtheiot.cda.sim.HvacActuatorSimTask import HvacActuatorSimTask

class ActuatorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self, useEmulator: bool = False):
		"""
		Initialization of class.
		Create an instance of ActuatorAdapterManager
		"""
		self.useEmulator = useEmulator
		self.dataMsgListener = None
		if self.useEmulator :
			logging.info("---> Emulators will be used ")
		else:
			logging.info("---> Simulators will be used ")
			# create the humidifier actuator
			self.humidifierActuator = HumidifierActuatorSimTask()
			# create the HVAC actuator
			self.hvacActuator = HvacActuatorSimTask()
			

	def sendActuatorCommand(self, data: ActuatorData) -> bool:
		"""
		Send Actuator Command to Actuator
		
		@return bool
		"""
		if self.dataMsgListener :
			self.dataMsgListener.handleActuatorCommandResponse(data)
			logging.info('Actuator command received. Processing...')
			if ~self.useEmulator:
				if (data.getActuatorType() == ActuatorData.HUMIDIFIER_ACTUATOR_TYPE):
					if ~data.isResponseFlagEnabled(): 
						self.humidifierActuator.updateActuator(data)
				if (data.getActuatorType() == ActuatorData.HVAC_ACTUATOR_TYPE):
					if ~data.isResponseFlagEnabled(): 
						self.hvacActuator.updateActuator(data)
			
	
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		"""
		set Data MessageListener which is used for monitor the Actuator excuate
		
		@return bool
		"""
		if listener:
			self.dataMsgListener = listener
