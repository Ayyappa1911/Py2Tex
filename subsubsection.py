
class subsubsection:
    def __init__(self,name="",content="",type=1):
        self.name = name
        self.content = content
        self.type = type
    def addcontent(self,content=""):
        self.content += content
    def addimage(self,i):
        self.content += i.getcontent()
    def newpage(self):
        self.content += "\n\\newpage\n"
    def newline(self):
        self.content += "\n\\newline\n"