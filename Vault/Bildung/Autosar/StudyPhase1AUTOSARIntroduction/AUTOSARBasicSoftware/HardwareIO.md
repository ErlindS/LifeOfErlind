
The module IoHwAb (I/O Hardware Abstraction) represents the connection between the RTE and the ECU’s I/O channels. It encapsulates access to the I/O drivers and thereby makes the I/O signals of the ECU available to the SWCs.

**Quick facts:**

- Abstraction of location of I/O peripheral devices (on-chip / on-board) and layout
- No abstraction of sensor/actuator
    - I/O signal interface
    - Conditioning of the read values of inputs
    - e.g. debouncing of signals
- Drivers
    - ADC, DIO, PWM