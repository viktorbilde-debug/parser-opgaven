#Importing packages
import json
#Functions

#takes a string and split lines by the given list of seperators
def splitlines(input:str,seperator:list):
    list_lines=[]
    counter=0
    quotation=False
    for i in range(len(input)):
        if input[i]=="\"":
            quotation= not quotation
        if input[i] in seperator and quotation==False:
            list_lines.append(input[counter:i])
            counter=i+1
    list_lines.append(input[counter:len(input)])
    return list_lines
#takes a string and split the string by given seperator
def splitBySeperator(input:str,seperator:str):
    list_info=[]
    counter=0
    quotation=False
    for i in range(len(input)):
        if input[i]=="\"":
            quotation= not quotation
        if input[i]==seperator and quotation==False:
            list_info.append(input[counter:i])
            counter=i+1
    list_info.append(input[counter:len(input)])
    return list_info
#takes a input data list and a list which is the header of the data. Sorts the 
#data and header in a dictionary. Keys=header, key values=data
def dictionary(input:list,header:list):
    dictionary={}
    j=0
    for i in header:
            dictionary[f"{i}"]=input[j]
            j+=1
    return dictionary

#Json converter. Converts input to Json format
def jsonconv(input):
    output=json.dumps(input)
    return output

#Classes

#Parser class. A class with no properties but a method "parse()" which takes 
#a string as input and parse the string according to given specifications
#and returns in Json format
class Parser:
    def __init__(self):
        pass

    def parse(self, input:str,header=True,seperator=",",lineseperator=["\n","\r"], Json=False):
        list_data=splitlines(input,lineseperator)
        if header==True:
            head=splitBySeperator(list_data.pop(0),seperator)
            list_data=[splitBySeperator(x,seperator) for x in list_data]
            output=[]
            for i in list_data:
                output.append(dictionary(i,head))
            if Json==True:
                return jsonconv(output)
            else:
                return output
        if header==False:
            output=[splitBySeperator(x,seperator) for x in list_data]
            if Json==True:
                return jsonconv(output)
            else:
                return output

#Example using the method parser()

if __name__ == "__main__":
    csv="name,email,department,role,salary,start_date,office\nMarcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco\nPriya Sharma,priya.sharma@example.com,Engineering,Staff Engineer,178000,2019-06-01,San Francisco"
    parser=Parser()
    print(parser.parse(csv))