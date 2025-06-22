# **Runtime Environment in Relation To Runnables*

**What is the function of the RTE in relation to runnables?**  

- Configuring itself. For example, by mapping runnables to Operating System tasks.
- Configuring parts of the Operating System (tasks, events, alarms).
- Triggering runnables via RTE events.
- Implementing communication between components. 
- Abstracting the Operating System and preventing SWC from directly accessing Operating System and BSW

**Which elements of the RTE are of existential importance to Runnables?**

The executable code units with calls of the Runnables. These are needed for the tasks.


# Take a Look at the RTE Events Which Trigger Runnables

Since the RTE is a purely event-driven system, an event must occur to activate a runnable. Below are some examples of such events that cause the RTE to execute a particular runnable.

- Init
- TimingEvent 
- DataReceivedEvent (S/R) 
- DataReceiveErrorEvent (S/R)
- DataSendCompletedEvent (S/R)
- OperationInvokedEvent (C/S)
- AsynchronousServerCallReturnsEvent (C/S)
- ModeSwitchEvent
- ModeSwitchAckEvent

Since AUTOSAR 4.x:

- ExternalTriggerOccurredEvent
    - Trigger from a different SWC  
        (inter SWC triggering)
- InternalTriggerOccurredEvent
    - Trigger within the same SWC  
        (inter runnable triggering)
- BackgroundEvent
    - Low priority triggering if no other trigger released


# How Does the Syntax Look Like?

# Examples of the Runnables' Syntax 
- Runnable triggered by any event except communication events 
    - _void  runnable (Rte_Instance self)_
- Server runnable triggered by OperationInvokedEvent, with 2 IN parameters and 1 OUT parameter)
    - _void LightServer (Rte_Instance self, UInt8 keyValue,  
          Boolean active, ResultTypeRef result)_

# RTE as a Communication Interface

The RTE as a communication mechanism acts as an implementation of the VFB.



# Inter ECU Sender/Receiver Communication
The figure below depicts a communication between two SWCs from two different ECUs. SWC1  sends a message to SWC2. Means: _Rte_Write_Port_Data()_ is executed regarding Runnable1 and _Rte_Read_Port_Data()_ is executed regarding Runnable2. The benefit of the RTE is, that the Code is the same, whether the communication happens between the Runnable and the Basic Software, or happens between two distinct ECUs . The only part that changes is the _Com_SendSignal()_ and _Com_ReceiveSignal()_ implementation in the Basic Software Layer. Through the high layer of abstraction, the code is independent from the RTE or the Basic Software Implementation and thus highly portable and reusable.


# Sender/Receiver Communication**
AUTOSAR distinguishes between three distinct types of Sender/Receiver communication methods, direct communication, buffered communication and queued communication. The Sender/Receiver communication enables the exchange of data. A typical example of this communication is that a sensor measures the current velocity and sends this value to other runnables that do various things with this value.  
All types of Sender/Receiver communication that get introduced in the following support either 1:n (1 sender, n receivers) or n:1 (n senders, 1 receiver) communication.

# Direct Communication
In the simplest form of communication, the RTE provides a buffer in which a runnable can write its data.  It is important to know that this is implemented according to the last-is-best principle, i.e. each write operation overwrites the complete buffer. So only the data of the last write operation is available in the buffer.

# Buffered Communication
The buffered communication implements the concept of a shadow buffer. When a runnable is executed, a shadow buffer is initialized within the RTE and assigned exclusively to that specific runnable. During runtime, the runnable writes all its data to this shadow buffer. When the runnable finishes its execution, all data is copied from the shadow buffer to the actual buffer within the RTE.

# Queued Communication
The RTE has a FIFO Queue to which the runnables can write to. In contrast to the direct communication there is no last-is-best-semantics but queued-semantics. Each write operation from a sender adds an element to the queue and each read operation from a receiver removes an element from the queue.

# Exclusive Areas
Since runnables running within the same software component can run on different tasks, it is perfectly normal for the operating system to interrupt a running task to switch to another task.

# Inter Runnable Variables (IRVs)

Variable that allows the communication between two runnables of the same component

Interrupt-safe access API provided from the RTE

# Exclusive Areas (EAs)
Allows to specify atomic sections for your implementation
Configurable implementation: e.g. interrupt lock, OS resource,...
# *Client/Server Communication*
The Server is a provider of operations, that can be called from the various clients. So the Client/Server Communication is a n:1 Communication. In simple words, the Server offers a kind of service, for example starting the engine and a client can invoke this service.

While the Sender/Receiver Communication is mostly about data exchange, the Client/Server Communication is about calling services. A simple example is shown on the right.

# **AUTOSAR Interfaces**
There are three AUTOSAR interface types: 
- AUTOSAR interface
- Standardized interface
- Standardized AUTOSAR interface

 Standardized interfaces are interfaces whose semantics are prescribed by the AUTOSAR standard.
- Example: EcuM: Rte_Start(), Rte_Stop()

AUTOSAR interfaces are interfaces that are described by generic AUTOSAR means and whose semantics are not prescribed by the AUTOSAR standard. These interfaces are used by the software components and ECU Abstraction. Ports are used for communication.

API function:
S/R -> Rte_Write_<p>_<d>
Rte_Write_DimmLight_DimmValue(value)
C/S -> Rte_Call_<p>_<o>

Standardized AUTOSAR interfaces are interfaces that are described by generic AUTOSAR means and whose semantics are prescribed by the AUTOSAR standard. Standardized AUTOSAR interfaces are used exclusively for the services of the basic software.

- Standardized AUTOSAR Interfaces are standardized and not ECU specific (e.g. ECU Abstraction)
- RTE -> BSW: Here one speaks of “Service Ports”
- API function
    - Communication mode for special SWC
- SWC à RTE 
    - Rte_Call_<portPrototype>_<operation>() 
- <Operation> DEM   
    - SetEventStatus (In Dem_EventStatusType status)