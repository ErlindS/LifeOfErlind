The Basic Software Layers are the Service Layer, ECU Abstraction Layer, Microcontroller Abstraction Layer and Complex Device Drivers. Click on the Headlines below to learn more about those Layers.

# Service Layer
**Fact**
- Is the uppermost layer of the BSW
**Services**
- Operating system services
- Vehicle network communication and management services
- Memory services (NVRAM management)
- Diagnostic Services (including UDS communication and error memory)
- ECU state management
**Functionalit****y**
- Diagnostics, NVRAM Management, Watchdog Manager, Communication, OS, Schedule Manager, ECU state management, Com Channel Management
**Task**
- Providing basic services to the application and basic software modules

# ECU Abstraction Layer
**Fact**
- Contains interfaces for internal and external periphery as well as drivers for external devices.
**Functionality**
- Providing an API (programming interface) for devices.
    - Interface is independent of the devices' location (µC internal/external)
- Organizing the I/O hardware access.
**Task**
- Making higher levels independent of ECU hardware.

# MCAL
**Facts**
- Is the lowermost layer of the BSW
- **MCAL** is the abbreviation of **Microcontroller Abstraction Layer**
- Contains drivers with direct access to the microcontrollers, the internal peripherals and the memory mapped microcontrollers of external devices

**Task**
- Making higher layers independent of microcontroller

# Complex Device Drivers
**Fact**
- Special case in the Layered Software Architecture of AUTOSAR

**Task**
- Controlling special sensors and actuators by direct microcontroller access
    - E.g. those sensors and actuators subject to special timing conditions or the integration of non-AUTOSAR technologies
- Have direct access to resources for critical applications
    - Examples: Injection control, battery management system
