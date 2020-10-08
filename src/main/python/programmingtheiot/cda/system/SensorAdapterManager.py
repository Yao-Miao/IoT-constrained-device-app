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

import programmingtheiot.common.ConfigConst as ConfigConst


class SensorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, useEmulator: bool = False, pollRate: int = 5, allowConfigOverride: bool = True):
		self.useEmulator = useEmulator
		self.pollRate = pollRate
		self.allowConfigOverride = allowConfigOverride
		self.dataMsgListener = None
		self.scheduler = BackgroundScheduler()
		self.scheduler.add_job(self.handleTelemetry, 'interval', seconds = self.pollRate)
		
		if self.useEmulator :
			logging.info("---> Emulators will be used ")
		else:
			logging.info("---> Simulators will be used ")
			self.dataGenerator = SensorDataGenerator()

			configUtil = ConfigUtil()

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
		#humidityVal = self.humiditySensorSimTask.getTelemetryValue()
		#pressureVal = self.pressureSensorSimTask.getTelemetryValue()
		#tempVal = self.temperatureSensorSimTask .getTelemetryValue()
		
		humiditySd = self.humiditySensorSimTask.generateTelemetry()
		pressureSd = self.pressureSensorSimTask.generateTelemetry()
		tempSd = self.temperatureSensorSimTask .generateTelemetry()
		
		if self.dataMsgListener :
			#self.dataMsgListener.handleSensorMessage(humidityVal)
			#self.dataMsgListener.handleSensorMessage(pressureVal)
			#self.dataMsgListener.handleSensorMessage(tempVal)
			self.dataMsgListener.handleSensorMessage(humiditySd)
			self.dataMsgListener.handleSensorMessage(pressureSd)
			self.dataMsgListener.handleSensorMessage(tempSd)
		
		
		logging.info(' >>>>>>>>> Humidity is < %s >,  Pressure is < %s >,  Temperature is < %s >.', str(humiditySd.getValue()), str(pressureSd.getValue()), str(tempSd.getValue()))
		
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		if listener:
			self.dataMsgListener = listener
			
	
	def startManager(self):
		logging.info("---> Started SensorAdapterManager.")
		self.scheduler.start()
		
	def stopManager(self):
		self.scheduler.shutdown()
		logging.info("---> Stopped SensorAdapterManager.")
