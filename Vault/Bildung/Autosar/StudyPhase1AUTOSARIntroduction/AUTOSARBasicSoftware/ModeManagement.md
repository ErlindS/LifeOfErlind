
# **System/Communication Services Explained**

# ECUM
**Module name**
- ECU State Manager (EcuM)
**Functionalities**
- Handles the fundamental states of your ECU (ECU state machine): On, Off and Sleep.
- Performs the necessary transitions between those states.
- Centralizes and validates wake-up events.
**Implementation**
- If you want to initialize an AUTOSAR stack the first function you call is _ECuM_init._
**Example**
- Responsible for
    - the initial startup of the system,
    - the start of the OS,
    - the proper shutdown of the system, 
    - for transitioning the system into sleep mode.

# COMM
**Module Name**
- Communication Manager (ComM)
**Functionalities**
- Abstracted Bus state machine.
- Has control over the communication states of all your channels.
    - Responsible for Startup/shutdown of communication.
- Uses Bus specific modules (**Bus SM**) to switch states of Buses.
**Fact** 
- Completely independent of hardware and technology.
- Controlled by Application from the top, also controlled by external influence through the network management.
**Example**
- The ComM is the direct interface to the application where you can request the communication

# NM IF and Bus NM
**Module Names**
- Network Management Interface (NM If)
- Bus Network Management (Bus NM)
**Functionalities**
- Handle the network management.
- Keep the bus awake or coordinate shutdown.
- Send periodic messages while ECU is in normal mode or bus segment is awake.
- Optimization for busload reduction
    - only 2 ECUs in the bus segment send NM messages, all others listen.
**Examples**
- NM wakes ComM and notifies it about external requests from the Bus, so ComM can wake others. 
- If the Application from the top wants to keep the bus awake then the ComM communicates to the NM: Keep Bus awake.

# Bus SM
**Module Name**
- Bus State Manager (Bus SM)

**Functionalities**
- Switches transceiver and controller state.

**Example**
- Switches the states of tranceiver and controller by translating the network communication mode requests from ComM.