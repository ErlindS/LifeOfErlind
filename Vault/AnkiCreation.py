import genanki

def erstelle_anki_karten(karten_liste, deck_name="Mein Deck", deck_id=1234567890):
    # Erstelle ein neues Deck
    mein_deck = genanki.Deck(
        deck_id,
        deck_name
    )

    # Einfaches Karten-Template
    mein_model = genanki.Model(
        1607392319,
        'Einfaches Modell',
        fields=[
            {'name': 'Frage'},
            {'name': 'Antwort'},
        ],
        templates=[
            {
                'name': 'Karte 1',
                'qfmt': '{{Frage}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Antwort}}',
            },
        ])

    # Karten hinzufügen
    for frage, antwort in karten_liste:
        karte = genanki.Note(
            model=mein_model,
            fields=[frage, antwort]
        )
        mein_deck.add_note(karte)

    # Deck speichern
    genanki.Package(mein_deck).write_to_file(f'{deck_name}.apkg')
    print(f"Deck '{deck_name}.apkg' wurde erfolgreich erstellt!")

cards = [
    # --- Set 1: Software Components, Ports, Runnables ---
    [
        "Was sind die Hauptunterschiede zwischen Sender/Receiver- und Client/Server-Ports bezüglich des Inhalts?",
        "Sender/Receiver-Ports enthalten Datenelemente (einfach wie Integer/Float oder komplex wie Array/Record), die bei Bus-Kommunikation auf Signale gemappt werden können. Client/Server-Ports enthalten Operationen mit Argumenten, die einzeln aufgerufen werden können."
    ],
    [
        "Wie unterscheidet sich die Kommunikationsrichtung und -art zwischen Sender/Receiver- und Client/Server-Ports?",
        "Sender/Receiver-Kommunikation ist 1:n oder n:1 und asynchron. Client/Server-Kommunikation ist 1:1 oder n:1 und kann synchron oder asynchron sein."
    ],
    [
        "Beschreibe das Sender-Prinzip bei Sender/Receiver-Ports.",
        "Ein Sender stellt Daten asynchron für einen oder mehrere Empfänger bereit. Er erwartet keine Daten zurück und kennt die Anzahl der Empfänger nicht. Dies entspricht der Signal-Kommunikation zwischen ECUs."
    ],
    [
        "Beschreibe das Client/Server-Prinzip bei Client/Server-Ports.",
        "Der Server bietet Dienste an, die vom Client angefordert werden. Eine AUTOSAR-Softwarekomponente kann Client, Server oder beides sein. Kommunikation ist sowohl innerhalb einer ECU (Intra-ECU) als auch zwischen ECUs (Inter-ECU) möglich."
    ],
    [
        "Wofür werden Sender-Receiver Ports hauptsächlich verwendet?",
        "Sender-Receiver Ports werden für den Datenfluss im System verwendet, um Daten zwischen Softwarekomponenten auszutauschen."
    ],
    [
        "Können über einen einzelnen Sender-Receiver Port mehrere Datenelemente ausgetauscht werden?",
        "Ja, an einen Sender-Receiver Port können mehrere Datenelemente angehängt werden, es sind nicht mehrere Ports für mehrere Datenelemente nötig."
    ],
    [
        "Wofür werden Client-Server Ports hauptsächlich verwendet?",
        "Client-Server Ports werden für den Kontrollfluss verwendet, um Operationen anzufordern."
    ],
    [
        "Was sind 'Operationen' im Kontext von Client/Server-Ports?",
        "Operationen sind Dienste, die von einem Server-Softwarekomponente angeboten und von einer Client-Softwarekomponente aufgerufen werden können. Sie sind an die Client/Server-Ports gebunden und können Argumente haben."
    ],
    [
        "Was sind 'Datenelemente' im Kontext von Sender/Receiver-Ports?",
        "Datenelemente sind die Informationen, die über Sender/Receiver-Ports ausgetauscht werden. Sie können einfache Datentypen (Integer, Float) oder komplexe Datentypen (Array, Record) sein."
    ],
    [
        "Was ist eine Application Component?",
        "Eine Application Component ist eine atomare AUTOSAR-Softwarekomponente, die den Algorithmus implementiert. Sie ist Teil der Applikation, unabhängig von der Infrastruktur und kann auf jede ECU gemappt werden."
    ],
    [
        "Was ist eine Sensor/Actuator Component?",
        "Eine Sensor/Actuator Component bereitet I/O-Daten für die Applikation auf. Sie ist an eine ECU gebunden (Constraint für Mapping) und repräsentiert die Abhängigkeit von einem speziellen Sensor oder Aktor."
    ],
    [
        "Was ist eine Composition Component?",
        "Eine Composition Component dient der logischen Organisation oder Kapselung von anderen Softwarekomponenten (SWCs) und/oder weiteren Composition Components."
    ],
    [
        "Was ist der Zweck des Virtual Function Bus (VFB)?",
        "Der Virtual Function Bus (VFB) symbolisiert die Kommunikation zwischen Softwarekomponenten auf einer logischen Ebene, bevor die Zuordnung zu ECUs erfolgt. Er abstrahiert die Kommunikation innerhalb einer ECU sowie zwischen ECUs, sodass die Applikationssoftware unabhängig von der Hardware entwickelt werden kann."
    ],
    [
        "Nenne die zwei Hauptarten von Ports, die in den Dokumenten beschrieben werden.",
        "Die zwei Hauptarten sind Sender-Receiver Ports (für Datenfluss) und Client-Server Ports (für Kontrollfluss/Operationen)."
    ],
    [
        "Was ist ein Runnable?",
        "Ein Runnable ist eine C-Funktion, die die eigentliche Implementierung innerhalb einer atomaren Softwarekomponente enthält. Es ist die ausführbare Einheit einer Softwarekomponente."
    ],
    [
        "Wodurch können Runnables ausgelöst (getriggert) werden?",
        "Runnables können durch RTE Events (Trigger) ausgeführt werden, z.B. wenn Daten empfangen werden, ein Timer abläuft oder durch einen Funktionsaufruf."
    ],
    [
        "Was ist die Funktion von Triggern im Kontext von Runnables?",
        "Trigger (RTE Events) lösen die Ausführung von Runnables aus. Beispiele sind Datenempfang, Timerablauf oder Funktionsaufrufe."
    ],

    # --- Set 2: BSW Layers & Functional Clusters ---
    [
        "Was ist die Hauptaufgabe des Service Layers im AUTOSAR BSW?",
        "Der Service Layer ist die oberste Schicht des BSW und stellt Basisdienste für die Applikation und andere BSW-Module bereit (z.B. OS, Kommunikationsdienste, Speicherdienste, Diagnosedienste, ECU State Management)."
    ],
    [
        "Welche Funktionalität bietet der Service Layer?",
        "Er beinhaltet Funktionalitäten wie Diagnose (DEM, DCM, FIM), NVRAM Management (NvM), Watchdog Manager (WdgM), Kommunikation (Com, PduR, etc.), OS, Schedule Manager, ECU State Management (EcuM) und Com Channel Management (ComM)."
    ],
    [
        "Was ist die Hauptaufgabe des ECU Abstraction Layers?",
        "Der ECU Abstraction Layer macht höhere Software-Schichten unabhängig von der spezifischen ECU-Hardware, indem er eine API für den Zugriff auf Peripheriegeräte bereitstellt, unabhängig davon, ob diese intern oder extern am Mikrocontroller angebunden sind."
    ],
    [
        "Welche Funktionalität bietet der ECU Abstraction Layer?",
        "Er enthält Schnittstellen für interne und externe Peripherie sowie Treiber für externe Geräte. Er organisiert den I/O-Hardwarezugriff und stellt eine API dafür bereit."
    ],
    [
        "Was bedeutet MCAL und was ist seine Hauptaufgabe?",
        "MCAL steht für Microcontroller Abstraction Layer. Es ist die unterste Schicht des BSW und macht höhere Schichten unabhängig vom spezifischen Mikrocontroller, indem es Treiber mit direktem Zugriff auf den Mikrocontroller und seine internen Peripherien bereitstellt."
    ],
    [
        "Welche Art von Treibern enthält der MCAL?",
        "Der MCAL enthält Treiber mit direktem Zugriff auf den Mikrocontroller, dessen interne Peripherien und speicher-gemappte externe Geräte."
    ],
    [
        "Was sind Complex Device Drivers (CDD) und wann werden sie eingesetzt?",
        "CDD sind ein Sonderfall in der AUTOSAR-Architektur. Sie werden für die Ansteuerung spezieller Sensoren/Aktoren mit besonderen Timing-Anforderungen oder zur Integration von Nicht-AUTOSAR-Technologien eingesetzt. Sie haben direkten Zugriff auf Mikrocontroller-Ressourcen."
    ],
    [
        "Nenne Beispiele für Anwendungen von Complex Device Drivers.",
        "Beispiele sind Einspritzsteuerung oder Batteriemanagementsysteme, also zeitkritische Anwendungen."
    ],
    [
        "Was ist die Aufgabe des COM Moduls im Kommunikations-Cluster?",
        "Das COM Modul stellt eine signalbasierte Datenschnittstelle für die RTE bereit. Es packt Signale in Nachrichten (PDUs), sendet sie, managt Empfangsbenachrichtigungen, Initialwerte, Update-Bits und Timeouts auf Signalebene. Es kann auch als Signal-Gateway fungieren."
    ],
    [
        "Was macht der PDU Router (PduR)?",
        "Der PduR verteilt Kommunikationspakete (PDUs) zwischen den Bussystemen und verschiedenen BSW-Modulen (z.B. COM, TP-Module, Interface-Module). Er bietet auch Gateway-Funktionen zum Routen von PDUs zwischen Bussystemen."
    ],
    [
        "Was ist die Aufgabe von Transport Protokoll (TP) Modulen (z.B. CanTp)?",
        "TP-Module sind für die segmentierte Übertragung von Daten zuständig, wenn eine Nachricht nicht in einen einzelnen Frame/PDU des darunterliegenden Busses passt."
    ],
    [
        "Welche Funktion haben die Interface-Module (z.B. CanIf, LinIf)?",
        "Interface-Module bieten Hardware-unabhängige, aber Bus-typische Funktionen wie Queuing, Zusammenbau von Data-Link-Layer-PDUs/Frames und Tx/Rx-Triggerung."
    ],
    [
        "Welche Funktion haben die Driver-Module (z.B. CanDrv, LinDrv)?",
        "Driver-Module führen Hardware-Operationen aus, wie Initialisierung, Pufferfüllung und Implementierung von Interrupt Service Routinen (ISR)."
    ],
    [
        "Welche Funktion haben die Transceiver-Module (z.B. CanTrcv)?",
        "Transceiver-Module steuern die Hardware-Leitungstreiber (Transceiver-Chips) für den jeweiligen Bus."
    ],
     [
        "Was macht der IPDU Multiplexer (IpduM)?",
        "Das IpduM Modul unterstützt die Multiplexierung von I-PDUs, d.h. das Senden unterschiedlicher Datenlayouts innerhalb derselben PDU-ID, gesteuert durch ein Selector Field, oder das dynamische Zusammenfassen von PDUs in Container-PDUs."
    ],
    [
        "Was ist die Hauptfunktion des ECU State Managers (EcuM)?",
        "EcuM handhabt die grundlegenden Zustände der ECU (ECU-Zustandsmaschine: On, Off, Sleep), führt Zustandsübergänge durch, zentralisiert und validiert Weckereignisse und ist verantwortlich für den Startup und Shutdown des Systems, inklusive OS-Start."
    ],
    [
        "Was ist die Hauptfunktion des Communication Managers (ComM)?",
        "ComM steuert die Kommunikationszustände aller Kanäle (Bus-Startup/Shutdown) über eine abstrahierte Bus-Zustandsmaschine. Es ist die Schnittstelle zur Applikation für Kommunikationsanfragen und interagiert mit den Bus-spezifischen State Managern (BusSM) und dem Network Management."
    ],
    [
        "Was ist die Aufgabe der Network Management Module (NM If, Bus NM)?",
        "NM-Module (z.B. CanNm) handhaben das Netzwerkmanagement, um den Bus wach zu halten oder einen koordinierten Shutdown zu ermöglichen. Sie senden periodische NM-Nachrichten und können den Buslast durch Optimierungen reduzieren. NM If stellt eine einheitliche Schnittstelle zu den Bus-spezifischen NM-Modulen dar."
    ],
    [
        "Was ist die Aufgabe der Bus State Manager Module (BusSM, z.B. CanSM)?",
        "BusSM-Module übersetzen die Netzkommunikations-Modus-Anfragen von ComM und schalten entsprechend die Zustände der zugehörigen Treiber (z.B. CanDrv) und Transceiver (z.B. CanTrcv)."
    ],
    [
        "Wofür werden Memory Services in AUTOSAR benötigt?",
        "Da AUTOSAR keine dynamische Speicherallokation oder ein Dateisystem vorsieht, bieten Memory Services eine Schnittstelle zum permanenten Speichern von Daten (z.B. Diagnosedaten, Konfigurationsparameter) im nicht-flüchtigen Speicher (NVRAM)."
    ],
    [
        "Was ist die Aufgabe des NVRAM Managers (NvM)?",
        "NvM ist die Schnittstelle zur Applikation (über RTE) für den Zugriff auf den nicht-flüchtigen Speicher. Es verwaltet konfigurierte Speicherblöcke und ermöglicht deren Schreiben und Lesen über die darunterliegenden Abstraktionsschichten."
    ],
    [
        "Welche Module befinden sich in der ECU Abstraction Schicht des Memory Stacks?",
        "Die Memory Abstraction Interface (MemIf), EEPROM Abstraction (Ea) und Flash EEPROM Emulation (Fee)."
    ],
    [
        "Was ist die Aufgabe des Memory Abstraction Interface (MemIf)?",
        "MemIf leitet die Anfragen vom NvM an die passenden technologie-spezifischen Abstraktionsmodule (Ea oder Fee) weiter."
    ],
    [
        "Was ist die Aufgabe der EEPROM Abstraction (Ea) und Flash EEPROM Emulation (Fee)?",
        "Ea und Fee bieten eine Abstraktion der spezifischen Speichertechnologie (EEPROM oder Flash). Sie implementieren die Logik zum Lesen und Schreiben für die jeweilige Technologie und kommunizieren mit den darunterliegenden Treibern."
    ],
    [
        "Welche Module befinden sich in der MCAL Schicht des Memory Stacks?",
        "Hardware-spezifische Speicher-Treiber (Memory Drivers), z.B. für internes Flash (Fls) oder EEPROM (Eep) oder für externe Speicherbausteine."
    ],
    [
        "Was ist die Aufgabe des Watchdog Managers (WdgM)?",
        "WdgM überwacht die korrekte zeitliche Ausführung von Software-Entitäten (z.B. Runnables), indem es deren 'Lebenszeichen' (Alive Indications) entgegennimmt. Er leitet einen globalen Überwachungsstatus ab und triggert periodisch die Watchdog Interface (WdgIf), wenn alles in Ordnung ist."
    ],
    [
        "Was ermöglicht der Watchdog Manager (WdgM)?",
        "Er ermöglicht verschiedene Überwachungsmechanismen wie Deadline Monitoring und Lebendüberwachung (Alive Supervision)."
    ],
    [
        "Was ist die Aufgabe der Watchdog Interface (WdgIf)?",
        "WdgIf stellt eine standardisierte Schnittstelle zu den Watchdog-Treibern dar und triggert den/die Hardware-Watchdog(s) basierend auf den Anweisungen des WdgM."
    ],
    [
        "Was ist die Aufgabe des Watchdog Drivers (WdgDrv)?",
        "WdgDrv steuert den eigentlichen Hardware-Watchdog (intern oder extern) an, z.B. um dessen Timer zurückzusetzen."
    ],
    [
        "Was passiert, wenn eine überwachte Entität den WdgM nicht rechtzeitig informiert?",
        "Wenn nicht alle überwachten Entitäten rechtzeitig 'melden', informiert der WdgM die WdgIf nicht (oder meldet einen Fehler). Daraufhin wird der WdgDrv den Hardware-Watchdog nicht triggern (zurücksetzen), der Timer läuft ab und löst einen Reset der ECU aus."
    ],
    [
        "Was ist die Aufgabe des Diagnostic Event Managers (DEM)?",
        "Der DEM ist der Fehlerspeicher. Er empfängt und verarbeitet Diagnose-Events (Fehler) von BSW-Modulen und der Applikation und speichert sie persistent (oft unter Nutzung des NvM)."
    ],
    [
        "Was ist die Aufgabe des Diagnostic Communication Managers (DCM)?",
        "Der DCM implementiert Diagnosekommunikationsprotokolle (wie UDS - Unified Diagnostic Services) busunabhängig. Er wickelt die Kommunikation mit externen Diagnosegeräten ab."
    ],
    [
        "Was ist die Aufgabe des Function Inhibition Managers (FIM)?",
        "Der FIM ermöglicht es, Funktionalitäten der Applikation abhängig vom Status bestimmter diagnostischer Events (Fehler im DEM) zu sperren oder freizugeben. Die Applikation fragt den FIM nach der Erlaubnis (_Fim_GetFunctionPermission_), eine Funktion auszuführen."
    ],
    [
        "Was ist das OS Modul in AUTOSAR?",
        "Das OS Modul ist das Echtzeitbetriebssystem einer AUTOSAR ECU. Es basiert auf dem OSEK/VDX Standard und erweitert diesen um Funktionen wie Schedule Tables, Timing Protection und Memory Protection (je nach Scalability Class SC1-SC4)."
    ],
    [
        "Was sind die Hauptelemente oder Objekte des AUTOSAR OS?",
        "Tasks, Events, Alarms, Interrupts, Inter OS Communication (IOC) und Resources."
    ],
    [
        "Wofür ist das AUTOSAR OS hauptsächlich verantwortlich?",
        "Es ist verantwortlich für das Scheduling von Tasks, die Verwaltung von Events, Alarms (zeitgesteuerte Aktivierung) und Interrupts, sowie die Verwaltung von Ressourcen und die Kommunikation zwischen Tasks/ISRs."
    ],
    [
        "Warum müssen OS und RTE oft gemeinsam regeneriert werden?",
        "Da das OS eng mit der RTE verbunden ist (z.B. löst ein RTE Timer Event einen OS Alarm aus, der eine Task aktiviert), müssen bei Änderungen, die beide betreffen (z.B. Änderung eines Timings), beide neu generiert werden. Beide sind statisch konfiguriert."
    ],
    [
        "Was ist die Hauptaufgabe des I/O Hardware Abstraction (IoHwAb) Moduls?",
        "IoHwAb stellt die Verbindung zwischen der RTE (und damit den SWCs) und den I/O-Kanälen der ECU dar. Es kapselt den Zugriff auf die I/O-Treiber (wie ADC, DIO, PWM) und stellt die I/O-Signale der ECU abstrahiert zur Verfügung."
    ],
    [
        "Welche Abstraktion bietet IoHwAb?",
        "Es abstrahiert die Lokation der I/O-Peripheriegeräte (on-chip/on-board) und das Pin-Layout, aber nicht den Sensor/Aktor selbst."
    ],
    [
        "Welche Funktionalitäten kann IoHwAb neben der reinen Abstraktion bieten?",
        "Es kann auch die Aufbereitung von gelesenen Werten übernehmen, z.B. das Entprellen von digitalen Signalen (Debouncing)."
    ],
    [
        "Nenne Beispiele für I/O Treiber, die unterhalb des IoHwAb liegen.",
        "ADC (Analog-Digital-Converter), DIO (Digital Input/Output), PWM (Pulse Width Modulation). Weitere wären z.B. ICU (Input Captur Unit) oder OCU (Output Compare Unit)."
    ],

    # --- Set 3: AUTOSAR Methodology ---
    [
        "Was ist die AUTOSAR Methodik?",
        "Die AUTOSAR Methodik definiert eine Abfolge von Schritten und Aktivitäten für die Entwicklung von AUTOSAR-Systemen. Sie führt von einer Beschreibung der Soft- und Hardware bis zur Generierung einer ausführbaren Datei pro Steuergerät (ECU)."
    ],
    [
        "Was sind die Hauptziele der AUTOSAR Methodik?",
        "1. Entwicklung von Softwarefunktionalität unabhängig vom Rest des Systems.\n2. Bereitstellung einer Basis für eine standardisierte Zusammenarbeit zwischen OEM und TIER1-Zulieferern durch einheitliche Vorlagen (Templates)."
    ],
    [
        "Welche Probleme löst die AUTOSAR Methodik?",
        "Sie ermöglicht die Entwicklung von Software unabhängig von der Hardware und schafft eine standardisierte Grundlage für die Zusammenarbeit zwischen verschiedenen Partnern (OEM, Tier1), was die Wiederverwendbarkeit und Austauschbarkeit von Software fördert."
    ],
    [
        "Welches Dateiformat wird in der AUTOSAR Methodik für den Austausch von Beschreibungen verwendet und warum?",
        "Das XML-Dateiformat (.arxml) wird verwendet, um einen standardisierten und funktionierenden Austausch von Beschreibungen (z.B. System Configuration Description, ECU Extract, ECU Configuration Description) zwischen OEM und Zulieferern sicherzustellen."
    ],
    [
        "Nenne Beispiele für Beschreibungsdateien (oft im .arxml Format) in der AUTOSAR Methodik.",
        "System Configuration Description, ECU Extract (Auszug aus der Systemkonfiguration für eine ECU), ECU Configuration Description (ECUC)."
    ],
    [
        "Skizziere grob den AUTOSAR Workflow zwischen OEM und Tier1.",
        "1. OEM trifft Designentscheidungen und erstellt die System Configuration Description.\n2. OEM teilt die Systemkonfiguration auf und gibt ECU-spezifische Auszüge (ECU Extracts) an die Tier1-Zulieferer.\n3. Tier1 konfiguriert die ECU-spezifischen Details (z.B. OS, BSW) mithilfe eines ECU Configuration Generators und dem ECU Extract.\n4. Tier1 generiert die ECU Configuration Description (ECUC).\n5. Basierend auf ECUC und den SWC-Infos aus dem Extract generiert Tier1 die RTE und die BSW-Konfiguration für die spezifische ECU."
    ],
    [
        "Was ist eine ECU Configuration Description (ECUC)?",
        "Eine ECUC ist eine Beschreibungsdatei, die die Konfiguration der Basissoftware (BSW) und des RTE für eine spezifische ECU enthält. Sie wird vom Zulieferer (Tier1) mithilfe eines ECU Configuration Generators erstellt."
    ],
    [
        "Warum muss der Tier1-Zulieferer die Konfiguration (z.B. des OS) oft selbst ergänzen?",
        "Weil der ECU Extract vom OEM oft nicht alle Details enthält, die sehr Hardware- oder ECU-spezifisch sind (wie z.B. OS-Konfiguration). Diese müssen vom Zulieferer hinzugefügt werden."
    ],
    [
        "Beschreibe kurz Use Case 1 bezüglich der Aufgabenverteilung zwischen OEM und Tier1.",
        "Use Case 1: OEM kümmert sich nur um die Netzwerkkommunikation. Tier1 ist verantwortlich für die komplette Implementierung aller ECU-Funktionen (Data Mapping, Strukturierung via Compositions, Atomics, Service Components)."
    ],
    [
        "Beschreibe kurz Use Case 2 bezüglich der Aufgabenverteilung zwischen OEM und Tier1.",
        "Use Case 2: OEM definiert Kommunikation, interne Struktur (Compositions, Connectors) und Data Mapping. Tier1 implementiert die Funktionen mittels Atomics und Services."
    ],
    [
        "Beschreibe kurz Use Case 3 bezüglich der Aufgabenverteilung zwischen OEM und Tier1.",
        "Use Case 3: OEM definiert Kommunikation, Compositions, Connectors, Data Mapping UND implementiert bereits einige Funktionen mittels Atomics. Tier1 implementiert die verbleibenden Funktionen mittels Atomics und Services."
    ],
    [
        "Was ist eine Herausforderung bei den verschiedenen Use Cases in der AUTOSAR Methodik?",
        "Die klare Abgrenzung und der standardisierte Austausch der Verantwortlichkeiten und der dazugehörigen Beschreibungsartefakte (.arxml) zwischen OEM und Tier1, je nachdem, wie detailliert der OEM die Vorgaben macht."
    ],

    # --- Set 4: RTE ---
    [
        "Was sind wichtige Funktionen und Charakteristika der AUTOSAR Runtime Environment (RTE)?",
        "Die RTE konfiguriert sich selbst (z.B. Mapping von Runnables zu OS-Tasks), konfiguriert Teile des OS (Tasks, Events, Alarms), triggert Runnables über RTE Events, implementiert die Kommunikation zwischen SWCs (als Realisierung des VFB), abstrahiert das OS und BSW und verhindert direkten Zugriff von SWCs darauf."
    ],
    [
        "Welche Rolle spielt die RTE als Kommunikationsschnittstelle?",
        "Die RTE agiert als Implementierung des Virtual Function Bus (VFB) und stellt die Kommunikationsmechanismen (API-Aufrufe wie Rte_Write, Rte_Read, Rte_Call) für SWCs bereit."
    ],
    [
        "Nenne Beispiele für RTE Events, die Runnables triggern können.",
        "Init, TimingEvent, DataReceivedEvent (S/R), DataReceiveErrorEvent (S/R), DataSendCompletedEvent (S/R), OperationInvokedEvent (C/S), AsynchronousServerCallReturnsEvent (C/S), ModeSwitchEvent, ModeSwitchAckEvent, ExternalTriggerOccurredEvent, InternalTriggerOccurredEvent, BackgroundEvent."
    ],
    [
        "Wie unterscheidet sich die Kommunikation aus Sicht der RTE/des SWC-Codes bei Inter-ECU vs. Intra-ECU Kommunikation?",
        "Aus Sicht des SWC-Codes gibt es keinen Unterschied. Die RTE abstrahiert die Kommunikationspfade. Der SWC verwendet immer dieselben RTE-API-Aufrufe (z.B. Rte_Write, Rte_Read). Die RTE leitet die Aufrufe entweder direkt an ein anderes Runnable (Intra-ECU) oder an das BSW (z.B. Com-Modul für Inter-ECU) weiter."
    ],
    [
        "Was ist eine Exclusive Area (EA)?",
        "Eine Exclusive Area erlaubt es, atomare Abschnitte im Code zu definieren, um Race Conditions zu verhindern, wenn Runnables derselben Komponente auf unterschiedlichen Tasks laufen und auf gemeinsame Ressourcen zugreifen könnten. Die Implementierung ist konfigurierbar (z.B. Interrupt Lock, OS Resource)."
    ],
    [
        "Was ist eine Inter Runnable Variable (IRV)?",
        "Eine IRV ist eine Variable, die die Kommunikation zwischen zwei Runnables derselben Softwarekomponente ermöglicht. Die RTE stellt eine Interrupt-sichere Zugriffs-API dafür bereit."
    ],
    [
        "Beschreibe die 'Direct Communication' bei Sender/Receiver.",
        "Direkte Kommunikation: Die RTE stellt einen Puffer bereit. Jeder Schreibvorgang überschreibt den Puffer vollständig (Last-is-best Semantik). Nur die zuletzt geschriebenen Daten sind verfügbar."
    ],
    [
        "Beschreibe die 'Buffered Communication' bei Sender/Receiver.",
        "Gepufferte Kommunikation: Ein Runnable schreibt während seiner Ausführung in einen exklusiven 'Shadow Buffer'. Erst am Ende der Ausführung werden die Daten aus dem Shadow Buffer in den eigentlichen RTE-Puffer kopiert."
    ],
    [
        "Beschreibe die 'Queued Communication' bei Sender/Receiver.",
        "Queued Kommunikation: Die RTE verwendet eine FIFO-Queue. Jeder Schreibvorgang fügt ein Element zur Queue hinzu, jeder Lesevorgang entfernt ein Element. Keine Last-is-best Semantik."
    ],
    [
        "Was ist ein 'AUTOSAR Interface'?",
        "Ein Interface, das mit generischen AUTOSAR-Mitteln beschrieben wird, dessen Semantik aber NICHT im AUTOSAR-Standard vorgeschrieben ist. Wird von SWCs und der ECU Abstraction verwendet. Kommunikation erfolgt über Ports (z.B. Rte_Write_<p>_<d> oder Rte_Call_<p>_<o>)."
    ],
    [
        "Was ist ein 'Standardized Interface'?",
        "Ein Interface, dessen Semantik im AUTOSAR-Standard vorgeschrieben ist, das aber NICHT mit generischen AUTOSAR-Mitteln (Ports) beschrieben wird. Beispiel: Direkte Aufrufe von BSW-Modulen wie EcuM (z.B. Rte_Start(), Rte_Stop() - Hinweis: Diese könnten auch als Standardized AUTOSAR Interfaces gelten, die Unterscheidung ist manchmal unscharf)."
    ],
    [
        "Was ist ein 'Standardized AUTOSAR Interface'?",
        "Ein Interface, das mit generischen AUTOSAR-Mitteln (Service Ports) beschrieben wird UND dessen Semantik im AUTOSAR-Standard vorgeschrieben ist. Wird exklusiv für die Dienste der Basissoftware (BSW) verwendet (z.B. Zugriff auf DEM über Rte_Call_<port>_SetEventStatus)."
    ]
]
# Du kannst diese Liste nun kopieren. Jede Karte ist jetzt eine Liste mit zwei Elementen:
# dem Text für die Vorderseite und dem Text für die Rückseite.
# print(cards) # Optional: Zum Anzeigen der Karten

erstelle_anki_karten(cards, "AUTOSARSection1")
