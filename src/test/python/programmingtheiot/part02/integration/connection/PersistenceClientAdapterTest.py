'''
Created on Oct 29, 2020

@author: miaoyao
'''
import logging
import unittest
import redis
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.data.SensorData import SensorData


from programmingtheiot.cda.connection.RedisPersistenceAdapter import RedisPersistenceAdapter

class RedisClientAdapterTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
        logging.info("Testing RedisClientAdapter class...")
        
        
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    
    def testConnectClient(self):
        rpa = RedisPersistenceAdapter()
        rpa.connectClient()
        rpa.connection.send_command('PING')
        response = rpa.connection.read_response()
        
        response = redis.Redis.RESPONSE_CALLBACKS['PING'](response)
        self.assertEqual(response, True)
        
        
    def testDisconnectClient(self):
        rpa = RedisPersistenceAdapter()
        rpa.disconnectClient()
        
        
    def testStoreSensorData(self):
        sd = SensorData()
        rpa = RedisPersistenceAdapter()
        rpa.storeData(ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, sd)
    
    if __name__ == "__main__":
        unittest.main()
    
