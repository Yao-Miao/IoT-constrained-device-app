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
from programmingtheiot.common.ConfigUtil import ConfigUtil

from programmingtheiot.cda.sim.TemperatureSensorSimTask import TemperatureSensorSimTask
from programmingtheiot.cda.sim.HumiditySensorSimTask import HumiditySensorSimTask
from programmingtheiot.cda.sim.PressureSensorSimTask import PressureSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator


from programmingtheiot.cda.embedded.HumidityI2cSensorAdapterTask import HumidityI2cSensorAdapterTask
from programmingtheiot.cda.embedded.PressureI2cSensorAdapterTask import PressureI2cSensorAdapterTask
from programmingtheiot.cda.embedded.TemperatureI2cSensorAdapterTask import TemperatureI2cSensorAdapterTask

import programmingtheiot.common.ConfigConst as ConfigConst


class SensorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, useEmulator: bool = False, pollRate: int = 5, allowConfigOverride: bool = True):
		"""
		Initialization of class.
		Create an instance of SensorAdapterManager
		"""
		self.useEmulator = useEmulator
		self.pollRate = pollRate
		self.allowConfigOverride = allowConfigOverride
		self.dataMsgListener = None
		self.scheduler = BackgroundScheduler()
		self.scheduler.add_job(self.handleTelemetry, 'interval', seconds = self.pollRate)
		
		configUtil = ConfigUtil()
		
		"""
		If self.useEmulator is true, we will use Emulator to generate sensor data
		Else we will use SensorDataGenerator
		"""
		if self.useEmulator :
			logging.info("---> Emulators will be used ")
			
			
			
			if configUtil.getBoolean(section= ConfigConst.CONSTRAINED_DEVICE, key= ConfigConst.ENABLE_SENSE_HAT_KEY):
				logging.info("---> SMbus will be used ")
				self.humidityI2cSensorAdapterTask = HumidityI2cSensorAdapterTask()
				self.pressureI2cSensorAdapterTask = PressureI2cSensorAdapterTask()
				self.temperatureI2cSensorAdapterTask = TemperatureI2cSensorAdapterTask()
			else:
				# load the Humidity emulator
				humidityModule = __import__('programmingtheiot.cda.emulated.HumiditySensorEmulatorTask', fromlist = ['HumiditySensorEmulatorTask'])
				heClazz = getattr(humidityModule, 'HumiditySensorEmulatorTask')
				self.humidityEmulator = heClazz()
			
				pressureModule = __import__('programmingtheiot.cda.emulated.PressureSensorEmulatorTask', fromlist = ['PressureSensorEmulatorTask'])
				peClazz = getattr(pressureModule, 'PressureSensorEmulatorTask')
				self.pressureEmulator = peClazz()
			
				temperatureModule = __import__('programmingtheiot.cda.emulated.TemperatureSensorEmulatorTask', fromlist = ['TemperatureSensorEmulatorTask'])
				teClazz = getattr(temperatureModule, 'TemperatureSensorEmulatorTask')
				self.temperatureEmulator =teClazz()
				
				##add by miaoyao for final project
				soilHumidityModule = __import__('programmingtheiot.cda.emulated.SoilHumiditySensorEmulatorTask', fromlist = ['SoilHumiditySensorEmulatorTask'])
				shClazz = getattr(soilHumidityModule, 'SoilHumiditySensorEmulatorTask')
				self.soilHumidityEmulator = shClazz()
				

			
		else:
			logging.info("---> Simulators will be used ")
			self.dataGenerator = SensorDataGenerator()

			

			humidityFloor = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.HUMIDITY_SIM_FLOOR_KEY, SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY)
			humidityCeiling = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.HUMIDITY_SIM_CEILING_KEY, SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)
			
			pressureFloor = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.PRESSURE_SIM_FLOOR_KEY, SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE)
			pressureCeiling = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.PRESSURE_SIM_CEILING_KEY, SensorDataGenerator.HI_NORMAL_ENV_PRESSURE)
			
			tempFloor = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TEMP_SIM_FLOOR_KEY, SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP)
			tempCeiling = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TEMP_SIM_CEILING_KEY, SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)
			
			humidityData = self.dataGenerator.generateDailyEnvironmentHumidityDataSet(minValue = humidityFloor, maxValue = humidityCeiling, useSeconds = False)
			pressureData = self.dataGenerator.generateDailyEnvironmentPressureDataSet(minValue = pressureFloor, maxValue = pressureCeiling, useSeconds = False)
			tempData = self.dataGenerator.generateDailyIndoorTemperatureDataSet(minValue = tempFloor, maxValue = tempCeiling, useSeconds = False)
			
			
			
			
			self.humiditySensorSimTask = HumiditySensorSimTask(dataSet= humidityData)
			self.pressureSensorSimTask = PressureSensorSimTask(dataSet= pressureData)
			self.temperatureSensorSimTask = TemperatureSensorSimTask(dataSet= tempData)

	def handleTelemetry(self):
		"""
		handle the Telemetry
		
		"""
		#humidityVal = self.humiditySensorSimTask.getTelemetryValue()
		#pressureVal = self.pressureSensorSimTask.getTelemetryValue()
		#tempVal = self.temperatureSensorSimTask .getTelemetryValue()
		configUtil = ConfigUtil()
		
		if self.useEmulator :
			if configUtil.getBoolean(section= ConfigConst.CONSTRAINED_DEVICE, key= ConfigConst.ENABLE_SENSE_HAT_KEY):
				humiditySd = self.humidityI2cSensorAdapterTask.generateTelemetry()
				pressureSd = self.pressureI2cSensorAdapterTask.generateTelemetry()
				tempSd = self.temperatureI2cSensorAdapterTask.generateTelemetry()
			else:
				humiditySd = self.humidityEmulator.generateTelemetry()
				pressureSd = self.pressureEmulator.generateTelemetry()
				tempSd = self.temperatureEmulator .generateTelemetry()
				soilHumiditySd = self.soilHumidityEmulator.generateTelemetry()
		else :
			
			humiditySd = self.humiditySensorSimTask.generateTelemetry()
			pressureSd = self.pressureSensorSimTask.generateTelemetry()
			tempSd = self.temperatureSensorSimTask .generateTelemetry()
		
		if self.dataMsgListener :
			self.dataMsgListener.handleSensorMessage(humiditySd)
			self.dataMsgListener.handleSensorMessage(pressureSd)
			self.dataMsgListener.handleSensorMessage(tempSd)
			self.dataMsgListener.handleSensorMessage(soilHumiditySd)
		
		
		logging.info(' >>>>>>>>> Humidity is < %s >,  SoilHumidity is <%s>,  Pressure is < %s >,  Temperature is < %s >.', str(humiditySd.getValue()), str(soilHumiditySd.getValue()), str(pressureSd.getValue()), str(tempSd.getValue()))
		
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		"""
		set Data MessageListener which is used for monitor the Sensor
		
		@return bool
		"""
		if listener:
			self.dataMsgListener = listener
			
	
	def startManager(self):
		"""
		Start the SensorAdapterManager. 
		
		"""
		logging.info("---> Started SensorAdapterManager.")
		self.scheduler.start()
		
	def stopManager(self):
		"""
		Stop the SensorAdapterManager. 
		
		"""
		self.scheduler.shutdown()
		logging.info("---> Stopped SensorAdapterManager.")
