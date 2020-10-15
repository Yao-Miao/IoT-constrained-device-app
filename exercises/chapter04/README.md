# Constrained Device Application (Connected Devices)

## Lab Module 04

Be sure to implement all the PIOT-CDA-* issues (requirements) listed at [PIOT-INF-04-001 - Chapter 04](https://github.com/orgs/programming-the-iot/projects/1#column-10488386).

### Description

What does your implementation do? 

Following the design principles from Chapter 3, use the SenseHAT emulator application to build real sensing and actuation functionality into your CDA. Deploy your CDA to a Raspberry Pi and talk to the I2C bus and GPIO.

How does your implementation work?

1.	Install and configure the SenseHAT emulator and supporting libraries for your platform
2.	Create the new Python modules that will implement the sensor emulator tasks. These will all be derived from BaseSensorSimTask, and will mimic the design of their simulator counterparts, but with a bit more implementation detail.
3.	Create the new Python modules that will implement the actuator emulator tasks. These will all be derived from BaseActuatorSimTask, and will mimic the design of their simulator counterparts, but with a bit more implementation detail.
4.	Create the new Python modules that will implement the sensor emulator tasks. These will all be derived from BaseSensorSimTask, and will mimic the design of their simulator counterparts, but with significantly more implementation detail.
5.	 Edit the Python module named SensorAdapterManager with class name SensorAdapterManager and add the SenseHAT emulator functionality.
6.	Edit the Python module named ActuatorAdapterManager with class name ActuatorAdapterManager and add the SenseHAT emulator functionality.

### Code Repository and Branch

NOTE: Be sure to include the branch (e.g. https://github.com/programming-the-iot/python-components/tree/alpha001).

URL: 

### UML Design Diagram(s)

NOTE: Include one or more UML designs representing your solution. It's expected each
diagram you provide will look similar to, but not the same as, its counterpart in the
book [Programming the IoT](https://learning.oreilly.com/library/view/programming-the-internet/9781492081401/).


### Unit Tests Executed



### Integration Tests Executed

- SenseHatEmulatorQuickTest
- SensorEmulatorManagerTest
- ActuatorEmulatorManagerTest
- EmbeddedSensorAdapterTest
- SensorAdapterManagerTest
- ActuatorAdapterManagerTest

EOF.
