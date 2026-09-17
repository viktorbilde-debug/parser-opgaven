#Funktions
def splitlines(input:str):
    input=input.splitlines()
    return input
def splitBySeperator(input:str,seperator:str):
    input=input.split(seperator)
    return input
def dictionary(input:list,header:list):
    dictionary={}
    j=0
    for i in header:
            dictionary[f"{i}"]=input[j]
            j+=1
    return dictionary
  
#Class
class Parser:
    def __init__(self):
        pass

    def parse(self, input:str,header=True,seperator=","):
        list_data=splitlines(input)
        if header==True:
            head=splitBySeperator(list_data.pop(0),seperator)
            list_data=[splitBySeperator(x,seperator) for x in list_data]
            output=[]
            for i in list_data:
                output.append(dictionary(i,head))
            return output
        if header==False:
            output=[splitBySeperator(x,seperator) for x in list_data]
            return output

if __name__ == "__main__": 
    parser=Parser()
    csv="name,email,department,role,salary,start_date,office\nMarcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco\nPriya Sharma,priya.sharma@example.com,Engineering,Staff Engineer,178000,2019-06-01,San Francisco"
    parsed=parser.parse(csv)
    print(parsed)
    print(parser.parse("Marcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco\nPriya Sharma,priya.sharma@example.com,Engineering,Staff Engineer,178000,2019-06-01,San Francisco",header=False))
   