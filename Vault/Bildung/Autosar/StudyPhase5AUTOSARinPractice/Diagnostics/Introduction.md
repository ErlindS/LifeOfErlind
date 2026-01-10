Imagine diagnostics in AUTOSAR like a health checkup for your car, similar to how you go to the hospital to ensure you're healthy. If there's an issue, diagnostic tools, like medical tests, help identify the problem so it can be fixed for your vehicle to run smoothly and safely. This process usually happens at a service station, using specific tools designed to pinpoint and resolve issues.

In the broader context, diagnostics in AUTOSAR is a significant topic. It involves understanding diagnostic standards, meeting OEM requirements, and integrating these into our ECU software. To delve into diagnostics, we need to grasp ISO Standards, key mechanisms configuration in AUTOSAR and how they interact with our application code.

This learning module builds on the knowledge gained from previous modules and AUTOSAR Fundamentals, bringing together the insights needed to navigate the complexities of automotive diagnostics.

1. 1
    
    **Communication:** To communicate with specific external devices.
    
2. 2
    
    **Mode Management:** To manage service requests and states.
    
3. 3
    
    **Memory:** To store errors in the nonvolatile memory which can be read out using diagnostics.
    

## 

Use Cases for Diagnostics:

First let us have a look at some typical scenarios in which diagnostic functionality is used to interact with ECUs. In general we can use it to read information, write settings, trigger actions or even update the software of our ECU.

The procedure to achieve these goals is always as follows:

Diagnostic Requests (REQ) and Diagnostic Responses (RES) may already contain data, but this is not necessarily the case and depends on the definition of the diagnostic service.

A diagnostic request will typically be followed by a diagnostic response. If there is no response at all, the tester will observe a timeout.

The Diagnostic Response (RES) can be one of the following:

## 

Positive Response:

The service request has been processed correctly and a response, possibly with data, is on its way to the tester.

## 

Negative Response with Negative Response Code (NRC):

The service processing encountered an error specified by the NRC code, and this is indicated to the tester.

## 

Negative Response with NRC RequestCorrectlyReceiveResponsePending (RCRRP):

The diagnostic server needs more time to process the request and cannot deliver a positive or negative response yet.

1. Click to flip
    
    How can you identify a positive response?
    
    Click to flip
    
    A positive response will start with the SID (Service Identifier) of the request increased by 0x40. For example, the SID 0x10 will be answered positively with 0x50.
    
2. Click to flip
    
    How does a negative response start?
    
    Click to flip
    
    A negative response starts with 0x7F followed by the SID of the request and a Negative Response Code (NRC). For example, if the request is $22 FD 78 (Read Data by Identifier FD 78) and service 0x22 is not supported, then the the negative response will be $7F 22 11. 
    
    0x11 is the code for service not supported. NRCs for each service can be found in ISO 14229-1.