import random
import matplotlib.pyplot as plt
# necessary packages

def throwdice(dicetype,thrownumber=1):
    """ Throws dice """
    value=0
    # # if thrownumber==1:
    # #     value=random.randint(0,dicetype)
    # elif thrownumber > 1:
    for i in range(1,thrownumber+1):
        value=value+random.randint(0,dicetype)
    return value

# begin diagnostics of dicethrows in game
# known

class combination(object):
    """Combination is a type of throw."""
    def __init__(self, whattothrow):
        self.whattothrow = whattothrow
        self.content = {}
        i=0
        textoconvert=""
        for letter in self.whattothrow:
            if letter == "+":
                if ("d" in textoconvert):
                    self.content[self.whattothrow[i+1]]=int(self.whattothrow[i-1])
                else:
                    self.content['constant']=int(textoconvert)
                textoconvert=""
            else:
                textoconvert+=letter
            i=i+1
        #if textoconvert == self.whattothrow:
        i=i-2 # to get back to the part unended by +
        self.content[self.whattothrow[i+1]]=int(self.whattothrow[i-1])

    def do(self):
        summa=0
        for dice in self.content.keys():
            if dice=="constant":
                summa += self.content["constant"]
            else:
                summa+=throwdice(int(dice),self.content[dice])
        return summa

    def statistics(self,plot=False,average=False):
        # this generating is going to done recursively
        dump=[0] # this is the easisest way to generate a histogram
        for dices in self.content.keys():
            if dices=="constant":
                i=0
                for element in dump:
                    dump[i] += self.content["constant"]
                    i=i+1
            else:
                top=1+int(self.content[dices])
                for throws in range(1,top):
                    # now begins the recursive function
                    i=0
                    toadd=[]
                    for element in dump:
                        dump[i] += 1
                        i=i+1 # one is added to the existing dump
                    i=0
                    for value in range(2,(int(dices)+1)):
                        for element in dump:
                            toadd.append(dump[i]+value-1)
                            i=i+1
                        i=0
                    dump=dump+toadd
        if plot==True:
            plt.hist(dump,normed=1)

    def manythrows(self,plot=False,throws=1000):
        #results=[]
        dump=[]
        for i in range(1,throws):
            throw=self.do()
            #results[self.do()]+=1
            dump.append(throw)
        if plot==False:
            #return results
            pass
        if plot==True:
            #return results
            plt.hist(dump,normed=1)
            #plt.show()
            #print dump

### class definition

STR=combination("3d6")
CON=combination("2d6+2d4")
INT=combination("6+2d6")

STR.statistics(plot=True)
CON.statistics(plot=True)
INT.statistics(plot=True)

plt.show()
