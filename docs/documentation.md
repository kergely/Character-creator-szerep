# Documentation for the character creator

This documentation documents the contents of the Mythras character creator.

## src.dices

The dices.py file is the first file in the creation

It creates the class called combination which takes the throw as a string, in the input type as: constant+xdy+zdw...
Initialization is done be giving a string in the type of xdy+z
It's functions are:
- self.do(): actually throws the necessary dice combination
- self.statistics(plot=bool,average=bool): creates all the possible throw combinations in a dump file. This can be plotted by setting plot to be true. Other functionalites will be incoming in the future
- self.manythrows(plot:Bool,throws:int): does the throw throws number of times. If plot is True then plots a histogram using pythons matplotlib

It is now a module, which can be called as src.dices from main.

### src.skills

The skills file is meant to be the creator of the skills, which later characters can draw upon.
The file first creates the _skill_ class, which is used to store the skills.
Two dictionaries are added by the program which are used as global variables in later runs of the module. The first one is _standardlist_ which contains all the STANDARD skills, why the similarly named _professionallist_ contains the PROFESSIONAL skills.
These dictionaries are 
