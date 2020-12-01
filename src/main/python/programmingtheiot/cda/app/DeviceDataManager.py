#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector
from programmingtheiot.cda.connection.MqttClientConnector import MqttClientConnector

from programmingtheiot.cda.system.ActuatorAdapterManager import ActuatorAdapterManager
from programmingtheiot.cda.system.SensorAdapterManager import SensorAdapterManager
from programmingtheiot.cda.system.SystemPerformanceManager import SystemPerformanceManager

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData
from programmingtheiot.cda.connection.RedisPersistenceAdapter import RedisPersistenceAdapter


class DeviceDataManager(IDataMessageListener):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self, enableMqtt: bool = True, enableCoap: bool = False):
		"""
		Initialization of class.
		Create an instance of DeviceDataManager
		"""
		
		self.configUtil = ConfigUtil()
		
		self.enableEmulator = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)
		
		self.enableRedis = False
		
		self.sysPerfManager = SystemPerformanceManager()
		self.sensorAdapterManager = SensorAdapterManager(useEmulator=self.enableEmulator)
		self.sensorAdapterManager.setDataMessageListener(self)
		self.actuatorAdapterManager = ActuatorAdapterManager(useEmulator=self.enableEmulator)
		self.actuatorAdapterManager.setDataMessageListener(self)
		##add by miaoyao @10/30/2020
		if self.enableRedis:
			self.redisClient = RedisPersistenceAdapter()
		
		self.enableHandleTempChangeOnDevice = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_HANDLE_TEMP_CHANGE_ON_DEVICE_KEY)

		self.triggerHvacTempFloor = self.configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TRIGGER_HVAC_TEMP_FLOOR_KEY);

		self.triggerHvacTempCeiling = self.configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TRIGGER_HVAC_TEMP_CEILING_KEY);
		
		##add by miaoyao @11/02/2020
		##self.enableMqtt = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_MQTT_KEY)
		self.enableMqtt = enableMqtt
		self.enableCoap = enableCoap
		
		if self.enableMqtt:
			self.mqttClient = MqttClientConnector()
		if self.enableCoap:
			self.coapClient = CoapClientConnector()
		
		
		
			
	def handleActuatorCommandResponse(self, data: ActuatorData) -> bool:
		"""
		handle the ActuatorCommandResponse
		
		@return bool
		"""
		
		# Use the DataUtil class to convert the ActuatorData to JSON.
		adJson= DataUtil.actuatorDataToJson(self, data)
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_ACTUATOR_RESPONSE_RESOURCE, adJson)
		
	def handleActuatorCommandMessage(self, data: ActuatorData) -> bool:
		"""
		handle the handleActuatorCommandMessage
		
		@return bool
		"""
		if data:
			logging.info("Processing actuator command message.")
			
			# TODO: add further validation before sending the command
			self.actuatorAdapterManager.sendActuatorCommand(data)
			return True
		else:
			logging.warning("Received invalid ActuatorData command message. Ignoring.")
			return False
		
	
	def handleIncomingMessage(self, resourceEnum: ResourceNameEnum, msg: str) -> bool:
		"""
		handle the IncomingMessage
		
		@return bool
		"""
		logging.info("----->>>The handleIncomingMessage method is being called")
		# Use the DataUtil class to convert the msg content (which should be JSON) to an ActuatorData instance
		ad = DataUtil.jsonToActuatorData(self, msg)
		self._handleIncomingDataAnalysis(msg)

	def handleSensorMessage(self, data: SensorData) -> bool:
		"""
		handle the SensorMessage
		
		@return bool
		"""
		logging.info("----->>>The handleSensorMessage method is being called")
		# Use the DataUtil class to convert the SensorData to JSON
		sdJosn = DataUtil.sensorDataToJson(self, data)
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, sdJosn)
		self._handleSensorDataAnalysis(data)
		
		
		
		if self.enableRedis:
			self.redisClient.storeData(ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, data)
		
	def handleSystemPerformanceMessage(self, data: SystemPerformanceData) -> bool:
		"""
		handle the SystemPerformanceMessage
		
		@return bool
		"""
		logging.info("----->>>The handleSystemPerformanceMessage method is being called")
		spmJson = DataUtil.systemPerformanceDataToJson(self, data)
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE, spmJson)
	
	def startManager(self):
		"""
		Start the DeviceDataManager. 
		Calls startManager() on the sysPerfManager instance.
		Calls startManager() on the sensorAdapterManager instance.
		
		"""
		logging.info("----->>>The DeviceDataManager will be started")
		self.sysPerfManager.startManager()
		self.sensorAdapterManager.startManager()
		if self.enableRedis:
			self.redisClient.connectClient()
		
		if self.enableMqtt:
			self.mqttClient.connectClient()
		
	def stopManager(self):
		"""
		Stop the DeviceDataManager. 
		Calls stopManager() on the sysPerfManager instance.
		Calls stopManager() on the sensorAdapterManager instance.
		
		"""
		self.sysPerfManager.stopManager()
		self.sensorAdapterManager.stopManager()
		
		if self.enableRedis:
			self.redisClient.disconnectClient()
		if self.enableMqtt:
			self.mqttClient.disconnectClient()
		
		logging.info("----->>>The DeviceDataManager stopped")
		
		

	def _handleIncomingDataAnalysis(self, msg: str):
		"""
		Call this from handleIncomeMessage() to determine if there's
		any action to take on the message. Steps to take:
		1) Validate msg: Most will be ActuatorData, but you may pass other info as well.
		2) Convert msg: Use DataUtil to convert if appropriate.
		3) Act on msg: Determine what - if any - action is required, and execute.
		"""
		logging.info("----->>>The _handleIncomingDataAnalysis method is being called")
		ad = DataUtil.jsonToActuatorData(self, msg)
		self.actuatorAdapterManager.sendActuatorCommand(ad)
		
		
	def _handleSensorDataAnalysis(self, data: SensorData):
		"""
		Call this from handleSensorMessage() to determine if there's
		any action to take on the message. Steps to take:
		1) Check config: Is there a rule or flag that requires immediate processing of data?
		2) Act on data: If # 1 is true, determine what - if any - action is required, and execute.
		"""
		logging.info("----->>>The _handleSensorDataAnalysis method is being called")
		if self.enableHandleTempChangeOnDevice:
			ad = ActuatorData(actuatorType = ActuatorData.HVAC_ACTUATOR_TYPE)
			value = data.getValue()
			if value >= self.triggerHvacTempFloor and value <= self.triggerHvacTempCeiling:
				ad.setCommand(ActuatorData.COMMAND_OFF)
			else:
				ad.setCommand(ActuatorData.COMMAND_ON)
			
			self.actuatorAdapterManager.sendActuatorCommand(ad)
			
		
	def _handleUpstreamTransmission(self, resourceName: ResourceNameEnum, msg: str):
		"""
		Call this from handleActuatorCommandResponse(), handlesensorMessage(), and handleSystemPerformanceMessage()
		to determine if the message should be sent upstream. Steps to take:
		1) Check connection: Is there a client connection configured (and valid) to a remote MQTT or CoAP server?
		2) Act on msg: If # 1 is true, send message upstream using one (or both) client connections.
		"""
		logging.info("----->>>The _handleUpstreamTransmission method is being called")
		if self.enableMqtt:
			if resourceName == ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE or resourceName == ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE:
				self.mqttClient.publishMessage(resourceName, msg)
		
		if self.enableCoap:
			self.coapClient.sendPostRequest(resource = resourceName, enableCON = True, payload = msg)
				
			
