
class subsection:
    def __init__(self, name="", content=""):
        self.name = name
        self.content = content
        self.subsubsections = []
    def addcontent(self,content=""):
        self.content = content
    def addsubsubsection(self,s):
        self.subsubsections.append(s)
        # self.content += "\n\n\\subsubsection{"+s.name+"}\n"
        # self.content+=s.content+"\n"