
class subsection:
    def __init__(self, name="", content=""):
        self.name = name
        self.content = content
        self.subsubsections = []
        # self.images = []
    def addcontent(self,content=""):
        self.content = content
    def addsubsubsection(self,s):
        self.subsubsections.append(s)
    def addimage(self,i):
        # self.images.append(i)
        self.content += i.getcontent()
        # print(i.getcontent())