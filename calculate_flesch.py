import nltk
from nltk import *
import textblob_de
from textblob_de import TextBlobDE
import pyphen

easytext = '''Die Länder Israel und USA machen dem Land Iran schwere Vorwürfe. Sie sagen: Die Regierung vom Iran will heimlich weiter Atom-Bomben bauen. Das verstößt gegen einen Vertrag.
Der Iran hat den Vertrag mit anderen Ländern geschlossen, zum Beispiel mit den USA, mit Russland und Deutschland. Darin steht: Der Iran baut keine Atom-Waffen. Dafür beenden die anderen Länder ihre Wirtschafts-Strafen gegen den Iran. Grund für die Strafen war das Atom-Programm.
Der Präsident von dem Land USA heißt Donald Trump. Er findet den Vertrag nicht gut. Er sagt: Wir beenden den Vertrag und machen einen neuen. Der Minister-Präsident von Israel heißt Benjamin Netanjahu. Er sagt: Der Iran macht heimlich weiter mit seinen Plänen für Atom-Waffen. Wir haben dafür Beweise. Der Iran sagt: Das stimmt nicht.
Viele andere Länder sagen: Es gibt keine Beweise, dass der Iran gegen den Atom-Vertrag verstößt. Der Vertrag soll weiter gelten.
Mehr zu dem Atom-Abkommen mit dem Iran können Sie hier lesen.'''

mytext = '''Das Wiener Atomabkommen soll verhindern, dass im Iran Atomwaffen entwickelt werden können. Bisher hält sich das Land offenbar daran. Nun droht der Iran, die Urananreicherung wiederaufzunehmen.
Der Iran will keine neuen Verhandlungen über das internationale Atomabkommen führen. Der iranische Außenminister Mohhamad Javad Zarif sagte in einem auf YouTube und Twitter veröffentlichten Video, sein Land werde das Abkommen weder verhandeln noch akzeptieren.
Bei einer Aufkündigung des Atomabkommens durch US-Präsident Donald Trump will sich auch der Iran daraus zurückziehen. "Wenn die USA das Atomabkommen verlassen, werden wir auch nicht bleiben", sagte Ali Akbar Welajati, der außenpolitische Berater von Irans geistlichem Oberhaupt Ayatollah Ali Chamenei, laut Staatsfernsehen.
Neuordnung der Zusammenarbeit mit der IAEA
"Wenn die Vereinigten Staaten aus dem Deal raus sind, bedeutet dies, dass es keinen Deal mehr gibt", sagte auch Irans Botschafter in London, Hamid Baeidinedschad, dem Fernsehsender CNN. In diesem Fall sei sein Land "bereit, zu der früheren Situation zurückzukehren".
Dies würde auch zu einer Neuordnung der Zusammenarbeit mit der Internationalen Atomenergiebehörde (IAEA) führen, sagte der Diplomat. Als mögliche Maßnahmen nannte der Diplomat die Wiederaufnahme der Urananreicherung.
Das Wiener Atomabkommen von 2015 zwischen dem Iran und den fünf UN-Vetomächten und Deutschland soll verhindern, dass Teheran die Fähigkeiten zur Entwicklung von Atomwaffen erlangt. Gemäß dem Abkommen hat Teheran die Urananreicherung deutlich reduziert und verschärfte Kontrollen der IAEA zugelassen.
Verstoß gegen den "Geist" der Vereinbarung'''

easynortext = '''*NN skal få spesialundervisning i skoleåret 2015/16
Vi viser til samtale *22. mai 2014.
På bakgrunn av deres melding om behov og sakkyndig vurdering fra pedagogisk-psykologisk tjeneste (PPT) har rektor ved *skole bestemt at *NN skal få spesialundervisning.
Vedtak
*NN, født *010101 er elev ved *skole. Det tildeles til sammen *250 timer spesialundervisning for skoleåret *2015/16.
Timene fordeles slik:
*50 årstimer (klokketimer) med pedagog	
*200 årstimer med assistent	
Innhold og organisering
Målet med opplæringen er at *NN skal styrke ferdighetene i *norsk og matematikk.
Skolen skal sammen med dere lage en individuell opplæringsplan som viser hvordan undervisningen skal utformes og gjennomføres. Planen skal inneholde realistiske mål for læring og utvikling. Den skal bygge på anbefalingene i PPTs sakkyndige vurdering som dere har fått i et eget brev.
Ved større endringer i elevens opplæringssituasjon gjør PPT en ny vurdering. Rektor vil da fatte nytt vedtak om spesialundervisning. 
Vurdering
Rektor vurderer at *NN har rett til å få spesialundervisning for å *videreutvikle ferdigheter i norsk og matematikk. Vedtaket stemmer med PPTs anbefaling.
'''

nortext = '''tildeling mikke mus
ePhorteskolen Rådhuset skole har mottatt melding om behov for spesialundervisning for * (navn). 
Retten til spesialundervisning er hjemlet i opplæringsloven § 5-1:
"Elevar som ikkje har eller som ikkje kan få tilfredsstillande utbytte av det ordinære opplæringstilbodet, har rett til spesialundervisning.”
Elevenes rettigheter når det gjelder omfang av opplæringen er i samsvar med rundskriv 
F - 12/2006 B oppgitt i 60 minutters enheter (klokketimer). Dette er ikke til hinder for at skolen kan organisere opplæringen i andre enheter og omregne tildelt ressurs til f.eks skoletimer av 45 minutters lengde.
PPT sakkyndige vurdering forteller at det skal arbeides hovedsakelig på følgende opplæringsområder: 
PPT har vurdert elevens behov og tilrår for skoleåret 20*- * følgende omfang av spesialundervisningen:
Årstimer (klokketimer) med pedagog:	
Årstimer med assistent:	
Sakkyndig tilråding fra PPT er tidligere tilsendt hjemmet.
Rektor har med hjemmel i Fredrikstad kommunes administrative fullmakter fattet følgende:
Vedtak
* (navn) gis skoleåret 20*- * rett til spesialundervisning etter oppl. § 5-1 og tildeles:
Årstimer (klokketimer) med pedagog:	
Årstimer med assistent:	
Organisering:
I henhold til sakkyndig vurdering vil det bli arbeidet hovedsakelig med følgende opplæringsområder:
Individuell opplæringsplan vil bli utarbeidet og ferdigstilt av skolen i samråd med foresatte når vedtak om spesialundervisning foreligger. Det forutsettes at det ved større endringer i elevens opplæringsforutsetninger -/betingelser foretas en ny tilråding og vedtak. Organisering og innhold i opplæringen skal være i samsvar med tilråding fra PPT og elevens vedtak om spesialundervisning.
Begrunnelse:
Ingen særskilt.'''


grundschultext = '''Kurz vor den Herbstferien wandert unsere Klasse 3a in den Wald. Wir Kinder freuen
uns sehr und sind gespannt, was uns der Forster zeigen und erz ¨ ahlen wird. ¨
Bevor die Wanderung beginnt, bittet uns Frau Neumann, unsere Lehrerin: ,,Vergesst
den Rucksack mit eurem Getrank und eurer Brotzeit nicht! Nehmt auch einen No- ¨
tizblock und einen Bleistift mit! Jedes Kind braucht eine kleine Tute, um Bl ¨ atter und ¨
Waldfruchte zu sammeln. Damit wollen wir sp ¨ ater im Klassenzimmer eine Ausstel- ¨
lung machen.”
Um 9 Uhr brechen wir auf. Zum Gluck hat sich der Nebel, der noch auf dem mor- ¨
gendlichen Schulweg uber dem Land lag, verzogen und die Sonne begleitet uns bis ¨
zum Waldrand.
Dort werden wir von Herrn Reichert, dem Forster, erwartet. Er begr ¨ ußt uns freund- ¨
lich und macht kleine Scherze. Auch schaut er lustig aus mit seinem grauen Jagerhut ¨
und seinem langen Vollbart. Herr Reichert hat einen kleinen Dackel dabei und verspricht
uns, dass jeder den Hund einmal an der Leine fuhren darf. Das macht Spaß! ¨
Wir alle freuen uns auf den schonen Vormittag.'''

semiotiktext = '''Das semiotische Dreieck ist ein in der Sprachwissenschaft und Semiotik verwendetes Modell. Es soll veranschaulichen, dass ein Zeichenträger (Graphem, Syntagma, Symbol) sich nicht direkt und unmittelbar auf einen außersprachlichen Gegenstand bezieht, sondern dieser Bezug nur mittelbar durch eine Vorstellung/einen Begriff erfolgt. Das semiotische Dreieck publizierten erstmals Charles Kay Ogden und Ivor Armstrong Richards in dem Werk The Meaning of Meaning (1923).'''


dic = pyphen.Pyphen(lang='de_DE')

'''
nordic = pyphen.Pyphen(lang='nn_NO')



norblob = TextBlobDE(nortext)

norsentnum = 0
norslength = 0
norsyllength = 0

for sentence in norblob.sentences:
    norsentnum = norsentnum +1
    norslength = norslength + len(sentence.tokens)

norasl = norslength / norsentnum

newnortokens = [x for x in norblob.tokens if x != '.']

print(len(norblob.tokens))
print(len(newnortokens))

for token in newnortokens:
    hyphenized = nordic.inserted(token)
    norsyls = hyphenized.split("-")
    norsyllength = norsyllength + len(norsyls)

norasw = norsyllength / len(norblob.tokens)

print('NORASL: ' + str(norasl))
print('NORASW: ' + str(norasw))


norflesch = 180 - norasl - (58.5 * norasw)

print('NORFLESCH: ' + str(norflesch))

'''

blob = TextBlobDE(grundschultext)

syllength = 0

sentnum = 0
slength = 0

for sentence in blob.sentences:
    sentnum = sentnum +1
    slength = slength + len(sentence.tokens)

asl = slength / sentnum

syllength = 0

#newtokens = [x for x in blob.tokens if x != '.']


for token in blob.words:
    hyphenized = dic.inserted(token)
    syls = hyphenized.split("-")
    syllength = syllength + len(syls)

asw = syllength / len(blob.tokens)


print('ASL: ' + str(asl))
print('ASW: ' + str(asw))


flesch = 180 - asl - (58.5 * asw)

print('FLESCH: ' + str(flesch))

    
