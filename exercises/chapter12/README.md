# Constrained Device Application (Connected Devices)

## Lab Module 12 - Semester Project - CDA Components

### Description

What does your implementation do? 

1.	Connect to the GDA using MQTT and  CoAP
2.	Collect and send system performance data for CPU and memory to the GDA
3.	Collect data from 4 sensors (emulated) and send to the GDA
4.	Use data from sensors to trigger a local (internal) actuation event due to a configured threshold crossing
5.	Implement 2 actuators (emulated)
6.	Process actuation events received from the GDA to trigger 1 actuation event
7.	Run for at least 1 hour without interruption, and collect / send at least 30 system performance samples, 30 sensor data samples, and trigger at least 2 actuator events internally.


How does your implementation work?

1.	Create sensor task: SoilHumiditySensorEmulatorTask
2.	Create actuator emulator task: SprinklerCtrlEmulatorTask and SprinklerEmulatorTask
3.	Update DeviceDataManager class in order to send data to the GDA and receive actuation events from GDA
4.	Update _handleSensorDataAnalysis method

### Code Repository and Branch

URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-MyronForNEU/tree/chapter12

### UML Design Diagram(s)

![CDA_UML](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-MyronForNEU/blob/chapter12/exercises/chapter12/CDA.png).


### Unit Tests Executed
 

### Integration Tests Executed

- SensorEmulatorManagerTest
- SensorEmulatorManagerTest
- DeviceDataManagerTest 

### Cloud Service
![CDA_CLOUD](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-MyronForNEU/blob/chapter12/exercises/chapter12/CDA_Cloud.jpg)

EOF.
