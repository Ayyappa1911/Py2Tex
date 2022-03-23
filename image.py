import document

# Making an Assumption for making ease for further dev ideas that Images always need to be in Images folder(sub folders can be created on Images folder.)
class image:
    def __init__(self,path="",width=5,caption="",position=0): #An Attribute label is not added yet.
        self.path = path
        self.position = position
        self.caption = caption
        self.width = width
        document.image_flag = 1
    def positioning(self,position):
        self.position = position
    def addcaption(self,caption=""):
        self.caption = caption
    def getcontent(self):
        a = ""
        a += "\n\n\\begin{figure}[h]\n"
        if(self.position == 0):
            a+="\t\\centering\n"
        elif(self.position == 1):
            a+="\t\\raggedright\n"
        elif(self.position == -1):
            a+="\t\\raggedleft\n"
        a+="\t\\includegraphics[width="+str(self.width)+"cm]{"+self.path+"}\n"
        if(self.caption != ""):
            a += "\t\\caption{"+self.caption+"}\n"
        a += "\\end{figure}\n\n"
        return a