### 

****Sender Receiver vs. Client/Server Ports****

| Category | Sender/Receiver Ports                                                                                                                                                                                                                        | Client/Server Ports                                                                                    |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Content  | - Contain data elements<br>    - Data element is 'mapped' to a signal if the information goes over the bus<br>    - Data Types<br>        - Simple:  <br>            Integer \| Float<br>        - Complex:  <br>            Array \| Record | - Client/Server ports contain operations with arguments<br>    - Operations can be called individually |

| Category                                                                                                                                                       | Sender/Receiver Ports                                        | Client/Server Ports                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------- |
| Communication                                                                                                                                                  | 1:n or n:1                                                   | 1:1 or n:1                              |
| Data is transmitted asynchronously                                                                                                                             | Communication is synchronous or asynchronous                 |                                         |
| Sender<br><br>- provides data to one or more Receivers asynchronously<br>- neither expects any data nor receives any<br>- doesn't know the number of Receivers | The Server offers services which are requested by the Client |                                         |
| An AUTOSAR software component may be implemented as a<br><br>- Client<br>- Server or<br>- Client and Server                                                    |                                                              |                                         |
| Principle corresponds to the familiar signal communication between ECUs                                                                                        | Inter und Intra ECU communication is possible                |                                         |
| Example API                                                                                                                                                    | Receiver API  <br>_Rte_Read_Door_DoorOpen()_                 | Client API  <br>_Rte_Call_Door_State()_ |
**Sender-Receiver Ports**

Sender-Receiver Ports are used for the data flow in our system, to exchange data between Software Components.

If we connect two Software Components with a port and we want to exchange multiple data elements, we dont need to use multiple ports but instead we can not only attach a single data element to a port but we can attach multiple data elements.

### 

**Client-Server Ports**

Client-Server ports are used for control flow so these are ports which can request operations. 

How do they work? We have Software Components that act as the server (in the example below SWC3) and Software Components which connect to the server as clients (in the example on the left SWC1). They can now request the server to perform operations. Instead of data elements connected to the ports, we now have operations connected to the ports so every server port offers different operations. 

Click on the numbers in the image below to get an example of Client-Server Communication.