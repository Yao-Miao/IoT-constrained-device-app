#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import psutil

from programmingtheiot.cda.system.BaseSystemUtilTask import BaseSystemUtilTask

class SystemMemUtilTask(BaseSystemUtilTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		"""
		Initialization of class.
		Create an instance of SystemMemUtilTask
		"""
		super(SystemMemUtilTask, self).__init__()
	
	def _getSystemUtil(self) -> float:
		"""
		Get memory utilization and return it
	
		"""
		
		return psutil.virtual_memory().percent
		