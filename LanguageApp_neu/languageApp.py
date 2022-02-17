#import language_check
import language_tool_python
from tkinter import *
import xml.etree.ElementTree as ET
from alternative_wörter import basic_german
from konjunktionen import Konjunktionen as bezugswoerter
import spacy 
from stopwoerter import stop_woerter
import re
#from compound_split import doc_split
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.edmundson import EdmundsonSummarizer as Summarizer
from nlp_melanie.compounds import *


class App:

    def __init__(self, window):

        # Farbe der Anwendung
        Farbe = '#e9d0af'

        # Allgemeine Fenstereinstellungen
        window.title('Autorenunterstützung Leichte Sprache')
        window.resizable(width=FALSE, height=FALSE)
        window.geometry("1250x660")

        # Instanziiere ein Unterfenster innerhalb des Hauptfensters
        frame0 = Frame(window)
        frame0.pack(side=RIGHT)

        # Instanziiere ein Unterfenster innerhalb des Unterfensters
        frame0_0 = Frame(frame0)
        frame0_0.pack(side=TOP, expand=FALSE)

        # Instanziiere ein Unterfenster innerhalb des Unterfensters
        frame0_1 = Frame(frame0)
        frame0_1.pack(side=BOTTOM)

        # Instanziiere ein Unterfenster innerhalb des Hauptfensters
        frame1 = Frame(window)
        frame1.pack()

        # Instanziiere ein Unterfenster innerhalb des Hauptfensters
        frame2 = Frame(window)
        frame2.pack()

        # Instanziiere ein Unterfenster innerhalb des Hauptfensters
        frame3 = Frame(window)
        frame3.pack()

        # Instanziiere ein Unterfenster innerhalb des Hauptfensters
        frame4 = Frame(window)
        frame4.pack()

        # Instanziiere einen Schiebebalken für die Auswahlliste
        scrollbarY0 = Scrollbar(frame0_0)
        scrollbarY0.pack(side=RIGHT, fill=Y)

        # Instanziiere einen Schiebebalken für die Auswahlliste
        scrollbarX = Scrollbar(frame0_0)
        scrollbarX.pack(side=BOTTOM, fill=X)

        # Instanziiere einen Schiebebalken für das Eingabetextfeld
        scrollbarY1 = Scrollbar(frame1)
        scrollbarY1.pack(side=RIGHT, fill=Y)

        # Instanziiere einen Schiebebalken für das Ausgabetextfeld
        scrollbarY2 = Scrollbar(frame2)
        scrollbarY2.pack(side=RIGHT, fill=Y)

        # Instanziiere einen Schiebebalken für das Ausgabetextfeld
        scrollbarY3 = Scrollbar(frame3)
        scrollbarY3.pack(side=RIGHT, fill=Y)

        # Instanziiere eine Überschrift für die Regelliste
        headlineRules = Label(frame0_0, text="Regelliste")
        headlineRules.pack()

        # Instanziiere einen Canvas der die Auswahlkästen beinhalten wird
        self.canvas = Canvas(frame0_0, background="gray95", width=200, height=400)
        self.canvas.pack(side=TOP, fill="both", expand=FALSE)

        # Instanziiere ein Unterfenster innerhalb des Canvas
        self.frame5 = Frame(self.canvas)
        self.frame5.pack()

        # Kreiere das Fenster des Canvas innerhalb des Unterfensters innerhalb des Canvas
        self.canvas.create_window((4, 4), window=self.frame5, anchor="nw", tags="self.frame5")
        # Bei einer Konfiguration die angegebene Methode aufrufen
        self.frame5.bind("<Configure>", self.configure_frame)

        # Instanziiere eine Leerzeile
        leerzeile = Label(frame0_1, text="")
        leerzeile.pack()

        # Instanziiere eine Überschrift für den Slider
        headlineSlider = Label(frame0_1, text="Länge der Zusammenfassung in %")
        headlineSlider.pack()

        # Deklariere das Attribut als wechselseitige Variable für den Slider
        self.scale = DoubleVar()
        # Lege den Standartwert der wechselseitigen Variable fest
        self.scale.set(50)
        # Instanziiere einen Slider zum Kontrollieren der Länge der Zusammenfassung
        slider = Scale(frame0_1, from_=10, to=100, orient=HORIZONTAL, digits=2, resolution=10, variable=self.scale)
        slider.pack()

        # Weise dem Attribut ein Wörterbuch mit den IDs aller Regeln zu
        self.rule_status = self.get_rule_ids()

        # Instanziiere einen Auswahlkasten für jeden Eintrag in dem Wörterbuch welches die Regel IDs beinhaltet
        for rule in self.rule_status:
            # Deklariere den Wert eines spezifischen Schlüssels als eine wechselseitige Variable
            self.rule_status[rule] = IntVar()
            # Aktiviere den Auswahlkasten standartmäßig
            self.rule_status[rule].set(1)
            # Instanziiere den Auswahlkasten und verbinde den jeweiligen Wert im Wörterbuch mit dem Auswahlkasten
            # Der Wert ist 1 wenn der Kasten ausgewählt ist und 0 wenn nicht
            check = Checkbutton(self.frame5, text=rule, variable=self.rule_status[rule], background=Farbe)
            check.pack(anchor="w")

        # Verbinde den Schiebebalken mit der Auswahlliste
        scrollbarY0.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=scrollbarY0.set)

        # Verbinde den Schiebebalken mit der Auswahlliste
        scrollbarX.config(command=self.canvas.xview, orient=HORIZONTAL)
        self.canvas.config(xscrollcommand=scrollbarX.set)

        # Instanziiere eine Überschrift für das Eingabefeld
        headline = Label(frame1, text="Eingabefeld")
        headline.pack()

        # Instanziiere das Eingabetextfeld
        self.input = Text(frame1, bd=2, width=120, height=12, wrap=WORD)
        self.input.pack(side=TOP)

        # Verbinde den Schiebebalken mit dem Eingabetextfeld
        scrollbarY1.config(command=self.input.yview)
        self.input.config(yscrollcommand=scrollbarY1.set)

        # Instanziiere eine Überschrift für das Ausgabetextfeld
        headline2 = Label(frame2, text="Zusammengefasst & geprüft")
        headline2.pack()

        # Instanziiere das Ausgabetextfeld
        self.output = Text(frame2, bd=2, width=120, height=11, wrap=WORD, state=NORMAL)
        self.output.pack(side=BOTTOM)

        # Instanziiere eine Überschrift für das Ausgabetextfeld2
        headline3 = Label(frame3, text="Zusammengefasst & automatisch korrigiert")
        headline3.pack()

        # Instanziiere das Ausgabetextfeld2
        self.output2 = Text(frame3, bd=2, width=120, height=11, wrap=WORD, state=NORMAL)
        self.output2.pack(side=TOP)

        # Verbinde den Schiebebalken mit dem Ausgabetextfeld2
        scrollbarY3.config(command=self.output2.yview)
        self.output2.config(yscrollcommand=scrollbarY3.set)

        # Verbinde den Schiebebalken mit dem Ausgabetextfeld
        scrollbarY2.config(command=self.output.yview)
        self.output.config(yscrollcommand=scrollbarY2.set)

        # Instanziiere einen Button welcher beim Klick die Fehler im Text findet
        submit = Button(frame4, text = "Zusammenfassen & Korrigieren", command = self.summarize_and_correct)
        submit.pack(side="right")

        # Instanziiere einen Button welcher beim Klick den Text zusammenfasst und korrigiert
        submit2 = Button(frame4, text="Zusammenfassen & Prüfen", command=self.summarize_and_proof)
        submit2.pack(side="left")

        window.configure(background=Farbe)
        frame0.configure(background=Farbe)
        frame0_0.configure(background=Farbe)
        frame0_1.configure(background=Farbe)
        frame1.configure(background=Farbe)
        frame2.configure(background=Farbe)
        frame3.configure(background=Farbe)
        frame4.configure(background=Farbe)
        headlineRules.configure(background=Farbe)
        self.canvas.configure(background=Farbe)
        self.frame5.configure(background=Farbe)
        leerzeile.configure(background=Farbe)
        headlineSlider.configure(background=Farbe)
        slider.configure(background=Farbe)
        headline.configure(background=Farbe)
        headline2.configure(background=Farbe)
        headline3.configure(background=Farbe)
        submit.configure(background=Farbe)
        submit2.configure(background=Farbe)

    def configure_frame(self, event):
        # Die Scrollregion resetten um das innere Fenster zu berücksichtigen
        # Die Größe des Unterfensters der scrollregion zuweisen damit diese der Größe des Unterfensters entspricht
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def find_errors(self, text):

        # Spacy initialisieren
        nlp = spacy.load("de_core_news_sm", disable=["parser", "ner"])

        # Instanziiere ein LanguageTool Objekt mit dem angegebenen Regelsatz
        tool = language_tool_python.LanguageTool('de-DE-x-simple-language')
        # Prüfe den angegebenen Text auf Fehler auf Basis des Regelsatzes
        result = tool.check(text)

        # Die Variable deklarieren, die das Resultat beinhalten wird
        errors = ""

        # Füge alle gefundenen Fehler zur Variable hinzu
        for n in result:
            for rule in self.rule_status:
                # Prüfe ob die ID eines gefundenen Fehlers mit der ID vom Wörterbuch übereinstimmt
                if n.ruleId == rule:
                    # Füge den gefundenen Fehler zur Variablen hinzu, wenn der zugehörige Auswahlkasten aktiviert ist
                    if self.rule_status[rule].get() == 1:
                        errors += str(n) + "\n"

        # Füge Ersetzungsvorschläge für Wörter zum Resultat hinzu, wenn die Regel ERSETZEN aktiviert ist
        if self.rule_status["ERSETZEN"].get() == 1:
            # Segmentieren des Eingabetextes in Wörter
            doc = nlp(self.input.get(1.0, END))
            # Iteriere durch alle Wörter
            for token in doc:
                if token.text in list(basic_german.keys()):
                    errors += "Rule ID: ERSETZEN[1]" + "\n" + "Message: Dieses Wort hat ein Synonym, welches für leichte Sprache besser geeignet ist." + "\n" + "Gefundenes Wort: " + str(
                        token.text) + "\n" + "Verbesserung: " + str(basic_german[token.text]) + "\n" + "\n"
                # Iteriere durch das Wörterbuch, das die Leichte-Sprache-Version eines komplexen Wortes enthält
                elif token.tag_.startswith("N"):
 #                   comps = doc_split.maximal_split(token.text)
                    comps = analyze_compound(token.text)
                    comp = []
                    for i, c in enumerate(comps):
                        if i == 0:  comp.append(c)
                        else:       comp.append(c.lower())
                    if len(comp) > 1:
                        errors += "Rule ID: KOMPOSITUM" + "\n" + "Message: Dieses Wort ist komplex." + "\n" + "Gefundenes Wort: " + str(
                            token.text) + "\n" + "Verbesserung: " + ('·'.join(str(elem) for elem in comp)) + "\n" + "\n"

        # Stelle des Status der Auswahlkästen im Terminal dar
        for n in self.rule_status:
            print(str(n) + ": " + str(self.rule_status[n].get()))

        return errors

    def get_rule_ids(self):

        # XML Dokument als Baum parsen
        # tree = ET.parse('grammar.xml')
        tree = ET.parse('grammar.xml')
        # Das Wurzelelement der XML Datei ermitteln
        root = tree.getroot()

        # Eine Liste für die Regeln deklarieren
        rule_list = []

        # Durch die Unterelemente iterieren
        for child in root:
            # Durch die Unterelemente der Unterelemente iterieren
            for grandchild in child:
                # Die Attributwerte des Attributs id einer liste zuweisen
                rule_list.append(grandchild.attrib["id"])

        # Sonderregel zuweisen da diese nicht im XML Dokument vorkommt
        rule_list.append("ERSETZEN")

        # Transformation der Liste mit den Regeln in ein Wörterbuch
        # Beispielwert für das Wörterbuch: {"SATZ": 0,"LANGES_WORT": 0}
        # Die Werte der Regeln repräsentieren ob eine Regel aktiviert ist oder nicht -> 0 für deaktiviert und 1 für aktiviert
        rule_status = {rule: 0 for (rule) in rule_list}

        # Das resultierende Wörterbuch zurückgeben
        return rule_status

    def summarize(self, text):

        # Spacy initialisieren
        nlp = spacy.load("de_core_news_sm", disable=["parser", "ner"])

        # Segmentiere den Eingabetext in Wörter
        doc = nlp(text)

        # Deklariere ein Wörterbuch um die Anzahl aller unterschiedlichen Wörter festzuhalten
        wortanzahl = dict()

        # Iteriere durch alle Wörter des Textes
        for token in doc:
            lemma = token.lemma_
            # Terminiere die aktuelle Iteration wenn das Wort ein Stoppwort ist
            if lemma in stop_woerter:
                continue

            # Wenn ein Wort schon im Wörterbuch ist wird die Anzahl des Worts um 1 erhöht
            if lemma in wortanzahl:
                wortanzahl[lemma] += 1
            # Wenn ein Wort noch nicht im Wörterbuch vorhanden ist wird ein neuer Eintrag kreiert und die Anzahl wird auf 1 gesetzt
            else:
                wortanzahl[lemma] = 1

        # Zerlegung des Textes in Sätze nach diesen Regeln:
        # (?<!\w\.\w.)\s 		-> Keine Trennung wenn zwei Zeichen mit einem Punkt in der Mitte und am Ende dem Leerzeichen vorausgehen (z.B. etc.)
        # (?<![0-9]\.)\s 		-> Keine Trennung wenn eine Nummer folgend von einem Punkt dem Leerzeichen vorausgeht (9. etc.)
        # (?<![0-9][0-9]\.)\s 	-> Keine Trennung wenn zwei Nummern folgend von einem Punkt dem Leerzeichen vorausgehen (18. etc.)
        # (?<![A-Z]\.)			-> Keine Trennung wenn ein Großbuchstabe gefolgt von einem Punkt dem Leerzeichen vorausgehen (W. etc)
        # (?<![A-Z][a-z]\.)\s 	-> Keine Trennung wenn ein Großbuchstabe gefolgt von einem Kleibuchstaben und einem Punkt dem Leerzeichen vorausgehen (Dr. etc)
        # (?<=\.|\?|\!)\s 		-> Trennen wenn ein Punkt, Fragezeichen oder Ausrufezeichen dem Leerzeichen vorausgehen
        saetze = re.split(r"(?<!\w\.\w.)(?<![0-9]\.)(?<![0-9][0-9]\.)(?<![A-Z]\.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s", text)

        # Deklariere ein Wörterbuch um den Wert eines Satzes festzuhalten
        # Der Wert eines Satzes ist die Summe der Anzahl aller Wörter in diesem Satz
        satzwerte = dict()

        # Iteriere durch alle Sätze und prüfe welche Wörter in dem Satz vorkommen
        for satz in saetze:
            for wort, anzahl in wortanzahl.items():
                if wort in satz.lower():
                    # Wenn ein Satz schon im Wörterbuch ist wird der Wert des Satzes um die Anzahl des zugehörigen Wortes erhöht
                    if satz in satzwerte:
                        satzwerte[satz] += anzahl
                    # Wenn ein Satz nicht im Wörterbuch vorhanden ist wird ein neuer Eintrag kreiert und der Wert des Satzes wird auf die Anzahl des Wortes gesetzt
                    else:
                        satzwerte[satz] = anzahl

        # Deklariere die Variable welche die Summer der Werte aller Satze beinhalten wird
        summe_satzwerte = 0

        # Füge für jeden Satz den Wert dieses Satzes zur Variablen hinzu
        for satz in satzwerte:
            summe_satzwerte += satzwerte[satz]

        # Dividiere die Summe aller Satzwerte durch die Anzahl der Sätze um den durchschnittlichen Satzwert zu erhalten
        mittelwert = int(summe_satzwerte / len(satzwerte))

        # Deklariere die Variable welche die resultierende Zusammenfassung beinhalten wird
        zusammenfassung = ""

        # Deklariere die Variable welche den vorherigen Satz in der Schleife festhalten wird
        vorheriger_satz = ""

        # Prüfe für jeden Satz ob dessen Wert die definierte Grenze überschreitet
        for satz in saetze:
            if (satz in satzwerte) and (satzwerte[satz] > mittelwert):
                # Segmentiere den Satz in Wörter um auf das erste Wort zugreifen zu können
                doc = nlp(satz)
                # Wenn die Variable den vorherigen Satz enthält und wenn das erste Wort des Satzes in der Liste der Bezugswörter vorkommt wird der Satz zum Resultat hinzugefügt
                if (vorheriger_satz != "") and (doc[0].text.lower() in bezugswoerter):
                    zusammenfassung += " " + vorheriger_satz
                # Füge den aktuellen Satz zum Resultat hinzu wenn dessen Wert die Grenze überschreitet
                zusammenfassung += " " + satz + "\n\n"
                # Weise der Variablen eine leere Zeichenkette zu wenn der aktuelle Satz schon zum Resultat hinzugefügt wurde
                vorheriger_satz = ""
            # Weise der Variable den aktuellen Satz zu damit dieser in der nächsten Iteration verwendet werden kann wenn der Satz nicht zum Resultat hinzugefügt wurde
            else:
                vorheriger_satz = satz

        # Füge die Zusammenfassung in das Ausgabetextfeld ein
        return zusammenfassung

    def edmunson(self, text):

        # Sprache wählen
        language = "german"
        # Die Prozentzahl vom Schieberegler ziehen
        divident = 100 / self.scale.get()

        # Den Text tokenizen und einen Stemmer zum Summarizer hinzufügen
        parser = PlaintextParser.from_string(text, Tokenizer(language))
        stemmer = Stemmer(language)
        summarizer = Summarizer(stemmer)

        # Spezifische Wortlisten definieren
        # Die bonus, stigma und null words sollen nicht genutzt werden aber es wird kein leerer Input akzeptiert
        summarizer.stop_words = get_stop_words(language)
        summarizer.bonus_words = ["nsdgdf"]
        summarizer.stigma_words = ["mtrtf"]
        summarizer.null_words = ["zngg"]

        summary = ""
        count = 0

        # Anzahl der Sätzte zählen
        for sentence in summarizer(parser.document, 10000000000):
            count += 1

        # Die Satzanzahl aus dem Przentanteil ermitteln
        sentence_number = round(count / divident)

        # Die Sätze zu einem Text zusammenfügen
        for sentence in summarizer(parser.document, sentence_number):
            summary += " " + str(sentence)

        return summary

    def correct(self, text):

        # Instanziiere ein LanguageTool Objekt mit dem angegebenen Regelsatz
        tool = language_tool_python.LanguageTool('de-DE-x-simple-language')
        # Mit dem LanguageTool auf Basis der Regeln den Text automatisch verbessern
        corrected_text = tool.correct(text)

        # Spacy initialisieren
        nlp = spacy.load("de_core_news_sm", disable=["parser", "ner"])
        doc = nlp(corrected_text)

        result = ""

        # Füge Ersetzungsvorschläge für Wörter zum Resultat hinzu, wenn die Regel ERSETZEN aktiviert ist
        if self.rule_status["ERSETZEN"].get() == 1:
            # Iteriere durch alle Wörter
            for token in doc:
                if token.text in list(basic_german.keys()):
                    result += basic_german[token.text] + token.whitespace_
                # Iteriere durch das Wörterbuch, das die Leichte-Sprache-Version eines komplexen Wortes enthält
                elif token.tag_.startswith("N"):
#                    comps = doc_split.maximal_split(token.text)
                    comps = analyze_compound(token.text)
                    comp = []
                    for i, c in enumerate(comps):
                        if i == 0:  comp.append(c)
                        else:       comp.append(c.lower())
                    if len(comp) > 1:
                        result += "•".join(str(elem) for elem in comp) + token.whitespace_
                    else:
                        result += token.text + token.whitespace_
                else:
                    result += token.text + token.whitespace_
            # Gebe das Resultat hiervon nur zurück wenn ERSETZEN aktiviert ist da sonst ein leeres Ergebnis zurückgegeben werden würde
            return result

        # Füge den korrigierten Text in das Ausgabetextfeld ein wenn ERSETZEN nicht aktiviert ist
        return corrected_text

    def summarize_and_correct(self):

        # Den Eingabetext einer Variablen zuweisen
        text = self.input.get(1.0, END)
        # Leere den Inhalt des Ausgabetextfelds
        self.output2.delete(1.0, END)

        summary = self.edmunson(text)
        correction = self.correct(summary)

        # Füge das Resultat in das Ausgabetextfeld ein
        self.output2.insert(END, correction)

    def summarize_and_proof(self):

        # Den Eingabetext einer Variablen zuweisen
        text = self.input.get(1.0, END)
        # Leere den Inhalt des Ausgabetextfelds
        self.output.delete(1.0, END)

        summary = self.edmunson(text)
        errors = self.find_errors(summary)

        result = summary + "\n\n" + errors

        # Füge das Resultat in das Ausgabetextfeld ein
        self.output.insert(END, result)


# Kreiere ein leeres Fenster
window = Tk()

# Rufe die Kontruktorfunktion auf
app = App(window)

# Zeige das Fenster kontinuierlich auf dem Bildschirm an. Ansonsten würde das Fenster nur kurz angezeigt und sofort wieder geschlossen werden
window.mainloop()





