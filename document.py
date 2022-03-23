import image

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
            if (type(s)==image): #Adding images on Document is not fine
                self.file.write(s.getcontent())
            else:
                self.file.write("\\section{"+ s.name+"}\n")
                self.file.write(s.content+"\n\n")
                for ss in s.subsections:
                    self.file.write("\\subsection{"+ ss.name+"}\n")
                    self.file.write(ss.content+"\n\n")
                    for sss in ss.subsubsections:
                        self.file.write("\\subsubsection{"+ sss.name+"}\n")
                        self.file.write(sss.content+"\n\n")
        self.file.write("\\end{document}\n")
        self.file.close()
    

    def addimage(self,i): #For not missing the position of Image to be inserted images of the document are added to sections class
        self.sections.append(i)

    # Assuming that only document object exists for the each script.
    # @staticmethod
    # def is_image(i):
    #     if isinstance(i,image):
    #         document.image_flag = 1
    