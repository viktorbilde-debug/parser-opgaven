
#read file general with more than one line
#with open("testflere.csv") as k:
    #d=0
    #dd = {}
    #for x in k:
       #h=x.split(",")
       #dd[f"{d}"]= Person(h[0],h[1],h[2],h[3],h[4],h[5],h[6])
       #d +=1
#print(dd["1"].get_info())
#def DSP(file):
   #with open(file) as k:
    #d=0
    #dd = {}
    #for x in k:
       #h=x.split(",")
       #dd[f"{d}"]= Person(h[0],h[1],h[2],h[3],h[4],h[5],h[6])
       #d +=1
    #return(dd["0"].get_info())

class dict_dict:
  def __init__(self,[shoe,size]):
    self.name = name
    self.mail= mail
    self.area=area
    self.position=position
    self.salary=salary
    self.start_date=start_date
    self.office=office
  def get_info(self):
    return dict(name = self.name,mail=self.mail, area=self.area, position=self.position,salary=self.salary,start_date=self.start_date,office=self.office)
