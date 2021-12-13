
class coder:
    loc=100
    def error():
        error=20
        

jv=coder()
jv.error()


activ=(500,300,500,1000,1500)
print(activ[4])
game=[1,2,3]
print(game[1])




dd={"morning":"eating","noon":"sleeping"}

name="jvt"
dirctly variable and data

indexing list and tuple

object

many values access with for loop
for obj in obj as a list,tuple,dict

dict inside list
obj[1]["id"]

list inside list
obj[1][2]

list inside dict inside list inside dict



#apparoach 1
Name="Sheryl"

#approach 2

class friday:
    __work="python"
    def __init__(self):
        self.__tea=5
    def display(self):
        print(self.__tea)

sub=friday()
sub.display()


#approach 3

saturday =("sleep","eat","play","repeat")

print (saturday [2])


#approach 4

sunday = {"morning":"eat", "noon":"sleep", "eve":"idle", "night":"tv"}

print(sunday["morning"])

#approach 5


print(saturday)

for i in saturday:
    print(i)

for i in sunday.values():
    print(i)

for i in sunday.keys():
    print(i)


#approach 6

student = [{"id":23, "name":"Anu", "branch":"bba"}, {"id":67, "name":"Caesy", "branch":"bca"}, {"id":32, "name":"Caroline", "branch":"BE"}]
print(student[0], student[1])

for i in student:
    if (i["name"]=="Anu"):
        print("Anu is available")
    if (i["branch"]=="bba"):
        print("bba")

#approach 7

comp = [{"intern":[{"empname":"Tom","id":"DIN07","gender":"male"},{"empname":"Shep","id":"DIN10","gender":"male"},{"empname":"Odette","id":"DIN03","gender":"female"}],
        "fulltimejob":[{"empname":"Jamie","id":"DIN113","gender":"male"},{"empname":"Lydia","id":"DIN116","gender":"female"},{"empname":"Sawyer","id":"DIN118","gender":"female"}],
"contractjob":[{"empname":"Lindsey","id":"DIN818","gender":"female"},{"empname":"Dustin","id":"DIN515","gender":"male"}]}]
print (comp[0])


for i in comp:
    if (i["intern"][0]["empname"]== "DIN07"):
        print ("empname regards present")
    if (i["fulltimejob"][1]["empname"]== "DIN116"):
        print ("empname fulltime present")
    if (i["contractjob"][0]["empname"]== "DIN818"):
        print ("empname contract present")

for i in comp:
    for j in i.values():
        for k in j:
            print(k)

#approach 8
lambda x : print("coder")

fn = 


class disys:
    def __init__(self,vacc):
        self.vac=[]
        self.vac.append(vacc)
        self.count=0
    def logic(self):
        for i in self.vac:
            if i["vaccine"] == None:
                self.count = self.count+1
            else:
                continue

        print (self.vac)
        def __del__(self):
            print("deallocation")
            del self.vac
            del self.count

jb=disys({"name":"jamesbond", "empid":"007", "vaccine":None})
ri=disys({"name":"ritesh", "empid":"005", "vaccine":"1st dose"})
ri.logic()
del jb


import collections

dictob = collections.OrderedDict()

dictob.clear()

c = collections.Counter()





    
         
        
    





