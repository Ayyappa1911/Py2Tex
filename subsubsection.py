
class subsubsection:
    def __init__(self,name="",content=""):
        self.name = name
        self.content = content
        # self.images = [] # See whether list of images is required!
    def addcontent(self,content=""):
        self.content += content
    def addimage(self,i):
        # self.images.append(i)
        self.content += i.getcontent()
