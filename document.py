
# Steps to execute this code and generate a .pdf file.

# Run 

# $python3 main.py
# $pylatex test.tex
# ---> Enter the name of the file (if asked) as test.tex
# ***Click 'ENTER' until command line appear
# ---> You might not get all the Overleaf features for this execution!!

class document:
    
    image_flag = 0
    
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
        # if(self.image_flag):
        self.headers.append("\\usepackage{graphicx}\n")
        self.file.writelines(self.headers)
        self.file.write("\n")
        self.file.writelines(self.intro)
        self.file.write("\n")
        # if(self.image_flag):
        self.file.write("\\graphicspath{{Images/}}\n\n")
        self.file.write("\\begin{document}\n")
        if(len(self.intro)):
            self.file.write("\\maketitle\n")
        if(self.toc):
            self.file.write("\\tableofcontents\n\n")
        self.file.writelines(self.content)
        for s in self.sections:
            if(s.type):
                self.file.write("\\section{"+ s.name+"}\n")
            elif((s.type) == 0):
                self.file.write("\\section*{"+ s.name+"}\n")
            self.file.write(s.content+"\n\n")
            for ss in s.subsections:
                if(ss.type):
                    self.file.write("\\subsection{"+ ss.name+"}\n")
                elif(ss.type == 0):
                    self.file.write("\\subsection*{"+ ss.name+"}\n")
                self.file.write(ss.content+"\n\n")
                for sss in ss.subsubsections:
                    if(sss.type):
                        self.file.write("\\subsubsection{"+ sss.name+"}\n")
                    elif(sss.type == 0):
                        self.file.write("\\subsubsection*{"+ sss.name+"}\n")
                    self.file.write(sss.content+"\n\n")
        self.file.write("\\end{document}\n")
        self.file.close()
    

    def addimage(self,i):
        self.content += i.getcontent()

    def newpage(self):
        self.content += "\\newpage\n"
    
    def newline(self):
        self.content += "\n\\newline\n"
    
    def addcontent(self,content=""):
        self.content += content