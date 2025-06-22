Client Server Ports serve as a communication interface to enable function calls between different SWCs. A Client Port can be accessed by a runnable and used to invoke an operation provided by the server SWC, which is associated with a specific runnable.

What distinguishes C/S Ports is their capability to facilitate 'function calls' across core boundaries, ASIL contexts, and even ECU boundaries. This allows for the possibility of 'Remote Procedure Calls' through this mechanism, but it is essential to note that such remote calls may result in significant CPU resource consumption.

# Client Calls
As IoHwAb utilizes Client/Server Communication, we will now explore the various Client Calls. However, before we proceed, let's first review the important aspects of the C/S Ports using the next graphic.

1. SWC A is equipped with two client ports. the left port contains two opertaions, and the right port contains three operations. TO use an operation in your application code, you need to configure access points for your runnable. access is granted per operation available at any port prototype attached to the swc the left runnable has access o two Operations on two separate ports while the right runnable has access to two operations on the same port
2. Server ports can be located on other application SWCs or on BSW modules. Each operation has a server runnable, which is triggered by a call to the corresponding operation
3. An operation invocation trigger cannot be combined with any other kind of trigger. It can only be combined with triggers of other operations, provided that they have a compatible list of argument prototypes.
4. Ensure to enable the concurrent activation and that the runnable entity is implemented in a way that allows multiple concurrent calls to the runnable entity
## **Operation Arguments**
If you are required to declare arguments for your operation, the mandatory configuration for each argument includes specifying Name, DataType, and Direction. The view of "in" and "out" is taken from the server side.

### Runtime of Servers
When creating an access point on a client port to invoke an operation, you have to choose how this call is handled. Let's take a short example to easily understand the differences between the options. 
Imagine you have some code executed in a runnable, and at a certain point, you need to invoke an operation. You use the wellknow function Rte_call_port_operation. What happens after your call now depends on your settings. Find out about the different selection options:
- Synchronous
	-  Synchronous calls are suitable for tasks that require immediate feedback or a timely response from the server.
- Asynchronous and Waiting
	- This method is similar to synchronous calls, but instead of immediately passively waiting, the client can still execute some code before waiting is unavoidable
- Asynchronous and Polling
	- This approach allows the client to be more responsive and utilize its reousrces efficiently while polling for the servers result
- Asynchronous and Trigger on runnable
	- This approach allows the client to be event-driven and respond to the servers completion event without active polling

