import dices


class skill(object):
    """
    Contains a skill.
    calling is done by skill(bases,value,known=True)
    bases::string : attributes it depends on. (either ABCx2 or ABC+XYZ format)
    value: value of the skill. If left empty, standard is calculated.

    study(learned) --> learned is added to the value of the skill.
    learn --> teaches the charcter the learned skills
    """

    def __init__(self, bases, value=None, encaffect=True):
        super(skill, self).__init__()
        self.encaffect = encaffect
        self.value = value
        self.base = ["", ""]
        self.base[0] = bases[:3]
        if bases[3] == "x":
            self.base[1] = self.base[0]
        else:
            self.base[1] = bases[-3:]

    def basevalue(self, inp):
        self.value = 0
        self.value = inp  # TODO decide how to do this

    def study(self, learned):
        self.value += learned


# now the skills as a class is generated
# the next step is creating all the skills


standardlist = {
    "Athletics": skill("STR+DEX"),
    "Boating": skill("STR+CON"),
    "Brawn": skill("STR+SIZ"),
    "Conceal": skill("DEX+POW"),
    "Customs": skill("INTx2", encaffect=False),
    "Dance": skill("DEX+CHA"),
    "Deceit": skill("INT+CHA", encaffect=False),
    "Drive": skill("DEX+POW"),
    "Endurance": skill("CONx2", encaffect=False),
    "Evade": skill("DEXx2"),
    "FirstAid": skill("INT+DEX"),
    "Influence": skill("CHAx2", encaffect=False),
    "Insight": skill("INT+POW", encaffect=False),
    "Locale": skill("INTx2", encaffect=False),
    "Perception": skill("INT+POW", encaffect=False),
    "Ride": skill("DEX+POW"),
    "Sing": skill("CHA+POW", encaffect=False),
    "Stealth": skill("DEX+INT"),
    "Swim": skill("STR+CON"),
    "Unarmed": skill("STR+DEX"),
    "Willpower": skill("POWx2"),
}

# standard is used to store the standard skills used in the Mythras franchise

professionallist = {
    "Acrobatics": skill("STR+ DEX"),
    "Art": skill("POW+CHA"),
    "Bureaucracy": skill("INTx2"),
    "Commerce": skill("INT+CHA"),
    "Courtesy": skill("INT+CHA"),
    "Craft": skill("DEX+INT"),
    "Culture": skill("INTx2", encaffect=False),
    "Devotion": skill("POW+CHA"),
    "Disguise": skill("INT+CHA"),
    "Engineering": skill("INTx2"),
    "Exhort": skill("INT+CHA"),
    "Folk Magic": skill("POW +CHA"),
    "Gambling": skill("INT+POW"),
    "Healing": skill("INT+POW"),
    "Language": skill("INT+CHA", encaffect=False),
    "Literacy": skill("INTx2"),
    "Lockpicking": skill("DEXx2"),
    "Lore": skill("INTx2"),
    "Mechanisms": skill("DEX+INT"),
    "Musicianship": skill("DEX+CHA"),
    "Navigation": skill("INT+POW"),
    "Oratory": skill("POW+CHA"),
    "Seamanship": skill("INT+CON"),
    "Seduction": skill("INT+CHA"),
    "Sleight": skill("DEX+CHA"),
    "Streetwise": skill("POW+CHA"),
    "Survival": skill("CON+POW"),
    "Teach": skill("INT+CHA"),
    "Track": skill("INT+CON"),
}

# professionallist is used to store the professional skills in Mythras
# "Name" : [skill::skill]


class knownskills(dict):
    """
    A dictionary with a few special powers
    """

    def __init__(self, *args):
        super(knownskills, self).__init__()
        global standardlist
        global professionallist
        self.update(standardlist)  # creating the Standard skills
        for element in args:
            # one shold be capable off adding, this is with the arguments
            try:
                self[element] = professionallist[element]
            except KeyError as hiba:
                msg = str(hiba) + \
                    "is not a recognized professional skill in Mythras"
                print msg
                print "It was not added to the list of skills"
            except:
                print "Something went wrong"
                print element + " was not added to the list of skills"
            # this handled the input errors

    def learn(self, *args):
        global professionallist
        for element in args:
            if element in self:
                print element, "is already in the learned skills list", \
                    ", it was not added to protect the value"
            else:
                try:
                    self[element] = professionallist[element]
                except KeyError as hiba:
                    msg = str(hiba) + \
                        "is not a recognized professional skill in Mythras"
                    print msg
                    print "It was not added to the list of skills"
                except:
                    print "Something went wrong"
                    print element + " was not added to the list of skills"
            # this handled the input errors
            self[element] = professionallist[element]

# test = knownskills("Disguise")
# test.learn("Lore")
# print test["Swim"].base
# print test["Disguise"].base
# print test["Lore"].base
