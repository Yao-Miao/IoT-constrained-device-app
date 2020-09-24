# Constrained Device Application (Connected Devices)

## Lab Module 02

Be sure to implement all the PIOT-CDA-* issues (requirements) listed at [PIOT-INF-02-001 - Chapter 02](https://github.com/orgs/programming-the-iot/projects/1#column-9974938).

### Description

NOTE: Include two full paragraphs describing your implementation approach by answering the questions listed below.

What does your implementation do? 
Implement the Constrained Device App (CDA) in Python. Build an IoT performance monitoring applications to collect some simple telemetry about the constrained devices. In this exercise, the application will read and report on basic systems performance parameters, such as CPU utilization and memory utilization.

How does your implementation work?
1.	Create the ConstrainedDeviceApp application in Python. Add startApp() and stopApp() method.
2.	Create a new Python module named SystemPerformanceManager with class name SystemPerformanceManager.
3.	Create an instance of SystemPerformanceManager within ConstrainedDeviceApp and invoke the manager's start / stop methods within the app's start / stop methods.
4.	Create (edit) a new Python module named BaseSystemUtilTask with class name BaseSystemUtilTask.
5.	Create a new Python module named SystemCpuUtilTask with class name SystemCpuUtilTask.
6.  Create a new Python module named SystemMemUtilTask with class name SystemMemUtilTask.
7.  Create an instance of SystemCpuUtilTask and SystemMemUtilTask within SystemPerformanceManager and use the apscheduler library to run each task at a regular interval.

### Code Repository and Branch

NOTE: Be sure to include the branch (e.g. https://github.com/programming-the-iot/python-components/tree/alpha001).

URL: 

### UML Design Diagram(s)

NOTE: Include one or more UML designs representing your solution. It's expected each
diagram you provide will look similar to, but not the same as, its counterpart in the
book [Programming the IoT](https://learning.oreilly.com/library/view/programming-the-internet/9781492081401/).


### Unit Tests Executed

NOTE: TA's will execute your unit tests. You only need to list each test case below
(e.g. ConfigUtilTest, DataUtilTest, etc). Be sure to include all previous tests, too,
since you need to ensure you haven't introduced regressions.

- 
- 
- 

### Integration Tests Executed

NOTE: TA's will execute most of your integration tests using their own environment, with
some exceptions (such as your cloud connectivity tests). In such cases, they'll review
your code to ensure it's correct. As for the tests you execute, you only need to list each
test case below (e.g. SensorSimAdapterManagerTest, DeviceDataManagerTest, etc.)

- 
- 
- 

EOF.
