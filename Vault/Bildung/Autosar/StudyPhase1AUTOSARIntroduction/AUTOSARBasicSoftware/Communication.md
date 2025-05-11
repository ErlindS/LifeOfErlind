# COM 
The Com module provides a signal-based data interface for the RTE. It places signals in messages and send them according to the defined send type. The module contains various notification mechanisms for receiving signals. It also manages initial values, update bits and timeouts on the signal level. In multi-channel ECUs, the integrated signal gateway offers the ability to route signals between the communication buses

# IPDU Multiplexer
The module ipduM supports multiple layouts which can be chosen by a selector field within an I-PDU. Alternatively, it supports to dynamically combine PDUs into a Container PDU:

# PDU Router
The module PduR handles distribution of the communication packets (PDUs) between the bus systems and the various BSW modules. In addition, it offers gateway mechanisms for routing IF-PDUs (last-is-best or FIFO) and TP-PDUs (store-and-forward or on-the-fly) between the bus systems.

# Transport Protocol
Segmented data transmission

# Interface
HW independent, bus-typical functions
+ Queuing
+ Assembly of data link layer PDUS/frames
+ Tx/Rx triggering on time-triggered buses

# Driver
HW operations
Initialization, filling of buffer, Interrupt Service Routine (ISR) implementation

# Transceiver
Operation of hardwware line driver circuits

