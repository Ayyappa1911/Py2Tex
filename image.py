import document



# Making an Assumption for making ease for further dev ideas that Images always need to be in Images folder(sub folders can be created on Images folder.)
class image:
    def __init__(self,path="",width=5,caption="",center=0): #An Attribute label is not added yet.
        self.path = path
        self.center = center
        self.caption = caption
        self.width = width
        document.image_flag = 1
    def centering(self):
        self.center = 1
    def addcaption(self,caption=""):
        self.caption = caption
    def getcontent(self):
        a = ""
        a += "\n\n\\begin{figure}[h]\n"
        if(self.center):
            a+="\t\\centering\n"
        a+="\t\\includegraphics[width="+str(self.width)+"cm]{"+self.path+"}\n"
        if(self.caption != ""):
            a += "\t\\caption{"+self.caption+"}\n"
        a += "\\end{figure}\n\n"
        return a