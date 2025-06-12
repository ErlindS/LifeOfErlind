
What could be reasons for putting data into Nonvolatile Memory?

The central motivation is **Power-off data persistence.**
Every information that needs to be present after a power cycle, must be stored in nonvolatile memory. Either during runtime or during shutdown, as (volatile) RAM is loosing its content without voltage supply.


Question
Which use-cases do you have in your project that would require storing data nonvolatile? Think about it for a moment.

In the following example, a typical scenario where data is stored persistently and restored afterwards is displayed. Note the different stakeholders in this very simplified situation and try to keep them in mind. We will refer back to this overview as we get to know the subject.

1. SWC -> RAM
Your software component continuously calculates the average fuel consumption during runtime and stores it in an associated RAM-variable.

2. RAM -> Shut-Down
With shutdown of the car, we want to store this average fuel consumption nonvolatile in the data flash, to retain the historic average of the value.

The data can also be written to or read from the nonvolatile memory on demand by the application. E.g. reload is possible if invalid sensor data led to a diverging unrealistic average.


With the next startup, the value of the previously computed and stored average fuel consumption can be restored in the associated RAM-variable. This way the information dashboard can immediately show the last fuel consumption and the application can continue calculating new average values taking new sensor data into account.


**Overview**

**The following topics will be introduced:** 

- **Principles of Memory Technologies**
    - Here you will get to know the fundamental characteristics of the most commonly used Nv-memory hardware technologies - namely EEPROM & Flash - and learn about their differences.
- **The MICROSAR Classic MEM Solution**
    - Here, you will learn about the AUTOSAR Basic Software Modules that are part of the Nv-memory stack and are therefore in charge of managing the underlying hardware technologies as well as provide the application with access to these.
- **Memory Handling**
    - Here, you will learn how the application is interacting with the NvM through the Rte to access its assigned Nv-memory blocks and what mechanisms must be employed to maintain data consistency. We will also discuss, how different characteristics of Nv-memory blocks affect their handling and memory usage.
- **Service Mapping**
    - Here you will learn how Vector's tooling can support you in keeping your interfaces for the Nv-memory access consistent between the application layer and the BSW.
- **NvBlockSwComponents**
    - Here you will learn about the NvBlockSwComponents concept, which got developed to make the access to the Nv-memory from application layer more convenient and to reduce the number of individual interactions with the basic software.
- **Summary**
    - Here, we will recapitulate the different approaches to store data nonvolatile as well as revisit the different BSW module's enabling it in the AUTOSAR environment.


