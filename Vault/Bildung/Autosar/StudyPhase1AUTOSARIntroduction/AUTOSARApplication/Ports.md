 the interfaces to other software components for communication are called ports. They are connected by connectors. There are two types of ports: ports are either sender/receiver ports or client/server ports. Take a look at the following table for detailed information.

***Sender Receiver vs. Client/Server Ports***

| Category | Sender/Receiver Ports                                                                                                                                                                                                                        | Client/Server Ports                                                                                    |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Content  | - Contain data elements<br>    - Data element is 'mapped' to a signal if the information goes over the bus<br>    - Data Types<br>        - Simple:  <br>            Integer \| Float<br>        - Complex:  <br>            Array \| Record | - Client/Server ports contain operations with arguments<br>    - Operations can be called individually |


**Sender-Receiver Ports**

Sender-Receiver Ports are used for the data flow in our system, to exchange data between Software Components.

If we connect two Software Components with a port and we want to exchange multiple data elements, we dont need to use multiple ports but instead we can not only attach a single data element to a port but we can attach multiple data elements.

| Category      | Sender/Receiver Ports                                                                                                                                                                                                              | Client/Server Ports                                                                                                                                                         |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Communication | 1:n or n:1                                                                                                                                                                                                                         | 1:1 or n:1                                                                                                                                                                  |
|               | Data is transmitted asynchronously                                                                                                                                                                                                 | Communication is synchronous or asynchronous                                                                                                                                |
|               | The Server offers services which are requested by the Client<br><br>Sender<br><br>- provides data to one or more Receivers asynchronously<br>- neither expects any data nor receives any<br>- doesn't know the number of Receivers | The Server offers services which are requested by the Client<br>An AUTOSAR software component may be implemented as a<br><br>- Client<br>- Server or<br>- Client and Server |
|               | Principle corresponds to the familiar signal communication between ECUs                                                                                                                                                            | Inter und Intra ECU communication is possible                                                                                                                               |
| Example API   | Receiver API  <br>_Rte_Read_Door_DoorOpen()_                                                                                                                                                                                       | Client API  <br>_Rte_Call_Door_State()_                                                                                                                                     |

**Client-Server Ports**

Client-Server ports are used for control flow so these are ports which can request operations. 

How do they work? We have Software Components that act as the server (in the example below SWC3) and Software Components which connect to the server as clients (in the example on the left SWC1). They can now request the server to perform operations. Instead of data elements connected to the ports, we now have operations connected to the ports so every server port offers different operations. 

 An example of Client-Server Communication.
"Hi, my name is Software Component 3 and I am capable of calculating logarithms. I have a port called "logarithm" which has several operations like for example an operation to calculate binary logarithms and one operation to calculate a natural logarithm."

"Hi, I'm Software Component 1 and I have a client port connected to me. I would like some information. Maybe SWC3 can help?"

"Hi over there, I have some data here. Please calculate the natural logarithms for me"

This communication can work synchronously or asynchronously. Synchronously means that the client is blocked while the server performs its operations (similar to classical function call in C). Asynchronously means the client dispatches a job at the server and then continues running and once the server is finished then there are different ways of returning, either the client can pull the server state or the server notifies the client when it is finished.

"Sure thing, Software Component 1, here you go!"