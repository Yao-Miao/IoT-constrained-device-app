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

from programmingtheiot.data.SensorData import SensorData
import programmingtheiot.common.ConfigConst as ConfigConst

class BaseSensorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	DEFAULT_MIN_VAL = 0.0
	DEFAULT_MAX_VAL = 1000.0
	
	def __init__(self, sensorType: int = SensorData.DEFAULT_SENSOR_TYPE, dataSet = None, minVal: float = DEFAULT_MIN_VAL, maxVal: float = DEFAULT_MAX_VAL, sensorName = ConfigConst.NOT_SET):
		"""
		Initialization of class.
		Create an instance of BaseSensorSimTask
		"""
		self.sensorName = sensorName
		self.sensorType = sensorType
		self.minVal = minVal
		self.maxVal = maxVal
		self.index = -1
		self.latestSd = None
		
		
		if dataSet:
			self.dataSet = dataSet.dataEntries
			self.useRandomizer = False
		else:
			self.dataSet = None
			self.useRandomizer = True
		
	def generateTelemetry(self) -> SensorData:
		"""
		Generate the Telemetry
		
		@return SensorData
		"""
		sd = SensorData(sensorType = self.sensorType, name = self.sensorName)
		
		if self.useRandomizer:
			randomVal = random.uniform(self.minVal, self.maxVal)
			sd.setValue(randomVal)
		else:
			self.index += 1
			if self.index >= len(self.dataSet):
				self.index = 0
			data = self.dataSet[self.index]
			sd.setValue(data)
		return sd
		
		
	
	def getTelemetryValue(self) -> float:
		"""
		Generate the value of the last Telemetry
		
		@return float
		"""
		if self.latestSd:
			value = self.latestSd.getValue()
			return value
		else:
			sd = self.generateTelemetry()
			return sd.getValue()
			
		
	