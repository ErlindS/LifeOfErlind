## 

**Connecting the dots**

In the last chapter we learned how the SWCs and the NvM interact and we saw, that it mostly comes down to service Client/Server-Ports, which are connecting BSW-modules through the Rte to the Application. The SWCs of the Application use them to trigger NvM-Jobs. The NvM uses them to notify the SWCs about Job-results.

However, this assumes that there are connection endpoints available above and underneath the Rte. If a SWC wants to use a service-Client-Port to trigger a Write-Job for a Nv-block, there must be a Nv-Block providing a service-Server-Port it can get connected to.

Because the Vector tooling is designed to allow the independent development of the Application and the BSW-configuration with the DaVinci Developer Classic and the DaVinci Configurator, respectively, this imposes a synchronization challenge.

Synchronizing needs
The solution to this is built into the two tools, which are able to synchronize "needs" Top-down and Bottom-up.

Top-down synchronization
- On SWC level, "Service Needs" that contain the information, what is needed from the BSW, can be configured by the SWC developer.
- On BSW level, the information of the Service Needs is used to automatically derive the necessary configuration entities (e.g. Nv-blocks) and some of their properties.
- The BSW integrator then must take care to configure the remaining properties and references.

Bottom-up synchronization
- On BSW level, configuration entities with interactions to the Application can be created (e.g. Nv-Blocks, ComM users, Csm-Jobs etc.)
- The BSW provided service C/S-Ports then can be connected to **new** service C/S-Ports that get attached to the available SWCs, directly within the DaVinci Configurator.
- The SWC developer then must make use of these Ports. E.g. Use the ComM User to request Full-communication when a associated Bus shall be available.

Using the Top-down approach - by creating Service Needs - leaves the Application developers with the advantage, that they can proceed their development without waiting for the BSW integrators to create the necessary interfaces. And the BSW integrators only need to take care of the interfaces that are actually required and conveniently automatically synchronized from the Service Needs.