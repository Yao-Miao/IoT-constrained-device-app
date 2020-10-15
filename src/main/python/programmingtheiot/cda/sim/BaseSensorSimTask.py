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

class BaseSensorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	DEFAULT_MIN_VAL = 0.0
	DEFAULT_MAX_VAL = 1000.0
	
	def __init__(self, sensorType: int = SensorData.DEFAULT_SENSOR_TYPE, dataSet = None, minVal: float = DEFAULT_MIN_VAL, maxVal: float = DEFAULT_MAX_VAL):
		"""
		Initialization of class.
		Create an instance of BaseSensorSimTask
		"""
		self.__sensorType = sensorType
		self.__minVal = minVal
		self.__maxVal = maxVal
		self.__index = -1
		self.__latestSd = None
		
		
		if dataSet:
			print("------>" + str(type(dataSet)))
			self.__dataSet = dataSet.dataEntries
			self.__useRandomizer = False
		else:
			self.__dataSet = None
			self.__useRandomizer = True
		
	def generateTelemetry(self) -> SensorData:
		"""
		Generate the Telemetry
		
		@return SensorData
		"""
		sd = SensorData(sensorType = self.__sensorType)
		
		if self.__useRandomizer:
			randomVal = random.uniform(self.__minVal, self.__maxVal)
			sd.setValue(randomVal)
		else:
			self.__index += 1
			if self.__index >= len(self.__dataSet):
				self.__index = 0
			data = self.__dataSet[self.__index]
			sd.setValue(data)
		return sd
		
		
	
	def getTelemetryValue(self) -> float:
		"""
		Generate the value of the last Telemetry
		
		@return float
		"""
		if self.__latestSd:
			value = self.__latestSd.getValue()
			return value
		else:
			sd = self.generateTelemetry()
			return sd.getValue()
			
		
	