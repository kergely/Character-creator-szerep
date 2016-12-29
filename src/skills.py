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
    "Culture": skill("INTx2"),
    "Devotion": skill("POW+CHA"),
    "Disguise": skill("INT+CHA"),
    "Engineering": skill("INTx2"),
    "Exhort": skill("INT+CHA"),
    "Folk Magic": skill("POW +CHA"),
    "Gambling": skill("INT+POW"),
    "Healing": skill("INT+POW"),
    "Language": skill("INT+CHA"),
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
            # TODO -> a catch-try method against misspelling
            # one shold be capable off adding, this is with the arguments
            self[element] = professionallist[element]

    def learn(self, *args):
        global professionallist
        for element in args:
            # TODO -> a catch-try method against misspelling, can be copied
            # from the __init__ part
            # TODO also check whether it is already in the skills list
            self[element] = professionallist[element]

# test = knownskills("Disguise")
# test.learn("Lore")
# print test["Swim"].base
# print test["Disguise"].base
# print test["Lore"].base
