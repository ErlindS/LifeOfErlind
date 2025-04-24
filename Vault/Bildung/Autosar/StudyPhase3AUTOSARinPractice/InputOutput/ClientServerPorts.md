Client Server Ports serve as a communication interface to enable function calls between different SWCs. A Client Port can be accessed by a runnable and used to invoke an operation provided by the server SWC, which is associated with a specific runnable.

What distinguishes C/S Ports is their capability to facilitate 'function calls' across core boundaries, ASIL contexts, and even ECU boundaries. This allows for the possibility of 'Remote Procedure Calls' through this mechanism, but it is essential to note that such remote calls may result in significant CPU resource consumption.

# Client Calls
As IoHwAb utilizes Client/Server Communication, we will now explore the various Client Calls. However, before we proceed, let's first review the important aspects of the C/S Ports using the next graphic.
## **Operation Arguments**
If you are required to declare arguments for your operation, the mandatory configuration for each argument includes specifying Name, DataType, and Direction. The view of "in" and "out" is taken from the server side.

