import unittest;
from Parser2 import *;
parser=Parser()
class Testclass(unittest.TestCase):
    def test_1line(self):
        self.assertEqual(parser.parse("name,email,department,role,salary,start_date,office\nMarcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco"),
                          [{'name': 'Marcus Chen', 'email': 'marcus.chen@example.com', 'department': 'Engineering', 'role': 'Senior Software Engineer', 'salary': '155000', 'start_date': '2019-03-15', 'office': 'San Francisco'}])
    def test_multilinesn(self):
        self.assertEqual(parser.parse("name,email,department,role,salary,start_date,office\nMarcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco\nPriya Sharma,priya.sharma@example.com,Engineering,Staff Engineer,178000,2019-06-01,San Francisco"),
                          [{'name': 'Marcus Chen', 'email': 'marcus.chen@example.com', 'department': 'Engineering', 'role': 'Senior Software Engineer', 'salary': '155000', 'start_date': '2019-03-15', 'office': 'San Francisco'},
                            {'name': 'Priya Sharma', 'email': 'priya.sharma@example.com', 'department': 'Engineering', 'role': 'Staff Engineer', 'salary': '178000', 'start_date': '2019-06-01', 'office': 'San Francisco'}])
    def test_multilinesr(self):
        self.assertEqual(parser.parse("name,email,department,role,salary,start_date,office\rMarcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco\rPriya Sharma,priya.sharma@example.com,Engineering,Staff Engineer,178000,2019-06-01,San Francisco"),
                          [{'name': 'Marcus Chen', 'email': 'marcus.chen@example.com', 'department': 'Engineering', 'role': 'Senior Software Engineer', 'salary': '155000', 'start_date': '2019-03-15', 'office': 'San Francisco'},
                            {'name': 'Priya Sharma', 'email': 'priya.sharma@example.com', 'department': 'Engineering', 'role': 'Staff Engineer', 'salary': '178000', 'start_date': '2019-06-01', 'office': 'San Francisco'}])
    def test_noheader(self):
        self.assertEqual(parser.parse("Marcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco\nPriya Sharma,priya.sharma@example.com,Engineering,Staff Engineer,178000,2019-06-01,San Francisco",header=False),
                          [['Marcus Chen', 'marcus.chen@example.com', 'Engineering', 'Senior Software Engineer', '155000', '2019-03-15', 'San Francisco'], ['Priya Sharma', 'priya.sharma@example.com', 'Engineering', 'Staff Engineer', '178000', '2019-06-01', 'San Francisco']])
    def test_quotation(self):
        self.assertEqual(parser.parse("\"a ""\n a,b"" \",b\",\"\n b,h\"\n \"a\",\"b\"",header=False),[['"a \n a,b "', 'b","'], [' b', 'h"\n "a","b"']])
if __name__ == "__main__":#pragma: no cover
    unittest.main()
# For at lave covarage gå i terminal skrive .venv\Scripts\activate
#Skriv herefter covarage eller coverage report
#Kan også lave covarage html og ind på index så jeg kan finde hvad de rikke kørte
#husk at køre coverage run -m unittest discover inden
#java -jar .\JetUML-win-3.10.jar for at køre jet uml   