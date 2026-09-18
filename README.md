# Parser
This program takes an CSV-formattet string of text and parse this into a list of lists or a list of dictionaries depending on if there is a header or not. The program can also read text strings from a file. Output is in JSON representation of the input.
# Description
The program works with creating an object of the class Parser. This object is the parser an in the initlization you can define if it should consider a header or not, the line seperator and the general seperator.

By calling the method "parse" you can give the CSV-formattet string as input. The program splits the string by the given line seperator giving a list of strings where each element in the list is a line. From here the parsing proces now depends on if you have a header or not.
## With header
The program now pops the first element from the list of strings. The first line is therefore considered as the header. The header string is splitted by the general seperator giving a list of strings where each string a label. 

The rest of the list of strings from which the header was popped is now list comprehended where each element is splitted by the general seperator. This gives a list of lists where each element in the outer list correpsonds to a line/observation charachterized by a list of strings. Each element in the inner list is a string coresponding to data for this line/observation.

Both the list of labels made by the header and the list of lists of strings made by the rest of the data are now combined into a list of dictionaries where each dictionary correspond to a line/observation with keys being the labels from the header and the key value being the observation specefic value to the label.

The program returns the list of dictionaries as output and the output is converted to JSON format

## Without header
The list of strings is list comprehended where each element is splitted by the general seperator. This gives a list of lists where each element in the outer list correpsonds to a line/observation charachterized by a list of strings. Each element in the inner list is a string coresponding to data for this line/observation.

The program returns the list of lists as output and the output is converted to JSON format. 

# Getting started

## Dependencies
Libraries:
- JSON. This library is used to convert Python objects as lists and dictionaries into JSON

## Installing
The program can be installed by downloading the file "Parser2" from this repository "https://github.com/viktorbilde-debug/parser-opgaven"

## Executing program
- start by importing the content from the file\
`from Parser2 import *`
- Create an object using the Parser class initialised with optional header, lineseperator and generalseperator\
`parser=Parser()`
- Define you CSV-string and call the method "parse" on it. 
```Python
csv="name,email,department,role,salary,start_date,office\nMarcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco"
parser.parse(csv)
```
- We get the output:\
[{'name': 'Marcus Chen', 'email': 'marcus.chen@example.com', 'department': 'Engineering', 'role': 'Senior Software Engineer', 'salary': '155000', 'start_date': '2019-03-15', 'office': 'San Francisco'}]
## Help
- Remember to shift header to False or the lineseperator or general seperator if you dont have a header, have another lineseperator than "/n" or "/r" and/or have another general seperator than ","
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