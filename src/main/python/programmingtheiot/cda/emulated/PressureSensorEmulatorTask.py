#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.SensorData import SensorData

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator

from pisense import SenseHAT

class PressureSensorEmulatorTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, dataSet = None):
		# Create an instance of SenseHAT and set the emulate flag to True if running the emulator, or False if using real hardware
		# This can be read from ConfigUtil using the ConfigConst.CONSTRAINED_DEVICE section and the ConfigConst.ENABLE_SENSE_HAT_KEY
		# If the ConfigConst.ENABLE_SENSE_HAT_KEY is False, set the emulate flag to True, otherwise set to False
		super(PressureSensorEmulatorTask, self).__init__(SensorData.PRESSURE_SENSOR_TYPE, minVal = SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE, maxVal = SensorDataGenerator.HI_NORMAL_ENV_PRESSURE)
		
		configUtil = ConfigUtil()
		if configUtil.getBoolean(section= ConfigConst.CONSTRAINED_DEVICE, key= ConfigConst.ENABLE_SENSE_HAT_KEY):
			enableEmulation = False 
		else:
			enableEmulation = True
			
		self.sh = SenseHAT(emulate = enableEmulation)
		
	def generateTelemetry(self) -> SensorData:
		"""
		Generate the Telemetry
		
		@return SensorData
		"""
		sensorData = SensorData(sensorType = SensorData.PRESSURE_SENSOR_TYPE)
		sensorVal = self.sh.environ.pressure		
		sensorData.setValue(sensorVal)
		self.latestSensorData = sensorData

		return sensorData

