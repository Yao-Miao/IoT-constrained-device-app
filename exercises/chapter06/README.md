# Constrained Device Application (Connected Devices)

## Lab Module 06

Be sure to implement all the PIOT-CDA-* issues (requirements) listed at [PIOT-INF-06-001 - Chapter 06](https://github.com/orgs/programming-the-iot/projects/1#column-10488434).

### Description

What does your implementation do?

Build a robust publish/subscribe (pub/sub) data communications capability into your GDA using MQTT. Prove you can communicate between your GDA and CDA using this protocol and an MQTT message broker server.

How does your implementation work?

1.	Create a Java class named MqttClientConnector that can interact with an MQTT broker.
2.	Add callbacks to the MqttClientConnector module to handle the MQTT client events for connect, disconnect, and message received events.
3.	Add publish and subscribe capabilities to the MqttClientConnector module pub/sub functionality.
4.	S Connect MqttClientConnector into DeviceDataManager


### Code Repository and Branch

URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-MyronForNEU/tree/chapter06

### UML Design Diagram(s)

![CDA_UML](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-MyronForNEU/blob/chapter06/exercises/chapter06/CDA.png).


### Unit Tests Executed
- N/A

### Integration Tests Executed
- MqttClientConnectorTest

EOF.
