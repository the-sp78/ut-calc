print("Program to calculate Unit Test scores, grades, and percentage")

eng=eval(input("Enter english score: "))
math=eval(input("Enter math score: "))
phy=eval(input("Enter physics score: "))
chem=eval(input("Enter chemistry score: "))
bio=eval(input("Enter biology score: "))
his=eval(input("Enter history score: "))
geo=eval(input("Enter geo score: "))
tamil=eval(input("Enter tamil score: "))
opt=eval(input("Enter optional subject score: "))

sci_avg=(phy+chem+bio)/3
sst_avg=(his+geo)/2
mathout25=math*0.625
tamilout25=tamil*0.625

def gradecalc(sub):
    if sub>=21.5:
        subgrade="A"
    elif sub<21.5 and sub>=18:
        subgrade="B"
    elif sub<18 and sub>=15.5:
        subgrade="C"
    elif sub<15.5 and sub>=10:
        subgrade="D"
    else:
        subgrade="E"
    return subgrade

def t_scoregradecalc(tscore):
    if tscore>=129:
        tgrade="A"
    elif tscore<129 and tscore>=106.5:
        tgrade="B"
    elif tscore<106.5 and tscore>=91.5:
        tgrade="C"
    elif tscore<91.5 and tscore>=60:
        tgrade="D"
    else:
        tgrade="E"
    return tgrade

t_score=eng+mathout25+sci_avg+sst_avg+tamilout25+opt
inttscore=int(t_score)

print("\n--------------------------------------------------------------------------------")
print("English       ",eng,"       ",gradecalc(eng))
print("Mathematics   ",mathout25,"      ",gradecalc(mathout25))
print("Science       ",sci_avg,"       ",gradecalc(sci_avg))
print("Physics       ",phy,"       ",gradecalc(phy))
print("Chemistry     ",chem,"       ",gradecalc(chem))
print("Biology       ",bio,"       ",gradecalc(bio))
print("Social Science",sst_avg,"       ",gradecalc(sst_avg))
print("History       ",his,"       ",gradecalc(his))
print("Geography     ",geo,"       ",gradecalc(geo))
print("Tamil         ",tamilout25,"       ",gradecalc(tamilout25))
print("Optional Sub  ",opt,"       ",gradecalc(opt))

print("\nTotal score:",inttscore,"/ 150")
print("Percentage:",(inttscore/150)*100,"%")
print("Overall Grade:",t_scoregradecalc(inttscore))
print("\n--------------------------------------------------------------------------------")