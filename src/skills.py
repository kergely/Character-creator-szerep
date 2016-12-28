import dices


class skill(object):
    """
    Contains a skill.
    calling is done by skill(bases,value,known=True)
    bases::string : attributes it depends on. (either ABCx2 or ABC+XYZ format)
    value: value of the skill. If left empty, standard is calculated.
    known: whether the skill is known by the charcter. --> TODO remove

    study(learned) --> learned is added to the value of the skill.
    learn --> teaches the charcter the learned skills
    """

    def __init__(self, bases, value=0, encaffect=True):
        super(skill, self).__init__()
        self.base = ["", ""]
        self.base[1] = bases[:3]
        if bases[4] == x:
            self.base[2] = self.base[1]
        else:
            self.base[2] = bases[:-3]
        self.known = known
        if self.known is True:
            self.value = value
        else:
            self.value = None
    self.encaffect = encaffect

    def basevalue(self, inp):
        self.value = inp  # TODO decide how to do this

    def study(self, learned):
        self.value += learned

    # def learn(self):
    #     self.known = True

# now the skills as a class is generated
# the next step is creating all the skills
# TODO: decide the way to implement this --> chose a special dictionary

standardlist = dict{"Athletics": skill("STR+DEX")
                    "Boating": skill("STR+CON")
                    "Brawn": skill("STR+SIZ")
                    "Conceal": skill("DEX+POW")
                    "Customs": skill("INTx2", encaffect=False)
                    "Dance": skill("DEX+CHA")
                    "Deceit": skill("INT+CHA", encaffect=False)
                    "Drive": skill("DEX+POW")
                    "Endurance" = skill("CONx2", encaffect=False)
                    "Evade": skill("DEXx2")
                    "FirstAid": skill("INT+DEX")
                    "Influence": skill("CHAx2", encaffect=False)
                    "Insight": skill("INT+POW", encaffect=False)
                    "Locale" = skill("INTx2", encaffect=False)
                    "Perception": skill("INT+POW", encaffect=False)
                    "Ride": skill("DEX+POW")
                    "Sing": skill("CHA+POW", encaffect=False)
                    "Stealth": skill("DEX+INT")
                    "Swim": skill("STR+CON")
                    "Unarmed": skill("STR+DEX")
                    "Willpower": skill("POWx2")
                    }

# standard is used to store the standard skills used in the Mythras franchise

professionallist = dict{}

# professionallist is used to store the professional skills in Mythras
# "Name" : [skill::skill,]


class knownskills(dict):
    """
    A dictionary with a few special powers
    """"

    def __init__(self, *args):
        super(knownskills, self).__init__()
        global standardlist
        global professionallist
        self.update(standardlist)  # creating the Standard skills
        for element in args:
            # TODO -> a catch-try method against misspelling
            # one shold be capable off adding, this is with the arguments
            self[element] = allskills[element]

    def learn(self, *args):
        global professionallist
        for element in args:
            # TODO -> a catch-try method against misspelling, can be copied
            # from the __init__ part
            # TODO also check whether it is already in
            self[element] = allskills[element]
