Next, we encounter three important components: Units, Data Constraints and Compu Methods. They are highly valuable in achieving a comprehensive description of real-world values at the application layer. Through Units, Data Constraints and Compu Methods, we ensure precise interpretation and handling of data.

Units are used to establish a standardized and consistent representation of physical quantities within the system. They provide a way to associate real-world engineering units (e.g., meters, seconds, degrees Celsius) with data elements. By defining units for data, we ensure that values are expressed and interpreted consistently across different software components, regardless of the underlying microcontroller platform. This helps in maintaining accuracy and coherence during data exchange and supports seamless integration of software components.

- Units are globally defined
- Both Application Data Types and Compu Methods reference units
- They are meant to use Si Units
- Alternatively you can scale to the Si Unit

Data Constraints are utilized to impose restrictions or boundaries on the valid values that a data element can take. These constraints are defined based on real-world limitations or system requirements. By enforcing data constraints, we prevent the system from receiving or processing erroneous or invalid data. This helps in enhancing the safety and reliability of the automotive software system, as it ensures that the software components work within predefined acceptable ranges and conditions.

- Data Constraints are globally defined
- Data Constraints apply to an internal or physical value and set independent from each other
- ADTs and IDTs reference the data constraints

Compu Methods are employed to establish mappings and transformations between raw, internal values and meaningful external representations. They serve as a bridge between the logical behavior of data (Application Data Type) and its physical representation (Implementation Data Type). By using Compu Methods, we can convert data between different scales, units or formats, enabling seamless communication between software components with varying data requirements. This ensures that data is correctly interpreted and utilized throughout the system, regardless of the differences in data representation used by different components.

For enumerations, a TextTable Compu Method is used, allowing symbolic names to be mapped to their corresponding physical values using a lookup table, providing flexibility for non-linear relationships.

- Compu Methods are globally defined
- Categories: Identical, Linear, Scale-Linear, TextTable, Scale-LinearAndTextTable, BitfieldTextTable
- IDTs typically use Internal-To-Physical definitions
- ADTs typically use Physical-To-Internal definitions


1. Application Data Type
Our temperature value should be between -50 and 150 degrees. Additionally the accuracy should be 0,5 degrees.

So in other words: Our requirements for the range and the accuracy.
2. Compu Method 
According to the requirements of the ADT we have to define an appropriate Compu Method. In this example the factor is 2 so we don't get any floating points and an offset of 0. Through this we use a signed data type.
3. Implementation Data Type
The steps should be 1 so we have a total of 401 values. The range is between 300 and -100. This is because of the factor 2, which we chose in the Compu Method.
4. Data Type Mapping
The Compu Method in Step 2 was from physical to internal, so we need also a Compu Method from internal to physical. 

Through the two Compu Methods it's possible to automatically recalculate the values. But since the ADT and the IDT don't reference each other, the data type mapping is necessary.


**Type Mapping Set**

Type Mapping Sets are configurations that facilitate the establishment of mappings between Application Data Types and their corresponding Implementation Data Types within the software component. The Data Type Maps page displays a list of all Application Data Types in the workspace along with the assigned Implementation Data Types within the context of a specific Type Mapping Set.