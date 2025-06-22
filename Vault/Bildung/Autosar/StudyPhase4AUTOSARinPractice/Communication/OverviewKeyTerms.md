
DataElement: A DataElement is a specific information unit exchanged between SWCs via Sender-/Receiver-Connections.

Message: Although often used in other contexts, the term Message is used synonymously with Signal in the context of the AUTOSAR Com module.

Signal: A Signal is a logical representation of a DataElement.

PDU: A PDU (Protocol Data Unit) contains Signals as a unit, including metadata like IDs and error-checking. 

Frame: A Frame is a physical unit of data transmission within the communication bus. It corresponds to a PDU. A Frame contains the actual PDU data along with control information necessary for reliable transmission, such as start and end markers, synchronization bits, error-checking codes and acknowledgment mechanisms. Frames ensure that PDUs are transmitted accurately and orderly over the communication medium, such as a CAN bus.


**DataElement**
A DataElement represents a discrete unit of information within the AUTOSAR communication model. It encapsulates a specific attribute or parameter of a system, defined by its data type and size. DataElements serve as the elemental entities that need to be exchanged between different components within a vehicle's electronic system.

**Data Mapping**
Up till now it was shown how a signal can be transferred and how it can be received. Now we will look at how a data element in the application can be connected with a signal in the Com module. Until now it was assumed that the information is available.
Data Mapping is the process in which a data element in the application is introduced to a signal in the Com module. The data element gets mapped to a network signal. We call this data mapping. This is necessary for all to be received and to be sent informations. 

**Signal**
A Signal is a logical representation of a DataElement within the communication framework. It defines the semantics, bit-length, and encoding rules for the corresponding DataElement. Signals provide the mechanism for actual data transmission between Electronic Control Units (ECUs), encapsulating the value of the DataElement along with additional attributes such as scaling factors and units of measurement.

**Signal Groups**
AUTOSAR Com introduces signal groups for the consistent transmission of multiple signals. Signals associated with a signal group are termed 'group signals' and are expected to be interrelated. A dedicated shadow buffer accompanies each signal group to maintain the uniformity of the group signal values.


**Data Consistency Using Signal Groups**

**Single Signals**
Individual signals are sent separately. The Rte invokes constant signals, placing data into the Com Tx buffer. Eventually, Com initiates the PDU transmission, prompting the application to refresh the signal values, which triggers the next PDU transmission. On the left, only signals 1´ and 2´ update. This discrepancy can be problematic, especially in scenarios like end-to-end protection for safety systems. The issue arises because the CRC value, based on the counter and current values, might have an outdated Crc, a refreshed counter, and an updated payload.

Signal groups offer a solution to this.

**Signal Groups With Shadow Buffer**

Signal groups in the Com module utilize an extra buffer known as the shadow buffer. Every invocation of Com_SendSignal updates this buffer, ensuring we don't operate directly on the shadow buffer. The Com shadow buffer offers consistent updates. Once updated, Com_SendSignalGroup can be executed. If the RTE is in play, it can manage this process.

Signal Groups
- Logical group of signals that belong together
- Signal groups are defined in the communication matrix
- Complex data types are mapped to signal groups by the Rte
- Signal groups comprise group signals

Signal Groups signify the following
- All group signals within a signal group are consistent
- Access is done by the Rte via a dedicated signal group and group signal API
- Signal groups shadow buffer provided by the Com --> One global shadow buffer for each signal group


**PDU (Protocol Data Unit)**
A PDU, or Protocol Data Unit, serves as a container for signals. PDUs provide a structured format for organizing data exchange between ECUs. Each PDU holds one or more signals that are intended to be transmitted together. PDUs include metadata such as message IDs and error-checking information. They are processed through the protocol stack and directly transmitted over the communication bus.

PDU Concept
The term "PDU" (Protocol Data Unit) refers to different types of information packages transferred between layers. In the context of the AUTOSAR transmission path we've just explored, we can identify three primary types of PDUs: I-PDU, N-PDU, and L-PDU.

## I-PDU (Interaction Layer PDU)
I-PDU represents the data exchanged within the interaction layer of AUTOSAR. This PDU includes both the data itself and metadata related to the interaction.
Between Com and PduR
Here, the I-PDU facilitates communication between the Communication Interface (Com) and the PDU Router (PduR). It encapsulates the signal object and adds necessary metadata for routing within the interaction layer.
## N-PDU (Network Layer PDU)
N-PDU is specific to the network layer.
Between PduR and (CAN)Tp or (Can)IF
The I-PDU can also be used for communication between PDUR and the Transport Protocol (Tp) module or Interface module like CanIF in the network layer. The choice between Tp and IF depends on the communication requirements, such as whether segmentation and reassembly are needed.
Between (Can)Tp and (Can)IF
When the (Can) Transport Protocol is involved, the N-PDU is used for communication with the (CAN) Interface (IF). The N-PDU deals with the segmented data, handling the fragmentation and reassembly process.
## L-PDU (Data Link to Physical Layer PDU)
L-PDU acts as the bridge between the Data Link Layer and the Physical Layer within AUTOSAR.
Between Data Link Layer and Physical Layer
The L-PDU is handed over to the physical layer, which includes the driver like the CAN Driver. The L-PDU contains the actual frame that needs to be transmitted over the physical medium, like the CAN bus. It's the final encapsulation of the data before it goes "on the wire."

These three types of PDUs play essential roles in the data transmission process within AUTOSAR, reflecting different levels of abstraction and functionality:

- I-PDU deals with interactions and routing, being crucial in the higher layers.
- N-PDU is involved in the network layer, dealing with aspects like fragmentation.
- L-PDU represents the final encapsulation as the data transitions from the logical world to the physical medium.


**I-PDU Group**
I-PDU groups in AUTOSAR are used to collectively manage a set of I-PDUs that are logically grouped together. This grouping allows control over the transmission and reception paths of several I-PDUs at once, enabling or disabling them based on different system states or operational modes. 

I-PDU groups are initialized with the call of Com_Init an deinitialized with Com_Deinit.
After the call of Com_IpduGroupStart () the I-PDU group is activated and e.g. cyclic I-PDUs will be sent out cyclically.
The call of Com_IpduGroupStop () stops a preconfigured I-PDU group. For example the sending of cyclic I-PDUs will be stopped.
To ensure the activation of an I-PDU, it's essential that at leastone of its corresponding I-PDU groups is active.  
An I-PDU is deactivated if all I-PDU groups it belongs to are deactivated.  
I-PDUs without an assigned I-PDU group are considered to be always active. The state of these I-PDUs cannot be controlled by Com_IPduGroupStart/Stop APIs.
