import nouns
from nouns import nouns
import compounds_syllables
from compounds_syllables import analyze_compound_syls

# Hier wird zunächst nachgesehen, ob ein Wort in der aus der TIGER-Baumbank generierten Nomenliste
# enthalten ist.

def lookup_noun(word):
    for item in nouns:
        if word in item:
            return(True)

compound_exceptions = ['Dänemark','Partei','Haushalten']

# Hier wird nach Nominalkomposita gesucht, die aus zwei Elementen bestehen.

def analyze_compound_2(word):
    components = []
    if lookup_noun(word[0:3]) and lookup_noun(word[3:].capitalize()):      # es wird immer nachgeschaut, ob beide Teile in der Nomenliste sind.
        components = [word[0:3],word[3:].capitalize()]                       # dabei muss der zweite Teil großgeschrieben werden.
    elif lookup_noun(word[0:4]) and lookup_noun(word[4:].capitalize()):
        components = [word[0:4],word[4:].capitalize()]
    elif lookup_noun(word[0:5]) and lookup_noun(word[5:].capitalize()):
        components = [word[0:5],word[5:].capitalize()]
    elif lookup_noun(word[0:6]) and lookup_noun(word[6:].capitalize()):
        components = [word[0:6],word[6:].capitalize()]    
    elif lookup_noun(word[0:7]) and lookup_noun(word[7:].capitalize()):
        components = [word[0:7],word[7:].capitalize()]    
    elif lookup_noun(word[0:8]) and lookup_noun(word[8:].capitalize()):
        components = [word[0:8],word[8:].capitalize()]    
    elif lookup_noun(word[0:9]) and lookup_noun(word[9:].capitalize()):
        components = [word[0:9],word[9:].capitalize()]    
    elif lookup_noun(word[0:10]) and lookup_noun(word[10:].capitalize()):       
        components = [word[0:10],word[10:].capitalize()]
    elif lookup_noun(word[0:11]) and lookup_noun(word[11:].capitalize()):       # im Moment mache ich das mit höchstens 11 Buchstaben im ersten Teil
        components = [word[0:11],word[11:].capitalize()]
    elif "s" in word[2:]:                                                        # jetzt wird zusätzlich nach einem Fugen-S geschaut. Das ist aber nicht immer
        i = word.index("s")                                                      # notwendig, weil die Nomenliste ja Vollformen enthält
        if lookup_noun(word[0:i]) and lookup_noun(word[i+1:].capitalize()):
            components = [word[0:i],'s',word[i+1:].capitalize()]
        elif "s" in word[i+1:]:                                                   # vor der Fuge kann im Wort auch ein weiteres S stehen, das keine Fuge ist
            i2 = word[i+1:].index("s") + i + 1
            if lookup_noun(word[0:i2]) and lookup_noun(word[i2+1:].capitalize()):
                components = [word[0:i2],'s',word[i2+1:].capitalize()]
        else:
            components = [word]
    else:
        components = [word]
    return(components)


# Hier wird nach Nominalkomposita gesucht, die aus drei Elementen bestehen.

def analyze_compound_3(word):
    components = []
    if lookup_noun(word[0:3]) and len(analyze_compound_2(word[3:].capitalize())) > 1:
        components = analyze_compound_2(word[3:].capitalize())
        components.insert(0,word[0:3])
    elif lookup_noun(word[0:4]) and len(analyze_compound_2(word[4:].capitalize())) > 1:
        components = analyze_compound_2(word[4:].capitalize())
        components.insert(0,word[0:4])
    elif lookup_noun(word[0:5]) and len(analyze_compound_2(word[5:].capitalize())) > 1:
        components = analyze_compound_2(word[5:].capitalize())
        components.insert(0,word[0:5])
    elif lookup_noun(word[0:6]) and len(analyze_compound_2(word[6:].capitalize())) > 1:
        components = analyze_compound_2(word[6:].capitalize())
        components.insert(0,word[0:6])
    elif lookup_noun(word[0:7]) and len(analyze_compound_2(word[7:].capitalize())) > 1:
        components = analyze_compound_2(word[7:].capitalize())
        components.insert(0,word[0:7])
    elif lookup_noun(word[0:8]) and len(analyze_compound_2(word[8:].capitalize())) > 1:
        components = analyze_compound_2(word[8:].capitalize())
        components.insert(0,word[0:8])
    elif lookup_noun(word[0:9]) and len(analyze_compound_2(word[9:].capitalize())) > 1:
        components = analyze_compound_2(word[9:].capitalize())
        components.insert(0,word[0:9])
    elif lookup_noun(word[0:10]) and len(analyze_compound_2(word[10:].capitalize())) > 1:
        components = analyze_compound_2(word[10:].capitalize())
        components.insert(0,word[0:10])
    elif lookup_noun(word[0:11]) and len(analyze_compound_2(word[11:].capitalize())) > 1:
        components = analyze_compound_2(word[11:].capitalize())
        components.insert(0,word[0:11])
    elif lookup_noun(word[0:12]) and len(analyze_compound_2(word[12:].capitalize())) > 1:
        components = analyze_compound_2(word[12:].capitalize())
        components.insert(0,word[0:12])
    elif lookup_noun(word[0:13]) and len(analyze_compound_2(word[13:].capitalize())) > 1:
        components = analyze_compound_2(word[13:].capitalize())
        components.insert(0,word[0:13])
    elif lookup_noun(word[0:14]) and len(analyze_compound_2(word[14:].capitalize())) > 1:
        components = analyze_compound_2(word[14:].capitalize())
        components.insert(0,word[0:14])
    else:
        components = [word]
    return(components)
                   
def analyze_compound(word):
    if word in compound_exceptions:                       # nur wenn das Wort nicht in der Ausnahmeliste steht
        components = [word]
    elif len(word)< 3:                                                         # nur wenn das Wort mindestens aus 6 Buchstaben besteht
        components = [word]
    elif "-" in word[2:]:                                                    # Split immmer an den Bindestrichen (Lehr-Lern-Formen)
        components = word.split("-")
    else:
        components = analyze_compound_syls(word)
#        print("COMPONENTS SYLS: " + str(components))
    if len(components) < 2 and word not in compound_exceptions:  
        components = analyze_compound_2(word)
#        print("COMPONENT_2: "  + str(components))
    if len(components) < 2 and word not in compound_exceptions:
        components = analyze_compound_3(word)
    else:
        return(components)
    return(components)

def test_compounds():
    print("Sofabett " + str(analyze_compound("Sofabett")))
    print("Haustür " + str(analyze_compound("Haustür")))
    print("Tagesschau " + str(analyze_compound("Tagesschau")))
    print("Lebensmittel " + str(analyze_compound("Lebensmittel")))
    print("Gipfelsturm " + str(analyze_compound("Gipfelsturm")))
    print("Barbezahlung " + str(analyze_compound("Barbezahlung")))
    print("Wasserkocher " + str(analyze_compound("Wasserkocher")))
    print("Wassereis " + str(analyze_compound("Wassereis")))
    print("Eiswasser " + str(analyze_compound("Eiswasser")))
    print("Waldmeister " + str(analyze_compound("Waldmeister")))
    print("Pilzsammler " + str(analyze_compound("Pilzsammler")))
    print("Autoverkäufer " + str(analyze_compound("Autoverkäufer")))
    print("Graswurzel " + str(analyze_compound("Graswurzel")))
    print("Wurzelgras " + str(analyze_compound("Wurzelgras")))
    print("Pilzexperte " + str(analyze_compound("Pilzexperte")))
    print("Rotwein " + str(analyze_compound("Rotwein")))
    print("Blumenvase " + str(analyze_compound("Blumenvase")))
    print("Bauernhof " + str(analyze_compound("Bauernhof")))
    print("Rotweinglas " + str(analyze_compound("Rotweinglas")))
    print("Geschmackssache " + str(analyze_compound("Geschmackssache")))
    print("Steuerungsmechanismus " + str(analyze_compound("Steuerungsmechanismus")))
    print("Softwarefirma " + str(analyze_compound("Softwarefirma")))
    print("Software-Firma " + str(analyze_compound("Software-Firma")))
    print("Lampenschirm " + str(analyze_compound("Lampenschirm")))
    print("Lampenschirme " + str(analyze_compound("Lampenschirme")))
    print("Musikkapelle " + str(analyze_compound("Musikkapelle")))
    print("Lehr-Lern-Forschung " + str(analyze_compound("Lehr-Lern-Forschung")))
    print("Katzenpfote " + str(analyze_compound("Katzenpfote")))
    print("Gesamtfläche " + str(analyze_compound("Gesamtfläche")))
    print("Apfelsaft " + str(analyze_compound("Apfelsaft")))
    print("Parkbank " + str(analyze_compound("Parkbank")))
    print("Schweineschnitzel " + str(analyze_compound("Schweineschnitzel")))
    print("Jägerschnitzel " + str(analyze_compound("Jägerschnitzel")))
    print("Blumentopferde " + str(analyze_compound("Blumentopferde")))
    print("Kaukasusrepublik " + str(analyze_compound("Kaukasusrepublik")))
    print("Glücksautomaten " + str(analyze_compound("Glücksautomaten")))
    print("Konsumentenverhalten " + str(analyze_compound("Konsumentenverhalten")))
    print("Regentropfen " + str(analyze_compound("Regentropfen")))
    print("Leistungsfähigkeit " + str(analyze_compound("Leistungsfähigkeit")))
    print("Urkundenfälschung " + str(analyze_compound("Urkundenfälschung")))
    print("Tagebuch " + str(analyze_compound("Tagebuch")))
    print("Strahlenbündel " + str(analyze_compound("Strahlenbündel")))
    print("Schmerzensschrei " + str(analyze_compound("Schmerzensschrei")))
    print("Kindergarten " + str(analyze_compound("Kindergarten")))
    print("Jahresbericht " + str(analyze_compound("Jahresbericht")))
    print("Einheitspreis " + str(analyze_compound("Einheitspreis")))
    print("Birnbaum " + str(analyze_compound("Birnbaum")))
    print("Staubecken " + str(analyze_compound("Staubecken")))
    print("Messerattentat " + str(analyze_compound("Messerattentat")))
    print("Sonderauszählungen " + str(analyze_compound("Sonderauszählungen")))
    print("Betriebsausflug " + str(analyze_compound("Betriebsausflug")))
    print("Bundessteuerbehörde " + str(analyze_compound("Bundessteuerbehörde")))
    print("Vermögensgegenstände " + str(analyze_compound("Vermögensgegenstände")))
    print("Sachanlagen " + str(analyze_compound("Sachanlagen")))
    print("Herstellungskosten " + str(analyze_compound("Herstellungskosten")))
    print("Nutzungsdauer " + str(analyze_compound("Nutzungsdauer")))
    print("Wertminderungen " + str(analyze_compound("Wertminderungen")))
    print("Bilanzstichtag " + str(analyze_compound("Bilanzstichtag")))   

