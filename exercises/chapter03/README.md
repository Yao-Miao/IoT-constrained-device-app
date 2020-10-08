# Constrained Device Application (Connected Devices)

## Lab Module 03

Be sure to implement all the PIOT-CDA-* issues (requirements) listed at [PIOT-INF-03-001 - Chapter 03](https://github.com/orgs/programming-the-iot/projects/1#column-10488379).

### Description

What does your implementation do? 

Add a simulation and data generation capability to The Edge Tier. Add simulated sensing and actuation to the Constrained Device App (CDA) using a data generator for humidity, pressure, and temperature. Use the generator to create data sets that can then package as telemetry objects containing additional information about the device. Create a simple threshold trigger to issue a simulated actuator command.

How does your implementation work?

1.	Create (or edit the exiting) Python modules that will contain the sensor and actuator data: SensorData, ActuatorData, and SystemPerformanceData. 
2.	Create and implement the BaseSensorSimTask module.
3.	Create the new Python modules that will implement the sensor simulator tasks: HumiditySensorSimTask, PressureSensorSimTask, TemperatureSensorSimTask.
4.	Create the BaseActuatorSimTask
5.	Create the new Python modules that will implement the actuator simulator tasks: HumidifierActuatorSimTask, HvacActuatorSimTask
6.	Create a new  Python module named SensorAdapterManager with class name SensorAdapterManager
7.	Create a new / edit the existing Python module named ActuatorAdapterManager with class name ActuatorAdapterManager.
8.	Create a new Python module named DeviceDataManager with class name DeviceDataManager.
9.	Create an instance of DeviceDataManager within ConstrainedDeviceApp and invoke the manager's start / stop methods within the app's start / stop methods.


### Code Repository and Branch

Chapter03 Branch URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-MyronForNEU/tree/chapter03

Main Branch URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-MyronForNEU/tree/alpha001

### UML Design Diagram(s)

![CDA_UML](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-MyronForNEU/blob/chapter03/exercises/chapter03/CDA.png).


### Unit Tests Executed

- ActuatorDataTest
- SensorDataTest
- SystemPerformanceDataTest

- HumiditySensorSimTaskTest
- PressureSensorSimTaskTest
- TemperatureSensorSimTaskTest

- HumidifierActuatorSimTaskTest
- HvacActuatorSimTaskTest


### Integration Tests Executed

- SensorAdapterManagerTest
- ActuatorAdapterManagerTest
- DeviceDataManagerNoCommsTest
- ConstrainedDeviceAppTest

EOF.
