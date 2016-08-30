# Documentation for the character creator

## dices.py

The dices.py file is the first file in the creation

It creates the class called combination which takes the throw as a string, in the input type as: constant+xdy+zdw...
It's functions are:
- self.do(): actually throws the necessary dice combination
- self.statistics(plot=bool,average=bool): creates all the possible throw combinations in a dump file. This can be plotted by setting plot to be true. Other functionalites will be incoming in the future
- sel.manythrows(plot:Bool,throws:int): does the throw throws number of times
