
# Terms and Defintions
Before we start we must define our wording. It may become confusing when we are talking about “state” machines and “mode” management in the same sentence. As the concept of mode management has changed considerably from AUTOSAR 3.x to AUTOSAR 4.x it is essential that we have a common understanding of the wording.

-> Es ist wichtig die Begriffe zu unterscheiden. 

# State
States are internal to their respective BSW component and thus not visible to the application. So they are only used by the BSW’s internal state machine. The States inside the ECU Manager build the phases and therefore handle the modes.

# Mode
A Mode is a certain set of states of the various state machines (not only of the ECU Manager) that are running in the vehicle and are relevant to a particular entity, an application or the whole vehicle.

# Phase
A logical or temporal assembly of ECU Manager’s actions and events, e.g.  STARTUP, UP, SHUTDOWN, SLEEP, …  
Phases can consist of Sub-Phases which are often called Sequences if they above all exist to group sequences of executed actions into logical units. Phases in this context are not the phases of the AUTOSAR Methodology.

# Technical Agreements
Mode and Network Management address a wide area of applications. We must restrict ourselves to the discussion of the essential basic feature set.
- We will use and discuss EcuM Flexible, the solution for AUTOSAR 4.x.  
    The EcuM Fixed specification is not a topic.
- Nevertheless we will use a state model corresponding to EcuM Fixed. Vector’s Auto Configuration feature creates such a state machine as a BswM rule set.
- Network Management will be discussed for the CAN bus. Being a general concept it should be easy to apply it with other buses. Only the link layer protocols are different, but this is explained in the respective AUTOSAR specification.