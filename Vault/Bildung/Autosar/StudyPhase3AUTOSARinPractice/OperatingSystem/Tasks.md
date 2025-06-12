# Tasks
In Autosar, tasks are a fundamental concept for organizing and executing software functionality within the automotive system. They represent units of work that can be scheduled and executed by the AUTOSAR Os.

# Properties of Tasks
Tasks in AUTOSAR have associated priorities that determine their relative importance and influence the order of execution in case of scheduling conflicts. The AUTOSAR Os uses priority-based scheduling algorithms to ensure that tasks are executed in a timely and deterministic manner, with higher-priority tasks preempting lower-priority tasks if necessary. 
Tasks can interact with each other and with other software components in the system through inter-task communication mechanisms provided by the AUTOSAR Os. These mechanisms include communication primitives such as events, flags, semaphores and shared resources. 
Tasks play a crucial role in achieving realtime behavior, responsiveness and proper coordination within the AUTOSAR system. They enable the execution of different software functions, contribute to the overall system performance and facilitate the modular and scalable design of automotive software applications.

# What is a basic task?
Basic tasks are typically associated with periodic activations, but can also be activated by user code. Basic tasks are tpically used for timetriggered operations and perform activities such as data processing, control operations or communication tasks but also initializations. 

States: Suspended - activate Task -> Ready - start -> running
running - preempt ->Ready
running - TerminateTask -> Suspend

# What is an extended task?
Extended tasks offer more flexibility and event-driven execution compared to basic tasks. They can be triggered by specific events or stimuli rather than strictly following a fixed periodic schedule. Extended tasks are activated in response to external events or system conditions and are used for handling event-triggered operations or sporadic activities. 

States: Suspended - activate Task -> Ready - start -> running
running - WaitEvent -> Waiting (setEvent) - Release -> Ready
running - preempt ->Ready
running - TerminateTask -> Suspend

