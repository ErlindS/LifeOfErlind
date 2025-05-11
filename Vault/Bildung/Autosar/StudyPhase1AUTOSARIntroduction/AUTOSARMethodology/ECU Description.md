Each ECU extraction is handed over to a supplier. The supplier is able to generate a ECU Configuration Description (ECUC) with an AUTOSAR ECU Configuration Generator. 

Each supplier configures this configurator based on his own needs. For example, the ECU extract does not contain much information about the Operating System, because this configuration is usually very hardware and ECU specific. Therefore the supplier has to configure this information by himself and feed it to the ECU Configuration Generator.

1. After the successful ECUC generation, the suppliers now have all the information about the used SWCs...
2. ... is able to generate the actual RTE for this specific ECU ...
3. ... and generate all the Basic Software Configuration, for example the OS config.