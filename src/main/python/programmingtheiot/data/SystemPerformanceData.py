#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.BaseIotData import BaseIotData

class SystemPerformanceData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_VAL = 0.0
	
	def __init__(self, d = None):
		super(SystemPerformanceData, self).__init__(d = d)
		self.__cpuUtil = 0
		self.__diskUtil = 0
		self.__memUtil = 0
	
	def getCpuUtilization(self):
		return self.__cpuUtil 
	
	def getDiskUtilization(self):
		return self.__diskUtil 
	
	def getMemoryUtilization(self):
		return self.__memUtil
	
	def setCpuUtilization(self, cpuUtil):
		self.__cpuUtil= cpuUtil
	
	def setDiskUtilization(self, diskUtil):
		self.__diskUtil = diskUtil
	
	def setMemoryUtilization(self, memUtil):
		self.__memUtil = memUtil
	
	def _handleUpdateData(self, data):
		self.__cpuUtil = data.__cpuUtil
		self.__diskUtil = data.__diskUtil
		self.__memUtil = data.__memUtil
