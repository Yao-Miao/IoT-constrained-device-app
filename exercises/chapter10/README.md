# Constrained Device Application (Connected Devices)

## Lab Module 10

Be sure to implement all the PIOT-CDA-* issues (requirements) listed at [PIOT-INF-10-001 - Chapter 10](https://github.com/orgs/programming-the-iot/projects/1#column-10488510).

### Description

What does your implementation do? 

Add intelligent edge messaging using MQTT and / or CoAP to handle various messaging scenarios between the GDA and CDA. Use MQTT and / or CoAP to process sensor messages the CDA and trigger actuation events from both the CDA and GDA.

How does your implementation work?

1.	Use your CDA and GDA MQTT client to test the publish performance of MQTT using QoS 0,1, and 2.
2.	Use your CDA and GDA CoAP client, along with your GDA CoAP server, to test the POST or PUT (your choice) performance of CoAP using CON (confirmed) and NON (non-confirmed) requests.
3.	Update DeviceDataManager and IDataMessageListener to support ActuatorData command messages from the GDA.
4.	Update MqttClientConnector to subscribe to ActuatorData command messages from the GDA, and send received messages to the IDataMessageListener instance.
5.	Update DeviceDataManager to handle sensor data and system performance data
6.	The sensor and actuator data the CDA generates will need to have a name associated with it, in addition to the type value that's already been set previously. This is to allow mapping into a cloud-based virtualized representation of the device with a later exercise.
7.	Now that SensorData and ActuatorData accept a 'name' in the constructor, the name for each instance of SensorData or ActuatorData will need to be set throughout the source code.


### Code Repository and Branch

NOTE: Be sure to include the branch (e.g. https://github.com/programming-the-iot/python-components/tree/alpha001).

URL: 

### UML Design Diagram(s)
![CDA_UML](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-MyronForNEU/blob/chapter10/exercises/chapter10/CDA.png).


### Unit Tests Executed

- HumiditySensorSimTaskTest
- PressureSensorSimTaskTest
- TemperatureSensorSimTaskTest
- HumidifierActuatorSimTaskTest
- HvacActuatorSimTaskTest
- ActuatorDataTest
- SensorDataTest
- SystemPerformanceDataTest

### Integration Tests Executed

- MqttClientPerformanceTest
- CoapClientPerformanceTest
- DeviceDataManagerCallbackTest
- MqttClientConnectorTest
- DeviceDataManagerWithCommsTest
- HumidifierEmulatorTaskTest
- HvacEmulatorTaskTest
- LedDisplayEmulatorTaskTest
- DataIntegrationTest


EOF.
