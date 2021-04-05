#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import json

import logging

from json import JSONEncoder

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class DataUtil():
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, encodeToUtf8 = False):
		"""
		Initialization of class.
		
		"""
		pass
	
	def actuatorDataToJson(self, actuatorData):
		"""
		Convert ActuatorData to JSON
		
		@return str
		"""
		
		jsonData = json.dumps(actuatorData, indent = 4, cls = JsonDataEncoder, ensure_ascii = True)
		logging.info('Convert ActuatorData to JSON: ' + jsonData);
		return jsonData
	
	def sensorDataToJson(self, sensorData):
		"""
		Convert SensorData to JSON
		
		@return str
		"""
		
		jsonData = json.dumps(sensorData, indent = 4, cls = JsonDataEncoder, ensure_ascii = True)
		logging.info('Convert SensorData to JSON: ' + jsonData);
		return jsonData

	def systemPerformanceDataToJson(self, sysPerfData):
		"""
		Convert SystemPerformanceData to JSON
		
		@return str
		"""
		jsonData = json.dumps(sysPerfData, indent = 4, cls = JsonDataEncoder, ensure_ascii = True)
		logging.info('Convert SystemPerformanceData to JSON: ' + jsonData);
		return jsonData
	
	def jsonToActuatorData(self, jsonData):
		"""
		Convert JSON to an ActuatorData instance
		
		@return ActuatorData
		"""
		
		jsonData = jsonData.replace("\'", "\"").replace('False','false').replace('True', 'true')
		logging.info('Convert JSON to an ActuatorData instance: ' + jsonData);
		## Load the dictionary data for the JSON string
		adDict = json.loads(jsonData)
		
		##Create an instance of ActuatorData, extract the variables, then map the JSON dict into the new object via an iterative lookup of each key / value pair.
		ad = ActuatorData()
		mvDict = vars(ad)

		for key in adDict:
			if key in mvDict:
				setattr(ad, key, adDict[key])
		
		return ad
	
	def jsonToSensorData(self, jsonData):
		"""
		Convert JSON to an SensorData instance
		
		@return SensorData
		"""
		
		jsonData = jsonData.replace("\'", "\"").replace('False','false').replace('True', 'true')
		logging.info('Convert JSON to an SensorData instance: ' + jsonData);
		## Load the dictionary data for the JSON string
		sdDict = json.loads(jsonData)
		
		##Create an instance of SensorData, extract the variables, then map the JSON dict into the new object via an iterative lookup of each key / value pair.
		sd = SensorData()
		mvDict = vars(sd)

		for key in sdDict:
			if key in mvDict:
				setattr(sd, key, sdDict[key])
				
		return sd
	
	def jsonToSystemPerformanceData(self, jsonData):
		"""
		Convert JSON to an SystemPerformanceDat instance
		
		@return SystemPerformanceDat
		"""
		
		jsonData = jsonData.replace("\'", "\"").replace('False','false').replace('True', 'true')
		logging.info('Convert JSON to an SystemPerformanceData instance: ' + jsonData);
		## Load the dictionary data for the JSON string
		sysdDict = json.loads(jsonData)
		
		##Create an instance of SensorData, extract the variables, then map the JSON dict into the new object via an iterative lookup of each key / value pair.
		sysd = SystemPerformanceData()
		mvDict = vars(sysd)

		for key in sysdDict:
			if key in mvDict:
				setattr(sysd, key, sysdDict[key])
		
		return sysd		
		
class JsonDataEncoder(JSONEncoder):
	"""
	Convenience class to facilitate JSON encoding of an object that
	can be converted to a dict.
	
	"""
	def default(self, o):
		return o.__dict__
	