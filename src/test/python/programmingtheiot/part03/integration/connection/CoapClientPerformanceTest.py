'''
Created on Nov 24, 2020

@author: miaoyao
'''

import logging
import unittest

import time
from time import sleep

from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector

from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.DataUtil import DataUtil

class CoapClientPerformanceTest(unittest.TestCase):
    
    NS_IN_MILLIS = 1000000
    
    # NOTE: We'll use only 10,000 requests for CoAP
    MAX_TEST_RUNS = 1000
    
    @classmethod
    def setUpClass(self):
        logging.disable(level = logging.WARNING)
        self.coapClient = CoapClientConnector()
        
    def setUp(self):
        pass

    def tearDown(self):
        self.coapClient.stopObserver(5)
                    
    """
    Testing POST - CON
    """                
    #@unittest.skip("Ignore for now.")
    def testPostRequestCon(self):
        print("Testing POST - CON")
        
        self._execTestPost(self.MAX_TEST_RUNS, True)
    
    """
    Testing POST - NON
    """
    #@unittest.skip("Ignore for now.")
    def testPostRequestNon(self):
        print("Testing POST - NON")
        
        self._execTestPost(self.MAX_TEST_RUNS, False)

    def _execTestPost(self, maxTestRuns: int, useCon: bool):
        sensorData = SensorData()
        payload = DataUtil().sensorDataToJson(sensorData)
        
        startTime = time.time_ns()
        
        for seqNo in range(0, maxTestRuns):
            self.coapClient.sendPostRequest(resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, payload = payload, enableCON = useCon)
            
        endTime = time.time_ns()
        elapsedMillis = (endTime - startTime) / self.NS_IN_MILLIS
        if useCon :
            print("POST message - useCON = " + str(useCon) + " [" + str(maxTestRuns) + "]: " + str(elapsedMillis) + " ms")
        else:
            print("POST message - useNON = " + str(useCon) + " [" + str(maxTestRuns) + "]: " + str(elapsedMillis) + " ms")
