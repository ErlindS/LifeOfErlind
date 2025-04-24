# Category 1 ISR

Category 1 interrupts in AUTOSAR are usually software-generated interrupts or SWIs. 

They are triggered by software components or applications within the AUTOSAR system. 

Category 1 interrupts are typically used for inter-task communication, event signaling and synchronization between tasks or software modules. 

These interrupts do not have direct access to Os services and are executed in the context of the task or ISR that was active when the interrupt occurred.

# Category 2 ISR

Category 2 interrupts in AUTOSAR are usually external interrupts triggered by events from hardware devices or external signals. 

They are associated with events such as physical buttons, sensors, communication interfaces or other external events. 

Category 2 interrupts are handled by the AUTOSAR Os and used for event-driven operations, such as responding to external stimuli, triggering specific actions or activating tasks. 

The handling of Category 2 interrupts may involve invoking Os services, such as event signaling, task activation or resource management, based on the specific implementation and configuration of the AUTOSAR Os.

# Differences

|                       | Cat 1 Interrupts<br>                                                                  | Cat 2 Interrupts                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Execution             | occurs in the context of the task or ISR that was active when the interrupt occurred. | occurs within the context of the AUTOSAR Os and interrupt handling routines.                                          |
| Interrupt function    | finished with Return from Interrupt (RTI).                                            | finished with Return from Subroutine (RTS).                                                                           |
| Access to OS services | not within the interrupt itself.                                                      | available within the interrupt handling routine except for TerminateTask, WaitEvent, ClearEvent, Schedule, ChainTask. |
# Example

A **Category 1** interrupt can be used to signal specific events or conditions to other software components. For instance, a software component detecting a critical error or an important event can generate a Category 1 interrupt to notify other tasks or modules to handle the event appropriately. 

**Category 2** interrupts are commonly employed for handling communication events on various interfaces like UART, CAN bus or Ethernet. When a new message arrives, a communication error occurs, or specific conditions are met, a Category 2 interrupt can be generated to process the event and trigger the appropriate response. 

These are just two examples of use cases for each type of interrupt in AUTOSAR. The actual use cases may vary depending on the specific requirements, hardware platform and system design of the AUTOSAR application.