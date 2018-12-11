import random
import sqlite3

class Plec:
    def PLEC(self):
        a = "kobieta"
        b = "mezczyzna"
        d = "k"
        e = "m"
        plec_1 = (input("Podaj plec: \n"))
        while (plec_1 != a.upper()) and (plec_1 != b.upper())and(plec_1 != d.upper()) and (plec_1 != e.upper())and(plec_1 != a.lower()) and (plec_1 != b.lower())and(plec_1 != d.lower()) and (plec_1 != e.lower()):
            plec_1 = (input("Bledna plec. Dostepna plec to:\nKobieta\nMezczyzna\n"))
        return plec_1
    #plec = PLEC()

class Rasa:
    def RASA(self):
        a = "czlowiek"
        b = "elf"
        c = "krasnolud"
        d = "niziolek"
        rasa_1 = (input("Podaj rase: \n"))
        while (rasa_1 != a.upper()) and (rasa_1 != b.upper())and(rasa_1 != a.lower()) and (rasa_1 != b.lower())and(rasa_1 != c.upper()) and (rasa_1 != d.upper()) and (rasa_1!= c.lower()) and (rasa_1 != d.lower()):
            rasa_1 = (input("Bledna rasa. Dostepna rasy to:\n%s\n%s\n%s\n%s\n" %(a,b,c,d)))
        return rasa_1
    #rasa = RASA()

class Profesja(Rasa):
    def PROFESJA(self):

        profesje = ["Akolita"
		,"Banita"
		,"Berserker z Norski"
		,"Chlop"
		,"Ciura obozowa"
		,"Cyrkowiec"
		,"Cyrulik"
		,"Fanatyk"
		,"Flisak"
		,"Giermek"
		,"Gladiator"
		,"Goniec"
		,"Gornik"
		,"Guslarz"
		,"Hiena cmentarna"
		,"Kanciarz"
		,"Kozak kislevski"
		,"Lesnik"
		,"Lowca"
		,"Lowca nagród"
		,"Mieszczanin"
		,"Mytnik"
		,"Najemnik"
		,"Ochotnik"
		,"Ochroniarz"
		,"Oprych"
		,"Paz"
		,"Podzegacz"
		,"Porywacz zwlok"
		,"Poslaniec"
		,"Przemytnik"
		,"Przepatrywacz"
		,"Przewoznik"
		,"Rybak"
		,"Rzecznik rodu"
		,"Rzemieslnik"
		,"Rzezimieszek"
		,"Skryba"
		,"Sługa"
		,"Strażnik"
		,"Straznik drog"
		,"Straznik pol"
		,"Straznik wiezienny"
		,"Szczurolap"
		,"Szermierz estalijski"
		,"Szlachcic"
		,"Smieciarz"
		,"Tarczownik"
		,"Uczeń czarodzieja"
		,"Węglarz"
		,"Wloczykij"
		,"Wojownik klanowy"
		,"Woznica"
		,"Zabojca trolli"
		,"Zarzadca"
		,"Zlodziej"
		,"Zak"
		,"Zeglarz"
		,"Zolnierz"
		,"Zolnierz okretowy"]
        a = "t"
        b = "n"
        czlowiek = "czlowiek"
        elf = "elf"
        krasnolud = "krasnolud"
        niziolek = "niziolek"

        wybor = input("Czy chesz wylosowac profesje: t::n\n")
        while (wybor == b.upper())or(wybor == b.lower()):
            wpisz = input("Podaj profesje: \n")
            for i in profesje:
                if i == wpisz:
                    return wpisz
                if i == 59:
                    print("Bledna profesja")
        while (wybor == a.upper())or(wybor == a.lower()):
            p=random.choice(profesje)
            if (rasa == czlowiek.upper())or(rasa == czlowiek.lower()):
                if (p == profesje[11])or(p == profesje[34])or(p == profesje[41])or(p == profesje[47])or(p == profesje[51])or(p == profesje[53]):
                    continue
                else:
                    return p
            if (rasa==elf.upper())or(rasa==elf.lower()):
                if (p==profesje[1])or(p==profesje[5])or(p==profesje[15])or(p==profesje[18])or(p==profesje[22])or(p==profesje[26])or(p==profesje[29])or(p==profesje[33])or(p==profesje[34])or(p==profesje[35])or(p==profesje[37])or(p==profesje[48])or(p==profesje[50])or(p==profesje[51])or(p==profesje[55])or(p==profesje[56])or(p == profesje[57]):
                    return p
            if (rasa==krasnolud.upper())or(rasa==krasnolud.lower()):
                if (p==profesje[1])or(p==profesje[5])or(p==profesje[10])or(p==profesje[11])or(p==profesje[12])or(p==profesje[14])or(p==profesje[18])or(p==profesje[20])or(p==profesje[21])or(p==profesje[22])or(p==profesje[23])or(p==profesje[24])or(p==profesje[27])or(p==profesje[30])or(p==profesje[35])or(p==profesje[36])or(p == profesje[37])or(p==profesje[38])or(p==profesje[39])or(p==profesje[42])or(p==profesje[43])or(p==profesje[45])or(p==profesje[47])or(p==profesje[52])or(p==profesje[53])or(p==profesje[55])or(p==profesje[56])or(p == profesje[57])or(p==profesje[58])or(p == profesje[59]):
                    return p
            if (rasa==niziolek.upper())or(rasa==niziolek.lower()):
                if (p==profesje[1])or(p==profesje[4])or(p==profesje[5])or(p==profesje[6])or(p==profesje[15])or(p==profesje[14])or(p==profesje[18])or(p==profesje[19])or(p==profesje[21])or(p==profesje[22])or(p==profesje[23])or(p==profesje[20])or(p==profesje[26])or(p==profesje[27])or(p==profesje[28])or(p==profesje[29])or(p == profesje[30])or(p==profesje[32])or(p==profesje[33])or(p==profesje[38])or(p==profesje[39])or(p==profesje[40])or(p==profesje[47])or(p==profesje[40])or(p==profesje[41])or(p==profesje[42])or(p==profesje[46])or(p == profesje[49])or(p==profesje[50])or(p ==profesje [55])or(p==profesje[56])or(p ==profesje [58]):
                    return p

class Imie(Profesja,Plec):
    def IMIE(self):
        imie_czlowiek_kobieta_1 = ["Abbie", "Abighild", "Abigund", "Abigunda",
                                   "Ada", "Adel", "Adelind", "Adeline", "Adelyn", "Adelle",
                                   "Agathe", "Agnete",
                                   "Aldreda", "Alfreda", "Alicia", "Allane", "Althea",
                                   "Amalie", "Amalinde", "Amalyn",
                                   "Anhilida", "Annabella", "Anna", "Anthea",
                                   "Arabella",
                                   "Avera",
                                   "Bechilda", "Bella", "Bellane", "Benedicta", "Berlinda", "Betlyn",
                                   "Bertha", "Berthilda", "Bess", "Beth",
                                   "Broncea", "Brunhilda",
                                   "Camilla", "Carla", "Carlinda", "Carlotta",
                                   "Cilicia", "Cilie",
                                   "Clora", "Clothilda",
                                   "Connie", "Constance", "Constanza", "Cordelia",
                                   "Dema", "Demona", "Desdemona",
                                   "Dorthilda",
                                   "Drachena", "Drachilda",
                                   "Edhilda", "Edith", "Edyth", "Edythe",
                                   "Eleanor", "Elinor", "Elisinda", "Elsina", "Ella", "Ellene", "Ellinde",
                                   "Eloise", "Elsa", "Elsbeth", "Elspeth", "Elyn",
                                   "Emagunda", "Emelia", "Emme", "Emmalyn", "Emmanuel", "Emerlinde",
                                   "Emerlyn",
                                   "Erica", "Ermina", "Erminlind", "Ermintrude",
                                   "Esmaralda", "Estelle",
                                   "Etheldreda", "Ethelinda", "Ethelind", "Ethelreda",
                                   "Fay",
                                   "Fried", "Friedhilda", "Friedrun", "Fredrica",
                                   "Gabby", "Gabriele", "Galina",
                                   "Gena", "Genevieve", "Genoveva", "Gerberga", "Gerda", "Gerlinde",
                                   "Gertie", "Gertrud",
                                   "Greta", "Gretchen", "Grizelda", "Grunhilda",
                                   "Gudrun", "Gudryn",
                                   "Hnna",
                                   "Hedwig", "Heidi", "Heidrun", "Helga", "Herlinde", "Herwig",
                                   "Hilda", "Hildegart", "Hildegund",
                                   "Honoria",
                                   "Ida",
                                   "Ingrid", "Ingrun", "Ingrund",
                                   "Irmellda", "Irmine",
                                   "Isabella", "Isadora", "Isolde",
                                   "Jocelin", "Johanna", "Josie",
                                   "Karin", "Katarine", "Katheryn", "Katharina", "Katerine", "Keterlind",
                                   "Keterlyn",
                                   "Kitty",
                                   "Kristen", "Kristena", "Kristyn",
                                   "Kirsten", "Kirstyn",
                                   "Lavina", "Lavinia,",
                                   "Lenora", "Leanora", "Leticia", "Letty", "Lena", "Lenora",
                                   "Lisa", "Lisbeth", "Lizzie",
                                   "Lorinda", "Lornda",
                                   "Lucinda", "Lucretia", "Lucie", "Ludmilla",
                                   "Mabel", "Madge", "Magdalyn", "Maggie", "Maghilda", "Maglind",
                                   "Maglyn", "Magunda", "Magreta", "Maida", "Marien", "Marietta",
                                   "Margaret", "Marget", "Margreta", "Marline", "Marlyn", "Mathilda",
                                   "Maude", "May",
                                   "Meg", "Melicent",
                                   "Miranda",
                                   "Moll",
                                   "Nathilda", "Nellie", "Nora", "Olga", "Ophelia", "Osterhild",
                                   "Ostelle", "Ostia", "Ottagunda", "Ottaline", "Ottilda", "Ottilyn",
                                   "Perdita", "Pergale", "Perginda", "Petronella", "Philomelia",
                                   "Reikhilda", "Renata", "Rosabel", "Rosabella", "Rosale", "Rosalia",
                                   "Rosalin", "Rosalinde", "Rosamunde", "Rosanne", "Rose", "Roz",
                                   "Rozhilda", "Salina", "Saltza", "Sigismunda", "Sigrid", "Sigunda",
                                   "Solla", "Styrine", "Talima", "Theodora", "Therese", "Tilea", "Ursula",
                                   "Ulrica", "Valeria", "Verena", "Wilfreda", "Wilhelmina", "Winifred",
                                   "Wolfhilde", "Zemelda", "Zena"]
        imie_czlowiek_mezczyzna_1 = ["Abelhard", "Abelhelm", "Admund", "Adred", "Adric", "Agis", "Alatic",
                                     "Alberic", "Albrecht", "Aldebrand", "Alderd", "Aldric", "Alfreid",
                                     "Altmar", "Alric", "Andre", "Andred", "Andric", "Anshelm", "Anton",
                                     "Arne", "Arnulf", "Axel", "Axlebrand", "Baldred", "Baldric",
                                     "Baldwin", "Balthasam", "Barnabas", "Bart", "Bartolf", "Bartomar",
                                     "Bernolt", "Bertold", "Bertolf", "Boris", "Bruno", "Burgolf",
                                     "Calvin", "Casimir", "Caspar", "Cedred", "Condrad", "Corwin",
                                     "Dagmar", "Dankmar", "Dankred", "Dekmar", "Detlef", "Diebold",
                                     "Diel", "Dietfried", "Dieter", "dietmar", "Dietmund", "Dietrich",
                                     "Dirk", "Donat", "Durnhelm", "Eber", "Eckel", "Eckhart", "Edgar",
                                     "Edmund", "Edwin", "Ehrhart", "Ehrl", "Ehrwig", "Eldred", "Elmeric",
                                     "Emil", "Engel", "Engelbert", "Engelbrecht", "Engelhart", "Eodred",
                                     "Eomund", "Erdman", "Erdred", "Erkenbrand", "Erasmus", "Erich",
                                     "Erman", "Ernst", "Erwin", "Eugen", "Eustasius", "Ewald", "Fabian",
                                     "Faustus", "Felix", "Ferdinand", "Fleugweiner", "Fosten", "Franz",
                                     "frediger", "fredric", "Frebalt", "Fredtich", "Fulko", "Gawin",
                                     "Gerber", "Gerhart", "Gerlach", "Gernar", "Gerolf", "Gilbrecht",
                                     "Gisbert", "Giselbrecht", "Gismar", "Goran", "Gosbert", "Goswin",
                                     "Gotfried", "Gothard", "Gottolf", "Gotwin", "Gregor", "Graimold",
                                     "Grimwold", "Griswold", "Guidom", "Gundolf", "Gundred", "Gunnar",
                                     "Gunter", "Gunther", "Gustaf", "Hadred", "Hadwin", "Hagar", "Hagen",
                                     "Haldred", "Halman", "Hamlyn", "Hans", "Halbrand", "Hartmann",
                                     "Harman", "Haug", "Heidric", "Heimar", "Heinfried", "Heinman",
                                     "Heinrich", "Heinz", "Helmut", "Henlyn", "Hermann", "Herwin",
                                     "Hieronymus", "Hildebart", "Hildebrand", "hildemar", "Hildemund",
                                     "Hildbred", "Hidric", "Horst", "Hugo", "Igor", "Ingwald", "Jander",
                                     "Jekil", "Jodokus", "Johann", "Jonas", "Jorg", "Jorn", "Josef",
                                     "Jost", "Jurgen", "Karl", "Kaspar", "Klaus", "Kleber", "Konrad",
                                     "Konradin", "Kurt", "Lamprecht", "Lanfried", "Lanric", "Lanwin",
                                     "Leo", "leopold", "Lewin", "Liebert", "Liebrecht", "Liebwin",
                                     "Lienhart", "Linus", "Lodwig", "Lothar", "Lucius", "Ludwig",
                                     "Luitpold", "Lukas", "Lupold", "Lupus", "Luther", "Lutolf", "Madred",
                                     "MAgnus", "Mandred", "Manfred", "Mathias", "Max", "Maximillian",
                                     "Meiner", "Meinhart", "Meinolf", "Mekel", "Merkel", "Nat",
                                     "Nathandar", "Nicodemus", "Odamar", "Odric", "Odwin", "Olbrecht",
                                     "Oldred", "Oldric", "Ortlieb", "Ortolf", "Orwin", "Oswald", "Osric",
                                     "Oswin", "Otfried", "Otto", "Otwin", "Paulus", "Prospero", "Ragen",
                                     "Ralf", "Rambrecht", "Randulf", "Ranulf", "Ranald", "Reikhard",
                                     "Rein", "Reiner", "Reinhard", "Reinolt", "Reuban", "Rigo", "Roderic",
                                     "Rolf", "Ruben", "Rudel", "Rudgar", "Rudolf", "Rufus", "Ruprecht",
                                     "Sebasitan", "Semund", "Sepp", "Siger", "Siegfried", "Siegmund",
                                     "Sigismund", "Sigric", "Steffan", "Tankred", "Theoderic", "Tilmann",
                                     "Tomas", "Trubald", "Trubert", "Udo", "Ulli", "Elfred", "Ulfman",
                                     "Ulman", "Uto", "Valdred", "Valdric", "Varl", "Viggo", "Viktor",
                                     "Vilmar", "Volker", "Volkhard", "Volkrad", "Volkin", "Voltz",
                                     "Walbrecht", "Waldor", "Waldred", "Walther", "Warmund", "Werner",
                                     "Wilbert", "Wilfried", "Wilhelm", "Woldred", "Wolfram", "Wolfhart",
                                     "Wolfgang", "Wulf", "Xavier"]
        imie_elf_1 = ["Aed", "Ael", "Aelf", "Aen", "Aeth", "Alth", "An", "And", "Ar", "Arg", "Ast", "Ath",
                      "Av", "Ban", "Bel", "Beth", "Cad", "Cael", "Caem", "Caeth", "Cal", "Cam", "Cel",
                      "Cirt", "El", "Eld", "Elt", "En", "End", "Er", "Ers", "Fand", "Fer", "Ferg", "Fim",
                      "Fin", "Gal", "Gald", "Gaen", "Gaes", "Ged", "Gen", "Ges", "Geth", "Glor", "Has",
                      "Hath", "Hel", "Heth", "Hilth", "Ill", "Ind", "Ist", "Ith", "Iy", "Kor", "Ky",
                      "Kyr", "La", "Lan", "Lil", "Lim", "Lith", "Loth", "Mal", "Mar", "Mas", "Math", "Me",
                      "Mes", "Meth", "Men", "Mor", "Mort", "Nal", "Nar", "Nen", "Nor", "Norl", "Ri",
                      "Riabb", "Riann", "Rid", "Riell", "Rien", "Ruth", "Ryn", "Tab", "Tal", "Tan", "Tar",
                      "Teth", "Tel", "Tor", "Ty", "Ul", "Um", "Ur", "Yr", "Yv"]
        imie_elf_lacznik = ["A", "Al", "An", "Ar", "As", "E", "El", "En", "Er", "Es", "Fan", "Fin", "I",
                            "Il", "In", "Ir", "Is", "O", "Ol", "On", "Or", "Os", "Ra", "Ral", "Ran", "Re",
                            "Rel", "Ren", "Ri", "Ril", "Rin", "Ro", "Rol", "Ron", "Ry", "Sa", "Sal",
                            "San", "Se", "Sel", "Sen", "Si", "Sil", "Sin", "So", "Sol", "Son", "U", "Ul"]
        imie_elf_kobieta_2 = ["A", "Aine", "Am", "Ann", "Arma", "Arna", "Arth", "Ath", "Beann", "Bet",
                              "Beth", "Brim", "Brys", "Deann", "Det", "Deth", "Dys", "Drian", "Driel",
                              "Drys", "Eann", "Eanna", "Earna", "Earth", "Elle", "Eth", "Eys", "eyth",
                              "Felle", "Fionn", "Flys", "Fyll", "Fynn", "Fyr", "Feys", "I", "Ille", "Ina",
                              "Ira", "Isa", "Ithi", "Itt", "La", "Lam", "Lana", "Larna", "Lath", "Leann",
                              "Leath", "Lel", "Lelle", "Leth", "Let", "Lielle", "Lieth", "Leann", "Nelle",
                              "Nem", "Neth", "Ni", "Niell", "Niella", "Nith", "Ras", "Reann", "Rell",
                              "Relle", "Rielle", "Ris", "Rith", "Rys", "Sar", "Sath", "Ser", "Seth",
                              "Sir", "Sith", "Sor", "Soeth", "Shar", "Sher", "Shir", "Sys", "Tar", "Teal",
                              "Teann", "Ter", "Thea", "Ther", "Thi", "Thryn", "Thyn", "Tir", "Tor", "Tos",
                              "Trean", "Tys", "Yll", "Yrs", "Ys"]
        imie_elf_mezczyzna_2 = ["Baem", "Naine", "Baire", "Bar", "Byhir", "Brier", "Brior", "Brin",
                                "Daen", "Daine", "daire", "Dar", "Dhil", "Dhir", "Grel", "Drir", "Dror",
                                "Eorl", "Eos", "Eoth", "Fil", "Fin", "Fir", "Hil", "Hin", "Hir", "Hor",
                                "Il", "In", "Ion", "Ir", "Is", "Ith", "Lael", "Laen", "Laer", "Laine",
                                "Laire", "Lan", "Las", "Len", "Les", "Lil", "Lin", "Lior", "Lis", "Lor",
                                "Los", "Mael", "Maen", "Mair", "Main", "Mal", "Mar", "Mil", "Min", "Mir",
                                "Nael", "Naen", "Ner", "Nail", "Nair", "Nal", "Nan", "Nar", "Neal",
                                "Nean", "Near", "Nil", "Nin", "Nir", "Nis", "Ran", "Rea", "Rel", "Ril",
                                "Riol", "Rion", "Rior", "Riorl", "Riorn", "Rir", "ryl", "Taen", "Tair",
                                "Tain", "Than", "Thar", "Thel", "Thil", "Thir", "Thin", "Thril", "Thrin",
                                "Thwe", "Til", "Tin", "Tis", "We", "Yan"]
        imie_krasnolud_1 = ["Al", "Ath", "Athran", "Bal", "Bala", "Bara", "Bel", "Bela", "Ber", "Bok",
                            "Bor", "Bur", "Da", "Dam", "Dora", "Drok", "Drong", "Dur", "Dwal", "El",
                            "Ela", "Elan", "Elda", "Fa", "Far", "Fara", "Fim", "Fima", "Firen", "Fur",
                            "Fura", "Ga", "Gim", "Gol", "Gollen", "Got", "Gota", "Grim", "Gro", "Grun",
                            "Hak", "Haka", "Har", "Hega", "Hur", "Kad", "Kar", "Kata", "Kaz", "Kaza",
                            "Krag", "Logaz", "Lok", "Lun", "Mo", "Mola", "Mor", "Mora", "No", "Nola",
                            "Nor", "Noran", "Nun", "Oda", "Oka", "Olla", "Olf", "Oth", "Othra", "Ro",
                            "Ror", "Roran", "Ska", "Skalla", "Skalf", "Skar", "Skor", "Skora", "Snor",
                            "Sora", "Sven", "Thar", "Thor", "Thora", "Thron", "Thrun", "Thura", "Un",
                            "Utha", "Ulla", "Vala", "Var", "Vara", "Zak", "Zaka", "Zakan", "Zar", "Zara",
                            "Zam", "Zama"]
        imie_krasnolud_kobieta_2 = ["Bina", "Bora", "Dila", "Dina", "Dotina", "Dora", "Drinella", "Fina",
                                    "Fya", "Gana", "Gara", "Gella", "Gina", "Groma", "Grondella",
                                    "Grotha", "Gruma", "Grunda", "Gruntina", "Gona", "Gora", "Grimella",
                                    "Grina", "Gromina", "Gula", "Gunella", "Gundina", "Kina", "Kragella",
                                    "Krina", "Kya", "Lina", "Likina", "Loka", "Luna", "Mina", "Mira",
                                    "Nina", "Nira", "Nya", "Ragina", "Riga", "Rika", "Rina", "Runa",
                                    "Runella", "Skina", "Skinella", "Tina", "Toka", "trekella", "Trekina",
                                    "Troka", "Zina", "Zora"]
        imie_krasnolud_mezczyzna_2 = ["Bin", "Bor", "Dil", "Din", "Dok", "Dor", "Drin", "Fin", "Gan",
                                      "Gar", "Gil", "Gin", "Gni", "Grom", "Grond", "Groth", "Grum",
                                      "Grund", "Grunt", "Gon", "Gor", "Grin", "Grim", "Gul", "Gun",
                                      "Gund", "Ki", "Kin", "Krak", "Kri", "Krin", "Li", "Lin", "Lik",
                                      "Lok", "Lun", "Min", "Mir", "Nin", "Nir", "Rag", "Ri", "Rig", "Rik",
                                      "Rin", "Run", "Skin", "Tim", "Tok", "Trek", "Trok", "Zin", "Zor"]
        imie_niziolek_1 = ["Bag", "Balf", "Berc", "Bill", "Bobb", "Bodg", "Bog", "Bom", "Bonn", "Brog",
                           "Bulc", "Bull", "Bust", "Cam", "Cap", "Ced", "Chund", "Clog", "Clof", "Cob",
                           "Cog", "Crum", "Crump", "Curl", "Dod", "Dog", "Dott", "Dram", "Drub", "Drog",
                           "Dron", "Durc", "Elm", "Enn", "Ermin", "Ethan", "Falc", "Fald", "Falm", "Far",
                           "Fild", "Flac", "Fogg", "Frit", "Ful", "Func", "Gaff", "Galb", "Gamm", "Gert",
                           "Giff", "Gild", "Gon", "Grop", "Gudd", "Gump", "Ham", "Hal", "Hart", "Harp",
                           "Jac", "Jas", "Jasp", "Joc", "Lac", "Lil", "Lob", "Lott", "Lud", "Lurc", "Mad",
                           "Mag", "Man", "May", "Mer", "Mul", "Murc", "Murd", "Nag", "Nell", "Nobb", "Od",
                           "Og", "Old", "Pipp", "Podd", "Porc", "Riff", "Rip", "Rob", "Sam", "Supp",
                           "Taff", "Talb", "Talc", "Tay", "Tom", "Wald", "Watt", "Will"]
        imie_niziolek_kobieta_2 = ["A", "Adell", "Alot", "Apple", "Bell", "Berr", "Eena", "Ella", "Era",
                                   "Et", "Ia", "Flower", "Lotta", "Petal", "Riella", "Sweet", "Trude",
                                   "Rose", "Willow", "Y"]
        imie_niziolek_mezczyzna_2 = ["Belly", "Er", "Fast", "In", "It", "Mutch", "O", "Odoc", "Riadoc",
                                     "Regar", "Wick", "Wise", "Wit", "Y"]
        a = "kobieta"
        b = "mezczyzna"
        czlowiek="czlowiek"
        elf = "elf"
        krasnolud = "krasnolud"
        niziolek = "niziolek"
        if (plec == a.upper())or (plec == a.lower()):
            if (rasa == czlowiek.upper())or(rasa == czlowiek.lower()):
                imie_human = random.choice(imie_czlowiek_kobieta_1)
                return imie_human
            if (rasa == elf.upper())or(rasa == elf.lower()):
                imie_elf_a = random.choice(imie_elf_1)
                imie_elf_b = random.choice(imie_elf_lacznik)
                imie_elf_c = random.choice(imie_elf_kobieta_2)
                return imie_elf_a+imie_elf_b+imie_elf_c
            if (rasa == krasnolud.upper())or(rasa == krasnolud.lower()):
                imie_krasnolud_a = random.choice(imie_krasnolud_1)
                imie_krasnolud_b = random.choice(imie_krasnolud_kobieta_2)
                return imie_krasnolud_a+imie_krasnolud_b
            if (rasa == niziolek.upper())or(rasa == niziolek.lower()):
                imie_niziolek_a = random.choice(imie_niziolek_1)
                imie_niziolek_b = random.choice(imie_niziolek_kobieta_2)
                return imie_niziolek_a+imie_niziolek_b

        if (plec == b.upper())or(plec == b.lower()):
            if (rasa == czlowiek.upper()) or (rasa == czlowiek.lower()):
                imie_human = random.choice(imie_czlowiek_mezczyzna_1)
                return imie_human
            if (rasa == elf.upper())or(rasa == elf.lower()):
                imie_elf_a = random.choice(imie_elf_1)
                imie_elf_b = random.choice(imie_elf_lacznik)
                imie_elf_c = random.choice(imie_elf_mezczyzna_2)
                return imie_elf_a + imie_elf_b + imie_elf_c
            if (rasa == krasnolud.upper()) or (rasa == krasnolud.lower()):
                imie_krasnolud_a = random.choice(imie_krasnolud_1)
                imie_krasnolud_b = random.choice(imie_krasnolud_mezczyzna_2)
                return imie_krasnolud_a + imie_krasnolud_b
            if (rasa == niziolek.upper())or(rasa == niziolek.lower()):
                imie_niziolek_a = random.choice(imie_niziolek_1)
                imie_niziolek_b = random.choice(imie_niziolek_mezczyzna_2)
                return imie_niziolek_a+imie_niziolek_b

class Cechy(Imie):
    def CECHY(self):
        tab =[]
        czlowiek = "czlowiek"
        elf = "elf"
        krasnolud = "krasnolud"
        niziolek = "niziolek"

        if (rasa == czlowiek.upper())or(rasa == czlowiek.lower()):
            zycie = [10, 11, 12, 13]
            for x in range(7):
                tab.append(random.randrange(1, 10, 1)+random.randrange(1, 10, 1)+20)
            tab.append(1)
            tab.append(random.choice(zycie))
            tab.append(int(tab[2] / 10))
            tab.append(int(tab[2] / 10))
            tab.append(4)
            tab.append(0)
            tab.append(0)
            tab.append(0)
            return tab
        if (rasa == elf.upper())or(rasa == elf.lower()):
            zycie = [9,10,11,12]
            for x in range(7):
                tab.append(random.randrange(1, 10, 1)+random.randrange(1, 10, 1)+20)
                if (x == 1)or(x == 4):
                    tab.append(random.randrange(1, 10, 1) + random.randrange(1, 10, 1) + 30)
            tab.append(1)
            tab.append(random.choice(zycie))
            tab.append(int(tab[2] / 10))
            tab.append(int(tab[2] / 10))
            tab.append(5)
            tab.append(0)
            tab.append(0)
            tab.append(0)
            return tab
        if (rasa == krasnolud.upper())or(rasa == krasnolud.lower()):
            zycie = [11, 12, 13, 14]
            for x in range(7):
                tab.append(random.randrange(1, 10, 1) + random.randrange(1, 10, 1) + 20)
                if (x == 0) or (x == 3):
                    tab.append(random.randrange(1, 10, 1) + random.randrange(1, 10, 1) + 30)
                if (x == 4) or (x == 7):
                    tab.append(random.randrange(1, 10, 1) + random.randrange(1, 10, 1) + 10)
            tab.append(1)
            tab.append(random.choice(zycie))
            tab.append(int(tab[2] / 10))
            tab.append(int(tab[2] / 10))
            tab.append(3)
            tab.append(0)
            tab.append(0)
            tab.append(0)
            return tab
        if (rasa == niziolek.upper())or(rasa == niziolek.lower()):
            zycie = [8, 9, 10, 11]
            for x in range(7):
                tab.append(random.randrange(1, 10, 1) + random.randrange(1, 10, 1) + 20)
                if (x == 4) or (x == 7) or(x == 1):
                    tab.append(random.randrange(1, 10, 1) + random.randrange(1, 10, 1) + 30)
                if (x == 0) or (x == 2) or (x == 3):
                    tab.append(random.randrange(1, 10, 1) + random.randrange(1, 10, 1) + 10)
            tab.append(1)
            tab.append(random.choice(zycie))
            tab.append(int(tab[2] / 10))
            tab.append(int(tab[2] / 10))
            tab.append(4)
            tab.append(0)
            tab.append(0)
            tab.append(0)
            return tab



con = sqlite3.connect('Postac.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

Klasa_1 = Plec()
Klasa_2 = Rasa()
Klasa_3 = Profesja()
Klasa_4 = Imie()
Klasa_5 = Cechy()
plec = Klasa_1.PLEC()
rasa = Klasa_2.RASA()
profesja = Klasa_3.PROFESJA()
imie = Klasa_4.IMIE()
cechy = Klasa_5.CECHY()
#print (Klasa_1.PLEC())
#print (Klasa_2.RASA())

#print (Klasa_3.PROFESJA())
#print (Klasa_4.IMIE())
#print (Klasa_5.CECHY())

#cur.execute("DROP TABLE IF EXISTS postac")

cur.execute("""CREATE TABLE IF NOT EXISTS postac (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            imie TEXT ,
            rasa TEXT ,
            plec TEXT ,
            profesja TEXT )""")

#cur.execute("DROP TABLE IF EXISTS cechy")
cur.execute("""CREATE TABLE IF NOT EXISTS cechy(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            WW int NULL,
            US int NULL,
            K int NULL,
            Odp int NULL,
            Zr int NULL,
            Int int NULL,
            SW int NULL,
            Ogd int NULL,
            A int NULL,
            Zyw int NULL,
            S int NULL,
            Wt int NULL,
            Sz int NULL,
            Mag int NULL,
            PO int NULL,
            PP int NULL)""")



cur.execute('INSERT INTO cechy VALUES(NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);', (cechy[0],cechy[1],cechy[2],cechy[3],cechy[4],
            cechy[5],cechy[6],cechy[7],cechy[8],cechy[9],cechy[10],cechy[11],
            cechy[12],cechy[13],cechy[14],cechy[15]))

postac = {"Imie":[imie],
          "Rasa":[rasa],
          "Plec":[plec],
          "Profesja":[profesja],
        "WW":[cechy[0]],"US":[cechy[1]],"K":[cechy[2]],"Odp":[cechy[3]],"Zr":[cechy[4]],"Int":[cechy[5]],"SW":[cechy[6]],
        "Ogd":[cechy[7]],"A":[cechy[8]],"Zyw":[cechy[9]],"S":[cechy[10]],"Wt":[cechy[11]],"Sz":[cechy[12]],"Mag":[cechy[13]],
        "PO":[cechy[14]],"PP":[cechy[15]]}



cur.execute('INSERT INTO postac  VALUES(NULL, ?, ?, ?, ?);', (imie,rasa,plec,profesja))
con.commit()