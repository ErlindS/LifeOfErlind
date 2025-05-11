# Communication
This cluster is responsible for CAN, LIN, FlexRay and Ethernet bus communication.

**Mode Management**
The Mode Management takes care of the different states of an ECU. These states can be Startup-, Up-, Sleep- and Shutdown-state. The Mode Management also takes care of the transition between these different states. 

**Watchdog**
Like most modules, the Watchdog module is divided into three different layers.  
During runtime, the system constantly restarts the watchdog timer to prevent it from timing out. If the system runs into an invalid state, the watchdog times out and calls a reset routine, because it assumes, that the system is in a faulty state. The reset routine tries to correct the current state, so that the system can continue it's work.

**Memory Services**
In AUTOSAR there is no dynamic memory allocation and hence no filesystem. In order to still be able to store something permanently AUTOSAR offers the memory services cluster. These kind of services just provide an interface to store data in the non volatile memory section. That is especially useful for diagnostic messages, which can be read out in a workshop and help the mechanic to find a possible fault in the car.

**Diagnostics**
This cluster does everything diagnostics related. If an error occurs, it stores this specific error and maybe asks the application for more data to provide more meaningful error-messages. As mentioned above, the diagnostics cluster makes use of the memory services cluster in order to store the error messages permanently.

**Hardware I/O**
The I/O controlls values (DIO, ADC, ICU, OCU,...) from the Hardware.

**Operating System (OS)**
The operating system is mainly responsible to handle tasks, events, alarms and interrupts of the ECU. In the OS, a timer, which interrupts the system, is defined. The OS is scalable in functionality and size.

********After completing this chapter you are able to...********
- name characteristics of the Basic Software Layers (Service Layer, ECU Abstraction Layer, MCAL and Complex Device Drivers).
- list important modules of the functional clusters Communication, Mode Management, NV Manager, Watchdog, Diagnostics, OS and I/O and describe their basic functionality.