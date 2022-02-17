############################################
#
#
#  Installationsguide für die Language App
#  
#
#  Autor: Pascal F. Fichtner, Kjell Kunz, Florian Heinz und Melanie Siegel
#
#
############################################


############################################
#
# Schritt 1: Die Installation von Python.
#
############################################
- Besuchen Sie die Seite: https://www.python.org/downloads/ und laden Sie sich die aktuellste Pyhton-Version herunter. 
    	- Tipp: Sollten Sie sich nicht mit Python auskennen und/oder es nicht regelmäßig verwenden, installieren Sie die entsprechende Version nach den vorgegebenen Default-Einstellungen der Installation. Merken Sie sich den Installationspfad. 
- Installieren Sie dies
- Während der Installation sollte "Add python to PATH" angekreuzt werden.


############################################
#
# Schritt 2: Entpacken der zip-Datei.
#
############################################
- Für die Installation der App exisitert bisher (noch) kein einfacher Weg, über eine Installations-Datei. Deshalb ist hierfür ein manuelles vorgehen von nöten. Die benötigten Dateien befinden sich in dem beiligenden zip-Archiv.
- Entpacken Sie das zip-Archiv. 
- Führen Sie das Skript LanguageApp.py aus. Öffnen Sie hierfür die cmd-Line bzw die Python-Kommando-Zeile und geben Sie den Befehle: "python LanguageApp.py" ein
- Es erscheint eine Fehlermeldung. Grund ist, dass noch nicht alle Pakete installiert wurden.
- Öffnen Sie die cmd-Line bzw die Python-Kommando-Zeile und geben sie nacheinenander die Befehle: 
    	- "pip install language_tool_python spacy sumy nltk compound-split" und 
	- "python -m spacy download de_core_news_sm" ein.


############################################
#
# Schritt 3: Austausch der Datei: grammar.xml.
#
############################################
- Hierfür müssen sie in das Verzeichnis gehen, indem Sie Python installierten. 
- Gehen sie in das Unterverzeichnis: <Python_Verzeichnis>\Lib\site-packages\language_check\LanguageTool-3.2\org\languagetool\rules\de-DE-x-simple-language.
	- Tipp: Unter den meisten Windows-System funktioniert es, wenn sie diesen "Master-Pfad" verwenden: C:\Users\[Benutzer des PCs]\AppData\Local\Programs\Python\[Pythonversion]\Lib\site-packages\language_check\[LanguageTool Version]\org\languagetool\rules\de-DE-x-simple-language
- Kopieren Sie die grammar.xml aus der zip-Datei in das obige Unterverzeichnis und überschreiben Sie die dortige grammar.xml-Datei.


############################################
#
# Schritt 4: Ausführen der LanguageApp
#
############################################
- Führen Sie erneut das Skript LanguageApp.py aus. Öffnen Sie hierfür die cmd-Line bzw die Python-Kommando-Zeile und geben Sie den Befehle: "python LanguageApp.py" ein.
- Es öffnet sich nun ein Fenster, dies bedeutet, dass die Installation erfolgreich beendet wurde.



