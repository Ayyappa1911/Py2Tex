
# Steps to execute this code and generate a .pdf file.

# Run 

# $python3 main.py
# $pylatex test.tex
# ---> Enter the name of the file (if asked) as test.tex
# ***Click 'ENTER' until command line appear
# ---> You might not get all the Overleaf features for this execution!!

from document import document
from section import section
from subsection import subsection
from subsubsection import subsubsection
from image import image
# from . import document
# from . import image

d = document("test.tex")
d.title("Testing the document")
d.author("Ayyappa Koppuravuri")
d.table_of_contents()
d.newpage()
d.para("Helmo")
d.boundary()

s = section("Story")
s.addcontent("This is the content of the story")
d.addsection(s)

ss = subsection("story part1")
ss.addcontent("This is the content belonging to part1 of the story")
s.addsubsection(ss)

sss = subsubsection("story part1.1")
sss.addcontent("This is the content belonging to part1.1 of the story")
ss.addsubsubsection(sss)

s1 = section("Story1","This is the content of story 1",0)
d.addsection(s1)

ss1 = subsection("Story1 part1","This is the content belonging to part1 of the story1",0)
s1.addsubsection(ss1)

sss1 = subsubsection("Story1 part1.1","This is the content belonging to part1 of the story1.1",0)
ss1.addsubsubsection(sss1)

i = image("image1.jpg",5,"This is a Center aligned image",0)
s1.newpage()
ss1.addimage(i)
i = image("image1.jpg",5,"This is a left aligned image",1)
d.addimage(i)
i = image("image1.jpg",5,"This is a right aligned image",-1)
s.addimage(i)


d.close()