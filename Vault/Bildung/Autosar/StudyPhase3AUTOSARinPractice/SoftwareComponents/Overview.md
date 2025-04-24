# **Overview of MICROSAR Classic Software Components**

Welcome to the world of software components (SWCs). As the backbone of modern automotive systems, SWCs enable the modular and scalable development of complex functionalities. In this chapter, we will delve into the fascinating realm of SWCs, exploring their role, capabilities and the incredible benefits they bring to the automotive industry. Get ready to unlock the potential of SWCs and discover the possibilities they offer for efficient and flexible software development.

Software components are essential parts of the application layer[[SoftwareComponents]] in AUTOSAR. They enable communication between other SWCs within the same Electronic Control Unit (ECU) or with Basic Software (BSW) modules. To execute SWCs and manage their communication, a Rte (Runtime Environment) is required. The Rte also runs BSW modules through the Schedule Manager (SchM), ensuring proper timing and coordination.

# **Overview of the kinds of SWCs**

A Composition... 
- ... can have Port Prototypes,
- ... represents the structure of atomic software components and their connections.
- ... does not result in executable code itself, but helps software designers to maintain a better overview.

The Atomic software component type...
- ... can have Port Prototypes,
- ... has internal behavior (runnables,...),
- ... results in executable code and
- ... can not be divided any further.

Calibration and NvBlock are implemented by Rte. ServiceSWCs are implemented by the BSW.

Atomic can be categorized into subtypes: 
### Application
A hardware-independent software component that is fully reusable across different platforms and systems.

### Sensor/Actuator
A software component that is technically hardware independent but relies on the existence of a corresponding hardware sensor or actuator. It provides characteristics related to sensor or actuator functionality.

### IoHwAb

## Service Proxy
A stand-in software component used in multi-core scenarios, representing a basic software service module for efficient communication and coordination.

## Calibration
 An AUTOSAR term referring to a ROM constant component that stores and distributes calibration parameters in the system.
## NvBlockSWC
An aggregation of NvRAM (Nonvolatile Random Access Memory) data before writing it to a specific NvRAM block. It facilitates the distribution of NvRAM data elements.


In our tools, we distinguish between Application Component Types and Service Component Types:

**Application Component Types**
- Constituting parts of the application
- Information exchange over AUTOSAR Interface

**Service Component Types**
- Representation of the Service Layer Modules 
- Services of the BSW be accessed by the application (Standardized AUTOSAR Interface)