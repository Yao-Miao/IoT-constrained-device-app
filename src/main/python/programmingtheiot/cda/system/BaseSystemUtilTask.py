#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from programmingtheiot.data.SensorData import SensorData

logging.basicConfig(format = '%(asctime)s:%(name)s:%(levelname)s:%(message)s', level = logging.DEBUG)

class BaseSystemUtilTask():
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self):
		"""
		Initialization of class.
		
		"""
		###
		# TODO: fill in the details here
		self.latestSensorData = None
	
	def generateTelemetry(self) -> SensorData:
		"""
		Generate the Telemetry
		
		@return SensorData
		"""
		
		###
		# TODO: fill in the details here
		#
		# NOTE: Use self._getSystemUtil() to retrieve the value from the sub-class
		self.latestSensorData = SensorData()
		val = self._getSystemUtil()
		self.latestSensorData.setValue(val)
		return self.latestSensorData
		
	def getTelemetryValue(self) -> float:
		"""
		Generate the value of the Telemetry
		
		@return float
		"""
		
		if self.latestSensorData == None:
			self.latestSensorData = self.generateTelemetry()
		
		val = self.latestSensorData.getValue()
			
		logging.info('The subclass <' + self.__class__.__name__ + '> get a value: ' + str(val))
		
		return val
	
	def _getSystemUtil(self) -> float:
		"""
		Template method implemented by sub-class.
		
		Retrieve the system utilization value as a float.
		
		@return float
		"""
		pass
		