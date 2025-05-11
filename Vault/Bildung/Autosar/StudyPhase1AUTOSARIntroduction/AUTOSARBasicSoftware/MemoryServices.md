# Memory Services Cluster and Its Modules
The Memory Services are used if something has to be stored into the non volatile memory. It abstracts locations of internal (on-chip) and external (on-board) memory devices.  

It is subdivided into: 
- Service Module: NVRAM Manager
- ECU Abstraction: Memory Abstraction Interface, EEPROM Abstraction and Flash EEPROM Emulation 
- MCAL Layer: Memory Drivers

# NVRAM
+ Is the interface to the application
+ Provides access to the non volatile memory with sender/receiver, client/Server ports
+ allows you to write memory blocks to the lower layer.
+ There are no files, there are only memory blocks (= blocks of data of a certain lengths which have to be configured in advance)
	+ Means: No dynamic allocation of memory. 

# Memory abstraction Interface
Maps APIs to the lower layer abstraction modules.


# EEPROM abstraction & Flash EEPROM emulation
Is the technology abstraction. In AUTOSAR there are 2 technologies which are specified:
- EEPROM abstraction and
- Flash Memory

+ For each of those technologies exist different approaches how to read and write from them.

# Hardware Specific Drivers
+ Are either used for external memory blocks or
+ for internal Flash or EEPROM Memory
