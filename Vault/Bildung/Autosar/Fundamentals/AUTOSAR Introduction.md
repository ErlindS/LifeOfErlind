# Introduction
In the past, hardware and software of an ECU were often tightly interwoven. ECUs usually had to be redeveloped from the scratch whenever there were additional features, new controllers, different OEMs or modified architectures. 
Nowadays with Autosar, the hardware is abstracted from the application software which makes development more flexiable. Means: Software can be redeveloped independently from the hardware and ECUs no longer need to be redeveloped from scratch. 
The approach of the AUTOSAR Initiative is to use modular components. ECU suppliers can, for example, develop application components that can be reused on the projects of different OEMs.

## Today's Challenges 
+ The automotive industry is faced with great challenges in upcoming years. Today in-vehicle electronics have already reached a level of complexity that can hardly be mastered.
+ Quantity of functions implemented in software is rising very steeply (e.g. in the field of driver assistance systems).  Customers of the OEMs want even greater diversity in variants and equipment features. Moreover, automotive OEMs also need to observe criteria that are generally not even experienced by the end customer. Some examples of these non-functional requirements are diagnostic capability, availability and upgradeability.
+ The life of cars is usually longer than that of their ECUs (need for sustainable spare parts, especially software for maintenance reasons).
+ Embedded systems traditionally do not support full hardware abstraction, therefore most of the time there is a limited modularity of the software. Because of this limited modularity, the reusability is also limited. Software must often be rewritten from scratch when the hardware is changed.
+ Suppliers have to support a large variety of OEMs and vehicle platform variants with their software.
## Main Objectives of AUTOSAR
+ Standardization of interfaces: Different AUTOSAR software components can be bought from different suppliers and they should still be able to talk to each other.
+ Standardization of exchange formats: The way in which data is exchanged between the OEM and TIER 1 or within the TIER 1 and the data itself is standardized. Instead of a textual description, the suppliers work on XML based description with all data that is being designed, imported and exported out of the tools in AUTOSAR.
+ Standardization of methodology: With AUTOSAR, the development is shifting away from a purely code-based development to a code generation approach. The approach is mostly to configure parameters and then generate code based on the configuration.
## AUTOSAR Objectives
+ Serviceability: Serviceability over the entire product lifecycle. Means: Software updates and upgrades over the entire life of a vehicle.
+ Abstraction: Abstraction of hardware from software, making development more flexible.
+ Configuration: Shift development activities from implementation to configuration. Standardized AUTOSAR code generation/modeling tools.
+ Software Quality: Improvement in software quality by standardized Basic Software (BSW).
+ Competition: Competition is focused onto OEM-relevant features.
+ Reusability: Reusability of functionalities beyond the vehicle network is a key characteristic of AUTOSAR. The uniform and standardized description of functions and the system makes it possible.  Furthermore, functionalities can be moved across OEM boundaries as long as the standardized AUTOSAR interfaces are being used.
## AUTOSAR Core Partners
There are 9 core partners. BMW Group, Bosch, Continental, Daimler, Ford, GM, PSA, Toyota, Volkswagen.
At the same time one differentiates between Core, Premium, Development and Associate Partners.
Premium Partners make use of the AUTOSAR Standard and collaborate with the Core and Development Partners in order to define AUTOSAR. Associate Partners only make use of AUTOSAR.
## AUTOSAR Classic Architecture
The classical AUTOSAR Architecture consists of multiple Layers. Firstly the Application Layer with different SWC implementation for e.g. Dimmer. The Real Time Environment, which connect the SWC. The basis software, which is the OS and the hardware the controller. 