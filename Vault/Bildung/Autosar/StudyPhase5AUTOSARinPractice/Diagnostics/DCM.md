The Diagnostic Communication Manager (Dcm) is a network independent module and provides a common API for diagnostic services. The functionality of this AUTOSAR BSW module is used by external diagnostic tools e.g. in the development, manufacturing, service or legislative OBD.

The Dcm handles different (application layer) diagnostic protocols OBD (ISO 15031-5) and Enhanced diagnostics (ISO 14229-1).

For diagnostic session handling, the network independent sections of the following specifications are also handled by the Dcm: 

- ISO 15765-3: Implementation of unified diagnostic services (UDS on CAN)
- ISO 15765-4: Requirements for emissions-related systems

In the AUTOSAR architecture, the Diagnostic Communication Manager (Dcm) is located in the Communication Services (Service Layer). In the Communication process, the DCM receives a diagnostic message from the PDU Router. The Dcm will check the diagnostic message. Depending on the Diagnostic Service ID (SID), the corresponding calls in the Application Layer will be done (communicated with SWC via RTE (if required)) or DEM module to read snapshot data in case of $19 or other BSW modules. 

The Dcm ensures diagnostic data flow which manages the diagnostic states (Diagnostic sessions, Security states). It checks that the diagnostic service request is supported or not and checks that the service may be executed in the current session and with the current security state or not.

For a valid process, it invokes a certain action based on the requested service and provides the  response to tester tool via PduR.

****Example****

To get a better feeling for diagnostic communication let’s have a look at a simple example of a request and response.

In the picture below we find two messages:

- msg_diag_Request_MyECU
- msg_diag_Response_MyECU

The ISO Standards have already covered UDS and OBD services. Dcm is adaptable for Bootloader software as it inherently supports the necessary services.

For Bootloader-specific use cases, Dcm provides relevant APIs such as Dcm_SetProgConditions and Dcm_GetProgConditions.

The table on the right shows some UDS services which are used in this context.

Legend:  C = Callout/ Opt. = optionally available
**Dcm Configuration**

Click through the following steps to learn about the Dcm configuration.

- 1
- 2
- 3

Dcm Configuration

Dcm is all about diagnostic request and response. So during the configuration of the Dcm module you must know the supported services, security access and session state of each service. To configure Dcm means, you need to configure DSD, DSL and DSP.

START

Step 1
Configuration of DcmDsd: Diagnostic Service Dispatcher
The Diagnostic Service Dispatcher contains all parameters for all service dispatchers. All supported services and sub services are shown here including security and session access.

Step 2
Configuration of DcmDsl :Diagnostic Session Layer
All parameters related to a Diagnostic Session Layer are configured here, e.g.:
- The diagnostic buffer needs to be set to the size of the longest diagnostic message.
- The protocol used for the session (e.g. UDS or OBD on CAN or Flexray) is set here.
- The Tx and Rx (functional and physical) Pdus are configured here.

Step 3
Configuration of DcmDsp: Diagnostic Service Processing
The Diagnostic Service Processing contains additional parameter configuration, e.g:

- Read/Write access to DIDs
- Port access for operations via Client/Server or Sender/Receiver
- Settings of P2 and P2* values for the sessions

Dcm - Mode Management

The Dcm issues mode requests to the BswM in response to UDS requests it receives. Let's take the DcmCommunicationControl_<symbolic name of ComMChannelId> service (0x28) as an example. When the tester sends a request to disable communication (28 03 03), the Dcm can request the BswM to disable normal communication. The BswM takes the necessary actions, such as deactivating the corresponding I-PDU groups and Nm PDUs. The Dcm functions as a Mode Manager similarly for other services:

- •   
    DcmDiagnosticSessionControl (service 0x10)
    
- •   
    DcmEcuReset (part of service 0x11)
    
- •   
    DcmModeRapidPowerShutDown (part of service 0x11) 
    
- •   
    DcmControlDTCSetting (service 0x85)
    
- •   
    DcmResponseOnEvent_<RoeEventID> (service 0x86) 
    

### 

Dcm ComM Request

Apart from Active/Passive wake-up learned during ModeManagement, a Com Mode User can be requested by Dcm during a diagnostic session. Dcm requests and releases communication directly through the ComM.

During an ongoing communication service, 

- Dcm calls ComM_DCM_ActiveDiagnostic upon reception of the UDS request (Dcm_TpRxIndication)
- Dcm calls ComM_DCM_InactiveDiagnostic upon transmission of the UDS response (Dcm_TpTxConfirmation)

During session control service, upon transition into a non-default session, Dcm calls ComM_DCM_ActiveDiagnostic and upon transition into the default session Dcm calls ComM_DCM_InactiveDiagnostic. An ongoing diagnostics session keeps the communication channels requested. 

Communication Control service is an exception; this is handled by BswM. Additionally Dcm notifies the BswM about its current mode using the BswM_DCM API.