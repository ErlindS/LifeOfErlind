**Transmission Modes - I-PDU Tx Modes**
Transmission modes in AUTOSAR provide control over the communication behavior, particularly regarding when and how I-PDUs are transmitted. For every transmission mode it is possible to choose a value. In the following we will go through the 4 different values.

None
The PDU is never transmitted or the transmission never gets triggered by the Com module. 
You can use this setting if tranmission of a PDU shall be deactivated in one of the two modes described shortly.

Direct
A trigger is necessary so the PDU gets transmitted. Once the trigger is received, the Com proceeds to transmit the PDU. Furthermore, the number of repetitions and the duration can be customized. In our example, this involves a repetition of two with a configured repetition period.

Periodic
In periodic mode, it's possible to configure both an offset and a period. In this mode, the Com module operates without requiring an external trigger, instead, it relies on a timer. Whenever the timer reaches its expiration, the Com module initiates the transmission of the PDU.

Mixed
In the mixed mode, we combine the two modes mentioned earlier. It consists of a periodic part and an event driven part, that can use repetitions. Plus, you can set a Minimum Delay Time. This delay is important when triggers for both direct and regular transmissions happen at the same time. For example, if you set a 1-millisecond delay, there will be a 1-millisecond break between two PDU transmissions.

**Transmission Modes - Mechanism**
Various filters can be defined and the evaluation of these filters determines which transmission mode is activated. Let's delve into the details:

**Transmission Modes**
Transmission modes dictate the conditions under which the I-PDUs are sent. They are mainly divided into two categories, corresponding to the evaluation of filters:

Mode True
Activated when one or more filters evaluate to true.

Mode False
Activated when all filters evaluate to false.

### **Filters**
Filters are conditions that must be met for a particular transmission mode to be activated.

**Transmission Mode Selector (OR Gate)**
The evaluation of the filters is done through a transmission mode selector that acts as an OR gate:
- If at least one filter evaluates to true, the "Mode True" is selected.
- If all filters evaluate to false, the "Mode False" is selected.
This OR gate logic ensures that if any single condition is met (true), it will activate the "Mode True," allowing for flexibility in controlling transmission behavior.

**Transmission Modes - COM Signal Filters**
Filters in the context of Com Transmission Modes allow us to decide whether a signal fulfills specific criteria. Here are the filter algorithms that help us in this endeavor:

| Filter Type               | Description                                              | Outcome                                                                        | Use Case                                                                                        | Formula                        |
| ------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | ------------------------------ |
| Always                    | The "always true" filter.                                | This filter algorithm will always yield a TRUE evaluation result.              | Suitable for signals that should be evaluated positively regardless of any conditions.          | /                              |
| Never                     | The "always false" filter.                               | This filter algorithm will always result in a FALSE evaluation.                | Effective for signals that should never meet the criteria for evaluation.                       | /                              |
| MaskedNewDiffersMaskedOld | A filter focusing on bit-level comparisons.              | Compares the masked bits of the new and old values.                            | Appropriate when seeking to detect specific bit changes.                                        | ((new & mask) != (old & mask)) |
| MaskedNewEqualsX          | Filter based on masked bit equality.                     | Verifies if masked bits of the new value match a specific value.               | Useful when a positive evaluation hinges on the masked bits aligning with a predefined pattern. | ((new & mask) == x)            |
| MaskedNewDiffersX         | Detecting deviations from a specific masked bit pattern. | Determines if the masked bits of the new value differ from a specific pattern. | Valuable when the evaluation should rely on masked bits deviating from a predetermined pattern. | ((new & mask) != x)            |
| NewIsOutside              | Establishing conditions based on value range.            | Checks whether the new value falls outside a specified range.                  | Helpful when evaluating whether values exceed or are below predetermined thresholds.            | ((new < min) \| (max < new))   |
| NewIsWithin               | Pinpointing conditions based on value range.             | Determines if the new value is within a specified range.                       | Suitable for evaluating whether values lie within specific boundaries.                          | ((min <= new) && (new <= max)) |

Remember, the outcomes of these filters collectively shape the transmission mode for a Protocol Data Unit (PDU). This transmission mode, denoted as "true" or "false," presents you with unique configuration avenues, without directly dictating the transmission or non-transmission of signals or PDUs.
