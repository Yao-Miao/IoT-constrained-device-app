#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from apscheduler.schedulers.background import BackgroundScheduler

from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.cda.system.SystemCpuUtilTask import SystemCpuUtilTask
from programmingtheiot.cda.system.SystemMemUtilTask import SystemMemUtilTask

class SystemPerformanceManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""


	def __init__(self, pollRate: int = 60):
		"""
		Create an instance of SystemCpuUtilTask
		Create an instance of SystemMemUtilTask
		Add a job to the scheduler
		"""
		self.cpuUtilTask = SystemCpuUtilTask()
		self.memUtilTask = SystemMemUtilTask()
		self.scheduler = BackgroundScheduler()
		self.scheduler.add_job(self.handleTelemetry, 'interval', seconds = pollRate)
									

	def handleTelemetry(self):
		"""
		Call getTelemetryValue() method to get the CPU utilization and memory utilization. 
		Logs the values of self.cpuUtilPct and self.memUtilPct
		
		"""
		self.cpuUtilPct = self.cpuUtilTask.getTelemetryValue()
		self.memUtilPct = self.memUtilTask.getTelemetryValue()
		
		logging.info('CPU utilization is %s percent, and memory utilization is %s percent.', str(self.cpuUtilPct), str(self.memUtilPct))
		
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		pass
	
	def startManager(self):
		"""
		Start the System Performance Manager. Call scheduler.start() method to start the job scheduler
		
		"""
		logging.info("---> Started SystemPerformanceManager.")
		self.scheduler.start()
		
	def stopManager(self):
		"""
		Stop the System Performance Manager. Call scheduler.shutdown() method to shutdown the job scheduler
		
		"""
		self.scheduler.shutdown()
		logging.info("---> Stopped SystemPerformanceManager.")
