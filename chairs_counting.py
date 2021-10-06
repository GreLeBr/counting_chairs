import re

linelist=[]
for line in open("/data/rooms.txt"):
  line=line.replace("-+-","---")
  line=line.replace("-+","-|")
  line=line.replace("+-","|-")
  line=line.replace(" + "," | ")
  line=line.replace("/","|")
  line=line.split("|")
  linelist.append(line)
  print (repr(line))

room=[]
rooms=[]
j=1
for i in range (1,len(linelist)):
    if i != 1:
      if len(linelist[i])<len(linelist[i-1]):
          j-=1
      if len(linelist[i])>len(linelist[i-1]):
        j+=1    
    if "-"*len(linelist[i-1][j]) == linelist[i][j]:
      rooms.append(room)
      room=[]
      if i != len(linelist)-1 and j!=len(linelist[i]): 
        if len(linelist[i+1][j])==len(linelist[i][j]):
          i+=1
        if len([x for x in linelist[i] if "-" in x])+2 == len(linelist[i]):
          i+=1
        if len(linelist[i+2][j])<len(linelist[i][j]):
          i+=1          
        if len(linelist[i+2][j])>len(linelist[i][j]):    
          break
    if i != len(linelist) and j!=len(linelist[i]):  
      if "-" in linelist[i][j]:
        if len(linelist[i-1][j]) != len(linelist[i][j]):
              if "-"*len(linelist) == linelist[i][j]:
                rooms.append(room)
                room=[]  
              j+=1
      if len(linelist[i][j])==1:
        j-=1        
      print(i,j,linelist[i][j])
      room.append(linelist[i][j])
    if i== len(linelist):
      rooms.append(room)

for i in range (len(rooms)):
  print(re.findall(r"\w+ ?\w+\)", "".join([x for x in rooms[i]]))[0].split(")")[0]+":", "\n",   
        "W:", len([x for x in "".join([x for x in rooms[i]]) if x =="W"]),
        "P:", len([x for x in "".join([x for x in rooms[i]]) if x =="P"]),
        "S:", len([x for x in "".join([x for x in rooms[i]]) if x =="S"]),
        "C:", len([x for x in "".join([x for x in rooms[i]]) if x =="C"]))
