# What are software components?
At the beginning, a system (for example a vehicle's lightning control) is described only by its functionality. The partial functionalities are distributed on software components. These software components transmit information to other software components via defined interfaces

# Communication
The **Virtual Function Bus (VFB)** symbolizes the communication between the software components (see figure below).  
At this point in time, the assignments of software components to ECUs have not yet been defined. Only a logical perspective exists. The VFB maps communication within an ECU as well as between ECUs. The application has no knowledge of the underlying technologies. This makes it possible to develop the application software independently of the hardware.

## Two Types of Software Components
## Atomic Components
**Application Component**

- Implementation of the algorithm
- AUTOSAR software component
    - atomic software code fragment 
    - part of the application
    - independent of the infrastructure /  
        can be mapped to any ECU

**Sensor/actuator Component**

- Preparation of I/O data for the application
- Component is bound to ECU (constraint for mapping!)
- Represent dependency on a special sensor or actuator
## Composition Component

Logical organization or encapsulation of SWCs and/or Composition
