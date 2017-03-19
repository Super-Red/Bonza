'''
Author:     Super_Red
Date:       3/3/2017
Describe:   Search English words from the dataset for the game "Bonza"
'''

class Bonza(object):

    def __init__(self, fileName="vocabulary.txt"):
        self.dataSet = self.getDataSet(fileName)

    def getDataSet(self, fileName):
        dataSet = {}
        # if "\ufeff" appears in the first line, alter the encoding into "utf-8_sig"
        with open(fileName, encoding="utf-8_sig") as file:
            for line in file.readlines():
                lineArr = line.strip().split()
                dataSet[lineArr[0].lower()] = lineArr[1:]
        return dataSet

    def findWords(self, *snip):
        result = []
        snippets = list(snip)
        for word in self.dataSet.keys():
            if len(snippets) == len([snippet for snippet in snippets if snippet in word]):
                result.append([word, self.dataSet[word]])
        for i in result:
            print(i)

    def addWordsFromFile(self, fileName):
        existingWords = set(self.dataSet.keys())
        with open(fileName, encoding="utf-8") as supfile:
            supplement = [line.strip().split(" ") for line in list(supfile.readlines())]
        words2write = [word + ["\n"] for word in supplement]
        with open("vocabulary.txt", "a", encoding="utf-8_sig") as file:
            for word in words2write:
                if word[0] not in existingWords:
                    file.write("   ".join(word))
                    existingWords.add(word[0])

a = Bonza()






