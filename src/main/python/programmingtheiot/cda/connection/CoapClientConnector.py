#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import socket

from coapthon import defines
from coapthon.client.coap import CoAP
from coapthon.client.helperclient import HelperClient
from coapthon.messages.message import Message
from coapthon.messages.request import Request
from coapthon.utils import parse_uri
from coapthon.utils import generate_random_token


import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.cda.connection.IRequestResponseClient import IRequestResponseClient


class CoapClientConnector(IRequestResponseClient):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self):
		"""
		Use the ConfigUtil configuration information for the CoAP Gateway to retrieve the host and port information.
		"""
		self.config = ConfigUtil()
		self.dataMsgListener = None
		self.coapClient = None

		self.host = self.config.getProperty(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.HOST_KEY, ConfigConst.DEFAULT_HOST)
		self.port = self.config.getInteger(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.PORT_KEY, ConfigConst.DEFAULT_COAP_PORT)

		logging.info('\tCoAP Server Host: ' + self.host)
		logging.info('\tCoAP Server Port: ' + str(self.port))
		
		
		"""
		Validate the url information
		"""
		self.url = "coap://" + self.host + ":" + str(self.port) + "/"

		try:
			logging.info("Parsing URL: " + self.url)
	
			self.host, self.port, self.path = parse_uri(self.url)	
			tmpHost = socket.gethostbyname(self.host)
	
			if tmpHost:
				self.host = tmpHost
				self._initClient()
			else:
				logging.error("Can't resolve host: " + self.host)
				
		except socket.gaierror:
			logging.info("Failed to resolve host: " + self.host)
		
		self._initClient()
			

	"""
	Send DISCOVER request to the server
	"""
	def sendDiscoveryRequest(self, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		logging.info('Discovering remote resources...')

		# NOTE: we can use the API to send a discovery 'GET', or - per [RFC7252](https://tools.ietf.org/html/rfc7252#section-7.2) 
		# and its reference of [RFC6690](https://tools.ietf.org/html/rfc6690#section-1.2.1), we can just send the following:
		# self.coapClient.get(path = '/.well-known/core', callback = self._onDiscoveryResponse, timeout = timeout)
		self.coapClient.discover(callback = self._onDiscoveryResponse, timeout = timeout)
	
	
	"""
	Send delete request to the server
	"""
	def sendDeleteRequest(self, resource: ResourceNameEnum, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		logging.info("the method sendDeleteRequest is called")
		if resource:
			logging.debug("Issuing DELETE with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.DELETE, path = resource.value)
			request.token = generate_random_token(2)
	
			if not enableCON:
				request.type = defines.Types["NON"]
		
			self.coapClient.send_request(request = request, callback = self._onDeleteResponse, timeout = timeout)
		else:
			logging.warning("Can't test DELETE - no path or path list provided.")
	
	"""
	Send get request to the server
	"""
	def sendGetRequest(self, resource: ResourceNameEnum, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		logging.info("the method sendGetRequest is called")
		if resource:
			logging.debug("Issuing GET with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.GET, path = resource.value)
			request.token = generate_random_token(2)
	
			if not enableCON:
				request.type = defines.Types["NON"]
		
			self.coapClient.send_request(request = request, callback = self._onGetResponse, timeout = timeout)
		else:
			logging.warning("Can't test GET - no path or path list provided.")

	"""
	Send post request to the server
	"""
	def sendPostRequest(self, resource: ResourceNameEnum, payload: str, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		#logging.info("the method sendPostRequest is called")
		if resource:
			logging.debug("Issuing POST with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.POST, path = resource.value)
			request.token = generate_random_token(2)
			request.payload = payload
	
			if not enableCON:
				request.type = defines.Types["NON"]
		
			self.coapClient.send_request(request = request, callback = self._onPostResponse, timeout = timeout)
		else:
			logging.warning("Can't test POST - no path or path list provided.")
	

	"""
	Send put request to the server
	"""
	def sendPutRequest(self, resource: ResourceNameEnum, payload: str, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		#logging.info("the method sendPutRequest is called")
		if resource:
			logging.debug("Issuing PUT with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.PUT, path = resource.value)
			request.token = generate_random_token(2)
			request.payload = payload
	
			if not enableCON:
				request.type = defines.Types["NON"]
		
			self.coapClient.send_request(request = request, callback = self._onPutResponse, timeout = timeout)
		else:
			logging.warning("Can't test PUT - no path or path list provided.")
			
			
	"""
	Set the Data Message Listener
	"""
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		self.dataMsgListener = IDataMessageListener

	def startObserver(self, resource: ResourceNameEnum, ttl: int = IRequestResponseClient.DEFAULT_TTL) -> bool:
		pass

	def stopObserver(self, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		self.coapClient.close()
	
	"""
	Initialize the coap client
	"""
	def _initClient(self):
		if not self.coapClient:
			self.coapClient = HelperClient(server = (self.host, self.port))

	"""
	Callback function for sendDiscoveryRequest()
	"""
	def _onDiscoveryResponse(self, response):
		if response:
			logging.info(response.pretty_print())
		
			# get the payload and convert to a list of paths
			self.pathList = response.payload.split(',')
			index = 0
		
			# the following is optional, but provides an easy way to track all the returned resource names
			for path in self.pathList:
				for char in '<\>':
					path = path.replace(char, '')
				
				self.pathList[index] = path
			
				logging.info('  Path entry [' + str(index) + ']:' + self.pathList[index])
				index += 1
		else:
			logging.info("No response received.")
	
	
	"""
	Callback function for sendGetRequest()
	"""
	def _onGetResponse(self, response):
		
		logging.info('GET response received.')

		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
	
			#
			# NOTE: This next section is optional if you want to send a callback to the self.dataMsgListener instance
			#
	
			# TODO: get the URI and convert to ResourceNameEnum
			resource = None
	
			if self.dataMsgListener:
				self.dataMsgListener.handleIncomingMessage(resource, str(response.payload))

	"""
	Callback function for sendPutRequest()
	"""		
	def _onPutResponse(self, response):
		#logging.info('PUT response received.')

		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
	
	"""
	Callback function for sendPostRequest()
	"""			
	def _onPostResponse(self, response):
		#logging.info('POST response received.')

		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
	
	"""
	Callback function for sendDeleteRequest()
	"""		
	def _onDeleteResponse(self, response):
		logging.info('DELETE response received.')

		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
		
			
	