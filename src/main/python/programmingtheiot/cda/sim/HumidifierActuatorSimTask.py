#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask
import programmingtheiot.common.ConfigConst as ConfigConst

class HumidifierActuatorSimTask(BaseActuatorSimTask):
	"""
	This is a simple wrapper for an Actuator abstraction - it provides
	a container for the actuator's state, value, name, and status. A
	command variable is also provided to instruct the actuator to
	perform a specific function (in addition to setting a new value
	via the 'val' parameter.
	
	"""

	def __init__(self):
		"""
		Initialization of class.
		Create an instance of HumidifierActuatorSimTask
		"""
		super(HumidifierActuatorSimTask, self).__init__(actuatorType = ActuatorData.HUMIDIFIER_ACTUATOR_TYPE, simpleName = "HUMIDIFIER", actuatorName = ConfigConst.HVAC_ACTUATOR_NAME)
		
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
