The following Modules - specified by AUTOSAR - participate in the Nv-memory stack and form the MICROSAR Classic MEM Solution:

- **Nonvolatile Memory Manager  (NvM)**
- **Memory Interface (MemIf)**
- **EEPROM Abstraction (Ea)**
- **Flash EEPROM Emulation (Fee)**
- **EEPROM Driver (EEPDRV)**
- **Flash Driver (FLSDRV)**

NvM 
The NvM (Nonvolatile Memory Manager) represents the interface to your application-/software-components, providing them with abstract Nv data storage areas and an uniform handling of them - independently of the underlying memory technologies.

MemIf
In the NvM, you can choose to configure Nv-blocks being stored in Data Flash or in EEPROM. The responsibility of the MemIf (Memory Interface) is to dispatch requests (e.g. read-/write-operations) from NvM to the lower layer modules (Fee or Ea) of the different memory technologies (FLASH or EEPROM), depending on the Nv-block setup.

Fee/Ea
**Fee** abbreviates **F**lash **E**EPROM **E**mulation and **Ea** stands for **E**EPROM **A**bstraction. These components abstract and organize the related memory technologies considering their hardware limitations e.g. segmentation and number of write/erase cycles. The Fee is handling the Data Flash whereas the Ea is handling the EEPROM technology.

Fls/Eep
Fls (Flash Driver) and EEP (EEPROM Driver) are NV memory drivers directly accessing the hardware. The Fls handles the commands to e.g. write or read data provided by the Fee. The same applies to the combination of the Eep and the Ea. This includes the additional handling/interaction required for external memory devices connected e.g. via Spi.


**Nonvolatile Memory Manager (NvM)**

The NvM takes care of three distinct tasks:

1. Providing abstract storage space to the application and the basic software.
2. 2 Manages the characteristics of the provided storage spaces.
3. 3Handling the storage space according to the chosen characteristics.

These tasks follow a top down order: The storage space has specific characertistics that require an adequate handling.


Central element of the NvM are the **NvBlockDescriptors**, representing the configurable entity which defines the abstract storage space usable by the application or other BSW modules that need to store information nonvolatile. In favor of readability, we use Nv-block as synonymous term.

  
## Storage Space
Each NvBlockDescriptor is identified with a unique ID and can hold a definable amount of data measured in Bytes. It requires a 1:1 mapping to a Fee- or an Ea-block, which establishes the link to the lower layers and decides in which memory the data will eventually be persisted. Additionally, a quite extensive set of characteristics is defined for each Nv-block. To learn more about these, switch to the next Tab.

Note: Some of these characteristics add to the information that is actually stored in memory - e.g. a CRC value calculated over the data. The Nv-block's ID however is not stored in memory and only relevant during configuration and implementation.

## Storage Charateristics

Attached to every Nv-block, a set of configurable properties is specified, that allows to customize its partly automatic and user-defined handling in various situations. The most relevant ones will be discussed here.

**Data Validity/Reliability & Confidentiality:**
- Nv-blocks can be configured to be stored with an attached CRC value calculated over the data. This can be used after reading from Nv-memory to check if the data is valid.
- Redundant storage and associated checks increase the reliability of the Nv-block's data significantly. In case of loss of redundancy, or generally read errors, defined default data can be provided by configuring ROM block data or application callbacks.
- By configuring interfaces to the Crypto Stack, Nv-block data can also be stored encrypted. More generically, also Application callbacks can be used to transform the data before writing/after reading to/from memory.

**Data Availability:**
- Nv-blocks can be configured to be stored during shutdown and restored during startup of the ECU. 
- Prioritization can be used to achieve immediate storing of e.g. crash-data. Other ongoing Nv-job requests will be interrupted.

**Data Protection:**
- Access to Nv-block data can be restricted by activating the write protection during runtime. This is persisted, but can be deactivated.
- Nv-blocks can be marked to be "write once". If they get stored once, a persistent not deactivatable write protection becomes active.

**Data consistency and synchronization between RAM mirror and Nv-data:**
(try to recall the picture of the initial example of this point)
- The Ram Block (or variable) associated with the Nv-block can be assigned a "status" if the "Set Ram Block Status" feature is enabled within the Nv-block's properties. This way it is easy to determine, if the value in RAM changed. This can be combined with the calculation of a CRC checksum for the RAM value. Utilizing this "status" and/or the Ram Block CRC can make the decision, if the Nv-data needs to be stored - e.g. during shutdown - more efficient.
- Writing or reading data to or from Nv-memory requires the NvM to access the RAM block associated with the respective Nv-block at a certain time during the processing. Unfortunately, there is no automatic mechanism in place securing the RAM block from concurrent access from the NvM as well as from the Application. This may lead to data corruption. Thus, NvM provides an explicit synchronization feature utilizing Callbacks to trigger the Application to either fetch or provide the most recent data synchronously.

Additionally, there are further opportunities to configure Application callbacks allowing to implement special functionalities during certain stages of the Nv-block handling. To learn a little more about the Nv-block handling within the NvM, switch to the next Tab.

The interaction between the Nv-block and the Ram block as well as the involvement of the Application in these mechanisms will be revisited and discussed in greater detail in the chapter Nv-memory handling.