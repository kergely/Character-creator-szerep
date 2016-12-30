class item(object):
    """
    Contains an item
    TODO -> create a normal description
    """

    def __init__(self, name, value, ENC=0):
        super(item, self).__init__()
        self.name = name
        self.value = value
        self.ENC = ENC


class inventory(dict):
    """
    Contains items of the charcter
    """

    def __init__(self,):
        pass

    def sell(self, name, numbers):
        # TODO check if there are enough to be sold
        self[name]
        return self[name].value
