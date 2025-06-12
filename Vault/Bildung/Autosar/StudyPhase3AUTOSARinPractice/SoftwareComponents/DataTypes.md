1. The C-Code Variable

In the world of C-Code, a variable is essential to store and manipulate data. When declaring a variable, we need to specify its type. However, in AUTOSAR, the process of defining data types involves a more structured approach.

2. Base Types

These fundamental data types include booleans, integers and floating-point numbers. By selecting an appropriate Base Type, we lay the groundwork for consistent data representation across different microcontroller platforms.

Base Types are the actual code-level type. There are no semantics. Base Types can be specified platform-specific, but for the sake of portability it is recommended to keep them platform independent. Native Declaration can be used to influence the Rte generator directly.

3. Implementation Data Type
Implementation Data Types (IDTs) describe the code level:

- Concrete data type
- For implementers
- Mandatory for code generation

IDTs represent the implementation-specific data types within software components. They decouple application-level data types from the underlying implementation details. They ensure consistency and compatibility between interface definitions and actual data types used in the implementation (Base Type).

4. Application Data Type 
Application Data Types (ADTs) describe the conceptual level:
- Abstract data types
- Conceptual/algorithmic view
- For function developers
- Optional usage

This data type is a physical representation accordingly described by CompuMethod, DataConstraint and Unit.

5. Mapping ADT to IDT
To bridge the gap between logical representation and hardware implementation, we establish a mapping between the ADT and the IDT. This mapping ensures that the ADT inherits the characteristics of the selected Base Type, aligning it with the hardware requirements.

6. Data Element with a Variable Type
Through this systematic approach, our data element gains its variable type. The ADT, mapped to the IDT, which in turn references the Base Type, defines the concrete representation of the data.



Data Type Sets in AUTOSAR allow developers to categorize and group related data types within a software component. They enable the definition of a specific prefix for the data types, promoting code readability, reusability and consistency across the project.

For each SWC, you can define lists of data types that shall share the same prefix.