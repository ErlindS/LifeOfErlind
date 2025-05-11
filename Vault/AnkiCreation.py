import genanki

def erstelle_anki_karten(karten_liste, deck_name="Tensorflow1", deck_id=1234567890):
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

# Beispiel-Input
cards2 = [
  ['Wer begann 1991 mit der Entwicklung von Linux?', 'Linus Torvalds. [Source 1]'],
  ['Auf welcher Grundlage entwickelte Linus Torvalds Linux?', 'Auf dem MINIX-Clone (Unix-Derivat) von Tannenbaum. [Source 2]'],
  ['Welche Lizenz verwendete Torvalds für Linux?', 'Die GNU General Public Licence (GPL), was die freie Nutzung ermöglichte. [Source 1]'],
  ['In welcher Programmiersprache ist Linux hauptsächlich entwickelt?', 'In C, ähnlich wie Unix. [Source 3]'],
  ['Nach welchem Standard ist Linux zertifiziert?', 'POSIX 1003.1a. [Source 3]'],
  ['Welche weiteren Unix-Systemaufrufe realisiert Linux?', 'Systemaufrufe von SVID Rel. 4 und BSD-Unix. [Source 4]'],
  ['Was sind Linux-Distributionen?', 'Verschiedene Zusammenstellungen von Software, die auf dem Linux-Kernel aufsetzen (z.B. Debian, RedHat, SUSE, Ubuntu, Android). [Source 5, 6]'],
  ['Was ist die primäre Aufgabe eines Betriebssystems?', 'Die Abstraktion der Hardware, sodass Anwendungsprogrammierer keine direkten Hardware-Kenntnisse benötigen. [Source 8]'],
  ['Was ist der Unterschied zwischen "Bare-metal" und "OS-based" Systemen?', 'Bare-metal: Anwendung läuft direkt auf der Hardware. OS-based: Ein Betriebssystem abstrahiert die Hardware für die Anwendung. [Source 10]'],
  ['Welche Hauptkomponenten gehören zur Architektur eines typischen Betriebssystems?', 'Kernel (mit Prozess-, Speicher-, I/O-Management, Gerätetreibern), Systemcall-Interface, Service-Bibliotheken und Applikationen im Userland. [Source 10]'],
  ['Was implementiert das Systemcall-Interface?', 'Die API-Funktionen (Systemcalls), die den Übergang von Anwendungen in den Kernel ermöglichen. [Source 11]'],
  ['Wie greift eine Applikation auf Hardware-Ressourcen zu?', 'Über Systemcalls (Systemaufrufe), die vom Betriebssystem bereitgestellt werden. [Source 12]'],
  ['Was ist der Unterschied zwischen User-Modus und Kernel-Modus?', 'Kernel-Modus: privilegierter Modus mit vollem Zugriff. User-Modus: nicht-privilegierter Modus mit Einschränkungen. [Source 14]'],
  ['Welche Einschränkungen gelten typischerweise im User-Modus?', 'Bestimmte Prozessorbefehle sind nicht verfügbar und es ist nur ein Teil des Adressraums zugänglich (gesteuert durch MMU-Seitentabellen). [Source 15, 16]'],
  ['Was ist ein Prozess (Task)?', 'Die Ablaufumgebung eines Programms, die vom Betriebssystem bereitgestellt wird; ein Programm zur Laufzeit. [Source 18, 20]'],
  ['Was versteht man unter dem Prozess-Kontext?', 'Alle Informationen, die den Zustand eines Prozesses beschreiben (Programmcode, Daten, Stack, Registerinhalte/Hardware-Kontext, geöffnete Dateien etc.). [Source 22]'],
  ['Was passiert bei einem Kontextwechsel (Context Switching)?', 'Der Hardware-Kontext (Register etc.) des aktuellen Prozesses wird gesichert und der des nächsten Prozesses wird geladen. [Source 23]'],
  ['In welche Segmente wird der Adressraum eines Prozesses typischerweise unterteilt?', 'Codesegment (Programm), Stacksegment (lokale Variablen, Rücksprungadressen), Datensegment (globale/statische Variablen), Heap (dynamisch allokierter Speicher). [Source 24, 25]'],
  ['Was ist ein Prozesskontrollblock (PCB oder TCB)?', 'Ein Eintrag in der Prozesstabelle des Betriebssystems, der alle wichtigen Verwaltungsinformationen über einen Prozess enthält. [Source 28]'],
  ['Welche Informationen enthält ein PCB typischerweise?', 'Informationen über Code-, Daten-, Stacksegment, Speicherort des Kontexts, Prozesszustand, Priorität, Prozess-ID (PID), Eltern-Prozess-ID (PPID). [Source 29, 30, 31]'],
  ['Welche besondere Rolle spielt der Prozess mit PID 1 unter Unix/Linux?', 'Es ist der Init-Prozess, der vom Kernel nach dem Booten gestartet wird und der (direkte oder indirekte) Elternprozess aller anderen Prozesse ist. [Source 32, 33]'],
  ['Was sind Threads (Leichtgewichtige Prozesse / LWP)?', 'Ausführungsfäden innerhalb eines Prozesses, die sich Ressourcen wie den Adressraum teilen, aber einen eigenen Ausführungskontext (inkl. Stack) haben. [Source 36, 37, 38, 39]'],
  ['Was teilen sich Threads desselben Prozesses?', 'Den Adressraum (Code-, Daten-, Heap-Segment), offene Dateien und Netzwerkverbindungen. [Source 37]'],
  ['Was hat jeder Thread eines Prozesses eigenständig?', 'Ein eigenes Stacksegment und einen eigenen Threadkontext (inkl. CPU-Register). [Source 38, 39]'],
  ['Was sind die drei grundlegenden Zustände eines Prozesses im Prozesslebenszyklus?', 'Aktiv (laufend), Bereit (lauffähig, wartet auf CPU), Blockiert (wartet auf ein Ereignis, z.B. I/O). [Source 46]'],
  ['Welche Unterscheidung gibt es beim Zustand "Blockiert" (Schlafen) in Linux?', 'Unterbrechbar (TASK_INTERRUPTIBLE) und nicht-unterbrechbar (TASK_UNINTERRUPTIBLE). [Source 48]'],
  ['Was bedeutet Nebenläufigkeit (Concurrency) von Prozessen?', 'Mehrere Prozesse sind gleichzeitig im System aktiv und teilen sich die verfügbare(n) CPU(s), was zu einer quasi-parallelen Ausführung führt. [Source 51]'],
  ['Was ist eine Race Condition (Wettlaufsituation)?', 'Ein Fehlerzustand, der auftritt, wenn das Ergebnis einer Operation von der unvorhersehbaren Reihenfolge oder dem Timing anderer Ereignisse abhängt (z.B. beim Zugriff mehrerer Prozesse auf geteilte Daten). [Source 52]'],
  ['Was ist ein kritischer Abschnitt (Critical Section)?', 'Ein Codeabschnitt, der auf gemeinsame Ressourcen zugreift und der zu einem Zeitpunkt nur von einem Thread/Prozess ausgeführt werden darf, um Race Conditions zu vermeiden. [Source 60]'],
  ['Was sind die Grundideen hinter dem Konzept des virtuellen Speichers?', '1. Prozess kann laufen, auch wenn nur Teile im Hauptspeicher sind.\n2. Speicherbedarf kann größer als phys. Speicher sein.\n3. Programmierer sieht kontinuierlichen Adressraum (ab 0). [Source 62, 64, 65]'],
  ['Was ist Swapping?', 'Das Auslagern von Speicherbereichen (ganzer Prozesse oder Teile davon) aus dem Hauptspeicher auf einen Sekundärspeicher (z.B. Festplatte), um Hauptspeicher freizugeben. [Source 68, 69]'],
  ['Was ist der Unterschied zwischen Swapping und Paging?', 'Swapping bezieht sich auf das Auslagern von Speicherbereichen. Paging ist der Mechanismus der virtuellen Adressierung, der virtuelle Adressen auf physische abbildet (oft seitenweise). Paging *ermöglicht* effizientes Swapping von einzelnen Seiten (Demand Paging). [Source 72, 73]'],
  ['Wer entwickelte das Konzept des virtuellen Speichers?', 'Fritz-Rudolf Güntsch (1956 an der TU Berlin). [Source 76]'],
  ['Unterscheide virtuelle und physikalische Adressen.', 'Virtuelle Adresse: Adresse aus Sicht des Programms/Prozesses. Physikalische Adresse: Adresse, die tatsächlich an den Speicherbus angelegt wird. Die MMU übersetzt virtuelle in physikalische Adressen. [Source 79, 87]'],
  ['Was sind Seiten (Pages) und Seitenrahmen (Page Frames)?', 'Pages: Blöcke fester Größe im virtuellen Adressraum. Page Frames: Blöcke fester Größe im physikalischen Hauptspeicher, in die Pages geladen werden können. [Source 81, 82]'],
  ['Was ist eine typische Seitengröße in 32-Bit-Systemen und warum ist die Größe ein Kompromiss?', 'Typisch 4 kByte. Kompromiss: Zu kleine Seiten -> hohe Verwaltungs-Overhead, viele I/O-Operationen. Zu große Seiten -> interne Fragmentierung (Speicherverschwendung innerhalb einer Seite). [Source 83, 84]'],
  ['Wie unterstützt die virtuelle Adressierung den Speicherschutz?', 'Die Seitentabellen enthalten Zugriffsrechte (Lesen, Schreiben, Ausführen) pro Seite. Die MMU prüft diese bei jedem Zugriff und löst bei Verletzung einen Fehler (Interrupt) aus. [Source 88, 89, 90]'],
  ['Was ist ein Page Fault?', 'Ein Interrupt, der von der MMU ausgelöst wird, wenn auf eine virtuelle Adresse zugegriffen wird, deren Seite sich aktuell nicht im Hauptspeicher befindet (oder der Zugriff ungültig ist). Das OS muss die Seite dann laden (Demand Paging). [Source 93, 90]'],
  ['Warum verwendet man mehrstufige Seitentabellen (Multi-Level Paging)?', 'Um den Speicherbedarf für die Seitentabellen selbst zu reduzieren, insbesondere bei großen Adressräumen. Eine lineare Tabelle wäre riesig. [Source 95, 96, 97]'],
  ['Wie viele Stufen von Seitentabellen verwendet Linux standardmäßig (seit Kernel 2.6.11)?', 'Vierstufige Seitentabellen. [Source 101]'],
  ['Was ist ein Systemcall (Systemaufruf)?', 'Ein Dienstaufruf einer Anwendung an das Betriebssystem, um privilegierte Operationen auszuführen (z.B. I/O, Prozessmanagement). Dabei wird in den Kernel-Modus gewechselt. [Source 109, 110]'],
  ['Nenne Beispiele für typische Systemcalls unter Linux.', '`fork` (Prozess erzeugen), `exit` (Prozess beenden), `open`/`close` (Datei öffnen/schließen), `read`/`write` (Datei lesen/schreiben). [Source 114]'],
  ['Was ist ein Trap im Kontext von Systemcalls?', 'Ein Software-Interrupt, der den kontrollierten Übergang vom User-Modus in den Kernel-Modus auslöst, um einen Systemdienst auszuführen. Die Anwendung übergibt dabei meist eine Nummer für den gewünschten Dienst. [Source 115, 122]'],
  ['Warum ist ein Systemcall deutlich langsamer als ein normaler Funktionsaufruf?', 'Weil ein Moduswechsel (User->Kernel), ein Kontextwechsel (Sichern/Laden von Registern, evtl. MMU-Anpassung) und die Ausführung im privilegierten Modus erforderlich sind. [Source 127, 128, 129]'],
  ['Was sind die Hauptaufgaben des I/O-Managements?', '1. Schnittstelle zur Hardware-Integration bereitstellen.\n2. Einheitliche API für Peripherie-Zugriff bieten.\n3. Ordnungsstrukturen für Daten (Dateisysteme) realisieren. [Source 139]'],
  ['Was ist ein Gerätetreiber?', 'Kernelspezifischer Code, der die Ansteuerung eines bestimmten Hardware-Geräts oder Gerätetyps ermöglicht. Läuft typischerweise im Kernel-Modus. [Source 138, 185]'],
  ['Was ist ein Dateisystem (File System)?', 'Der Teil des Betriebssystems, der sich mit der Organisation, Speicherung und Verwaltung von Dateien auf Speichermedien befasst. Oft hierarchisch (Verzeichnisbaum). [Source 142, 144]'],
  ['Was ist die Wurzel (Root) des Dateisystems unter Unix/Linux?', 'Das oberste Verzeichnis im systemweiten Verzeichnisbaum, bezeichnet mit `/`. [Source 148]'],
  ['Was ist ein Inode?', 'Eine Datenstruktur in Unix-artigen Dateisystemen, die Metadaten über eine Datei (Typ, Rechte, Größe, Zeitstempel) enthält und auf die Datenblöcke der Datei verweist. Jeder Inode hat eine eindeutige Nummer. [Source 154, 155, 157]'],
  ['Was ist Journaling in Dateisystemen (z.B. ext3, ext4)?', 'Ein Mechanismus, bei dem Änderungen am Dateisystem zuerst in einem Protokoll (Journal) festgehalten werden, bevor sie tatsächlich durchgeführt werden. Dies erhöht die Robustheit gegen Systemabstürze. [Source 161, 162]'],
  ['Was ist das Virtuelle Dateisystem (VFS) in Linux?', 'Eine Abstraktionsschicht im Kernel, die eine einheitliche Schnittstelle (API) für Anwendungen zu verschiedenen konkreten Dateisystemtypen (ext4, FAT, NFS etc.) bietet. [Source 163]'],
  ['Was sind virtuelle Dateisysteme wie `/proc` und `/sys`?', 'Dateisysteme, die nicht auf einem physischen Datenträger liegen, sondern als Schnittstelle zum Kernel dienen, um Informationen abzufragen oder Kernel-Parameter zu ändern. [Source 166]'],
  ['Wozu dient das `/proc`-Dateisystem (procfs)?', 'Zur Bereitstellung von Informationen über laufende Prozesse und Kernel-Subsysteme (Speicher, Peripherie etc.) und teilweise zur Steuerung des Kernels. [Source 167, 168]'],
  ['Wozu dient das `/sys`-Dateisystem (sysfs)?', 'Zur Darstellung der Kernel-Sicht auf Geräte und Treiber in einer hierarchischen Struktur, ermöglicht Abfrage und Konfiguration von Kernelobjekten aus dem Userspace. [Source 170, 171]'],
  ['Welche Rolle spielt der `udev`-Dämon?', 'Er überwacht Kernel-Events (via netlink, oft ausgelöst durch Änderungen in `sysfs`) und erstellt/löscht dynamisch Gerätedateien im `/dev`-Verzeichnis, wenn Geräte hinzugefügt/entfernt werden. [Source 175, 176, 177]'],
  ['Was bedeutet der Grundsatz "Everything is a file" in Unix/Linux?', 'Die Idee, dass auf viele Systemressourcen, einschließlich Hardware-Geräte, über das Dateisystem-Interface (Gerätedateien in `/dev`) zugegriffen werden kann. [Source 178]'],
  ['Welche Hauptklassen von Geräten unterscheidet Linux?', '1. Zeichengeräte (char devices, z.B. serielle Schnittstelle, Terminal)\n2. Blockgeräte (block devices, z.B. Festplatte, USB-Stick)\n3. Netzwerkschnittstellen (networking devices). [Source 181]'],
  ['Was kennzeichnet einen monolithischen Kernel?', 'Alle wesentlichen Betriebssystemdienste (Speicherverwaltung, Prozessverwaltung, Treiber etc.) laufen im selben Adressraum im privilegierten Kernel-Modus. [Source 194]'],
  ['Welche Nachteile hat ein monolithischer Kernel für die Treiberentwicklung?', '1. Fehler im Treiber können das gesamte System zum Absturz bringen.\n2. Traditionell muss der Kernel für neue/geänderte Treiber neu übersetzt und gestartet werden. [Source 195, 196]'],
  ['Wie löst Linux das Problem des Kernel-Neustarts bei Treiberänderungen?', 'Durch das Konzept der ladbaren Kernelmodule (.ko-Dateien), die zur Laufzeit in den Kernel geladen und wieder entfernt werden können. [Source 197, 200]'],
  ['Unterscheide Built-in-Treiber und Modul-Treiber.', 'Built-in-Treiber sind fest in das Kernel-Image einkompiliert. Modul-Treiber liegen als separate Dateien vor und können dynamisch geladen/entladen werden. [Source 198, 200]'],
  ['Warum muss ein Kernelmodul normalerweise genau zur laufenden Kernelversion passen?', 'Weil es die interne API (Funktionen, Datenstrukturen) des Kernels nutzt, die sich zwischen Versionen ändern kann. Das Modul wird gegen die Header der Ziel-Kernelversion kompiliert. [Source 201, 203, 204, 205]'],
  ['Welche drei Arten von Funktionen enthält ein typisches Kernelmodul/Treiber?', '1. Management-Funktionen (Initialisierung/Aufräumen beim Laden/Entladen).\n2. Applikations-getriggerte Funktionen (Reaktion auf Systemcalls wie open, read, write).\n3. Hardware-Interrupt-getriggerte Funktionen (Interrupt Service Routinen). [Source 206, 207]'],
  ['Welche drei Abarbeitungskontexte unterscheidet Linux prinzipiell?', '1. User-Kontext (Applikation läuft).\n2. Prozess-Kontext (Kernel führt Code im Auftrag einer Applikation aus, z.B. nach Systemcall).\n3. Interrupt-Kontext (Kernel behandelt einen Hardware- oder Software-Interrupt). [Source 209]'],
  ['Was ist im Prozess-Kontext möglich, was im User-Kontext nicht geht?', 'Zugriff auf Kernel-Datenstrukturen und -Funktionen, privilegierte Instruktionen, direkter Hardware-Zugriff (über Treiber). Es besteht noch ein Bezug zum aufrufenden Prozess (`current`). [Source 211, 212]'],
  ['Was ist im Interrupt-Kontext *nicht* möglich oder erlaubt?', 'Zugriff auf den Speicher des User-Prozesses, Aufruf von Funktionen, die schlafen legen (blockieren) könnten. Der Code sollte möglichst schnell ablaufen. [Source 214, 217, 218, 239]'],
  ['Welche Ebenen des Unterbrechungsmodells gibt es in Linux (von unten/höchste Priorität nach oben/niedrigste Priorität)?', '1. ISR-Ebene (Hard-IRQ)\n2. Soft-IRQ-Ebene (Softirqs, Tasklets, Timer)\n3. Kernel-Ebene (Prozesskontext)\n4. User-Ebene (Applikationen). [Source 219-231]'],
  ['Was besagt das Schichtenmodell der Unterbrechbarkeit?', 'Code auf einer bestimmten Ebene kann nur von Code auf einer darunterliegenden (höher priorisierten) Ebene unterbrochen werden. [Source 221]'],
  ['Welche Arbeiten werden typischerweise auf die Soft-IRQ-Ebene verschoben?', 'Arbeiten, die durch einen Interrupt ausgelöst wurden, aber nicht sofort in der ISR erledigt werden müssen (zu zeitaufwändig) und nicht blockieren. [Source 227, 228]'],
  ['Kann eine Applikation direkt auf den Kernelspace zugreifen?', 'Nein, auch nicht mit Superuser-Rechten. Der Zugriff erfolgt kontrolliert über das Systemcall-Interface. [Source 239]'],
  ['Kann der Kernel im Prozesskontext auf den Userspace des aufrufenden Prozesses zugreifen?', 'Ja, der Kernel kennt die Seitentabellen des Prozesses und kann spezielle Funktionen (z.B. `copy_to_user`, `copy_from_user`) für den Datentransfer nutzen. [Source 213, 234]'],
  ['Kann der Kernel im Interruptkontext auf den Userspace zugreifen?', 'Nein, im Interruptkontext gibt es keinen Bezug zu einem bestimmten Prozess und dessen Adressraum. [Source 214, 239]']
]

cards = [
  ["Was ist ein Tensor in TensorFlow?", "Ein Tensor ist eine mehrdimensionale Datenstruktur, die in TensorFlow verwendet wird. Man kann ihn sich als einen mehrdimensionalen Array vorstellen, der einen einheitlichen Datentyp (dtype) hat. Ein Tensor kann 0 Dimensionen (Skalar), 1 Dimension (Vektor), 2 Dimensionen (Matrix) oder mehr haben."],
  ["Wie erstellt man einen nicht veränderbaren (konstanten) Tensor in TensorFlow und was sind seine Eigenschaften?", "Einen konstanten Tensor erstellt man mit `tf.constant()`. Dieser Tensor kann nach seiner Erstellung nicht mehr modifiziert werden. Wichtige Parameter bei der Erstellung sind der Wert (`value`), der Datentyp (`dtype`) und die Form (`shape`)."],
  ["Erkläre die Tensor-Dimensionen: Skalar, Vektor, Matrix.", "Ein **Skalar** ist ein Tensor der Dimension 0 (eine einzelne Zahl).\nEin **Vektor** ist ein Tensor der Dimension 1 (ein Array von Zahlen).\nEine **Matrix** ist ein Tensor der Dimension 2 (ein zweidimensionaler Array).\nGenerell ist ein Tensor ein n-dimensionaler Array."],
  ["Was gibt der Parameter `dtype` bei TensorFlow-Tensoren an?", "Der Parameter `dtype` (Datentyp) spezifiziert den Typ der Daten, die im Tensor enthalten sind. Beispiele hierfür sind `tf.float32` für 32-Bit-Gleitkommazahlen oder `tf.int32` für 32-Bit-Integer. TensorFlow unterstützt verschiedene Datentypen, die mit `tf.dtypes.DType` eingesehen werden können."],
  ["Was definiert der Parameter `shape` bei TensorFlow-Tensoren?", "Der Parameter `shape` definiert die Anzahl und Größe der Dimensionen des Tensors. Zum Beispiel bedeutet `shape=(2, 2)`, dass der Tensor zwei Dimensionen hat, jede mit der Größe 2. `shape=(1,1,4)` bedeutet drei Dimensionen mit den Größen 1, 1 und 4. Die Form kann auch dazu dienen, die Eingabedaten zu validieren und die Berechnungen im Graph zu optimieren."],
  ["Wie erstellt man einen veränderbaren Tensor in TensorFlow und wie kann dessen Inhalt geändert werden?", "Einen veränderbaren Tensor erstellt man mit `tf.Variable()`, wobei ein initialer Wert angegeben werden muss. Der Inhalt eines `tf.Variable` kann mit der Methode `assign()` geändert werden. Dies ist ein Hauptunterschied zu `tf.constant`, dessen Werte nicht änderbar sind."],
  ["Was ist der Zweck der `assign()` Methode für `tf.Variable`?", "Die Methode `assign()` wird verwendet, um einem `tf.Variable` neue Werte zuzuweisen, ohne ein neues Tensor-Objekt zu erstellen. Dies ist nützlich in Szenarien wie dem maschinellen Lernen, wo Gewichte oder Parameter während des Trainingsprozesses aktualisiert werden müssen."],
  ["Wie kann man in TensorFlow Tensoren mit zufälligen Werten aus einer Normalverteilung erstellen?", "Man kann `tf.random.normal()` verwenden. Diese Funktion erstellt einen Tensor mit der angegebenen Form (`shape`), gefüllt mit Werten aus einer Normalverteilung. Man kann den Mittelwert (`mean`) und die Standardabweichung (`stddev`) der Verteilung spezifizieren."],
  ["Wozu dient `tf.random.Generator.from_seed()` in TensorFlow?", "`tf.random.Generator.from_seed()` erstellt einen Zufallszahlengenerator, der mit einem bestimmten Seed initialisiert wird. Dies stellt sicher, dass die generierten Zufallszahlen reproduzierbar sind, wenn derselbe Seed verwendet wird. Dieser Generator kann dann Methoden wie `normal()` oder `uniform()` aufrufen."],
  ["Wie funktioniert die Methode `random.normal()` eines TensorFlow-Zufallszahlengenerators?", "Die Methode `random.normal()` (aufgerufen auf einem `tf.random.Generator` Objekt) generiert einen Tensor mit Werten, die aus einer Normalverteilung (Gaußschen Verteilung) mit einem spezifizierbaren Mittelwert und einer Standardabweichung gezogen werden. Die Form des Tensors wird ebenfalls als Parameter übergeben."],
  ["Wie funktioniert die Methode `random.uniform()` eines TensorFlow-Zufallszahlengenerators?", "Die Methode `random.uniform()` (aufgerufen auf einem `tf.random.Generator` Objekt) generiert einen Tensor mit Werten, die aus einer Gleichverteilung über ein spezifiziertes Intervall [minval, maxval) gezogen werden. Die Form des Tensors und optional der Datentyp können ebenfalls angegeben werden."],
  ["Was bewirkt `tf.random.shuffle()` in TensorFlow und welche Rolle spielt der Seed?", "`tf.random.shuffle()` mischt einen Tensor zufällig entlang seiner ersten Dimension. Wenn ein `seed` (Seed-Wert) angegeben wird, führt das Mischen bei wiederholter Ausführung mit demselben Tensor und demselben Seed immer zum selben Ergebnis, was für Reproduzierbarkeit wichtig ist."],
  ["Erkläre den Unterschied zwischen globalen und operationalen Seeds in TensorFlow.", "**Globaler Seed:** Wird mit `tf.random.set_seed()` gesetzt und beeinflusst alle nachfolgenden Zufallsoperationen in TensorFlow. Er hilft, die Ergebnisse über mehrere Programmläufe hinweg reproduzierbar zu machen.\n**Operationaler Seed:** Wird direkt als Parameter an eine spezifische Zufallsoperation übergeben (z.B. `tf.random.uniform(..., seed=42)`). Er steuert die Zufälligkeit nur für diese spezielle Operation. Wenn sowohl ein globaler als auch ein operationaler Seed gesetzt sind, werden beide kombiniert, um die Zufallszahlen zu generieren, wobei dies die beste Methode für reproduzierbare Zufälligkeit ist."],
  ["Wie erstellt man mit TensorFlow Tensoren, die nur Einsen (`tf.ones()`), nur Nullen (`tf.zeros()`) oder eine Identitätsmatrix (`tf.eye()`) enthalten?", "`tf.ones(shape, dtype=tf.float32)`: Erstellt einen Tensor mit der angegebenen Form (`shape`), bei dem alle Elemente 1 sind.\n`tf.zeros(shape, dtype=tf.float32)`: Erstellt einen Tensor mit der angegebenen Form (`shape`), bei dem alle Elemente 0 sind.\n`tf.eye(num_rows, num_columns=None, batch_shape=None, dtype=tf.float32)`: Erstellt eine Identitätsmatrix (oder einen Batch von Identitätsmatrizen). Die Diagonalelemente sind 1, alle anderen 0."],
  ["Welche wichtigen Attribute hat ein Tensor in TensorFlow und wie greift man darauf zu?", "Wichtige Attribute eines Tensors sind:\n- `tensor.shape`: Gibt die Form (Dimensionen) des Tensors als `tf.TensorShape` zurück.\n- `tensor.ndim`: Gibt die Anzahl der Dimensionen (Rang) des Tensors als Integer zurück.\n- `tf.size(tensor)`: Gibt die Gesamtzahl der Elemente im Tensor als `tf.Tensor` zurück.\n- `tensor.dtype`: Gibt den Datentyp der Elemente im Tensor als `tf.DType` zurück."],
  ["Wie funktioniert das Indexieren und Slicing von Tensoren in TensorFlow?", "Ähnlich wie bei Python-Listen oder NumPy-Arrays kann man auf Elemente oder Bereiche (Slices) eines Tensors zugreifen. Die Syntax ist typischerweise `tensor[start:stop:step]`.\n- `start`: Der Startindex des Slice (inklusiv).\n- `stop`: Der Endindex des Slice (exklusiv).\n- `step`: Die Schrittweite.\nNegative Indizes zählen vom Ende des Tensors. TensorFlow bietet auch spezialisierte Operationen wie `tf.slice`, `tf.gather` für komplexere Indexierungsaufgaben."]
]

# Du kannst diese Liste nun kopieren. Jede Karte ist jetzt eine Liste mit zwei Elementen:
# dem Text für die Vorderseite und dem Text für die Rückseite.
# print(cards) # Optional: Zum Anzeigen der Karten

erstelle_anki_karten(cards, "Tensorflow1")
