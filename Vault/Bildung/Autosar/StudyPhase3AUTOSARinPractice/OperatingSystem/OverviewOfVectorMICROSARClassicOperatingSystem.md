# MICROSAR Classic Operating System

The Os and the Complex Drivers are the only modules without a layered approach. As a result, they can directly access the Microcontroller and the MICROSAR Classic Rte.  
It is a static operating system, meaning it does not change its behavior during runtime. Additionally, it is fully preemptive, event-triggered and scalable in both functionality and size.
![[Pasted image 20250418214057.png]]

- *Tasks*: You can find tasks e.g. on your Windows Os too. Just open the task manager and see what tasks are running right now. [[Tasks]]
- *Context*: Like on your Laptop you might be able to have different things open, like this course and an email program - to use it actively you have to change to this program. This is how you can think of a context switch between different tasks on an ECU too. [[ContextSwitch]]
- *Alarms*: When you are woken up by an alarm in the morning you will do things afterwards (execute different actions) like grabbing a coffee. In your ECU there'll be an (defined) action too once an alarm expires. [[Alarms]]
- *Os Counter*: To know when an alarm expires your system has to know a time, therefore you use an Os Counter. [[Os Counter]]
- *Interrupts*: Your laptop screen is locked and you unlock it by pressing a key - that's when you cause an interrupt. In ECUs means you interrupt one task to execute another. The importance gets clear when you think of airgabs. They blow up in seconds cause there's a major interrupt happening. [[Interrupts]]
- *Os Resources*:  Important mechanism in Task scheduling - over Os Ressources you can temporarily give a task a higher priority/make it more important. [[Os Resources]]
- *Os Application*: An Os Application is a logical grouping of related tasks, resources and configurations within the AUTOSAR Os. 

#operatingSystem
#Microsar
