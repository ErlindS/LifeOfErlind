If we want our ECU to communicate now, we need to add more managers. But why is this necessary?

1. **Aligning ECU Modes:**  
    The ECU has certain parts that can turn on or off, helping us save battery or power. It's important to make sure this turning on and off fits well with the ECU's different operations or modes.
    
2. **Managing RUN and RELEASE Requests:**  
    There are many parts or modules in our system, and several might want to start a chat or send messages. To avoid confusion and ensure smooth talks, we need a main part, or module, to oversee these chats.
    
3. **Connecting with Other ECUs:**
    Our ECU doesn't work alone; it connects with others. A few key points:
    - If an ECU on the same network needs info from ours, we can only pause or stop our chat when all are okay with it.
    - If another ECU needs info quickly, our ECU should be prepared to send it.
    - And sometimes, our ECU might have to make sure other ECUs don't go into a rest mode if they're still waiting for info.

Therfore, we need the Communication Manager (ComM) which interacts with the lower layer NM like CAN Network Management (CanNm).
In the next graphic you can explore the differences between an external and an internal Wake-up. Here is a description of the similarities:  
In both cases, before entering FULL COMMUNICATION, the communication will be allowed and the transceiver and controller will be set to a communicative state. I-PDU groups handled by the BSWM will be activated.  
When the network management indicates a preparation for bus sleep, the Tx communication is stopped. The SILENT COMMUNICATION will either be left on reception of a new network management message or the final bus sleep indication.  
Before entering NO COMMUNICATION Rx communication is stopped and the transceiver and controller are set for bus sleep.

Actually there is one more manager involved in the communication handling. The State Manager (SM) for the specific bus, in case of CAN communication the CanSM. This module handles the bus controller and transceiver.  It interacts directly with the physical bus.

Physical Bus -> "bus" SM
-> Handles On/Off, Disturbances

Inter ECU Coordination (Network Management) -> "bus" NM, NM-IF
-> Handles Sleep Transition, Wake-up by Bus, Node Identification

Intra ECU Coordination (Mode Management) -> ComM
-> Handles Com. Run Requests, Com. Release Requests, NM state notifications, Bus state notifications

Together with the bus specific NM - handling the inter ECU coordination - and with the ComM - handling the intra ECU coordination, the communication management is achieved in the layered AUTOSAR approach.
