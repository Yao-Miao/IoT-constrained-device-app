#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.BaseIotData import BaseIotData
import programmingtheiot.common.ConfigConst as ConfigConst

class SystemPerformanceData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_VAL = 0.0
		
	def __init__(self, d = None):
		"""
		Constructor.
		
		@param d Defaults to None. The data (dict) to use for setting all parameters.
		It's provided here as a convenience - mostly for testing purposes. The utility
		in DataUtil should be used instead.
		"""
		super(SystemPerformanceData, self).__init__(name = ConfigConst.SYS_PERF_DATA, d = d)
		
		if d:
			self.cpuUtil = d['cpuUtil']
			self.diskUtil = d['diskUtil']
			self.memUtil = d['memUtil']
		else:
			self.cpuUtil = self.DEFAULT_VAL
			self.diskUtil = self.DEFAULT_VAL
			self.memUtil = self.DEFAULT_VAL
	
	def getCpuUtilization(self):
		"""
		Get the CpuUtilization of the instance
		
		@return float
		"""
		return self.cpuUtil 
	
	def getDiskUtilization(self):
		"""
		Get the DiskUtilization of the instance
		
		@return float
		"""
		return self.diskUtil 
	
	def getMemoryUtilization(self):
		"""
		Get the MemoryUtilization of the instance
		
		@return float
		"""
		return self.memUtil
	
	def setCpuUtilization(self, cpuUtil):
		"""
		Set the CpuUtilization of the instance
		"""
		self.cpuUtil= cpuUtil
	
	def setDiskUtilization(self, diskUtil):
		"""
		Set the DiskUtilization of the instance
		"""
		self.diskUtil = diskUtil
	
	def setMemoryUtilization(self, memUtil):
		"""
		Set the MemoryUtilization of the instance
		"""
		self.memUtil = memUtil
	
	def _handleUpdateData(self, data):
		"""
		update the instance
		"""
		self.cpuUtil = data.cpuUtil
		self.diskUtil = data.diskUtil
		self.memUtil = data.memUtil
