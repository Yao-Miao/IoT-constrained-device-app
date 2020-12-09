#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import paho.mqtt.client as mqttClient

from programmingtheiot.common import ConfigUtil
from programmingtheiot.common import ConfigConst

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.data.DataUtil import DataUtil

from programmingtheiot.cda.connection.IPubSubClient import IPubSubClient

DEFAULT_QOS = 1

class MqttClientConnector(IPubSubClient):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, clientID: str = None):
		"""
		Default constructor. This will set remote broker information and client connection
		information based on the default configuration file contents.
		
		@param clientID Defaults to None. Can be set by caller. If this is used, it's
		critically important that a unique, non-conflicting name be used so to avoid
		causing the MQTT broker to disconnect any client using the same name. With
		auto-reconnect enabled, this can cause a race condition where each client with
		the same clientID continuously attempts to re-connect, causing the broker to
		disconnect the previous instance.
		"""
		self.config = ConfigUtil.ConfigUtil()

		self.host = self.config.getProperty(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.HOST_KEY, ConfigConst.DEFAULT_HOST)

		self.port = self.config.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.PORT_KEY, ConfigConst.DEFAULT_MQTT_PORT)

		self.keepAlive = self.config.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)
		
		self.clientID = clientID
		self.mc = None

		logging.info('\tMQTT Broker Host: ' + self.host)
		logging.info('\tMQTT Broker Port: ' + str(self.port))
		logging.info('\tMQTT Keep Alive:  ' + str(self.keepAlive))
		
		
		"""
		add listener
		"""
		self.dataMsgListener = None

	def connectClient(self) -> bool:
		"""
		Connect to a remote broker.
		host is the hostname or IP address of the remote broker.
        port is the network port of the server host to connect to.
		"""
		
		if not self.mc:
			self.mc = mqttClient.Client(client_id = self.clientID, clean_session = True)
			self.mc.on_connect = self.onConnect
			self.mc.on_disconnect = self.onDisconnect
			self.mc.on_message = self.onMessage
			self.mc.on_publish = self.onPublish
			self.mc.on_subscribe = self.onSubscribe
			
	
		if not self.mc.is_connected():
			self.mc.connect(self.host, self.port, self.keepAlive)
			self.mc.loop_start()
			return True
		else:
			logging.warn('MQTT client is already connected. Ignoring connect request.')
			return False
		
	def disconnectClient(self) -> bool:
		"""
		Disconnect from the remote broker.
		"""
		
		if self.mc.is_connected():
			self.mc.disconnect()
			self.mc.loop_stop()
		
		return True
	
	def onActuatorCommandMessage(self, client, userdata, msg):
		logging.info('[Callback] Actuator command message received. Topic: %s.', msg.topic)
		jsonData = str(msg.payload, encoding = "utf-8")
		if self.dataMsgListener:
			try:
				actuatorData = DataUtil().jsonToActuatorData(jsonData)
				self.dataMsgListener.handleActuatorCommandMessage(actuatorData)
			except:
				logging.exception("Failed to convert incoming actuation command payload to ActuatorData: ")
		
	def onConnect(self, client, userdata, flags, rc):
		"""
		callback method to handle connection notification events
		"""
		
		#logging.info('[Callback] Connected to MQTT broker. Result code: ' + str(rc))

		# NOTE: Use the QoS of your choice - '1' is only an example
		self.mc.subscribe(topic = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE.value, qos = 1)
		self.mc.message_callback_add(sub = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE.value, callback = self.onActuatorCommandMessage)
		
		
	def onDisconnect(self, client, userdata, rc):
		"""
		callback method to handle connection notification events
		"""
		
		logging.info('[Callback] Disconnected from MQTT broker. Result code:' + str(rc))
		
	def onMessage(self, client, userdata, msg):
		"""
		callback method - this will be called whenever a message is received on the topic for which your client has subscribed
		"""
		
		#logging.info('[Callback] onMessage is being called client:' + str(client._client_id) + '   msg:' + str(msg.payload))
			
	def onPublish(self, client, userdata, mid):
		"""
		callback method to handle message publish notification events
		"""
		
		#logging.info('[Callback] onPublish is being called client:' + str(client._client_id) + '   mid:' + str(mid))
		
	
	def onSubscribe(self, client, userdata, mid, granted_qos):
		"""
		callback method to handle topic subscription notification events
		"""
		
		#logging.info('[Callback] Subscribed client:' + str(client._client_id) + '   MID:' + str(mid))
	
	
	
	
	def publishMessage(self, resource: ResourceNameEnum, msg, qos: int = IPubSubClient.DEFAULT_QOS):
		"""
		handle all publish functionality
		@param resource: that is used to get topic. The topic that the message should be published on
		@param msg: The actual message to send
		@param qos: The quality of service level to use.
		"""
		topic = resource.value
		if qos < 0 or qos > 2:
			qos = IPubSubClient.DEFAULT_QOS
		msgInfo = self.mc.publish(topic=topic, payload=msg, qos=qos)
		#msgInfo.wait_for_publish()
		return True
	
	def subscribeToTopic(self, resource: ResourceNameEnum, qos: int = IPubSubClient.DEFAULT_QOS):
		"""
		Subscribe the client to one or more topics
		@param resource: that is used to get topic. A string specifying the subscription topic to subscribe to.
		@param qos: The desired quality of service level for the subscription.
		"""
		topic = resource.value
		if qos < 0 or qos > 2:
			qos = IPubSubClient.DEFAULT_QOS
		self.mc.subscribe(topic=topic, qos=qos)
		return True
	
	def unsubscribeFromTopic(self, resource: ResourceNameEnum):
		"""
		Unsubscribe the client to one or more topics
		@param resource: that is used to get topic. A string specifying the subscription topic to subscribe to.
		"""
		topic = resource.value
		self.mc.unsubscribe(topic=topic)
		return True

	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		"""
		Set the Data Message Listener
		"""
		if listener:
			self.dataMsgListener = listener
			return True
		return False
	
	
