class item(object):
    """
    Contains an item
    name: name of the item
    value: value of the item
    ENC: is the encumberance of the item. If it's zero, it shold be left empty,
    not as a zero
    num: numbers of the item (normally zero)
    """

    def __init__(self, name, value, ENC=0.1, num=1):
        super(item, self).__init__()
        self.name = name
        self.value = value
        ENC = float(EN)
        if (ENC == 0.0):
            self.ENC = 0.1  # clearing up if ENC= zero is given
        else:
            self.ENC = float(ENC)
        self.num = num

    def more(self, howmany, add=False):
        self.num = self.howmany


class inventory(dict):
    """
    Contains items of the charcter
    is a dict where item names ar paired with an item. This is overkill
    (item name stored twice, but it is easy)
    """

    def __init__(self, *args):
        for item in args:
            if type(item) is item:
                self[item.name] = item
            else:
                print "Error, " + str(item) + " is not a valid item"
                print "it was therefore omitted"

    def sell(self, name, amount=1):
        # TODO check if there are enough to be sold
        if self[name].num > amunt:
            self[name].num -= amount
        else:
            # handled error of selling more than you have
            print "Error, you cannot sell that many items"
        return self[name].value * self[name].num

    def add(self, *args):
        for item in args:
            if type(item) is __main__.item:  # TODO make this work
                if self[item.name] in self:
                    self[item.name].num += item.num
                else:
                    self[item.name] = item
            else:
                print "Error, " + str(item) + " is not a valid item"

# testing area

fa = item("fa", 1)
print type(fa)
taska = inventory(fa)
