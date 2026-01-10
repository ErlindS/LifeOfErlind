CanTp, short for Controller Area Network Transfer Protocol, comes into play when dealing with Diagnostic requests and responses that can grow significantly in size. Diagnostic messages, in particular, may extend to multiple kBytes or even more. In instances where we need to transmit data exceeding the standard CAN protocol's limit of 8 bytes per message, we employ the CanTp concept, as defined in ISO 15765-2. This is crucial, given that the maximum payload capacity of a standard CAN frames is limited to 8 bytes.

The following picture gives an overview of the PDUs and SDUs interacting with the different layers. The N-SDU (Network-layer Service Data Unit) is the CanTp payload. The N-PDU (Network-layer Protocol Data Unit) is the payload with the PCI (Protocol Control Information) added by CanTp building the Single (SF), First (FF) and Consecutive Frames (CF).


The P-SDUs between Can and CanIf are not modeled in the EcuC module but we find the L-SDU, the N-SDU and the I-SDU in here.

In the DaVinci Configurator Classic, try to use a right click on the PDUs and use „element usage“ to get a list of all containers/parameters that refer to this specific configuration element.

If you want to know more about the timing requirements, there is a nice figure in the TechnicalReference_CanTp in the chapter “Connection Timings”. You can find the handling of a single frame transmission and for segmented transmission with multiple consecutive frames. 

## 

**Addressing**

Peer-to-peer communication, known as physical addressing, operates on a point-to-point basis, where both requests and responses are directed to specific addresses.

On the other hand, functional addressing functions as a "broadcast" communication method, reaching all ECUs. Utilizing Functional Addressing involves broadcasting a functional request to all ECUs, and each ECU responds individually.

The inefficiency of sending the same diagnostic requests to every ECU individually is addressed by functional addressing. In this scenario, a diagnostic client sends a single frame, which is received by all ECUs on the bus. Subsequently, each ECU processes the request and provides a response.

Why is there no functional response?
    
As you can see there is no special message for functional responses. Since the tester will receive many responses on a functional request it is important to distinguish which ECU sent which response. The simple but effective approach is: every ECU responds to functional requests with its physical response.