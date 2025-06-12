
AUTOSAR BSW Modules for Memory Abstraction

The following Modules - specified by AUTOSAR - participate in the Nv-memory stack and form the MICROSAR Classic MEM Solution:

- Nonvolatile Memory Manager  (NvM)
- Memory Interface (MemIf)
- EEPROM Abstraction (Ea)
- Flash EEPROM Emulation (Fee)
- EEPROM Driver (EEPDRV)
- Flash Driver (FLSDRV)

Optionally, above Rte on application layer, there is the NvBlock-Sw-Component-Type.

In the Figure below, an AUTOSAR architecture overview is shown where the mentioned BSW modules amongst the memory stack are highlighted in red.

NvM
The NvM (Nonvolatile Memory Manager) represents the interface to your application-/software-components, providing them with abstract Nv data storage areas and an uniform handling of them - independently of the underlying memory technologies.

MemIf
In the NvM, you can choose to configure Nv-blocks being stored in Data Flash or in EEPROM. The responsibility of the MemIf (Memory Interface) is to dispatch requests (e.g. read-/write-operations) from NvM to the lower layer modules (Fee or Ea) of the different memory technologies (FLASH or EEPROM), depending on the Nv-block setup.

Fee/Ea
**Fee** abbreviates **F**lash **E**EPROM **E**mulation and **Ea** stands for **E**EPROM **A**bstraction. These components abstract and organize the related memory technologies considering their hardware limitations e.g. segmentation and number of write/erase cycles. The Fee is handling the Data Flash whereas the Ea is handling the EEPROM technology.

Fls/Eep
Fls (Flash Driver) and EEP (EEPROM Driver) are NV memory drivers directly accessing the hardware. The Fls handles the commands to e.g. write or read data provided by the Fee. The same applies to the combination of the Eep and the Ea. This includes the additional handling/interaction required for external memory devices connected e.g. via Spi.


Nonvolatile Memory Manager (NvM)
The NvM takes care of three distinct tasks:
1. Providing abstract storage space to the application and the basic software.
2. Manages the characteristics of the provided storage spaces.
3. Handling the storage space according to the chosen characteristics.
These tasks follow a top down order: The storage space has specific characertistics that require an adequate handling. 

Storage Space:

Central element of the NvM are the **NvBlockDescriptors**, representing the configurable entity which defines the abstract storage space usable by the application or other BSW modules that need to store information nonvolatile. In favor of readability, we use Nv-block as synonymous term.
Each NvBlockDescriptor is identified with a unique ID and can hold a definable amount of data measured in Bytes. It requires a 1:1 mapping to a Fee- or an Ea-block, which establishes the link to the lower layers and decides in which memory the data will eventually be persisted. Additionally, a quite extensive set of characteristics is defined for each Nv-block. To learn more about these, switch to the next Tab.
Note: Some of these characteristics add to the information that is actually stored in memory - e.g. a CRC value calculated over the data. The Nv-block's ID however is not stored in memory and only relevant during configuration and implementation.

Storage Characteristics:

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

Storage Handling:

NvM MainFunction & NvM Jobs:
- Most of the Nv-block handling, especially also the requests to e.g. read/write them, is processed **asynchronously** within the Main-Functions of the NvM itself and the lower layer modules Fee/Fls & Ea/Eep. Therefore, the NvM provides a Job-queue with configurable depth that will accommodate and track the status of the requested Jobs. The Job status is updated either via polling or via notification callbacks from the lower layers.
- The queue itself can be handled as simple FIFO-buffer (First In First Out), or also consider prioritization.
- Jobs can get cancelled by the Application while they are still queued or currently in progress.
- The NvM-MainFunction also handles other asynchronous tasks like processing the NvMSetRamBlockStatus, calculating Ram block CRCs and informing the BswM (Basic Software Mode Manager) or the Dem (Diagnostic Event Manager) about Nv-block status information. Of course, always depending on the individual configuration of the Nv-blocks.
Shutdown/Startup Handling:
- Prominently, the NvM implements the NvM_WriteAll() and NvM_ReadAll() APIs, managing the persisting and restoring of the relevant Nv-blocks automatically.
Additional APIs that are provided by the NvM module of the MICROSAR.MEM solution for extended features concerning the handling of Nv-blocks can be found in the modules TechnicalReference document.


### 

Summary and what's next...

At this point, we learned a lot about the different features addressing different characteristics of Nv-blocks and the respective handling that comes with them, all provided by the NvM. However, the NvM itself does not care about the underlying memory technology. It assumes indefinite read/write & erase cycles for the Nv-block's data and attachments (e.g. CRC), irrespective of its size.

Fulfilling these assumptions is delegated to the next lower layer in AUTOSAR's memory abstraction architecture.

**EEPROM Abstraction (Ea)**
As we learned in the chapter **Principles of Memory Technologies**, the EEPROM-memory's biggest challenge is that it's endurable (re-)write cycles are quite limited. However, for some use cases - like the odometer - where typically more write cycles than the endurable number of write cycles are necessary, we need a coping mechanism.
The EEPROM Abstraction, located between the NvM and Eep in AUTOSAR's architecture, provides a **walking block** concept for this.
The central element of this concept are the Ea-blocks, which accommodate the Nv-blocks that refer to them. Calculated by dividing the estimated write cycles of an Ea-block by the nominal possible write cycles of the EERPOM hardware, the Ea reserves space for a number of copies of the Ea-block itself. By writing to these copies of the Ea-block in a round robin manner, the total write cycles of the Ea-block (and thereby the Nv-block) multiplies by the number of its copies. The estimated number of write cycles is configured for each Ea-block.

Example
You estimate an Ea-block (Block 1) to be written 400.000 times. Your EEPROM memory is able to confidently withstand 100.000 write cycles. Following above's explanation, the Ea will create 4x copies of the block (Block 1.0, Block 1.1, Block 1.2, Block 1.3).  
Can you figure out how many write cycles were estimated for Block 2 and Block 3?


Of course, the walking block concept introduces the need for additional meta-information that needs to be maintained and persisted as well. The easiest example would be the information, which block holds the most recent data. Because, while writing always concerns the next block, reading shall return the value of the most recently updated block.
The MICROSAR Classic Mem Ea manages this and other meta-information in order to be able to offer further Key-features based on it:

Operation Success: Using header and footer areas, the Ea is able to detect incomplete write operations, caused by reset or cancellation.
Data Validity: Ea is using ECC mechanisms for internally-added management information to increase robustness and reliability.
Performance: HW-alignment aware structuring of data is used to speed up write operations and to prevent influences on other (adjacent) data blocks/instances.


EEPROM Driver (Eep)
The EEPROM Driver is located in the MCAL-layer in the AUTOSAR architecture. It is directly accessing the EEPROM hardware, manifesting the requests (read/write/erase) from the Ea. EEPROM Drivers developed for externally connected memory chips will also construct e.g. the SPI- or I2C-commands to operate on the memory and only leave the actual sending of these commands to the related communication bus driver.  
As all hardware drivers, the driver software can only utilize the features the hardware actually provides. Nevertheless, AUTOSAR Eep drivers are required to provide a certain set of features and operations via its interface to the upper layer (Ea), irrespective of the hardware's capabilities. Amongst them are:
1. Byte-wise writing and reading.
2. Erase operation (e.g. SPI EEPROMs usually do not support this).
Additionally, the configurable Eep module needs to publish a set of device information usable by the Ea e.g. the erase-value (0x00 / 0xFF), addressable-unit size etc.  
Eep drivers of the MICROSAR Classic MEM solution also implement a configurable Write-Cycle-Reduction mechanism, which effectively writes data only if it is different from the current content of the block.

**Summary and what's next...**
At this point, we learned about the Nv-blocks, how they are related to and managed by Ea and eventually are persisted by the Eep. We learned about the hardware-aware mechanisms the Ea implements to fulfill the NvM's assumptions and discussed the Ea's requirements towards the Eep and its responsibilities eventually managing the EEPROM hardware itself.
Now, we want to explore the second option and how the handling of Nv-blocks is done with regards to the limitations of Flash memory.


Flash EEPROM Emulation (Fee)
As we learned in the chapter **Principles of Memory Technologies**, the Flash memory's major weakness is its inability to easily rewrite its Pages, combined with the limited amount of erase-cycles of the full Sectors.  
The basic idea to cope with these challenges is to use the memory space of one sector as much as possible, before the latest information needs to be secured and the sector can be erased and subsequently used again. To do so, a statically allocated copy-concept of the block to be stored, like we saw it in the chapter Ea, is not enough.  
The Fee implements a linked-list mechanism with dynamically allocated list-members called **Chunk**. Each Chunk holds a configurable number of **Fee Blocks**, which in turn accommodate the referring Nv-blocks. For each configured Fee block, initially one Chunk is allocated. Each write-request of a Fee block - coming from the NvM - will fill one block instance in the Chunk. Consecutively allocated Chunks are linked to the initial Chunk and will be placed in the next available memory within the **Logical Sector**. A Logical Sector can span over 1:n physical Sectors. The Fee always binds together at least two Logical Sectors to a **Fee Partition**. If one Logical Sector is filled to a configurable threshold, the latest block-information will be secured to an erased logical sector in the partition, before the current logical sector will be erased. This process is called Sector-Switching and will be discussed in detail later on.

In the following animation the chunk concept is illustrated interactively. You can use the slider to move the car and see what will happen at the level of the Flash sector. Consider the Logical Sector matching the physical sector in the example. Note that the second logical sector was left out of scope for the visualization.

In the example, we chose the Chunk to hold 3x instances of the Fee block accommodating its referring Nv-block. Note that the management information in the chunk header and the footer containing the link are not shown proportionally.

**What happens once a chunk is full?**
The animation shows that only a new write request will trigger the allocation of a new chunk, once a chunk is full. In the example, the new Chunk is allocated directly after the first one. Usually, this does of course not reflect reality.

**What happens once a logical sector is full?** 
After some time, eventually the logical sector will run out of space to allocate new Chunks. Then, a sector switch will become necessary. During the sector switch, the most recent information will be secured to the next suitable erased logical sector within the partition.  
The following interactive graphic shows the situation within the Fee partition after a successful sector switch with respect to the layout of the logical sector on the left in the previous visualizations.


We distinguish between two **operation modes**:
1. BSS (Background Sector Switch): Is handled during idle time and can be interrupted by a write-request.
2. FSS (Foreground Sector Switch): Can not be interrupted. Usually, the FSS should not be necessary and is considered to be the last resort before a sector overflow is happening. This might cause the loss of data.
There are configurable thresholds defining the remaining available space in the Logical sector until a BSS or eventually a FSS needs to be performed.

The management information maintained for the individual chunks of the Fee blocks are also used to enable some further Key-Features of the MICROSAR Classic MEM Fee:
Operations Success: Fee is able to detect incomplete writes (e.g. due to reset or due to cancellation).
Data Robustness: Redundant internal management information for increased robustness. Additionally, redundant Nv-blocks are automatically handled with a separate chain of chunks. There is no need to create separate FEE blocks.
Partitioning: Multiple partitions (in pairs of at least 2 Fee sectors) are supported for independent operation. Especially considering sector switching.
Configuration Update: With limitations, the Fee supports configuration updates. Meaning e.g. adding or changing Fee block information. Nevertheless, without special consideration this might lead to data loss.
Shared Data Flash: Shared configuration between Flash Bootloader and Application possible to exchange data reset resistant.
Wear: The MICROSAR Fee is able to retrieve the number of sector erases and block writes to gain knowledge about these metrics during development & testing.

Flash driver (Fls):
The Flash Driver is located in the MCAL-layer in the AUTOSAR architecture. It is directly accessing the Flash hardware, manifesting the requests (read/write/erase) from the Fee. Fls drivers developed for externally connected memory chips will also construct e.g. the Spi- or I2C-commands to operate on the memory and only leave the actual sending of these commands to the related communication bus driver.  
Mcu derivatives are required to either provide a dedicated Data-flash or the flash areas the Fls-driver operates on need to support the RWW (Read While Write) feature. Because, the Fls drivers functionality shall work independently from e.g. the general instruction fetching from Program-flash.

Additionally, the configurable Fls module needs to publish a set of device information usable by the Fee e.g. the Page size, Sector size and the number of sectors. This information is used to validate the partition configuration within the Fee.