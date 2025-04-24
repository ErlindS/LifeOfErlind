### 

**Tasks**

Tasks are essential for organizing and executing software functionality. Each task has a priority to signal its importance. There are two types: basic and extended tasks. They share similarities but differ in key aspects.

### 

**Context Switch**

During task switching, a context switch takes place to maintain the functionality of AUTOSAR Os. The context switch involves five steps in total.

### 

**Alarms**

Alarms are a handy thing to trigger the activation of a task or set an event to initiate the execution of an extended task. 

### 

**Os Counter**

For time-based operations the Os Counters are fundamental in working with the AUTOSAR Os. There are two different types of Counters: The Periodic Interrupt Timer and the High Resolution Timer. 

### 

**Interrupts**

Category 1 interrupts in AUTOSAR execute within the active task or ISR and lack direct Os service access. Category 2 interrupts are handled by the AUTOSAR Os, allowing access to Os services, and execute within the Os context.

### 

**Inter OS Application Communicator (IOC)**

The IOC enables communication and synchronization between tasks of different applications. IOC ensures data integrity, coordination and safe resource access.

### 

**Os Resources**

An Os Resource can be used to protect against concurrent access by at least two concurrent tasks without using Interrupt locks. 

### 

**Scalability of the Os**

The MICROSAR Classic Os comes in different kinds and flavours. The Scalability Classes range from SC 1 until SC 4 and have different characteristics. Memory Protection, Timing Protection and other features are part of these Scalability Classes. 

### 

Knowledge in Action: Unveiling the Tool's Practical Potential

The last topic was the view in DaVinci Configurator Classic. Additionally to the theory you saw how to configure the Os, runnables and task mapping in the software.

# Requirements

********After completing this chapter you are able to...********

- name and rephrase the two types of Os Tasks.
- recall the meaning of Inter Os Application Communicator.
- describe the two types of timers.
- describe the use of alarms.
- name and describe the scalability classes of the Os.
- describe the two types of interrupts.
- list important aspects of the Os.
- name and describe the two tzpes of Os Counters.
- describe the functioning of a context switch.
- name the use of Os Resources.