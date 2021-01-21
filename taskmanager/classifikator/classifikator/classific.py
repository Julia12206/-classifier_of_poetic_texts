from django.conf import settings
import  string
import numpy as np
import pickle
global svmClass

class ClassificPredict:

    def __init__(self):
        self.glass = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", "А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я"]

        self.modelCnnSavePath = settings.PATH_TO_MODEL
        with open(self.modelCnnSavePath, 'rb') as SmartModel:
            self.svmPredict = pickle.load(SmartModel)


    def TextObr(self, textAll):
        text = textAll.split("\n")
        slogy = ''
        countOfStr = len(text)
        znakPrep = 0
        zagLet = 0
        for m in range(countOfStr):
            liter = 0
            count = 0

            for l in range(len(text[m])):
                if text[m][l] in self.glass:
                    count += 1
                if text[m][l] in string.punctuation:
                    znakPrep = 1
                if text[m][l].isupper()==True:
                    zagLet = 1

            slogy = slogy + str(count) + " "
        if (countOfStr)<5:
            nuls = 5 - countOfStr
            for n in range(nuls):
                slogy = slogy+str(0)+" "
        if (countOfStr)>5:
            nuls = countOfStr - 5
            slogySp = ''
            slogyStrip = []
            slogyStrip = slogy.split(" ")
            slogySrez = slogyStrip[:5]
            for n in range(len(slogySrez)):
                slogySp = slogySp + slogySrez[n] + " "
            slogy = slogySp

        textVect = ''
        textVect = str(slogy)+str(countOfStr)+" "+str(zagLet)+" "+str(znakPrep)

        return textVect

    def Classific(self, text):
        while True:
            userEnt1 = text.split(" ")
            testValues = np.array(
                [[userEnt1[0], userEnt1[1], userEnt1[2], userEnt1[3], userEnt1[4], userEnt1[5], userEnt1[6], userEnt1[7]]],
                    float)
            svmClass = self.svmPredict.predict(testValues)
            return svmClass