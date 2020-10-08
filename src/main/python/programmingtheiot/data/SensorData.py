#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.BaseIotData import BaseIotData

class SensorData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_VAL = 0.0
	DEFAULT_SENSOR_TYPE = 0
	
	# These are just sensor type samples - these can be changed however
	# you'd like; you can also create an enum representing the values
	HUMIDITY_SENSOR_TYPE = 1
	PRESSURE_SENSOR_TYPE = 2
	TEMP_SENSOR_TYPE = 3
	
		
	def __init__(self, sensorType = DEFAULT_SENSOR_TYPE, value = DEFAULT_VAL, d = None):
		super(SensorData, self).__init__(d = d)
		
		# initial the __value
		# The private member __value: record the current value that gets from sensor 
		# add by Yao Miao
		self.__value = value;
	
	def getSensorType(self) -> int:
		"""
		Returns the sensor type to the caller.
		
		@return int
		"""
		return self.sensorType
	
	def getValue(self) -> float:
		return self.__value
	
	def setValue(self, newVal: float):
		self.__value = newVal
		
	def _handleUpdateData(self, data):
		self.__value = data.__value
