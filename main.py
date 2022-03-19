from document import document
from section import section

d = document("test.tex")
d.title("Testing the document")
d.author("Ayyappa Koppuravuri")
d.table_of_contents()
d.para("Helmo")
d.boundary()

s = section("Story")
s.addcontent("This is the content of the story")
d.addsection(s)

s1 = section("Story2","This is the content of story 2")
d.addsection(s1)

d.close()