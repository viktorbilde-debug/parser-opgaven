class dict_dict:
  def __init__(self, name, mail,area, position, salary, start_date,office):
    self.name = name
    self.mail= mail
    self.area=area
    self.position=position
    self.salary=salary
    self.start_date=start_date
    self.office=office
  def get_info(self):
    return dict(name = self.name,mail=self.mail, area=self.area, position=self.position,salary=self.salary,start_date=self.start_date,office=self.office)

#Function
def DSP(x:str,header=True):
    g=x.splitlines()
    if header==True:
      h=g[0].split(",")
      dd=dict_dict(h[0],h[1],h[2],h[3],h[4],h[5],h[6])
      l[f"{s}"]=dd.get_info()
      s+=1
    return l
if __name__ == "__main__":
    #print(DSP("Marcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco\nPriya Sharma,priya.sharma@example.com,Engineering,Staff Engineer,178000,2019-06-01,San Francisco"))
a="Marcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco\nPriya Sharma,priya.sharma@example.com,Engineering,Staff Engineer,178000,2019-06-01,San Francisco"
print(a.splitlines())