
class subsection:
    def __init__(self, name="", content="", type=1):
        self.name = name
        self.content = content
        self.subsubsections = []
        self.type = type
    def addcontent(self,content=""):
        self.content = content
    def addsubsubsection(self,s):
        self.subsubsections.append(s)
    def addimage(self,i):
        self.content += i.getcontent()
    def newpage(self):
        self.content += "\n\\newpage\n"
    def newline(self):
        self.content += "\n\\newline\n"