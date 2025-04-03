## Git-Kommandos

Dir steht eine große Zahl von Git-Befehlen im Sandkasten-Modus zur Verfügung. Unter anderem

- commit
- branch
- checkout
- cherry-pick
- reset
- revert
- rebase
- merge


# Introduction 

## Commits
Ein Commit in einem Git-Repository speichert eine Abbildung aller Dateien in deinem Projektverzeichnis. Es ist wie ein riesiges Kopieren und Einfügen, nur besser.

Allerdings will Git die Commits so schlank wie möglich halten, also kopiert es nicht einfach stur das ganze Verzeichnis jedes Mal wenn du committest. Es kann (wenn möglich) Commits als Menge von Änderungen zusammenpacken, von einer Version des Repositorys zur nächsten.

Außerdem führt Git ein Protokoll darüber, welche Commits wann gemacht wurden, und welcher auf welchen folgt. Deshalb werden die Commits hier mit ihrem Vorgänger über sich gezeigt -- wir verwenden Pfeile zur Darstellung der Beziehung. Dieses Protokoll zu haben ist eine tolle Sache für jeden, der an einem Projekt arbeitet.

### Commands

'''
git commit 
git commit -m "This is a message"
'''
## Branches
Branches sind in Git extrem schlank. Sie sind einfach Verweise auf einen bestimmten Commit -- das ist alles. Es ist unter Git-Enthusiasten deshalb gängige Praxis, früh und oft Branches anzulegen.

Da das Anlegen von Branches keinen Plattenplatz und Speicher verbraucht, liegt es nahe die Arbeit in kleine logische Häppchen aufzuteilen, anstatt mit wenigen großen, monolithischen Branches zu hantieren.

Wir werden sehen wie Commits und Branches zusammengehören, sobald wir anfangen mit beiden zu arbeiten. Bis hierhin merk dir einfach, dass ein Branch im Prinzip bedeutet "ich möchte die Arbeit, die in diesem Commit und seinen Vorgängern steckt, sichern".

## Merge
Die einfachste Methode, mit der man Branches zusammenführen kann, ist `git merge`. Das Mergen erzeugt in git einen speziellen Commit, der zwei Vorgänger hat. Ein solcher Commit bedeutet im Prinzip "ich möchte alle Arbeit von dem Vorgänger hier und dem dort _und_ allen ihren jeweiligen Vorgängern miteinander kombinieren".

## Rebase

Der zweite Weg um Inhalte aus verschiedenen Branches zu kombinieren ist `git rebase`. Rebasen nimmt im Prinzip eine Menge von Commits, "kopiert" sie und packt sie auf etwas anderes drauf.

Auch wenn das erst mal komisch klingt, liegt der Vorteil von Rebase darin, dass man es benutzen kann um hübsch lineare Abfolgen von Commits zu erhalten. Das Commit-Protokoll des Repositorys wird durch Rebase eine ganze Ecke einfacher aussehen, weil Merge Commits vermieden werden.