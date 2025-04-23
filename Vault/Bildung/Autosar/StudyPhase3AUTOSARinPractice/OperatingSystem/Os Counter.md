# Os Counter
The Os Counter is a fundamental component of the AUTOSAR Os that provides timing services and facilitates the management of time-based operations within the system. There are two commonly used types of Os Counters: the Periodic Interrupt Timer (PIT) and the High Resolution Timer (HRT). 

Both the Periodic Interrupt Timer and the High Resolution Timer contribute to the timing services provided by the AUTOSAR Os. They ensure proper timing behavior, support task scheduling, enable event handling, and facilitate time synchronization within the system.

# Periodic interrupt timer
The Periodic Interrupt Timer is a type of Os Counter that generates periodic interrupts at fixed intervals. 

The Periodic Interrupt Timer...
- is typically based on a hardware timer peripheral available in the microcontroller or system on which the AUTOSAR Os is running. 
- is used to provide a timebase for the AUTOSAR Os, enabling the system to track time and execute time-triggered operations. 
- generates interrupts at a fixed frequency or interval, which serves as a reference for timing operations and enables tasks to be activated periodically. 
- provides a coarse-grained timebase, suitable for tasks and operations that do not require high-resolution timing. 

At the configured interval an Os Counter ISR is executed. 

Each time there is a check for expired alarms or data received events. 

If there is nothing to do the ISR finishes without any further action.

# High Resolution Timer
The High-Resolution Timer is an additional Os Counter that provides higher precision and accuracy for timing operations within the AUTOSAR Os. 

The High-Resolution Timer...

- utilizes a hardware timer with higher resolution or a dedicated timer peripheral designed to offer finer time granularity. 
- is typically used for time-sensitive or realtime operations that require precise timing, such as event handling or performance measurements. 
- enables tasks or events to be scheduled with greater accuracy and enables higher-resolution time measurement within the AUTOSAR system. 
- complements the Periodic Interrupt Timer by providing a finer level of time resolution when necessary. 

  

The period between two interrupts is calculated here each time. Superfluous interrupts are avoided, but also each time a calculation for setting the next timer is needed, which can create additional overhead.

# Example
The Periodic Interrupt Timer is commonly used for regular task activations and time-triggered operations like periodic task activations, time-triggered operations or periodic communication, for example: 

- In an engine control system, a task responsible for reading sensor data and adjusting fuel injection might be activated every 10 milliseconds. 
    
- Performing periodic system health checks, updating display data or monitoring communication interfaces at fixed intervals. 
    
- In applications requiring periodic communication, such as sending periodic status updates or cyclic frames on a CAN bus the transmission of data is triggered at regular time intervals.  
    

The High Resolution Timer is employed for event handling, performance measurements and real-time applications that require finer time granularity and precise timing.  
For event-driven applications that require precise timing for event handling an example is an ABS (Anti-lock Braking System). The High Resolution Timer can be used to measure the duration between wheel speed sensor readings to detect wheel lock conditions accurately.