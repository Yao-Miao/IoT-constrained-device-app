#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator

from programmingtheiot.data.SensorData import SensorData

class TemperatureSensorSimTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self,dataSet = []):
		"""
		Initialization of class.
		Create an instance of TemperatureSensorSimTask
		"""
		super(TemperatureSensorSimTask, self).__init__(SensorData.TEMP_SENSOR_TYPE, dataSet = dataSet, minVal = SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP, maxVal = SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)
	
	def generateTelemetry(self) -> SensorData:
		"""
		Generate the Telemetry
		
		@return SensorData
		"""
		return super().generateTelemetry()
	
	def getTelemetryValue(self) -> float:
		"""
		Generate the value of the Telemetry
		
		@return float
		"""
		return super().getTelemetryValue()
	