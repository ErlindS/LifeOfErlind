The module Os is the operating system of an AUTOSAR ECU. AUTOSAR extends the OSEK/VDX operating system standard. The OS is in close connection with the RTE (see figure below). If something changes in the SWC, the OS has to be regenerated just like the RTE.

Example: When you change the periodical event of a runnable, the RTE has to update the alarm settings and the OS has to update the corresponding timer. Both RTE and OS have to be regenerated. That is the reason why the OS aswell as the RTE are static.


What are the Elements of the OS?
- Tasks, 
- Events, 
- Alarms, 
- Interrupts, 
- Inter OS Communication (IOC) and 
- Resources.

As mentioned above, the module Os is actually an extended OSEK operating system. Extensions are divided into so-called Scalability Classes (SC1–SC4). They cover the following functionalities: 

- SC1: schedule tables 
- SC2: timing protection + schedule tables 
- SC3: memory protection + schedule tables 
- SC4: memory protection + timing protection + schedule tables