import re

def load_map(file):
  ''' This function rewrites the text file to split the line more easily'''
  linelist=[]
  
  for line in open(file):
    line=line.replace("-+-","---")
    line=line.replace("-+","-|")
    line=line.replace("+-","|-")
    line=line.replace(" + "," | ")
    line=line.replace("/","|")
    line=line.split("|")
    linelist.append(line)
  return linelist

def build_dict(rooms, results):
  ''' This function creates a dictionary with chair count'''
  for i in range (len(rooms)):
    roomcount={}
    roomcount["W:"]=len([x for x in "".join([x for x in rooms[i]]) if x =="W"])
    roomcount["P:"]=len([x for x in "".join([x for x in rooms[i]]) if x =="P"])
    roomcount["S:"]=len([x for x in "".join([x for x in rooms[i]]) if x =="S"])     
    roomcount["C:"]=len([x for x in "".join([x for x in rooms[i]]) if x =="C"])
    
    if re.findall(r"\w+ ?\w+\)", "".join([x for x in rooms[i]]))[0].split(")")[0]+":" in results.keys():
      if  sum(results[re.findall(r"\w+ ?\w+\)", "".join([x for x in rooms[i]]))[0].split(")")[0]+":"].values())<sum(roomcount.values()):
        results[re.findall(r"\w+ ?\w+\)", "".join([x for x in rooms[i]]))[0].split(")")[0]+":"]=roomcount
    else: 
      results[re.findall(r"\w+ ?\w+\)", "".join([x for x in rooms[i]]))[0].split(")")[0]+":"]=roomcount
  return results


def screening_rooms(linelist):
  ''' This function identifies rooms'''
  room=[]
  rooms=[]
  results={}
  for j in range (1,len(linelist[1])-1):
    for i in range (1,len(linelist)):
        if i != 1:
          if len(linelist[i])<len(linelist[i-1]):
            if "-" in linelist[i-1][j-1]:
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
          room.append(linelist[i][j])
        if i== len(linelist):
          rooms.append(room)     
    results=build_dict(rooms, results)

  # This part of the function looks for missing rooms
  maxi={}
  for i in range(len(linelist)):
    maxi[i]=len(linelist[i])
  leftrooms=[k for k,v in maxi.items() if maxi[k]>maxi[1] and maxi[k-1]!=maxi[k]]
  room=[]
  rooms=[]
  j=1
  for s in leftrooms:
    for i in range (s+1,len(linelist)):
      room.append(linelist[i][j])
      if "-" in linelist[i][j]:
        rooms.append(room)
        room=[]
        i+=1     
  results=build_dict(rooms, results)      
  return results

def build_total(results):
  ''' This function calculates the total amount of chairs '''
  total={}
  total_w=[]
  total_p=[]
  total_s=[]
  total_c=[]
  for x in results:
    total_w.append(results[x]["W:"])
    total_p.append(results[x]["P:"])
    total_s.append(results[x]["S:"])
    total_c.append(results[x]["C:"])
  total["W:"]=sum(total_w)
  total["P:"]=sum(total_p)
  total["S:"]=sum(total_s)
  total["C:"]=sum(total_c)
  return total

def print_result(total, results,filename, output):
  ''' This function outputs result file and print formated results '''
  if output=="":
    output=filename.split("/")[-1].split(".txt")[0]+"_ouput.txt"
    # output_name=filename.split("/")[-1].split(".txt")[0]+"_ouput.txt"
    # ouput=os.getcwd()+output_name
  with open(output, "a+") as f:
    f.write("total:"+'\n')
    for x in total:
      if x!="C:":
        f.write(f'{x}'+" "+f'{total[x]}'+", ")
      else:
        f.write(f'{x}'+" "+f'{total[x]}')
    f.write("\n")
    for x in results:
        f.write(f'{x}'+'\n')
        for y in results[x]:
          if y!="C:":
            f.write (f'{y}'+" "+f'{results[x][y]}'+", ")
          else:
            f.write (f'{y}'+" "+f'{results[x][y]}')
        f.write("\n")   
  for line in  open(output):
    print(line)

