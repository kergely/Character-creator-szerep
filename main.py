import src.dices as dices

number_to_compare=int(raw_input("How many throws do you want to compare? \n "))

inputs=[]
for i in range(0,number_to_compare):
    inputs.append(raw_input("What do you want to compare \n"))

for stuff in inputs:
    plotter=dices.combination(stuff)
    plotter.statistics(plot=True)

raw_input("Press enter to exit")
