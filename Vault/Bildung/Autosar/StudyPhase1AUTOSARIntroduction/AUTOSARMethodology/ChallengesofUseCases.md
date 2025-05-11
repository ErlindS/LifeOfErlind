There are multiple Modles:
+ Service Components
+ Service Mapping
+ atomics
+ Compositions
+ Data Mapping
+ Ecu Composition
+ Communication

**Use Case 1**
In this scenario the OEM takes only care about the network communication.
The TIER 1 is responsible for the complete implementation of all ECU functions like data mapping, structuring by compositions and the usage of atomics and needed service components.

**Use Case 2**
In this scenario the OEM defines next to the communication like Use Case 1 also the internal structure via usage of compositions and the connector between them. Also the data mapping is part of OEM duties.
The TIER 1 implements the complete ECU functions by using atomics and services.

**Use Case 3**
In this scenario the OEM defines like Use Case 2 the network communication, the compositions, the connector between the compositions, the data mapping and also additionally the implementation of some ECU functions by using atomics.
The TIER 1 is implementing the remaining functions by using atomics and services.