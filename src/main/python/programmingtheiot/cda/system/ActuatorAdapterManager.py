#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.data.ActuatorData import ActuatorData

from programmingtheiot.cda.sim.HumidifierActuatorSimTask import HumidifierActuatorSimTask
from programmingtheiot.cda.sim.HvacActuatorSimTask import HvacActuatorSimTask

#from programmingtheiot.cda.emulated.HumidifierEmulatorTask import HumidifierEmulatorTask
#from programmingtheiot.cda.emulated.HvacEmulatorTask import HvacEmulatorTask
#from programmingtheiot.cda.emulated.LedDisplayEmulatorTask import LedDisplayEmulatorTask

class ActuatorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self, useEmulator: bool = False):
		"""
		Initialization of class.
		Create an instance of ActuatorAdapterManager
		"""
		self.useEmulator = useEmulator
		self.dataMsgListener = None
		
		
		if self.useEmulator :
			logging.info("---> Emulators will be used ")
			
			# load the Humidifier actuation emulator
			humidifierModule = __import__('programmingtheiot.cda.emulated.HumidifierEmulatorTask', fromlist = ['HumidifierEmulatorTask'])
			hueClazz = getattr(humidifierModule, 'HumidifierEmulatorTask')
			self.humidifierEmulator = hueClazz()
			
			# load the hvac actuation emulator
			hvacModule = __import__('programmingtheiot.cda.emulated.HvacEmulatorTask', fromlist = ['HvacEmulatorTask'])
			hvacClazz = getattr(hvacModule, 'HvacEmulatorTask')
			self.hvacEmulator = hvacClazz()
			
			# load the led actuation emulator
			ledModule = __import__('programmingtheiot.cda.emulated.LedDisplayEmulatorTask', fromlist = ['LedDisplayEmulatorTask'])
			ledClazz = getattr(ledModule, 'LedDisplayEmulatorTask')
			self.ledEmulator = ledClazz()
			
			
			sprinklerModule = __import__('programmingtheiot.cda.emulated.SprinklerEmulatorTask', fromlist = ['SprinklerEmulatorTask'])
			sprClazz = getattr(sprinklerModule, 'SprinklerEmulatorTask')
			self.sprinklerEmulator = sprClazz()
			
			sprCtrlModule = __import__('programmingtheiot.cda.emulated.SprinklerCtrlEmulatorTask', fromlist = ['SprinklerCtrlEmulatorTask'])
			sprCtrlClazz = getattr(sprCtrlModule, 'SprinklerCtrlEmulatorTask')
			self.sprCtrlEmulator = sprCtrlClazz()
			
			sprMasterModule = __import__('programmingtheiot.cda.emulated.SprinklerMasterEmulatorTask', fromlist = ['SprinklerMasterEmulatorTask'])
			sprMasterClazz = getattr(sprMasterModule, 'SprinklerMasterEmulatorTask')
			self.sprMasterEmulator = sprMasterClazz()
			
			

			
		else:
			logging.info("---> Simulators will be used ")
			# create the humidifier actuator
			self.humidifierActuator = HumidifierActuatorSimTask()
			# create the HVAC actuator
			self.hvacActuator = HvacActuatorSimTask()
			

	def sendActuatorCommand(self, data: ActuatorData) -> bool:
		"""
		Send Actuator Command to Actuator
		
		@return bool
		"""
		if self.dataMsgListener :
			self.dataMsgListener.handleActuatorCommandResponse(data)
			logging.info('Actuator command received. Processing...')
			if self.useEmulator:
				if (data.getActuatorType() == ActuatorData.HUMIDIFIER_ACTUATOR_TYPE):
					if ~data.isResponseFlagEnabled(): 
						self.humidifierEmulator._handleActuation(data.getCommand(), data.getValue(), data.getStateData())
				if (data.getActuatorType() == ActuatorData.HVAC_ACTUATOR_TYPE):
					if ~data.isResponseFlagEnabled(): 
						self.hvacEmulator._handleActuation(data.getCommand(), data.getValue(), data.getStateData())
				if (data.getActuatorType() == ActuatorData.LED_DISPLAY_ACTUATOR_TYPE):
					if ~data.isResponseFlagEnabled(): 
						self.ledEmulator._handleActuation(data.getCommand(), data.getValue(), data.getStateData())
				if (data.getActuatorType() == ActuatorData.SPRINKLER_ACTUATOR_TYPE):
					if ~data.isResponseFlagEnabled(): 
						self.sprinklerEmulator._handleActuation(data.getCommand(), data.getValue(), data.getStateData())
				if (data.getActuatorType() == ActuatorData.SPRINKLER_CTRL_ACTUATOR_TYPE):
					if ~data.isResponseFlagEnabled(): 
						self.sprCtrlEmulator._handleActuation(data.getCommand(), data.getValue(), data.getStateData())
				if (data.getActuatorType() == ActuatorData.SPRINKLER_MASTER_ACTUATOR_TYPE):
					if ~data.isResponseFlagEnabled(): 
						self.sprMasterEmulator._handleActuation(data.getCommand(), data.getValue(), data.getStateData())
			else:
				if (data.getActuatorType() == ActuatorData.HUMIDIFIER_ACTUATOR_TYPE):
					if ~data.isResponseFlagEnabled(): 
						self.humidifierActuator.updateActuator(data)
				if (data.getActuatorType() == ActuatorData.HVAC_ACTUATOR_TYPE):
					if ~data.isResponseFlagEnabled(): 
						self.hvacActuator.updateActuator(data)
		
			
	
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		"""
		set Data MessageListener which is used for monitor the Actuator excuate
		
		@return bool
		"""
		if listener:
			self.dataMsgListener = listener
