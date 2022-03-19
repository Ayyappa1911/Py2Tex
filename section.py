

class section:
    def __init__(self,name = "",content=""):
        self.name = name
        self.content = content
        self.subsections = []
        # self.subsubsections = []
    def addcontent(self,content=""):
        self.content = content
    def addsubsection(self,s1):
        self.subsections.append(s1)
        # self.content += "\n\n\\subsection{"+s.name+"}\n"
        # self.content+=s.content+"\n"
    




    
     