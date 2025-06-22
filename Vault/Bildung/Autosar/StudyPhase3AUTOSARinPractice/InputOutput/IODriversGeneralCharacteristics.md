Channel:
One element of the specific driver. E.g. I/O pin, Adc/ Pwm channel.

Channel Group:
E.g. group of pins, group of Adc channels that can be called at the same time.

Port:
A port register (e.g. 8-bit port).

**General Informations**:
The drivers provide only access to the hardware. There is no further functionality like data conversion and do plain reading of register values.

No data conversion - plain reading of register values:
- Port: No level inversion
- Adc: No value conversion
- Pwm/ Icu: No time/ frequency conversion

Time unit of register values is ticks:
- Actual time values depend on the MCU settings
- Conversion from ticks to time is not done (Has to take place in the I/O Hardware Abstraction)

**Benefits**
You are very free in the usage of the drivers.
Drivers make use of dedicated hardware functions (e.g. Pwm, Capture Compare Unit).
A channel group can be called with just one action. This provides a way that guarantees a consistent state of alle port pins.

**Disadvantages**:
It requires more work to interpret the values. In some cases it is impossible if it is not clear from where the values are coming.