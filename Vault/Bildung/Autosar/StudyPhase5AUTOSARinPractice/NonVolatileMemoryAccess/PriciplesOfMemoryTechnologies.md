## EEPROM
In this chapter, the two most commonly used memory technologies will be introduced - EEPROM and Flash EEPROM.

**EEPROM** stands for **E**lectrically **E**rasable **P**rogrammable **R**ead-**O**nly **M**emory.
**Size and smallest addressable unit:**
On EEPROMs, the smallest adressable /changeable unit for read- and write-operations is usually sized from 1 byte to very few bytes (e.g. 4). We will call them Blocks within the scope of this course. The overall size of nowadays available EEPROM memory chips ranges from a few kB to several MB, which is comparatively small.

**Rewriting - How and how often?**
The EEPROM Blocks are directly rewritable. There is no need to erase the memory before rewriting it. Yet, the rewrite cycles per block are limited and heavily dependent on environ-mental boundary conditions (e.g. temperature) to ranges from ~100.000 cycles to 4*10^6 cycles in the best case.

**Costs and Handling:**
Considering cost per memory space, EEPROM is comparatively expensive and most modern MCU derivatives do not contain an integrated EEPROM. EEPROM memory is therefore usually connected via peripheral buses like I2C or SPI.

## Flash EEPROM
**Size and smallest addressable unit:**

On Flash, the smallest addressable/changeable unit for read- and write-operations is called Page, which is usually sized significantly larger than a single byte (e.g. Tricore Data-Flash Page == 8 byte). Pages are organized/clustered within Sectors, usually sized in the magnitude of several kByte.

**Rewriting - How and how often?**
Flash pages can not be overwritten directly. Beforehand, the memory cells which form the page need to be erased. Yet, erasing is only possible for full Sectors. Consequently, attempting to overwrite pages produces significant effort and affects memory areas not directly associated with the page. Additionally, also Flash-sectors are only erasable a limited amount of times. Usually in the magnitude of 10^5 erases.

**Costs and Handling:**
Considering cost per memory space, Flash memory is comparatively cheap. Most modern MCU derivatives contain a dedicated data-flash of considerable amount, which is directly usable to store data nonvolatile. Of course there are also Flash memory chips that are connected via peripheral buses like SPI or I2C available.