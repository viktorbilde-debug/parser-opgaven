# Parser
This program takes an CSV-formattet string of text and parse this according to specefifictions into a list of lists or a list of dictionaries depending on if there is a header or not. The program can also read text strings from a file. Output can be returned in JSON representation by enable it in specifications.
# Description
The program works with creating an object of the class "Parser()". This object is the parser and in the initlization you can define if it should consider a header or not, the list of line-seperatos, the general seperator and if the output should be in JSON format.

You can now call the method "parse" with CSV-formattet string as input. The program splits the string by the given line-seperators giving a list of strings where each element in the list is a line. From here the parsing proces now depends on you specification of header being TRUE og FALSE.
## With header
The program now pops the first element from the list of strings. The first line is therefore considered as the header. The header string is splitted by the general seperator giving a list of strings where each string is a label. 

The rest of the list of strings from which the header was popped is now list comprehended where each element is splitted by the general seperator. This gives a list of lists where each element in the outer list correpsonds to a line/observation. Each element in the inner list is a string coresponding to data for this line/observation.

Both the list of labels made by the header and the list of lists of strings made by the rest of the data are now combined into a list of dictionaries where each dictionary correspond to a line/observation with keys being the labels from the header and the key value being the observation specefic value to the label.

The program returns the list of dictionaries as output and the output can be converted to JSON format if specified in the specefication of the parser class "Parser()".

## Without header
The list of strings is list comprehended where each element is splitted by the general seperator. This gives a list of lists where each element in the outer list correpsonds to a line/observation. Each element in the inner list is a string coresponding to data for this line/observation.

The program returns the list of lists as output and the output is converted to JSON format if specified in the specefication of the parser class "Parser()". 

# Getting started

## Dependencies
Libraries:
- JSON. This library is used to convert Python objects as lists and dictionaries into JSON format

## Installing
The program can be installed by downloading the file "Parser" from this repository "https://github.com/viktorbilde-debug/parser-opgaven"

## Executing program
- start by importing the content from the file\
`from Parser import *`
- Create an object using the Parser class initialised with optional header, lineseperator, general-seperator and JSON:
`parser=Parser()` 
  - The standard without specefication is:  
  header=True  
  seperator=","  
  lineseperator=["\n","\r"]  
  Json=False"

- Define you CSV-string and call the method "parse" on it. 
```Python
csv="name,email,department,role,salary,start_date,office\nMarcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco"
parser.parse(csv)
```
- We get the output:\
[{'name': 'Marcus Chen', 'email': 'marcus.chen@example.com', 'department': 'Engineering', 'role': 'Senior Software Engineer', 'salary': '155000', 'start_date': '2019-03-15', 'office': 'San Francisco'}]
## Help
- Remember in the initialization of the object from the "Parser()" class to specify header to False or the lineseperator or general seperator or JSON to True if you dont have a header, have another lineseperator than "\n" or "\r" and/or have another general seperator than "," and/or want the output to be JSON formattet.
# Authors
Viktor Lønberg Bilde \
Mail: viktor.bilde@gmail.com
# Version history
- 0.1 initial release
# License
The project is licensed under the MIT License
# Acknowledgments
- Specialisterne Academy
- w3school
- geeksforgeeks 