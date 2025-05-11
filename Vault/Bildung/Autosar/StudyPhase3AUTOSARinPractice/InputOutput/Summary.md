- The I/O Drivers enable access to the external environment by reading values or configuring parameters. They typically do not involve any data conversion or interpretation.
- The I/O Hardware Abstraction accesses the I/O Drivers from within server runnables. It receives values, processes them, and returns results to the caller.
- The Rte manages the Client/Server communication.
- The Sensor/Actuator SWCs utilize client calls to interact with the lower layers. These SWCs represent the hardware sensors and actuators, exchanging data with the application SWC.

In our specific example, runnable 1 is triggered by an Operation Invoked Trigger (OIT) and utilizes standardized API calls to interact with the driver modules.

In addition to what we previously discussed, notifications via callback functions can execute runnable 2 directly in an ISR context. For instance, this can be employed to signal the completion of a conversion through a sender port. Consequently, an Rte event triggers a runnable on the SWC with the receiver port, allowing the value to be retrieved directly through the Client/Server Interface.

In this chapter, we have learned about different approaches to set up client calls, depending on specific requirements, in either a synchronous or asynchronous manner, with or without supervising timeouts.