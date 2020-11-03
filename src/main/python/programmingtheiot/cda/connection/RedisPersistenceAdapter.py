'''
Created on Oct 29, 2020

@author: miaoyao
'''
import logging
import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.DataUtil import DataUtil

import redis

class RedisPersistenceAdapter():
    
    
    def __init__(self):
        configUtil = ConfigUtil()
        self.host = configUtil.getProperty(section = ConfigConst.DATA_GATEWAY_SERVICE, key= ConfigConst.HOST_KEY)
        
        self.port = configUtil.getInteger(section = ConfigConst.DATA_GATEWAY_SERVICE, key= ConfigConst.PORT_KEY)
        
        
        self.redis = redis.Redis(host=self.host, port=self.port, db=0)
        self.connection_pool = self.redis.connection_pool
        self.connection = self.redis.connection
        
    
    def connectClient(self) -> bool:
        
        if self.connection:
            logging.info("Redis is already connected!!!")
            return True
        else:
            try:
                logging.info("connecting......")
                self.connection = self.connection_pool.get_connection('');
                self.connection.connect()
                logging.info("Redis is already connected!!!")
                return True
            except redis.ConnectionError:
                logging.error("Redis can't connect!!");
            
        
                
            
    
    def disconnectClient(self) -> bool:
        if self.connection:
            try:
                logging.info("disconnecting......")
                self.connection.disconnect()
                self.connection_pool.release(self.connection)
                self.connection = None
                logging.info("Redis is already disconnected!!!")
                return True
            except:
                logging.error("Redis can't disconnect!!");
        else:
            logging.info("Redis is already disconnected!!!")
            return True
            
            
    
    def storeData(self, resource: ResourceNameEnum, data: SensorData) -> bool:
        topic = 'SensorData'
        sdJosn = DataUtil.sensorDataToJson(self, data)
        self.redis.set(topic, sdJosn)
        return True
        
    