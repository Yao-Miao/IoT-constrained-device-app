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
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask
import programmingtheiot.common.ConfigConst as ConfigConst

class HvacActuatorSimTask(BaseActuatorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		"""
		Initialization of class.
		Create an instance of HvacActuatorSimTask
		"""
		super(HvacActuatorSimTask, self).__init__(actuatorType = ActuatorData.HVAC_ACTUATOR_TYPE, simpleName = "HVAC", actuatorName = ConfigConst.HVAC_ACTUATOR_NAME)
		
	def activateActuator(self, val: float) -> bool:
		"""
		Activate the Actuator
		
		@return bool
		"""
		return super().activateActuator(val)
		
	def deactivateActuator(self) -> bool:
		"""
		Deactivate the Actuator
		
		@return bool
		"""
		return super().deactivateActuator()
		
	def updateActuator(self, data: ActuatorData) -> ActuatorData:
		"""
		Update the Actuator
		
		@return ActuatorData
		"""
		super().updateActuator(data)
		return data
