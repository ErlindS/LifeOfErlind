Let's explore the next major functionality in the diagnosis stack: The Diagnostics Event Manager (Dem). This chapter delves into the wide array of configuration possibilities offered by the Dem and the limited APIs it utilizes.

The fundamental use of the Dem lies in calling the "set event status" API, allowing the diagnosis application to communicate the status of functional paths within the system. The Dem takes charge of automatically writing event states to an even states buffer, debouncing these states, and checking operation cycles against indicated events.

The Dem increases operation cycle counters and stores event states automatically in the NvM blocks, ensuring the presence of event states on the next startup of the system. It serves as a crucial component whenever the monitoring software detects an event, notifying the system and storing the event in memory, be it primary or secondary.

Software Components (SWCs) and BSW modules use Dem APIs to report an event status i.e. event is passed or failed. Fig. 1 shows Dem module and interfaced with other SWC and BSW modules. Dem communicate with SWCs and NvM module

A significant portion of  below picture is dedicated to comprehending Diagnostic Trouble Codes (DTC) and event states. Events, representing potential faults in the ECU project, can have various states, including being forgotten, pretty bounced, or learned based on specific conditions.

Below picture meticulously describes the meanings associated with each state bit within a DTC. It explains the test failed bit, the pending DTC, confirmed DTC, and other states that indicate the status and history of a fault.

## Event
Whenever the monitoring software detects an event, it will notify this to the Dem. The Dem then records this event.

## Status
Each DTC (Diagnostic Trouble Code) is coupled with one byte providing status information. The bits represent the following meanings:

**testFailed (bit0)**
If the testFailed bit is set it means that the fault is active. The test for an error condition or wrong behavior has succeeded.

**testFailedThisOperationCycle (bit1)**
This bit is only set if the fault occurs in the current operation cycle. If the fault is active and this flag is not set it means that the fault occurred in a previous operation cycle.

**pendingDTC – prefailed (bit2)**
Indicates that the corresponding DTC will be set in the near future.

**confirmedDTC – stored in Primary Memory (bit3)**
As soon as the fault is stored in the Primary Memory, this bit is set. If the fault is cleared from the event storage the value of this bit will be changed too.

**testNotCompletedSinceLastClear (bit4)**
If there is no information about whether the DTC test has passed or failed since the last clear, this flag is active.

**testFailedSinceLastClear (bit5)**
This flag informs you that the DTC  has   set since the last clearing action.

**notCompletedThisOperationCycle (bit6)**
This bit corresponds with the NotCompletedSinceLastClear. It informs whether the complete information was set or reset in the current operation cycle.

**warningIndicatorRequest (bit7)**
Indicates whether the occurrence of this DTC should set a warning indicator.

## Debouncing
“Learning” the fault and “Forgetting” the faults uses   (pre-)debouncing

## Indicators
There are indicator interfaces to indicate end user about malfunction inside vehicle, e.g. the Malfunction Indicator Lamp on dashboard to indicate emission relevant fault events are present in the vehicle.

Additional information to specify an event
- Freeze Frames  - have data objects
- Extended data records

## Freeze Frame(s)
OEM-specific set of the vehicle/system operation conditions at a specific time. The term “Freeze Frame” is defined as a record of data (DIDs / PIDs). ISO 14229-1 refers to FreezeFrames as “SnapShotRecords”. There is the possibility to use pre-stored FreezeFrames. It means the data is already available and does not need to be acquired when the event status changes. This way time-critical Freeze Frame data can be saved together with the event.

## Extended Data Record
OEM-specific additional information assigned for a distinctive event which is not contained in the Freeze Frame and also described in ISO 14229-1. Extended Data Records are implemented by callbacks to the application. These callbacks are issued by the Dem at the point in time when the Diagnostic Monitor sets the error event in the Dem. The diagnostic configuration can provide 1..n extended data records for a Dem event. Depending on the point in time, different extended data records will be recorded together with the error event. In this way the first occurrence and the last occurrence can be considered.

Differentiating between freeze frames and extended data records, the text elucidates their roles in storing additional information within the DTC. The freeze frames capture the initial occurrence of an event, providing examples such as RPM or temperature at the time of the fault.

Further insights are provided into extended data records, OEM-specific information, and their role in storing additional details. Occurrence flags, original odometer values, frequency, and operation cycle counters are discussed in detail.

## 

**Event Storage**

To provide the tester with more information about the point in time a DTC occurred, additional information is stored. This information is OEM-specific and is split into standardized and optional data. 

Examples for OEM-specific standardized data:

1. Click to flip
    
    Occurrence Flag
    
    Click to flip
    
    Distinguishes an entry as occurrence or fault.
    
2. Click to flip
    
    Original Odometer
    
    Click to flip
    
    This is the odometer value when the fault occurred for the first time.
    
3. Click to flip
    
    Most Recent Odometer
    
    Click to flip
    
    This is the odometer value when the fault occurred the most recent time.
    
4. Click to flip
    
    Frequency
    
    Click to flip
    
    This is the total number of times the DTC status has transitioned from “stored – not active” to “active.” 
    
5. Click to flip
    
    Operation Cycle Counter
    
    Click to flip
    
    This counter shows the amount of operation cycles (e.g., a new cycle starts after ignition off, ignition run, then wait 10 seconds). This information is used for a so-called self-healing process. If a DTC is stored but not active for a defined amount of operation cycles, it will be cleared from memory if it supports healing.


## 
**Pre-Debouncing**
To confirm the monitored fault event reported by SWC / BSW modules need debouncing mechanism.
The Dem can debounce Events reported to it via API i.e.   Dem_SetEventStatus(Dem_EventIdType EventId, uint8 EventStatus)
Argument values of EventStatus for debouncing are: 
- •
    DEM_EVENT_STATUS_PASSED: No debouncing, event is set to passed.
- •
     DEM_EVENT_STATUS_FAILED: No debouncing, event is set to failed.
- •
    DEM_EVENT_STATUS_PREPASSED: Debouncing relevant, configured debouncing done.
- •
    DEM_EVENT_STATUS_PREFAILED: Debouncing relevant, configured debouncing done.
There are three Algorithms for debouncing:
Counter based
Time based
Debounce monitor internal
A counter is used to do pre-debounce the fault event to qualify results (PASSED/FAILED) to the Dem.

## 
Internal and external events
There are two kinds of events: BSW events and SWC events.
BSW events are typically not accessible over UDS (to external world through DTC code). The BSW reports them as Production Errors, which are defined by AUTOSAR.
SWC events are defined by the application requirements and typically accessible over UDS with an respective DTC code defined.
If you assign a DTC to an event, it can be queried over UDS. You can also equip an existing event (especially EventKind BSW) with a DTC by redefining it in the diagnostic description file (CDD, DiagEx).

## 
Diagnostic Monitor Initialization
For every event, the monitor initialization function can be defined. This function (a runnable) is called after this event has been deleted from the DTC memory (Event is aged) or after the event is cleared i.e. Diagnostic Clear Service 0x14 / 0x04  a monitor initialization function is called. The application can check whether conditions for this event are still there or not.
Normally the monitor functions have large call cycles and may only be called seldom. With this initialization function, reaction time to a still-present event is very short.