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

#Parser class. A class with properties being "header,seperator,lineseperator, Json" 
# and a method "parse()" which takes 
#a string as input and parse the string according to the properties
class Parser:
    def __init__(self,header=True,seperator=",", lineseperator=["\n","\r"], Json=False):
        self.header=header
        self.seperator=seperator
        self.lineseperator=lineseperator
        self.Json=Json
    def parse(self,input:str):
        list_data=splitlines(input,self.lineseperator)
        if self.header==True:
            head=splitBySeperator(list_data.pop(0),self.seperator)
            list_data=[splitBySeperator(x,self.seperator) for x in list_data]
            output=[]
            for i in list_data:
                output.append(dictionary(i,head))
            if self.Json==True:
                return jsonconv(output)
            else:
                return output
        if self.header==False:
            output=[splitBySeperator(x,self.seperator) for x in list_data]
            if self.Json==True:
                return jsonconv(output)
            else:
                return output

#Example using the method parser()

if __name__ == "__main__":
    csv="name,email\nMarcus Chen,marcus.chen@example.com\nPriya Sharma,priya.sharma@example.com"
    parser=Parser()
    print(parser.parse(csv))