# **Transmission**
Let's focus on the transmission path from an Application Software Component to the CAN bus first. We'll do this by narrating a storyline that begins at the application layer and drills down to the hardware, highlighting the interactions between the different layers of AUTOSAR.

1. First Step

Application Layer - Rte_Write_*()
Imagine you're in the cockpit of a futuristic car, ready to activate the acceleration. This begins with the Application Software Component calling the Rte_Write_*() function, a part of AUTOSAR's Runtime Environment.
Here's what happens:
1. SWC Writes Data: The SWC is the encapsulated functionality like engine control, door control, etc. It invokes Rte_Write_*() to write a piece of information, like a sensor value.
2. Rte as a Middleman: Rte, acting as the middleman, translates this request into something that the lower layers of AUTOSAR can understand, ensuring communication between different SWCs.


3.  Second Step