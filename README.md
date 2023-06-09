# Pre-Commit-Basics

In diesem Repository befinden sich einige Dateien und Skripte, die für das Projekt und die Verwendung von Pre-Commit Hooks relevant sind.

## Dateistruktur

- **.pre-commit-config.yaml**: Diese Datei enthält die Konfiguration für die Pre-Commit Hooks, die automatisch vor jedem Commit ausgeführt werden. Die Hooks umfassen unter anderem das Überprüfen von YAML-Syntax, das Entfernen von überflüssigen Leerzeichen und das Formatieren von Python-Code.

- **script.py**: Dies ist ein Python-Skript, das im Rahmen des Projekts verwendet wird. Es enthält den Hauptcode für die Anwendung oder das Skript, das Sie entwickeln.

- **scripts** (Ordner): Dieser Ordner enthält zusätzliche Skripte, die von den Pre-Commit Hooks oder dem Hauptprojekt verwendet werden. Zum Beispiel enthält er das Skript `check_file_size.py`, das von einem der Pre-Commit Hooks verwendet wird, um die Größe der geänderten Dateien zu überprüfen.

## Verwendung

Um die Pre-Commit Hooks zu verwenden, stelle sicher, dass die notwendigen Abhängigkeiten installiert sind:

```bash
pip install pre-commit

```

Installiere anschließend die Pre-Commit Hooks:

```bash
pre-commit install
```

Nun werden die Hooks jedes Mal ausgeführt, wenn du versuchst, einen Commit durchzuführen. Wenn einer der Hooks fehlschlägt, wird der Commit abgebrochen.��