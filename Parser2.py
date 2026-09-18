#Funktions
import json
def splitlines(input:str,seperator:list):
    list_lines=[]
    counter=0
    for i in range(len(input)):
        if input[i] in seperator:
            list_lines.append(input[counter:i])
            counter=i+1
    list_lines.append(input[counter:len(input)])
    return list_lines
def splitBySeperator(input:str,seperator:str):
    list_info=[]
    counter=0
    for i in range(len(input)):
        if input[i]==seperator:
            list_info.append(input[counter:i])
            counter=i+1
    list_info.append(input[counter:len(input)])
    return list_info
def dictionary(input:list,header:list):
    dictionary={}
    j=0
    for i in header:
            dictionary[f"{i}"]=input[j]
            j+=1
    return dictionary

#Json converter
def jsonconv(input):
    output=json.dumps(input)
    return output

#Class

class Parser:
    def __init__(self):
        pass

    def parse(self, input:str,header=True,seperator=",",lineseperator=["\n","\r"]):
        list_data=splitlines(input,lineseperator)
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

#"name,email,department,role,salary,start_date,office\nMarcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco\nPriya Sharma,priya.sharma@example.com,Engineering,Staff Engineer,178000,2019-06-01,San Francisco"
if __name__ == "__main__":
    parser=Parser()
    csv=input("Enter your string or file: ")
    header=input("Do you have a header in your file? yes/no ")
    #lineseperator=input("what are you lineseperators?")
    #seperator=input("what are you seperator of columns?")
    if header=="yes":
        header=True
        print(parser.parse(csv,header=header))
    if header=="no":
        header=False
        print(parser.parse(csv,header=header))
#print(jsonconv(parsed))