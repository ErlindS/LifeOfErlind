
Introduction to NvBlockSwComponents
Now, after we learned about
1. the different memory technologies,
2. how they are managed by the memory stack and
3. saw the first approach on how to interact with the NvM from the Application to trigger and evaluate Jobs handling the associated Nv-blocks,
let's have a look into a different, more modern approach your SWCs can take. This involves the **NvBlockSwComponents** type that let's you define special Software Components, which are solely meant to handle the interaction with the NvM and manage the data distribution on application layer. This special SWC-type is a new feature associated with the Nv-memory stack, which was introduced with AUTOSAR 4.

In the following tabs you can learn about the changes between the legacy AUTOSAR 3 and the AUTOSAR 4 approach and its advantages.

AUTOSAR 3. :
Nonvolatile memory handling is block oriented. Usually, each SWC that needs to store nv-data has their own Nv-blocks and the respective interactions.
This leads to:
- Inefficient memory usage, because of the management information overhead for each block. Especially, if small data has to be stored individually.
- Distribution of nonvolatile data between SWCs is difficult to handle, because PiMs or module-local static variables are private members of a SWC.
- PIMs are not protected against concurrent access from different Runnables of a SWC.
- Data synchronization mechanisms between application and NvM need to be considered for each SWC individually.

AUTOSAR 4. :
The NvBlockSwComponents address this situation by introducing:

- Configurable automatic aggregation of data into one RAM-buffer that is associated with one Nv-block (analogous to Signals and Signal Groups in Com).  
    **Pro:** Larger Nv-blocks promise a better ratio of user-data to management data.  
    **New:** “Fan-in” and “Fan-out” of data elements to and from the RAM-buffer.
    - "Fan-in": Multiple SWCs can write their Nv-elements to the same Nv-block.  
        Additional RAM is required because an extra buffer stage is required for this.
    - “Fan-out”: Provide Nv-data to multiple receiving SWCs at once.  
        Overall RAM consumption can be lower, because the same data elements can be shared in the ECU with this feature (like calibration data).
- Inherent S/R-Port oriented data exchange via Rte.  
    **Pro:** Easy and flexible Nv-data distribution to SWCs.  
    **Pro:** Protection against concurrent access to the buffers by Rte.
- **Pro:** Less SWCs with interactions to NvM that need to be considered.


**Nv-Ports and Their Relation To Nv-Block Needs**
As stated in the interactive pictures, the Nv-Ports already have properties attached to them, which are used to define the characteristics of the Nv-data they carry (e.g. write cycles or CRC usage). These properties are propagated along with the port connection. The NvSWC then needs to merge these properties to be able to cluster different Nv-elements from the SWCs into common NvBlockDescriptors. The block descriptors will then inherit the merged set of characteristics of the individual Nv-elements.
The following table illustrates the rule-set used to merge the list of properties and gives some hints, which Nv-elements can be clustered sensibly:

**Legend**
‘=‘: recommended to be identical
‘=MAX‘: recommended to be the maximum of all existing values
‘OR’: recommended to be set TRUE if at least one of existing values of Nv data Ports is set TRUE.
‘!=‘: may be set differently among different Nv data Ports
