# from section import section

class document:
    def __init__(self,filename = "test.tex"):
        self.filename = filename
        self.file = open(self.filename, "w")
        self.headers = ["\\documentclass{article}\n","\\usepackage[utf8]{inputenc}\n\n"]
        self.intro = []
        self.content = []
        self.sections=[]
        self.toc = 0
    def title(self,title=""):
        self.intro.append("\\title{"+title+"}\n")
    def author(self,author=""):
        self.intro.append("\\author{"+author+"}\n")
    def para(self,para):
        self.content.append(para+"\n")
    def table_of_contents(self):
        self.toc = 1
    def boundary(self,top = 1,bottom = 1,left = 1,right = 1):
        self.headers.extend(["\\usepackage{calc}\n" , "\\usepackage{eso-pic}\n" ]);
        self.headers.append(
            '''\\newlength{\PageFrameTopMargin}
\\newlength{\PageFrameBottomMargin}
\\newlength{\PageFrameLeftMargin}
\\newlength{\PageFrameRightMargin}

\\setlength{\PageFrameTopMargin}{'''+str(top)+'''cm}
\\setlength{\PageFrameBottomMargin}{'''+str(bottom)+'''cm}
\\setlength{\PageFrameLeftMargin}{'''+str(right)+'''cm}
\\setlength{\PageFrameRightMargin}{'''+str(left)+'''cm}

\\makeatletter

\\newlength{\Page@FrameHeight}
\\newlength{\Page@FrameWidth}

\\AddToShipoutPicture{
   \\thinlines
   \\setlength{\Page@FrameHeight}{\paperheight-\PageFrameTopMargin-\PageFrameBottomMargin}
   \\setlength{\Page@FrameWidth}{\paperwidth-\PageFrameLeftMargin-\PageFrameRightMargin}
   \\put(\strip@pt\PageFrameLeftMargin,\strip@pt\PageFrameTopMargin){
   \\framebox(\strip@pt\Page@FrameWidth, \strip@pt\Page@FrameHeight){}}}

\\makeatother
            '''
        )
    def addsection(self,s):
        self.sections.append(s)

    def close(self):
        self.file.writelines(self.headers)
        self.file.write("\n")
        self.file.writelines(self.intro)
        self.file.write("\n")
        self.file.write("\\begin{document}\n")
        if(len(self.intro)):
            self.file.write("\\maketitle\n")
        if(self.toc):
            self.file.write("\\tableofcontents\n")
        if(len(self.sections)):
            for s in self.sections:
                self.file.write("\\section{"+ s.name+"}\n")
                self.file.write(s.content+"\n")
        
        self.content.append("\\end{document}\n")
        self.file.writelines(self.content)
        self.file.close()