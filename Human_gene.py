#coding = utf-8
import random
"""import random"""

geneNo = []
for i in range(1,24):
    geneNo.append(i)
"""Generating a sequence number contains 1~23"""

"""
print geneNo
geneNo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
         17, 18, 19, 20, 21, 22, 23]
"""

FatherGene = ['FGA', 'FGa']
MotherGene = ['MGB', 'MGb']
"""Each gene contains a pair (two) homologous genes"""

FatherGenome = []
MotherGenome = []
"""generate paternal genome and maternal genome"""

for i in range(0, 23):
    for j in range(0,2):
        FatherGenome.append(str(str(geneNo[i]) + '-' + FatherGene[j]))

for i in range(0, 23):
    for j in range(0,2):
        MotherGenome.append(str(str(geneNo[i]) + '-' + MotherGene[j]))

print "FatherGenome :\n", FatherGenome
print "-------------"
print "MotherGenome :\n", MotherGenome
print "-------------"
"""print paternal genome and maternal genome out"""

RealFatherGenome = zip(*[iter(FatherGenome)]*2)
RealMotherGenome = zip(*[iter(MotherGenome)]*2)
"""generate paternal genome pairs and maternal genome pairs"""

print "RealFatherGenome :\n", RealFatherGenome
print "-------------"
print "RealMotherGenome :\n", RealMotherGenome
print "-------------"
"""print paternal genome pairs and maternal genome pairs out"""

ChanceRealFatherGenome = []
ChanceRealMotherGenome = []
"""generate sperm gene and egg gene"""

for i in range(0, 23):
    j = random.randint(0, 1)
    ChanceRealFatherGenome.append(RealFatherGenome[i][j])

for i in range(0, 23):
    j = random.randint(0, 1)
    ChanceRealMotherGenome.append(RealMotherGenome[i][j])

print "ChanceRealFatherGenome :\n", ChanceRealFatherGenome
print "-------------"
print "ChanceRealMotherGenome :\n", ChanceRealMotherGenome
print "-------------"
"""show randomly generated sperm gene and egg gene"""

BabyGenome = zip(ChanceRealFatherGenome, ChanceRealMotherGenome)
"""Egg and sperm combine to form a  new life"""

print "BabyGenome :\n", BabyGenome
print "-------------"
"""show the-new-life's genome"""


print "The 23rd Gene is :\n", BabyGenome[22]
print "-------------"
"""show the 23rd gene is ?"""

if BabyGenome[22][0] == "23-FGa":
    print "He is your son!"
else:
    print "She is your girl!"
"""show boy or girl"""
