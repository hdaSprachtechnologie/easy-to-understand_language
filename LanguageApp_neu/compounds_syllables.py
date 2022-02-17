import nouns
from nouns import nouns
import pyphen
import nltk
from nltk.util import ngrams

# Hier wird zunächst nachgesehen, ob ein Wort in der aus der TIGER-Baumbank generierten Nomenliste
# enthalten ist.

def lookup_noun(word):
    for item in nouns:
        if word in item:
            return(True)

# Jetzt zerlege ich ein Wort in Silben. Das Ergebnis ist eine Liste der Silben
# etwa so: ['Do', 'nau', 'dampf', 'schiff']

def delete_empty_syls(syls):
    new_syls = []
    for syl in syls:
        if len(syl) > 0:
            new_syls.append(syl)
    return(new_syls)

def get_syls(word):
    dic = pyphen.Pyphen(lang='de_DE')
    hyphenized = dic.inserted(word)
    syls = hyphenized.split("-")
    syls = delete_empty_syls(syls)
    return(syls)

# Um Teilkomponenten nachzuschlagen, muss ich sie wieder kombinieren

def combine_syls(syls):
    syl_combinations = []
    bigrams = ngrams(syls,2)
    trigrams = ngrams(syls,3)
    fourgrams = ngrams(syls,4)
    for gram in bigrams:
        substr = gram[0].capitalize() + gram[1]
        syl_combinations.append(substr)
    for gram in trigrams:
        substr = gram[0].capitalize() + gram[1] + gram[2]
        syl_combinations.append(substr)
    for gram in fourgrams:
        substr = gram[0].capitalize() + gram[1] + gram[2] + gram[3]
        syl_combinations.append(substr)
    return(syl_combinations)

# Fugenelemente

def strip_fuge(syl):
    if syl.endswith('s'):
        return(syl[:-1])
    else:
        return(syl)


def analyze_compound_syls(word):
    components = []
    syls = get_syls(word)
#    print(str(syls))
    syl_combinations = combine_syls(syls)
#    print(str(syl_combinations))
    if len(syls) == 1:
        components = [word]
    elif len(syls) == 2:
        if lookup_noun(syls[0]) and lookup_noun(syls[1].capitalize()):
            components = [syls[0],syls[1].capitalize()]
        elif lookup_noun(strip_fuge(syls[0])) and lookup_noun(syls[1].capitalize()):
            components = [syls[0],syls[1].capitalize()]
        else:
            components = [word]
    elif len(syls) == 3:
        if lookup_noun(syls[0]) and lookup_noun(syls[1].capitalize()) and lookup_noun(syls[2].capitalize()):
            components =[syls[0], syls[1].capitalize(), syls[2].capitalize()]
        elif lookup_noun(syls[0]) and lookup_noun(syl_combinations[1]):
            components = [syls[0],syl_combinations[1]]
        elif lookup_noun(strip_fuge(syl_combinations[0])) and lookup_noun(syls[2].capitalize()):    # Schmerzensschrei
            components = [syl_combinations[0],syls[2].capitalize()]
        else:
            components = [word]
    elif len(syls) == 4:
        if lookup_noun(syls[0]) and lookup_noun(syls[1].capitalize()) and lookup_noun(syls[2].capitalize()) and lookup_noun(syls[3].capitalize()):
            components =[syls[0], syls[1].capitalize(), syls[2].capitalize(), syls[3].capitalize()]
        elif lookup_noun(syl_combinations[0]) and lookup_noun(syl_combinations[2]):
            components = [syl_combinations[0], syl_combinations[2]]
        elif lookup_noun(strip_fuge(syl_combinations[0])) and lookup_noun(syl_combinations[2]):
            components = [syl_combinations[0], syl_combinations[2]]
        elif lookup_noun(syls[0]) and lookup_noun(syl_combinations[1]) and lookup_noun(syls[3].capitalize()):
            components = [syls[0],syl_combinations[1], syls[3]]
        elif lookup_noun(syl_combinations[3]) and lookup_noun(syls[3].capitalize()):
            components = [syl_combinations[3],syls[3]]
        elif lookup_noun(syls[0]) and lookup_noun(syl_combinations[4]):
            components = [syls[0], syl_combinations[4]]
        elif lookup_noun(syls[0]) and lookup_noun(syls[1].capitalize()) and lookup_noun(syl_combinations[2]):    #Lehr-Lern-Forschung
            components = [syls[0], syls[1].capitalize(), syl_combinations[2]]
        else:
            components = [word]
    elif len(syls) == 5:
        if lookup_noun(syls[0]) and lookup_noun(syls[1].capitalize()) and lookup_noun(syls[2].capitalize()) and lookup_noun(syls[3].capitalize()) and lookup_noun(syls[4].capitalize()):
            components =[syls[0], syls[1].capitalize(), syls[2].capitalize(), syls[3].capitalize(), syls[4].capitalize()]
        elif lookup_noun(syl_combinations[0]) and lookup_noun(syl_combinations[6]):
            components =[syl_combinations[0], syl_combinations[6]]
        elif lookup_noun(strip_fuge(syl_combinations[4])) and lookup_noun(syl_combinations[3]):     #Herstellungskosten
            components =[syl_combinations[4], syl_combinations[3]]
        elif lookup_noun(strip_fuge(syl_combinations[0])) and lookup_noun(syl_combinations[6]):    # Leistungsfähigkeit
            components =[syl_combinations[0], syl_combinations[6]]
        elif lookup_noun(syl_combinations[0]) and lookup_noun(syl_combinations[2]) and lookup_noun(syls[4].capitalize()):    # Messerattentat - Messe-Ratten-Tat
            components =[syl_combinations[0], syl_combinations[2], syls[4].capitalize()]
        elif lookup_noun(syls[0]) and lookup_noun(syl_combinations[8]):    # Wertminderungen
            components =[syls[0], syl_combinations[8]]
        else:
            components = [word]
    elif len(syls) == 6:
        if lookup_noun(syls[0]) and lookup_noun(syls[1].capitalize()) and lookup_noun(syls[2].capitalize()) and lookup_noun(syls[3].capitalize()) and lookup_noun(syls[4].capitalize()) and lookup_noun(syls[5].capitalize()):
            components =[syls[0], syls[1].capitalize(), syls[2].capitalize(), syls[3].capitalize(), syls[4].capitalize(), syls[5].capitalize()]
        elif lookup_noun(syl_combinations[5]) and lookup_noun(syl_combinations[8]):     # Kaukasusrepublik, Bundessteuerbehörde
            components =[syl_combinations[5], syl_combinations[8]]
        elif lookup_noun(syl_combinations[0]) and lookup_noun(syl_combinations[11]):     # Glücksautomaten
            components =[syl_combinations[0], syl_combinations[11]]
        else:
            components = [word]
    elif len(syls) == 7:
        if lookup_noun(syls[0]) and lookup_noun(syls[1].capitalize()) and lookup_noun(syls[2].capitalize()) and lookup_noun(syls[3].capitalize()) and lookup_noun(syls[4].capitalize()) and lookup_noun(syls[5].capitalize())  and lookup_noun(syls[6].capitalize()):
            components =[syls[0], syls[1].capitalize(), syls[2].capitalize(), syls[3].capitalize(), syls[4].capitalize(), syls[5].capitalize(), syls[6].capitalize()]
        elif lookup_noun(syl_combinations[6]) and lookup_noun(syl_combinations[14]):
            components = [syl_combinations[6], syl_combinations[14]]
        elif lookup_noun(strip_fuge(syl_combinations[6])) and lookup_noun(syl_combinations[14]):
            components = [syl_combinations[6], syl_combinations[14]]
        elif lookup_noun(strip_fuge(syl_combinations[11])) and lookup_noun(syl_combinations[10]):   # Konsumentenverhalten
            components = [syl_combinations[11], syl_combinations[10]]        
        else:
            components = [word]
    elif len(syls) == 10:
        if lookup_noun(syl_combinations[0]) and lookup_noun(strip_fuge(syl_combinations[11])) and lookup_noun(strip_fuge(syl_combinations[14])) and lookup_noun(syl_combinations[8]):           #Bundesausbildungsförderungsgesetz
            components =[syl_combinations[0], syl_combinations[11], syl_combinations[14], syl_combinations[8]]
        else:
            components = [word]
    else:
            components = [word]
    return(components)

def test_compounds():
    if analyze_compound_syls("Sofabett") != ['Sofa', 'Bett']:
        print("Sofabett " + str(analyze_compound_syls("Sofabett")))
    if analyze_compound_syls("Haustür") != ['Haus', 'Tür']:
        print("Haustür " + str(analyze_compound_syls("Haustür")))
    if analyze_compound_syls("Tagesschau") != ['Tages', 'Schau']:
        print("Tagesschau " + str(analyze_compound_syls("Tagesschau")))
    if analyze_compound_syls("Lebensmittel") != ['Lebens', 'Mittel']:
        print("Lebensmittel " + str(analyze_compound_syls("Lebensmittel")))
    if analyze_compound_syls("Gipfelsturm") != ['Gipfel', 'Sturm']:
        print("Gipfelsturm " + str(analyze_compound_syls("Gipfelsturm")))
    if analyze_compound_syls("Barbezahlung") != ['Bar', 'Bezahlung']:
        print("Barbezahlung " + str(analyze_compound_syls("Barbezahlung")))
    if analyze_compound_syls("Wasserkocher") != ['Wasser', 'Kocher']:
        print("Wasserkocher " + str(analyze_compound_syls("Wasserkocher")))
    if analyze_compound_syls("Wassereis") != ['Wasser', 'Eis']:
        print("Wassereis " + str(analyze_compound_syls("Wassereis")))
    if analyze_compound_syls("Eiswasser") != ['Eis', 'Wasser']:
        print("Eiswasser " + str(analyze_compound_syls("Eiswasser")))
    if analyze_compound_syls("Waldmeister") != ['Wald', 'Meister']:
        print("Waldmeister " + str(analyze_compound_syls("Waldmeister")))
    if analyze_compound_syls("Pilzsammler") != ['Pilz', 'Sammler']:
        print("Pilzsammler " + str(analyze_compound_syls("Pilzsammler")))
    if analyze_compound_syls("Autoverkäufer") != ['Auto', 'Verkäufer']:
        print("Autoverkäufer " + str(analyze_compound_syls("Autoverkäufer")))
    if analyze_compound_syls("Graswurzel") != ['Gras', 'Wurzel']:
        print("Graswurzel " + str(analyze_compound_syls("Graswurzel")))
    if analyze_compound_syls("Wurzelgras") != ['Wurzel', 'Gras']:
        print("Wurzelgras " + str(analyze_compound_syls("Wurzelgras")))
    if analyze_compound_syls("Pilzexperte") != ['Pilz', 'Experte']:
        print("Pilzexperte " + str(analyze_compound_syls("Pilzexperte")))
    if analyze_compound_syls("Rotwein") != ['Rot', 'Wein']:
        print("Rotwein " + str(analyze_compound_syls("Rotwein")))
    if analyze_compound_syls("Blumenvase") != ['Blumen', 'Vase']:
        print("Blumenvase " + str(analyze_compound_syls("Blumenvase")))
    if analyze_compound_syls("Bauernhof") != ['Bauern', 'Hof']:
        print("Bauernhof " + str(analyze_compound_syls("Bauernhof")))
    if analyze_compound_syls("Rotweinglas") != ['Rot', 'Wein', 'Glas']:
        print("Rotweinglas " + str(analyze_compound_syls("Rotweinglas")))
    if analyze_compound_syls("Geschmackssache") != ['Geschmacks','Sache']:
        print("Geschmackssache " + str(analyze_compound_syls("Geschmackssache")))
    if analyze_compound_syls("Steuerungsmechanismus") != ['Steuerungs','Mechanismus']:
        print("Steuerungsmechanismus " + str(analyze_compound_syls("Steuerungsmechanismus")))
    if analyze_compound_syls("Softwarefirma") != ['Software', 'Firma']:
        print("Softwarefirma " + str(analyze_compound_syls("Softwarefirma")))
    if analyze_compound_syls("Software-Firma") != ['Software', 'Firma']:
        print("Software-Firma " + str(analyze_compound_syls("Software-Firma")))
    if analyze_compound_syls("Lampenschirm") != ['Lampen','Schirm']:
        print("Lampenschirm " + str(analyze_compound_syls("Lampenschirm")))
    if analyze_compound_syls("Lampenschirme") != ['Lampen','Schirme']:
        print("Lampenschirme " + str(analyze_compound_syls("Lampenschirme")))
    if analyze_compound_syls("Musikkapelle") != ['Musik','Kapelle']:
        print("Musikkapelle " + str(analyze_compound_syls("Musikkapelle")))
    if analyze_compound_syls("Lehr-Lern-Forschung") != ['Lehr','Lern','Forschung']:
        print("Lehr-Lern-Forschung " + str(analyze_compound_syls("Lehr-Lern-Forschung")))
    if analyze_compound_syls("Katzenpfote") != ['Katzen','Pfote']:
        print("Katzenpfote " + str(analyze_compound_syls("Katzenpfote")))
    if analyze_compound_syls("Gesamtfläche") != ['Gesamt','Fläche']:
        print("Gesamtfläche " + str(analyze_compound_syls("Gesamtfläche")))
    if analyze_compound_syls("Apfelsaft") != ['Apfel', 'Saft']:
        print("Apfelsaft " + str(analyze_compound_syls("Apfelsaft")))
    if analyze_compound_syls("Parkbank") != ['Park','Bank']:
        print("Parkbank " + str(analyze_compound_syls("Parkbank")))
    if analyze_compound_syls("Schweineschnitzel") != ['Schweine','Schnitzel']:
        print("Schweineschnitzel " + str(analyze_compound_syls("Schweineschnitzel")))
    if analyze_compound_syls("Jägerschnitzel") != ['Jäger','Schnitzel']:
        print("Jägerschnitzel " + str(analyze_compound_syls("Jägerschnitzel")))
    if analyze_compound_syls("Blumentopferde") != ['Blumen','Topf','Erde']:
        print("Blumentopferde " + str(analyze_compound_syls("Blumentopferde")))
    if analyze_compound_syls("Kaukasusrepublik") != ['Kaukasus','Republik']:
        print("Kaukasusrepublik " + str(analyze_compound_syls("Kaukasusrepublik")))
    if analyze_compound_syls("Glücksautomaten") != ['Glücks','Automaten']:
        print("Glücksautomaten " + str(analyze_compound_syls("Glücksautomaten")))
    if analyze_compound_syls("Konsumentenverhalten") != ['Konsumenten','Verhalten']:
        print("Konsumentenverhalten " + str(analyze_compound_syls("Konsumentenverhalten")))
    if analyze_compound_syls("Regentropfen") != ['Regen','Tropfen']:
        print("Regentropfen " + str(analyze_compound_syls("Regentropfen")))
    if analyze_compound_syls("Leistungsfähigkeit") != ['Leistungs','Fähigkeit']:
        print("Leistungsfähigkeit " + str(analyze_compound_syls("Leistungsfähigkeit")))
    if analyze_compound_syls("Urkundenfälschung") != ['Urkunden','Fälschung']:
        print("Urkundenfälschung " + str(analyze_compound_syls("Urkundenfälschung")))
    if analyze_compound_syls("Tagebuch") != ['Tage','Buch']:
        print("Tagebuch " + str(analyze_compound_syls("Tagebuch")))
    if analyze_compound_syls("Strahlenbündel") != ['Strahlen','Bündel']:
        print("Strahlenbündel " + str(analyze_compound_syls("Strahlenbündel")))
    if analyze_compound_syls("Schmerzensschrei") != ['Schmerzens','Schrei']:
        print("Schmerzensschrei " + str(analyze_compound_syls("Schmerzensschrei")))
    if analyze_compound_syls("Kindergarten") != ['Kinder','Garten']:
        print("Kindergarten " + str(analyze_compound_syls("Kindergarten")))
    if analyze_compound_syls("Jahresbericht") != ['Jahres','Bericht']:
        print("Jahresbericht " + str(analyze_compound_syls("Jahresbericht")))
    if analyze_compound_syls("Einheitspreis") != ['Einheits','Preis']:
        print("Einheitspreis " + str(analyze_compound_syls("Einheitspreis")))
    if analyze_compound_syls("Birnbaum") != ['Birn','Baum']:
        print("Birnbaum " + str(analyze_compound_syls("Birnbaum")))
    if analyze_compound_syls("Staubecken") != ['Staub','Ecken']:
        print("Staubecken " + str(analyze_compound_syls("Staubecken")))
    if analyze_compound_syls("Messerattentat") != ['Messer','Attentat']:
        print("Messerattentat " + str(analyze_compound_syls("Messerattentat")))
    if analyze_compound_syls("Sonderauszählungen") != ['Sonder','Auszählungen']:
        print("Sonderauszählungen " + str(analyze_compound_syls("Sonderauszählungen")))
    if analyze_compound_syls("Betriebsausflug") != ['Betriebs','Ausflug']:
        print("Betriebsausflug " + str(analyze_compound_syls("Betriebsausflug")))
    if analyze_compound_syls("Bundessteuerbehörde") != ['Bundes','Steuer','Behörde']:
        print("Bundessteuerbehörde " + str(analyze_compound_syls("Bundessteuerbehörde")))
    if analyze_compound_syls("Vermögensgegenstände") != ['Vermögens','Gegenstände']:
        print("Vermögensgegenstände " + str(analyze_compound_syls("Vermögensgegenstände")))
    if analyze_compound_syls("Sachanlagen") != ['Sach','Anlagen']:
        print("Sachanlagen " + str(analyze_compound_syls("Sachanlagen")))
    if analyze_compound_syls("Herstellungskosten") != ['Herstellungs','Kosten']:
        print("Herstellungskosten " + str(analyze_compound_syls("Herstellungskosten")))
    if analyze_compound_syls("Nutzungsdauer") != ['Nutzungs','Dauer']:
        print("Nutzungsdauer " + str(analyze_compound_syls("Nutzungsdauer")))
    if analyze_compound_syls("Wertminderungen") != ['Wert','Minderungen']:
        print("Wertminderungen " + str(analyze_compound_syls("Wertminderungen")))
    if analyze_compound_syls("Bilanzstichtag") != ['Bilanz','Stichtag']:
        print("Bilanzstichtag " + str(analyze_compound_syls("Bilanzstichtag")))   
