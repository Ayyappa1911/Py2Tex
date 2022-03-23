

class section:
    def __init__(self,name = "",content=""):
        self.name = name
        self.content = content
        self.subsections = []
        # self.subsubsections = []
        #self.images = []
    def addcontent(self,content=""):
        self.content = content
    def addsubsection(self,s1):
        self.subsections.append(s1)
    def addimage(self,i):
        # self.images.append(i)
        self.content += i.getcontent()
    