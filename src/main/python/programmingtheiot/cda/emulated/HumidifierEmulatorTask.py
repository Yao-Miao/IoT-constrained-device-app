#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

from pisense import SenseHAT
from pisense import *

class HumidifierEmulatorTask(BaseActuatorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		"""
		Initialization of class.
		Create an instance of HumidifierEmulatorTask
		"""
		super(HumidifierEmulatorTask, self).__init__(actuatorType = ActuatorData.HUMIDIFIER_ACTUATOR_TYPE, simpleName = "HUMIDIFIER")
		
		# Create an instance of SenseHAT and set the emulate flag to True if running the emulator, or False if using real hardware
		# This can be read from ConfigUtil using the ConfigConst.CONSTRAINED_DEVICE section and the ConfigConst.ENABLE_SENSE_HAT_KEY
		# If the ConfigConst.ENABLE_SENSE_HAT_KEY is False, set the emulate flag to True, otherwise set to False
		configUtil = ConfigUtil()
		if configUtil.getBoolean(section= ConfigConst.CONSTRAINED_DEVICE, key= ConfigConst.ENABLE_SENSE_HAT_KEY):
			enableEmulation = False 
		else:
			enableEmulation = True
		
		self.sh = SenseHAT(emulate = enableEmulation)
		

	def _handleActuation(self, cmd: int, val: float = 0.0, stateData: str = None) -> int:
		"""
		Receive command and val, display command on screen
		"""
		# NOTE: use the API instructions for pisense for help
		if cmd == ActuatorData.COMMAND_ON:
			if self.sh.screen:
				# create a message with the value and an 'ON' message, then scroll it across the LED display
				self.sh.screen.scroll_text('ON!')
			else:
				logging.warning("No SenseHAT LED screen instance to update.")
				return -1
		else:
			if self.sh.screen:
				# create a message with an 'OFF' message, then scroll it across the LED display
				self.sh.screen.scroll_text('OFF!')
			else:
				logging.warning("No SenseHAT LED screen instance to clear / close.")
				return -1
		
