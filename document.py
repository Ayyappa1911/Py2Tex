class document:
    def __init__(self,filename = "test.tex"):
        self.filename = filename
        self.file = open(self.filename, "w")
        self.headers = ["\\documentclass{article}\n","\\usepackage[utf8]{inputenc}\n"]
        self.intro = []
        self.content = []
    def title(self,title=""):
        self.intro.append("\\title{"+title+"}\n")
    def author(self,author=""):
        self.intro.append("\\author{"+author+"}\n")
    def para(self,para):
        self.content.append(para+"\n")
    def close(self):
        self.file.writelines(self.headers)
        self.file.write("\n")
        self.file.writelines(self.intro)
        self.file.write("\n")
        self.file.write("\\begin{document}\n")
        if(len(self.intro)):
            self.file.write("\\maketitle\n")
        self.content.append("\\end{document}\n")
        self.file.writelines(self.content)
        self.file.close()