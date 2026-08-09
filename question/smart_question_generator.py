# ============================================================
# SMART QUESTION GENERATOR
# ONLINE EXAM MANAGEMENT SYSTEM
# CLEAN FINAL VERSION
# PART 1/8
# ============================================================

import random
from db_connection import get_connection

# ============================================================
# QUESTION BANK
# ============================================================

QUESTION_BANK = {


# ============================================================
# PYTHON QUESTIONS
# ============================================================

"python": [

(
"Which keyword is used to define function in Python?",
"func",
"def",
"function",
"define",
"B) def"
),

(
"Python file extension is ______.",
".py",
".java",
".html",
".cpp",
"A) .py"
),

(
"Which symbol is used for comments in Python?",
"#",
"//",
"/* */",
"--",
"A) #"
),

(
"Which function is used to display output?",
"input()",
"print()",
"show()",
"display()",
"B) print()"
),

(
"Which data type stores True or False?",
"String",
"Integer",
"Boolean",
"List",
"C) Boolean"
),

(
"Which keyword creates class in Python?",
"class",
"object",
"struct",
"define",
"A) class"
),

(
"Which keyword is used to create a function in Python?",
"function",
"def",
"fun",
"define",
"B) def"
),

(
"Which symbol is used for floor division in Python?",
"/",
"//",
"%",
"**",
"B) //"
),

(
"Which function converts a value into string?",
"str()",
"string()",
"text()",
"convert()",
"A) str()"
),

(
"Which function returns the type of variable?",
"type()",
"typeof()",
"check()",
"var()",
"A) type()"
),

(
"Which collection does not allow duplicate values?",
"List",
"Tuple",
"Set",
"Dictionary",
"C) Set"
),

(
"Which keyword is used for conditional statements?",
"if",
"check",
"condition",
"case",
"A) if"
),

(
"Which keyword is used with if statement?",
"then",
"else",
"next",
"otherwise",
"B) else"
),

(
"Which keyword is used to handle exceptions?",
"error",
"try",
"catch",
"handle",
"B) try"
),

(
"Which function is used to get user input?",
"scan()",
"input()",
"get()",
"read()",
"B) input()"
),

(
"Which operator checks equality?",
"=",
"==",
"!=",
"+=",
"B) =="
),

(
"Which keyword is used to import modules?",
"include",
"import",
"using",
"module",
"B) import"
),

(
"Which file extension is used for Python files?",
".python",
".py",
".pt",
".p",
"B) .py"
),

(
"Which data type stores decimal numbers?",
"Integer",
"Float",
"String",
"Boolean",
"B) Float"
),

(
"Which method removes an item from list?",
"delete()",
"remove()",
"clearall()",
"erase()",
"B) remove()"
),

(
"Which method adds an element at the end of list?",
"append()",
"add()",
"insert()",
"push()",
"A) append()"
),

(
"Which loop is used to iterate over sequence?",
"if",
"for",
"switch",
"case",
"B) for"
),

(
"Which keyword creates an anonymous function?",
"lambda",
"function",
"anonymous",
"def",
"A) lambda"
),

(
"Which module provides mathematical functions?",
"random",
"math",
"calc",
"number",
"B) math"
),

(
"Which method converts all characters to uppercase?",
"upper()",
"uppercase()",
"capital()",
"up()",
"A) upper()"
),

(
"Which keyword exits a loop immediately?",
"stop",
"break",
"exit",
"end",
"B) break"
),

(
"Python is an open source programming language.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python supports object oriented programming.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python uses indentation to define blocks of code.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python variables have fixed data types.",
"True",
"False",
"",
"",
"B) False"
),

(
"Python can be used for web development.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python supports file handling operations.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python cannot perform mathematical operations.",
"True",
"False",
"",
"",
"B) False"
),

(
"Python is a case-sensitive language.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python supports multiple inheritance.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python code is executed line by line.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python was developed by Guido van Rossum.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python uses compiler only and not interpreter.",
"True",
"False",
"",
"",
"B) False"
),

(
"Lists in Python are mutable.",
"True",
"False",
"",
"",
"A) True"
),

(
"Tuples in Python are immutable.",
"True",
"False",
"",
"",
"A) True"
),

(
"Dictionary stores data in key-value pairs.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python supports exception handling.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python cannot connect with databases.",
"True",
"False",
"",
"",
"B) False"
),

(
"Functions are created using def keyword in Python.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python supports modules and packages.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python is a low level programming language.",
"True",
"False",
"",
"",
"B) False"
),

(
"Keyword used to create a class is ______.",
"class",
"def",
"object",
"new",
"A) class"
),

(
"Function used to get length of list is ______.",
"len()",
"length()",
"size()",
"count()",
"A) len()"
),

(
"Function used to convert integer into string is ______.",
"str()",
"int()",
"float()",
"text()",
"A) str()"
),

(
"Function used to convert value into integer is ______.",
"int()",
"str()",
"integer()",
"number()",
"A) int()"
),

(
"Collection used to store unique values is ______.",
"Set",
"List",
"Tuple",
"String",
"A) Set"
),

(
"Keyword used to import a module is ______.",
"import",
"include",
"using",
"module",
"A) import"
),

(
"Operator used for power calculation is ______.",
"**",
"//",
"%",
"^",
"A) **"
),

(
"Keyword used to exit loop is ______.",
"break",
"stop",
"exit",
"end",
"A) break"
),

(
"Keyword used to skip current iteration is ______.",
"continue",
"skip",
"pass",
"next",
"A) continue"
),

(
"Function used to display output is ______.",
"print()",
"display()",
"show()",
"output()",
"A) print()"
),

(
"Function used to take input from user is ______.",
"input()",
"get()",
"scan()",
"read()",
"A) input()"
),

(
"File extension of Python program is ______.",
".py",
".java",
".html",
".cpp",
"A) .py"
),

(
"Python single line comments start with ______ symbol.",
"#",
"//",
"/*",
"--",
"A) #"
),

(
"Keyword used for anonymous function is ______.",
"lambda",
"anonymous",
"function",
"def",
"A) lambda"
),

(
"Data type used to store True or False is ______.",
"Boolean",
"String",
"Integer",
"Float",
"A) Boolean"
),

(
"Method used to add element in list is ______.",
"append()",
"add()",
"push()",
"insert()",
"A) append()"
),

(
"Method used to remove an item from list is ______.",
"remove()",
"delete()",
"erase()",
"clearitem()",
"A) remove()"
),

(
"Module used for random number generation is ______.",
"random",
"math",
"number",
"rand",
"A) random"
),

(
"Python was created by ______.",
"Guido van Rossum",
"James Gosling",
"Dennis Ritchie",
"Bjarne Stroustrup",
"A) Guido van Rossum"
),

(
"Loop that executes while condition is true is ______.",
"while",
"for",
"do",
"repeat",
"A) while"
),

(
"Which function takes input from user?",
"input()",
"get()",
"read()",
"scan()",
"A) input()"
),

(
"Which collection stores key-value pairs?",
"List",
"Tuple",
"Dictionary",
"Set",
"C) Dictionary"
),

(
"Which operator is used for multiplication?",
"+",
"*",
"-",
"/",
"B) *"
),

(
"Which method adds item into list?",
"add()",
"append()",
"push()",
"insert()",
"B) append()"
),


# TRUE FALSE

(
"Python is an interpreted language.",
"True",
"False",
"",
"",
"A) True"
),

(
"Python supports Object Oriented Programming.",
"True",
"False",
"",
"",
"A) True"
),


# FILL BLANK

(
"Keyword used to define function is ______.",
"def",
"class",
"function",
"define",
"A) def"
),

(
"Function used to display output is ______.",
"print()",
"input()",
"show()",
"display()",
"A) print()"
),

],
# ============================================================
# JAVA QUESTIONS
# ============================================================


"java": [

(
"Java is developed by which company?",
"Sun Microsystems",
"Microsoft",
"Google",
"IBM",
"A) Sun Microsystems"
),

(
"Java is a ______ language.",
"High Level",
"Machine",
"Low Level",
"Assembly",
"A) High Level"
),

(
"Which company developed Java?",
"Sun Microsystems",
"Microsoft",
"Google",
"IBM",
"A) Sun Microsystems"
),

(
"Which keyword is used to inherit a class in Java?",
"extends",
"inherit",
"implements",
"super",
"A) extends"
),

(
"Which keyword is used to create an object?",
"new",
"create",
"object",
"class",
"A) new"
),

(
"Which method is the starting point of Java program?",
"main()",
"start()",
"run()",
"begin()",
"A) main()"
),

(
"Which component executes Java bytecode?",
"JVM",
"JDK",
"JRE",
"Compiler",
"A) JVM"
),

(
"Which symbol is used to end a statement in Java?",
":",
";",
".",
",",
"B) ;"
),

(
"Which data type stores whole numbers?",
"int",
"float",
"char",
"boolean",
"A) int"
),

(
"Which data type stores decimal values?",
"float",
"int",
"char",
"boolean",
"A) float"
),

(
"Which keyword is used to define a constant?",
"final",
"constant",
"static",
"fixed",
"A) final"
),

(
"Which access modifier allows access everywhere?",
"public",
"private",
"protected",
"default",
"A) public"
),

(
"Which keyword refers to current object?",
"this",
"self",
"current",
"object",
"A) this"
),

(
"Which keyword is used to call parent class constructor?",
"super",
"parent",
"base",
"extends",
"A) super"
),

(
"Which operator is used for addition?",
"+",
"-",
"*",
"/",
"A) +"
),

(
"Which package contains Scanner class?",
"java.util",
"java.io",
"java.lang",
"java.net",
"A) java.util"
),

(
"Which class is used to take input from user?",
"Scanner",
"Input",
"Reader",
"System",
"A) Scanner"
),

(
"Java supports ______.",
"OOP",
"Only procedural programming",
"Machine programming",
"Assembly",
"A) OOP"
),

(
"Which keyword is used to handle exception?",
"try",
"error",
"catching",
"handle",
"A) try"
),

(
"Which keyword is used to stop inheritance?",
"final",
"stop",
"static",
"private",
"A) final"
),

(
"Java source file extension is ______.",
".java",
".class",
".exe",
".txt",
"A) .java"
),

(
"Java is an object oriented programming language.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java programs are platform independent.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java uses JVM to run programs.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java source code file extension is .java.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java bytecode file extension is .class.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java does not support inheritance.",
"True",
"False",
"",
"",
"B) False"
),

(
"Java supports exception handling.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java is developed by Sun Microsystems.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java is a low level language.",
"True",
"False",
"",
"",
"B) False"
),

(
"Java supports multiple inheritance through classes.",
"True",
"False",
"",
"",
"B) False"
),

(
"Java supports multiple inheritance using interfaces.",
"True",
"False",
"",
"",
"A) True"
),

(
"Constructor name must be same as class name in Java.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java is case sensitive.",
"True",
"False",
"",
"",
"A) True"
),

(
"JDK contains JRE and development tools.",
"True",
"False",
"",
"",
"A) True"
),

(
"JVM converts bytecode into machine code.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java supports garbage collection.",
"True",
"False",
"",
"",
"A) True"
),

(
"Private members can be accessed from any class.",
"True",
"False",
"",
"",
"B) False"
),

(
"Public members can be accessed from anywhere.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java programs require a main() method for execution.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java does not support classes and objects.",
"True",
"False",
"",
"",
"B) False"
),

(
"Java source code file extension is ______.",
".java",
".class",
".exe",
".txt",
"A) .java"
),

(
"Java bytecode file extension is ______.",
".class",
".java",
".py",
".html",
"A) .class"
),

(
"Java program execution starts from ______ method.",
"main()",
"start()",
"run()",
"execute()",
"A) main()"
),

(
"Java keyword used to inherit a class is ______.",
"extends",
"inherit",
"implements",
"super",
"A) extends"
),

(
"Java keyword used to implement interface is ______.",
"implements",
"extends",
"interface",
"class",
"A) implements"
),

(
"Java keyword used to create an object is ______.",
"new",
"create",
"object",
"make",
"A) new"
),

(
"Java keyword used to define a class is ______.",
"class",
"define",
"struct",
"object",
"A) class"
),

(
"Java keyword used to stop inheritance is ______.",
"final",
"static",
"private",
"stop",
"A) final"
),

(
"Java keyword used for constant value is ______.",
"final",
"const",
"static",
"fixed",
"A) final"
),

(
"Java package keyword is ______.",
"package",
"import",
"include",
"using",
"A) package"
),

(
"Java keyword used to access package is ______.",
"import",
"package",
"include",
"use",
"A) import"
),

(
"Java default constructor has ______ return type.",
"No",
"void",
"int",
"null",
"A) No"
),

(
"Java class name starts with ______ letter convention.",
"Capital",
"Small",
"Number",
"Symbol",
"A) Capital"
),

(
"Java is based on ______ programming concept.",
"Object Oriented",
"Procedure",
"Machine",
"Assembly",
"A) Object Oriented"
),

(
"Java exception handling uses ______ block.",
"try-catch",
"if-else",
"switch-case",
"for-loop",
"A) try-catch"
),

(
"Java keyword used to throw exception is ______.",
"throw",
"throws",
"error",
"exception",
"A) throw"
),

(
"Java keyword used to declare exception is ______.",
"throws",
"throw",
"catch",
"try",
"A) throws"
),

(
"Java interface is declared using ______ keyword.",
"interface",
"class",
"abstract",
"implements",
"A) interface"
),

(
"Java method overloading is based on different ______.",
"parameters",
"classes",
"packages",
"objects",
"A) parameters"
),

(
"Java supports multiple inheritance through ______.",
"Interfaces",
"Classes",
"Objects",
"Methods",
"A) Interfaces"
),

(
"Java file extension is ______.",
".java",
".py",
".html",
".cpp",
"A) .java"
),

(
"Which keyword is used to create class?",
"class",
"object",
"define",
"struct",
"A) class"
),

(
"Which keyword is used to create object?",
"new",
"create",
"object",
"make",
"A) new"
),

(
"Which method is entry point of Java program?",
"main()",
"start()",
"run()",
"execute()",
"A) main()"
),

(
"JVM stands for ______.",
"Java Virtual Machine",
"Java Variable Machine",
"Java Visual Machine",
"None",
"A) Java Virtual Machine"
),

(
"Java supports ______ programming.",
"Object Oriented",
"Machine",
"Low Level",
"Assembly",
"A) Object Oriented"
),


# JAVA TRUE FALSE

(
"Java is platform independent.",
"True",
"False",
"",
"",
"A) True"
),

(
"Java supports inheritance.",
"True",
"False",
"",
"",
"A) True"
),


# JAVA FILL BLANK

(
"Java compiler creates ______ file.",
".class",
".java",
".exe",
".txt",
"A) .class"
),

(
"Java program starts from ______ method.",
"main()",
"start()",
"run()",
"execute()",
"A) main()"
),

],



# ============================================================
# DBMS QUESTIONS
# ============================================================


"dbms": [

(
"DBMS stands for ______.",
"Database Management System",
"Data Management System",
"Database Memory System",
"Data Backup System",
"A) Database Management System"
),

(
"Which language is used for database query?",
"SQL",
"HTML",
"CSS",
"Python",
"A) SQL"
),

(
"Which of the following is a database software?",
"MySQL",
"Python",
"HTML",
"CSS",
"A) MySQL"
),

(
"Which key uniquely identifies a record?",
"Primary Key",
"Foreign Key",
"Candidate Key",
"Alternate Key",
"A) Primary Key"
),

(
"Which command is used to create a table?",
"CREATE",
"INSERT",
"SELECT",
"UPDATE",
"A) CREATE"
),

(
"Which command removes a table?",
"DROP",
"DELETE",
"REMOVE",
"CLEAR",
"A) DROP"
),

(
"Which command is used to remove records?",
"DELETE",
"DROP",
"REMOVE",
"ERASE",
"A) DELETE"
),

(
"Which command changes existing data?",
"UPDATE",
"ALTER",
"CHANGE",
"MODIFY",
"A) UPDATE"
),

(
"Which command displays data from table?",
"SELECT",
"SHOW",
"DISPLAY",
"VIEW",
"A) SELECT"
),

(
"SQL stands for ______.",
"Structured Query Language",
"Simple Query Language",
"Standard Query Language",
"System Query Language",
"A) Structured Query Language"
),

(
"Which symbol is used for all columns in SQL?",
"*",
"#",
"%",
"&",
"A) *"
),

(
"Which clause is used to filter records?",
"WHERE",
"ORDER",
"GROUP",
"HAVING",
"A) WHERE"
),

(
"Which clause is used to sort records?",
"ORDER BY",
"SORT BY",
"GROUP BY",
"ARRANGE",
"A) ORDER BY"
),

(
"Which function counts rows in SQL?",
"COUNT()",
"SUM()",
"TOTAL()",
"NUMBER()",
"A) COUNT()"
),

(
"Which function finds maximum value?",
"MAX()",
"HIGH()",
"TOP()",
"LARGE()",
"A) MAX()"
),

(
"Which function finds average value?",
"AVG()",
"AVERAGE()",
"MEAN()",
"SUM()",
"A) AVG()"
),

(
"Which command adds new data into table?",
"INSERT",
"ADD",
"CREATE",
"PUT",
"A) INSERT"
),

(
"Which key creates relationship between tables?",
"Foreign Key",
"Primary Key",
"Unique Key",
"Super Key",
"A) Foreign Key"
),

(
"Database is a collection of ______.",
"Data",
"Programs",
"Files",
"Images",
"A) Data"
),

(
"DBMS provides ______ of data.",
"Security",
"Animation",
"Design",
"Formatting",
"A) Security"
),

(
"Which normal form removes repeating groups?",
"First Normal Form",
"Second Normal Form",
"Third Normal Form",
"BCNF",
"A) First Normal Form"
),

(
"Which language is used to manage databases?",
"SQL",
"HTML",
"Java",
"Python",
"A) SQL"
),

(
"DBMS is used to store and manage data.",
"True",
"False",
"",
"",
"A) True"
),

(
"SQL is a database query language.",
"True",
"False",
"",
"",
"A) True"
),

(
"Primary key can contain duplicate values.",
"True",
"False",
"",
"",
"B) False"
),

(
"Foreign key creates relationship between tables.",
"True",
"False",
"",
"",
"A) True"
),

(
"DELETE command removes records from a table.",
"True",
"False",
"",
"",
"A) True"
),

(
"DROP command removes a table completely.",
"True",
"False",
"",
"",
"A) True"
),

(
"SELECT command is used to retrieve data.",
"True",
"False",
"",
"",
"A) True"
),

(
"INSERT command is used to add new records.",
"True",
"False",
"",
"",
"A) True"
),

(
"UPDATE command modifies existing data.",
"True",
"False",
"",
"",
"A) True"
),

(
"DBMS improves data security.",
"True",
"False",
"",
"",
"A) True"
),

(
"SQL is a programming language.",
"True",
"False",
"",
"",
"B) False"
),

(
"A table contains rows and columns.",
"True",
"False",
"",
"",
"A) True"
),

(
"Database can store large amounts of data.",
"True",
"False",
"",
"",
"A) True"
),

(
"Normalization reduces data redundancy.",
"True",
"False",
"",
"",
"A) True"
),

(
"Primary key is always unique.",
"True",
"False",
"",
"",
"A) True"
),

(
"DBMS cannot provide data security.",
"True",
"False",
"",
"",
"B) False"
),

(
"Oracle is a database management system.",
"True",
"False",
"",
"",
"A) True"
),

(
"MySQL is an example of DBMS.",
"True",
"False",
"",
"",
"A) True"
),

(
"Database stores only images and videos.",
"True",
"False",
"",
"",
"B) False"
),

(
"SQL commands are used to communicate with databases.",
"True",
"False",
"",
"",
"A) True"
),


(
"DBMS full form is ______.",
"Database Management System",
"Data Management System",
"Database Memory System",
"Data Backup System",
"A) Database Management System"
),

(
"SQL full form is ______.",
"Structured Query Language",
"Simple Query Language",
"System Query Language",
"Standard Language",
"A) Structured Query Language"
),

(
"Command used to retrieve data is ______.",
"SELECT",
"INSERT",
"UPDATE",
"DELETE",
"A) SELECT"
),

(
"Command used to add new records is ______.",
"INSERT",
"DELETE",
"DROP",
"SELECT",
"A) INSERT"
),

(
"Command used to modify records is ______.",
"UPDATE",
"INSERT",
"CREATE",
"DROP",
"A) UPDATE"
),

(
"Command used to remove records is ______.",
"DELETE",
"DROP",
"REMOVE",
"CLEAR",
"A) DELETE"
),

(
"Unique identifier of a table is ______.",
"Primary Key",
"Foreign Key",
"Column",
"Row",
"A) Primary Key"
),

(
"Key used to connect two tables is ______.",
"Foreign Key",
"Primary Key",
"Candidate Key",
"Super Key",
"A) Foreign Key"
),

(
"A collection of related data is called ______.",
"Database",
"Program",
"File",
"Folder",
"A) Database"
),

(
"Rows in a table are called ______.",
"Records",
"Fields",
"Keys",
"Attributes",
"A) Records"
),

(
"Columns in a table are called ______.",
"Attributes",
"Records",
"Rows",
"Files",
"A) Attributes"
),

(
"Software used to manage database is called ______.",
"DBMS",
"HTML",
"Compiler",
"Browser",
"A) DBMS"
),

(
"Database language used to communicate with database is ______.",
"SQL",
"Python",
"Java",
"C++",
"A) SQL"
),

(
"Process of reducing data redundancy is called ______.",
"Normalization",
"Compilation",
"Execution",
"Encryption",
"A) Normalization"
),

(
"SQL command to create table is ______.",
"CREATE",
"MAKE",
"BUILD",
"NEW",
"A) CREATE"
),

(
"SQL command to delete table is ______.",
"DROP",
"DELETE",
"REMOVE",
"CLEAR",
"A) DROP"
),

(
"SQL command to sort records is ______.",
"ORDER BY",
"SORT",
"ARRANGE",
"GROUP",
"A) ORDER BY"
),

(
"SQL clause used for condition is ______.",
"WHERE",
"ORDER",
"GROUP",
"FROM",
"A) WHERE"
),

(
"MySQL is an example of ______.",
"DBMS",
"Operating System",
"Compiler",
"Browser",
"A) DBMS"
),

(
"Oracle is a type of ______.",
"Database Management System",
"Programming Language",
"Web Browser",
"Operating System",
"A) Database Management System"
),

(
"Which command retrieves data?",
"SELECT",
"INSERT",
"UPDATE",
"DELETE",
"A) SELECT"
),

(
"Which command adds new record?",
"INSERT",
"DELETE",
"SELECT",
"DROP",
"A) INSERT"
),

(
"Which command modifies data?",
"UPDATE",
"INSERT",
"DROP",
"CREATE",
"A) UPDATE"
),

(
"Primary key is used to ______.",
"Identify unique records",
"Delete table",
"Create folder",
"Print data",
"A) Identify unique records"
),


# DBMS TRUE FALSE

(
"DBMS manages databases.",
"True",
"False",
"",
"",
"A) True"
),

(
"SQL is used with databases.",
"True",
"False",
"",
"",
"A) True"
),


# DBMS FILL BLANK

(
"Database query language is ______.",
"SQL",
"CSS",
"HTML",
"Java",
"A) SQL"
),

(
"Unique identifier in table is ______.",
"Primary Key",
"Foreign Key",
"Column",
"Row",
"A) Primary Key"
),

],
# ============================================================
# SMART QUESTION GENERATOR
# PART 3/8
# HTML QUESTION BANK
# ============================================================


# ============================================================
# HTML QUESTIONS
# ============================================================

"html": [

(
"HTML stands for ______.",
"Hyper Text Markup Language",
"High Text Machine Language",
"Hyper Transfer Language",
"Home Tool Language",
"A) Hyper Text Markup Language"
),

(
"HTML stands for ______.",
"Hyper Text Markup Language",
"High Text Machine Language",
"Hyper Tool Language",
"Home Text Language",
"A) Hyper Text Markup Language"
),

(
"Which tag is used for largest heading?",
"<h1>",
"<h6>",
"<head>",
"<heading>",
"A) <h1>"
),

(
"Which tag is used to create line break?",
"<br>",
"<break>",
"<lb>",
"<line>",
"A) <br>"
),

(
"Which tag is used to create a list item?",
"<li>",
"<list>",
"<item>",
"<ul>",
"A) <li>"
),

(
"Which tag creates an ordered list?",
"<ol>",
"<ul>",
"<li>",
"<list>",
"A) <ol>"
),

(
"Which tag creates an unordered list?",
"<ul>",
"<ol>",
"<li>",
"<list>",
"A) <ul>"
),

(
"Which attribute specifies image path?",
"src",
"href",
"path",
"link",
"A) src"
),

(
"Which tag is used to create form?",
"<form>",
"<input>",
"<body>",
"<table>",
"A) <form>"
),

(
"Which tag is used for user input?",
"<input>",
"<text>",
"<field>",
"<data>",
"A) <input>"
),

(
"Which tag defines HTML document title?",
"<title>",
"<head>",
"<name>",
"<caption>",
"A) <title>"
),

(
"Which tag contains visible page content?",
"<body>",
"<head>",
"<html>",
"<main>",
"A) <body>"
),

(
"Which tag defines a table row?",
"<tr>",
"<td>",
"<th>",
"<row>",
"A) <tr>"
),

(
"Which tag defines table data?",
"<td>",
"<tr>",
"<data>",
"<cell>",
"A) <td>"
),

(
"Which tag defines table heading?",
"<th>",
"<head>",
"<thead>",
"<heading>",
"A) <th>"
),

(
"Which tag is used to add video?",
"<video>",
"<media>",
"<movie>",
"<play>",
"A) <video>"
),

(
"Which tag is used to add audio?",
"<audio>",
"<sound>",
"<music>",
"<mp3>",
"A) <audio>"
),

(
"HTML is a ______ language.",
"Markup",
"Programming",
"Database",
"Machine",
"A) Markup"
),

(
"Which software is used to write HTML code?",
"Text Editor",
"Compiler",
"Database",
"Debugger",
"A) Text Editor"
),

(
"HTML pages are viewed using ______.",
"Web Browser",
"Compiler",
"Database",
"Operating System",
"A) Web Browser"
),

(
"Which tag is the root element of HTML?",
"<html>",
"<body>",
"<root>",
"<main>",
"A) <html>"
),

(
"HTML is used to create web pages.",
"True",
"False",
"",
"",
"A) True"
),

(
"HTML uses tags to define elements.",
"True",
"False",
"",
"",
"A) True"
),

(
"HTML is a programming language.",
"True",
"False",
"",
"",
"B) False"
),

(
"HTML stands for Hyper Text Markup Language.",
"True",
"False",
"",
"",
"A) True"
),

(
"HTML files are saved with .html extension.",
"True",
"False",
"",
"",
"A) True"
),

(
"<h1> tag creates the biggest heading.",
"True",
"False",
"",
"",
"A) True"
),

(
"<p> tag is used to create paragraph.",
"True",
"False",
"",
"",
"A) True"
),

(
"<img> tag is used to insert images.",
"True",
"False",
"",
"",
"A) True"
),

(
"<a> tag is used to create hyperlinks.",
"True",
"False",
"",
"",
"A) True"
),

(
"HTML can create database tables.",
"True",
"False",
"",
"",
"B) False"
),

(
"<br> tag is used for line break.",
"True",
"False",
"",
"",
"A) True"
),

(
"<table> tag creates tables in HTML.",
"True",
"False",
"",
"",
"A) True"
),

(
"CSS is used with HTML for styling.",
"True",
"False",
"",
"",
"A) True"
),

(
"JavaScript can be added to HTML pages.",
"True",
"False",
"",
"",
"A) True"
),

(
"<body> tag contains visible webpage content.",
"True",
"False",
"",
"",
"A) True"
),

(
"<head> tag contains webpage information.",
"True",
"False",
"",
"",
"A) True"
),

(
"HTML cannot display images.",
"True",
"False",
"",
"",
"B) False"
),

(
"Web browsers can display HTML pages.",
"True",
"False",
"",
"",
"A) True"
),

(
"HTML tags are written inside angle brackets.",
"True",
"False",
"",
"",
"A) True"
),

(
"HTML is used for creating website structure.",
"True",
"False",
"",
"",
"A) True"
),

(
"HTML full form is ______.",
"Hyper Text Markup Language",
"High Text Machine Language",
"Hyper Transfer Language",
"Home Tool Language",
"A) Hyper Text Markup Language"
),

(
"HTML file extension is ______.",
".html",
".java",
".py",
".cpp",
"A) .html"
),

(
"Tag used to create heading is ______.",
"<h1>",
"<p>",
"<div>",
"<br>",
"A) <h1>"
),

(
"Tag used to create paragraph is ______.",
"<p>",
"<para>",
"<text>",
"<pg>",
"A) <p>"
),

(
"Tag used to insert image is ______.",
"<img>",
"<image>",
"<pic>",
"<src>",
"A) <img>"
),

(
"Tag used to create hyperlink is ______.",
"<a>",
"<link>",
"<href>",
"<url>",
"A) <a>"
),

(
"Tag used to create table is ______.",
"<table>",
"<tab>",
"<tr>",
"<td>",
"A) <table>"
),

(
"Tag used to create table row is ______.",
"<tr>",
"<td>",
"<th>",
"<row>",
"A) <tr>"
),

(
"Tag used to create table data is ______.",
"<td>",
"<tr>",
"<data>",
"<cell>",
"A) <td>"
),

(
"Tag used to create unordered list is ______.",
"<ul>",
"<ol>",
"<li>",
"<list>",
"A) <ul>"
),

(
"Tag used to create ordered list is ______.",
"<ol>",
"<ul>",
"<li>",
"<order>",
"A) <ol>"
),

(
"Attribute used to specify image location is ______.",
"src",
"href",
"path",
"link",
"A) src"
),

(
"Tag used for line break is ______.",
"<br>",
"<break>",
"<lb>",
"<line>",
"A) <br>"
),

(
"Tag used to create form is ______.",
"<form>",
"<input>",
"<body>",
"<table>",
"A) <form>"
),

(
"Tag used for user input is ______.",
"<input>",
"<field>",
"<data>",
"<text>",
"A) <input>"
),

(
"Tag containing visible content is ______.",
"<body>",
"<head>",
"<html>",
"<title>",
"A) <body>"
),

(
"Tag defining webpage title is ______.",
"<title>",
"<name>",
"<caption>",
"<head>",
"A) <title>"
),

(
"HTML root element is ______.",
"<html>",
"<body>",
"<root>",
"<main>",
"A) <html>"
),

(
"CSS is used for ______ HTML pages.",
"Styling",
"Programming",
"Database",
"Compilation",
"A) Styling"
),

(
"HTML pages are opened in a ______.",
"Web Browser",
"Compiler",
"Database",
"Editor",
"A) Web Browser"
),

(
"HTML is used to create ______.",
"Web Pages",
"Database",
"Operating System",
"Compiler",
"A) Web Pages"
),

(
"HTML file extension is ______.",
".html",
".java",
".py",
".cpp",
"A) .html"
),

(
"Which tag is used to create heading?",
"<h1>",
"<p>",
"<div>",
"<br>",
"A) <h1>"
),

(
"Which tag is used to create paragraph?",
"<p>",
"<para>",
"<text>",
"<pg>",
"A) <p>"
),

(
"Which tag is used to insert image?",
"<img>",
"<image>",
"<pic>",
"<src>",
"A) <img>"
),

(
"Which tag creates hyperlink?",
"<a>",
"<link>",
"<href>",
"<url>",
"A) <a>"
),

(
"HTML is a ______ language.",
"Markup",
"Programming",
"Database",
"Machine",
"A) Markup"
),

(
"Which tag creates table?",
"<table>",
"<tab>",
"<tr>",
"<td>",
"A) <table>"
),


# ==========================
# HTML TRUE/FALSE
# ==========================

(
"HTML is used to create web pages.",
"True",
"False",
"",
"",
"A) True"
),

(
"HTML uses tags.",
"True",
"False",
"",
"",
"A) True"
),

(
"HTML is a programming language.",
"True",
"False",
"",
"",
"B) False"
),


# ==========================
# HTML FILL BLANK
# ==========================

(
"HTML full form is ______.",
"Hyper Text Markup Language",
"Hyper Text Language",
"Home Tool Language",
"High Text Language",
"A) Hyper Text Markup Language"
),

(
"Image is inserted using ______ tag.",
"<img>",
"<image>",
"<pic>",
"<src>",
"A) <img>"
),

(
"Hyperlink is created using ______ tag.",
"<a>",
"<link>",
"<href>",
"<url>",
"A) <a>"
),
]
}
# ============================================================
# SMART QUESTION GENERATOR
# PART 4/8
# FUNCTIONS
# ============================================================


# ============================================================
# GET QUESTION BANK
# ============================================================

def get_question_bank(subject, question_type):

    subject = subject.strip().lower()

    all_questions = QUESTION_BANK.get(subject, [])

    filtered_questions = []


    for q in all_questions:

        question = q[0]
        option_a = q[1]
        option_b = q[2]


        # ==========================
        # MCQ FILTER
        # ==========================

        if question_type == "MCQ":

            if (
                option_a not in ["True", "False"]
                and option_b not in ["True", "False"]
                and "______" not in question
            ):

                filtered_questions.append(q)



        # ==========================
        # TRUE / FALSE FILTER
        # ==========================

        elif question_type == "True/False":

            if (
                option_a == "True"
                and option_b == "False"
            ):

                filtered_questions.append(q)



        # ==========================
        # FILL BLANK FILTER
        # ==========================

        elif question_type == "Fill in the Blanks":

            if (
                "______" in question
                and option_a not in ["True", "False"]
                and option_b not in ["True", "False"]
            ):

                filtered_questions.append(q)



    return filtered_questions




# ============================================================
# REMOVE DUPLICATE QUESTIONS
# ============================================================

def remove_duplicate_questions(questions):

    unique_questions = []

    seen = set()


    for q in questions:

        question_text = q[0].strip()


        if question_text not in seen:

            unique_questions.append(q)

            seen.add(question_text)



    return unique_questions
# ============================================================
# SMART QUESTION GENERATOR
# PART 5/8
# CREATE QUESTIONS
# ============================================================


def create_questions(
        subject,
        difficulty,
        number,
        question_type
):


    questions = get_question_bank(
        subject,
        question_type
    )


    if not questions:

        print("\nNo Questions Available!")

        return []


    questions = remove_duplicate_questions(
        questions
    )


    if number > len(questions):

        print(
            f"\nOnly {len(questions)} Questions Available!"
        )

        number = len(questions)


    selected_questions = random.sample(
        questions,
        number
    )


    return selected_questions




# ============================================================
# DISPLAY QUESTIONS
# ============================================================


def display_questions(questions):


    print("\n")

    print("=" * 60)

    print("        AI GENERATED QUESTIONS 🤖")

    print("=" * 60)



    for index, q in enumerate(questions, 1):


        print(
            f"\nQ{index}. {q[0]}"
        )


        print("A)", q[1])
        print("B)", q[2])

        if q[3]:
                 print("C)", q[3])

        if q[4]:
                print("D)", q[4])

        print(
            "Correct Answer:",
            q[5]
        )


        print("-" * 60)
        # ============================================================
# SMART QUESTION GENERATOR
# PART 6/8
# SAVE QUESTIONS TO DATABASE
# ============================================================

def save_questions(
        questions,
        subject,
        difficulty,
        question_type,
        exam_id=1
):

    conn = get_connection()

    cursor = conn.cursor()


    # ====================================================
    # DELETE OLD QUESTIONS
    # SAME SUBJECT
    # ====================================================

    cursor.execute(
        """
        DELETE FROM question
        WHERE subject = ?
        """,
        (
            subject,
        )
    )


    # ====================================================
    # INSERT NEW QUESTIONS
    # ====================================================

    for q in questions:
        cursor.execute(
            """
            INSERT INTO question
            (
                exam_id,
                question_text,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                subject,
                difficulty,
                topic,
                question_type
            )
            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
            """,
            (
                exam_id,
                q[0],
                q[1],
                q[2],
                q[3],
                q[4],
                q[5],
                subject,
                difficulty,
                subject,
                question_type
            )
        )

    conn.commit()
    conn.close()

    print("\nQuestions Saved Successfully! ✅")
    # ============================================================
# SMART QUESTION GENERATOR
# PART 7/8
# GENERATE AND SAVE QUESTIONS
# ============================================================


def generate_and_save_questions(
        subject,
        difficulty,
        number,
        question_type,
        exam_id=1
):


    questions = create_questions(
        subject,
        difficulty,
        number,
        question_type
    )


    if questions:


        save_questions(
            questions,
            subject,
            difficulty,
            question_type,
            exam_id
        )


        display_questions(
            questions
        )


    return questions
    # ============================================================
# SMART QUESTION GENERATOR
# PART 8/8
# MENU + MAIN FUNCTION
# ============================================================

def smart_question_generator_menu():


    print("\n")

    print("=" * 60)

    print("        SMART QUESTION GENERATOR 🤖")

    print("=" * 60)



    # SUBJECT INPUT

    subject = input(
        "Enter Subject (python/java/dbms/html): "
    ).strip().lower()



    print("\nSelect Question Type")

    print("1. MCQ")

    print("2. True / False")

    print("3. Fill in the Blanks")



    choice = input(
        "Enter Choice: "
    ).strip()



    if choice == "1":

        question_type = "MCQ"



    elif choice == "2":

        question_type = "True/False"



    elif choice == "3":

        question_type = "Fill in the Blanks"



    else:

        print(
            "\nInvalid Choice! ❌"
        )

        return




    difficulty = input(
        "Enter Difficulty (Easy/Medium/Hard): "
    ).strip()



    try:

        number = int(
            input(
                "Enter Number of Questions: "
            )
        )


    except ValueError:


        print(
            "\nEnter only numbers! ❌"
        )

        return




    generate_and_save_questions(

        subject,

        difficulty,

        number,

        question_type

    )





# ============================================================
# MAIN EXECUTION
# ============================================================


if __name__ == "__main__":


    smart_question_generator_menu()