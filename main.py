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

s1 = section("Story1","This is the content of story 1")
d.addsection(s1)

ss1 = subsection("Story1 part1","This is the content belonging to part1 of the story1")
s1.addsubsection(ss1)

sss1 = subsubsection("Story1 part1.1","This is the content belonging to part1 of the story1.1")
ss1.addsubsubsection(sss1)

i = image("image1.jpg",5,"This is a jpg image",1)
ss.addimage(i)
# d.addimage(i) #ISSUE CHECK IT!.
s.addimage(i)


d.close()