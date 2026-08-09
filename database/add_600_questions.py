import sqlite3
import random
import os


# ============================================================
# DATABASE
# ============================================================

DB_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "online_exam.db"
)


# ============================================================
# QUESTION DATA
# 50 concepts for each subject
# ============================================================

DATA = {

    "Python": [

        ("Which keyword is used to define a function in Python?",
         "def", ["func", "function", "define"]),

        ("Which function is used to display output in Python?",
         "print()", ["display()", "show()", "output()"]),

        ("Which data type stores True or False?",
         "bool", ["int", "str", "float"]),

        ("Which symbol is used for a comment in Python?",
         "#", ["//", "/*", "--"]),

        ("Which keyword is used to create a class?",
         "class", ["object", "struct", "define"]),

        ("Which keyword is used to create a loop over a sequence?",
         "for", ["loop", "repeat", "foreach"]),

        ("Which keyword is used for conditional statements?",
         "if", ["when", "check", "condition"]),

        ("Which keyword is used when a condition is false?",
         "else", ["otherwise", "false", "elif"]),

        ("Which keyword checks another condition?",
         "elif", ["elseif", "elseif", "check"]),

        ("Which collection stores ordered items and allows duplicates?",
         "list", ["set", "tuple", "dictionary"]),

        ("Which collection stores unique unordered items?",
         "set", ["list", "tuple", "array"]),

        ("Which collection stores key-value pairs?",
         "dictionary", ["list", "tuple", "set"]),

        ("Which collection is immutable?",
         "tuple", ["list", "set", "dictionary"]),

        ("Which operator is used for exponentiation?",
         "**", ["^", "//", "%%"]),

        ("Which operator performs floor division?",
         "//", ["/", "%", "**"]),

        ("Which operator returns the remainder?",
         "%", ["//", "/", "**"]),

        ("Which function returns the length of an object?",
         "len()", ["length()", "size()", "count()"]),

        ("Which function returns the type of an object?",
         "type()", ["typeof()", "datatype()", "classof()"]),

        ("Which keyword is used to import a module?",
         "import", ["include", "using", "require"]),

        ("Which keyword is used to handle exceptions?",
         "try", ["catch", "error", "handle"]),

        ("Which block handles an exception?",
         "except", ["catch", "error", "handle"]),

        ("Which block runs whether an exception occurs or not?",
         "finally", ["always", "last", "complete"]),

        ("Which keyword is used to raise an exception?",
         "raise", ["throw", "error", "exception"]),

        ("Which keyword exits a loop?",
         "break", ["exit", "stop", "end"]),

        ("Which keyword skips the current loop iteration?",
         "continue", ["skip", "pass", "next"]),

        ("Which keyword does nothing and acts as a placeholder?",
         "pass", ["skip", "null", "empty"]),

        ("Which function converts a value to an integer?",
         "int()", ["integer()", "number()", "convert()"]),

        ("Which function converts a value to a string?",
         "str()", ["string()", "text()", "convert()"]),

        ("Which function converts a value to a floating-point number?",
         "float()", ["decimal()", "double()", "real()"]),

        ("Which function reads input from the user?",
         "input()", ["read()", "scan()", "get()"]),

        ("Which keyword returns a value from a function?",
         "return", ["send", "output", "result"]),

        ("Which built-in function creates a sequence of numbers?",
         "range()", ["sequence()", "numbers()", "series()"]),

        ("Which method adds an item to the end of a list?",
         "append()", ["add()", "insertEnd()", "push()"]),

        ("Which method removes an item from a list?",
         "remove()", ["delete()", "erase()", "discard()"]),

        ("Which method sorts a list?",
         "sort()", ["order()", "arrange()", "sortedList()"]),

        ("Which method reverses a list?",
         "reverse()", ["back()", "invert()", "flip()"]),

        ("Which method returns dictionary keys?",
         "keys()", ["getKeys()", "keyList()", "index()"]),

        ("Which method returns dictionary values?",
         "values()", ["getValues()", "valueList()", "itemsOnly()"]),

        ("Which method returns key-value pairs of a dictionary?",
         "items()", ["pairs()", "entries()", "records()"]),

        ("Which keyword is used to create an anonymous function?",
         "lambda", ["anonymous", "function", "def"]),

        ("Which library is commonly used for mathematical functions?",
         "math", ["calc", "mathematics", "numeric"]),

        ("Which library is commonly used for random numbers?",
         "random", ["rand", "numbers", "chance"]),

        ("Which library is commonly used for working with dates?",
         "datetime", ["dateLib", "calendarLib", "timeDate"]),

        ("Which function opens a file?",
         "open()", ["file()", "load()", "readfile()"]),

        ("Which mode is used to read a file?",
         "r", ["read", "rd", "input"]),

        ("Which mode is used to write to a file?",
         "w", ["write", "wr", "output"]),

        ("Which mode adds data to an existing file?",
         "a", ["add", "append", "plus"]),

        ("Which keyword is used to create a generator value?",
         "yield", ["generate", "return", "produce"]),

        ("Which special method initializes an object?",
         "__init__", ["__start__", "__newobject__", "__create__"]),

        ("Which programming concept allows a class to inherit another class?",
         "inheritance", ["encapsulation", "iteration", "compilation"])
    ],


    "Java": [

        ("Which keyword is used to define a class in Java?",
         "class", ["define", "struct", "object"]),

        ("Which method is the entry point of a Java program?",
         "main()", ["start()", "run()", "execute()"]),

        ("Which keyword creates an object?",
         "new", ["create", "object", "make"]),

        ("Which keyword is used for inheritance?",
         "extends", ["inherits", "implements", "inherit"]),

        ("Which keyword is used to implement an interface?",
         "implements", ["extends", "interface", "uses"]),

        ("Which keyword prevents a class from being inherited?",
         "final", ["static", "private", "sealed"]),

        ("Which keyword creates a constant-like variable?",
         "final", ["const", "constant", "static"]),

        ("Which data type stores whole numbers?",
         "int", ["float", "double", "char"]),

        ("Which data type stores a single character?",
         "char", ["string", "character", "byte"]),

        ("Which data type stores true or false?",
         "boolean", ["bool", "bit", "logical"]),

        ("Which data type stores decimal values?",
         "double", ["decimal", "real", "number"]),

        ("Which keyword creates a method?",
         "void", ["method", "function", "define"]),

        ("Which keyword refers to the current object?",
         "this", ["self", "current", "object"]),

        ("Which keyword refers to the parent class?",
         "super", ["parent", "base", "upper"]),

        ("Which access modifier allows access from anywhere?",
         "public", ["global", "open", "protected"]),

        ("Which access modifier restricts access to the class?",
         "private", ["local", "protected", "hidden"]),

        ("Which access modifier allows package and subclass access?",
         "protected", ["private", "package", "internal"]),

        ("Which keyword makes a variable belong to the class?",
         "static", ["class", "shared", "global"]),

        ("Which keyword handles exceptions?",
         "try", ["catch", "error", "handle"]),

        ("Which block catches an exception?",
         "catch", ["except", "handle", "error"]),

        ("Which block always executes after try/catch?",
         "finally", ["always", "last", "complete"]),

        ("Which keyword manually throws an exception?",
         "throw", ["raise", "error", "exception"]),

        ("Which keyword declares that a method may throw an exception?",
         "throws", ["throw", "exception", "raise"]),

        ("Which collection allows duplicate elements?",
         "ArrayList", ["HashSet", "TreeSet", "Set"]),

        ("Which collection stores unique elements?",
         "HashSet", ["ArrayList", "LinkedList", "Vector"]),

        ("Which interface represents a key-value collection?",
         "Map", ["List", "Set", "Collection"]),

        ("Which class implements Map using hashing?",
         "HashMap", ["HashSet", "ArrayMap", "MapList"]),

        ("Which keyword is used for conditional statements?",
         "if", ["when", "check", "condition"]),

        ("Which keyword handles the alternative condition?",
         "else", ["otherwise", "alternative", "false"]),

        ("Which statement selects among multiple cases?",
         "switch", ["select", "choose", "case"]),

        ("Which loop is commonly used when the number of iterations is known?",
         "for", ["while", "repeat", "loop"]),

        ("Which loop executes while a condition is true?",
         "while", ["during", "for", "repeat"]),

        ("Which loop executes its body at least once?",
         "do-while", ["while", "for", "repeat"]),

        ("Which keyword exits a loop?",
         "break", ["exit", "stop", "end"]),

        ("Which keyword skips the current iteration?",
         "continue", ["skip", "next", "pass"]),

        ("Which package contains the Scanner class?",
         "java.util", ["java.io", "java.lang", "java.scan"]),

        ("Which class is commonly used to receive keyboard input?",
         "Scanner", ["InputReader", "Keyboard", "Reader"]),

        ("Which package is automatically imported in Java?",
         "java.lang", ["java.util", "java.io", "java.core"]),

        ("Which class represents text?",
         "String", ["Text", "Character", "StringType"]),

        ("Which method returns the length of a String?",
         "length()", ["size()", "count()", "len()"]),

        ("Which method compares String contents?",
         "equals()", ["compare()", "same()", "match()"]),

        ("Which keyword is used to define an interface?",
         "interface", ["implements", "abstract", "protocol"]),

        ("Which keyword defines an abstract class or method?",
         "abstract", ["virtual", "interface", "base"]),

        ("Which concept hides implementation details?",
         "abstraction", ["inheritance", "iteration", "compilation"]),

        ("Which concept bundles data and methods?",
         "encapsulation", ["inheritance", "polymorphism", "iteration"]),

        ("Which OOP feature allows one interface to have many forms?",
         "polymorphism", ["inheritance", "encapsulation", "abstraction"]),

        ("Which tool compiles Java source code?",
         "javac", ["java", "javadoc", "jar"]),

        ("Which command runs a compiled Java class?",
         "java", ["javac", "runjava", "execute"]),

        ("Which file extension is used for Java source code?",
         ".java", [".class", ".jar", ".jav"]),

        ("Which keyword is used to create a package in Java?",
         "package", ["namespace", "module", "library"])
    ],


    "HTML": [

        ("Which tag defines the main heading?",
         "<h1>", ["<head>", "<title>", "<heading>"]),

        ("Which tag creates a paragraph?",
         "<p>", ["<para>", "<text>", "<paragraph>"]),

        ("Which tag creates a hyperlink?",
         "<a>", ["<link>", "<href>", "<url>"]),

        ("Which attribute specifies a hyperlink destination?",
         "href", ["src", "link", "url"]),

        ("Which tag displays an image?",
         "<img>", ["<image>", "<picture>", "<src>"]),

        ("Which attribute specifies an image source?",
         "src", ["href", "source", "link"]),

        ("Which attribute provides alternative image text?",
         "alt", ["text", "title", "description"]),

        ("Which tag creates an unordered list?",
         "<ul>", ["<ol>", "<list>", "<li>"]),

        ("Which tag creates an ordered list?",
         "<ol>", ["<ul>", "<list>", "<order>"]),

        ("Which tag defines a list item?",
         "<li>", ["<item>", "<listitem>", "<ulitem>"]),

        ("Which tag creates a table?",
         "<table>", ["<tab>", "<grid>", "<data>"]),

        ("Which tag defines a table row?",
         "<tr>", ["<row>", "<td>", "<table-row>"]),

        ("Which tag defines a table cell?",
         "<td>", ["<cell>", "<tr>", "<data>"]),

        ("Which tag defines a table header cell?",
         "<th>", ["<header>", "<td>", "<theadcell>"]),

        ("Which tag defines a form?",
         "<form>", ["<input>", "<fieldset>", "<formbox>"]),

        ("Which tag creates a text input?",
         "<input>", ["<text>", "<textbox>", "<field>"]),

        ("Which attribute specifies the input type?",
         "type", ["inputtype", "kind", "control"]),

        ("Which attribute gives an input a name?",
         "name", ["id", "label", "field"]),

        ("Which tag creates a button?",
         "<button>", ["<btn>", "<inputbutton>", "<click>"]),

        ("Which tag creates a dropdown list?",
         "<select>", ["<dropdown>", "<list>", "<option>"]),

        ("Which tag defines an option in a dropdown?",
         "<option>", ["<item>", "<choice>", "<selectitem>"]),

        ("Which tag creates a line break?",
         "<br>", ["<break>", "<lb>", "<newline>"]),

        ("Which tag creates a horizontal line?",
         "<hr>", ["<line>", "<horizontal>", "<border>"]),

        ("Which tag contains metadata?",
         "<head>", ["<meta>", "<body>", "<data>"]),

        ("Which tag contains visible page content?",
         "<body>", ["<main>", "<content>", "<page>"]),

        ("Which tag defines the page title?",
         "<title>", ["<headtitle>", "<name>", "<caption>"]),

        ("Which declaration defines an HTML5 document?",
         "<!DOCTYPE html>", ["<HTML5>", "<DOCTYPE>", "<HTML5DOCTYPE>"]),

        ("Which tag is used for emphasized text?",
         "<em>", ["<italic>", "<iText>", "<emphasis>"]),

        ("Which tag makes text bold semantically?",
         "<strong>", ["<bold>", "<bolder>", "<important>"]),

        ("Which tag creates a generic block container?",
         "<div>", ["<block>", "<sectionbox>", "<container>"]),

        ("Which tag creates a generic inline container?",
         "<span>", ["<inline>", "<text>", "<label>"]),

        ("Which tag represents navigation links?",
         "<nav>", ["<navigation>", "<menu>", "<links>"]),

        ("Which tag represents the main content?",
         "<main>", ["<content>", "<primary>", "<bodymain>"]),

        ("Which tag represents an independent article?",
         "<article>", ["<post>", "<content>", "<story>"]),

        ("Which tag represents a section?",
         "<section>", ["<part>", "<area>", "<block>"]),

        ("Which tag represents footer content?",
         "<footer>", ["<bottom>", "<foot>", "<pagefooter>"]),

        ("Which tag represents header content?",
         "<header>", ["<top>", "<headarea>", "<pagehead>"]),

        ("Which attribute gives a unique identifier?",
         "id", ["class", "name", "unique"]),

        ("Which attribute assigns one or more CSS classes?",
         "class", ["style", "group", "css"]),

        ("Which tag links an external CSS file?",
         "<link>", ["<css>", "<style>", "<stylesheet>"]),

        ("Which tag contains internal CSS?",
         "<style>", ["<css>", "<design>", "<link>"]),

        ("Which tag contains JavaScript?",
         "<script>", ["<javascript>", "<js>", "<code>"]),

        ("Which tag embeds audio?",
         "<audio>", ["<sound>", "<music>", "<mediaaudio>"]),

        ("Which tag embeds video?",
         "<video>", ["<movie>", "<media>", "<videofile>"]),

        ("Which tag embeds another webpage?",
         "<iframe>", ["<framepage>", "<embedpage>", "<webframe>"]),

        ("Which tag creates a form label?",
         "<label>", ["<formlabel>", "<caption>", "<name>"]),

        ("Which attribute makes an input mandatory?",
         "required", ["mandatory", "must", "validate"]),

        ("Which attribute displays hint text inside an input?",
         "placeholder", ["hint", "help", "tip"]),

        ("Which tag defines a definition list?",
         "<dl>", ["<definition>", "<listdef>", "<deflist>"]),

        ("Which tag defines a term in a definition list?",
         "<dt>", ["<term>", "<definitionterm>", "<dterm>"])
    ],


    "DBMS": [

        ("What does DBMS stand for?",
         "Database Management System", ["Data Backup Management System", "Database Machine System", "Data Management Software"]),

        ("Which language is used to query relational databases?",
         "SQL", ["HTML", "CSS", "XML"]),

        ("Which command retrieves data?",
         "SELECT", ["GET", "FETCHDATA", "READ"]),

        ("Which command adds new records?",
         "INSERT", ["ADD", "CREATE", "APPEND"]),

        ("Which command modifies existing records?",
         "UPDATE", ["MODIFY", "CHANGE", "ALTERDATA"]),

        ("Which command removes records?",
         "DELETE", ["REMOVE", "DROP", "CLEAR"]),

        ("Which command creates a table?",
         "CREATE TABLE", ["NEW TABLE", "MAKE TABLE", "ADD TABLE"]),

        ("Which command removes a table?",
         "DROP TABLE", ["DELETE TABLE", "REMOVE TABLE", "CLEAR TABLE"]),

        ("Which clause filters rows?",
         "WHERE", ["FILTER", "HAVING", "WHEN"]),

        ("Which clause sorts query results?",
         "ORDER BY", ["SORT BY", "GROUP BY", "ARRANGE"]),

        ("Which clause groups rows?",
         "GROUP BY", ["ORDER BY", "COLLECT BY", "GROUP"]),

        ("Which clause filters grouped results?",
         "HAVING", ["WHERE", "GROUP", "FILTER"]),

        ("Which function counts rows?",
         "COUNT()", ["TOTAL()", "NUMBER()", "ROWS()"]),

        ("Which function calculates an average?",
         "AVG()", ["AVERAGE()", "MEAN()", "MID()"]),

        ("Which function calculates a total?",
         "SUM()", ["TOTAL()", "ADD()", "COUNT()"]),

        ("Which function finds the maximum value?",
         "MAX()", ["HIGH()", "TOP()", "LARGE()"]),

        ("Which function finds the minimum value?",
         "MIN()", ["LOW()", "SMALL()", "BOTTOM()"]),

        ("Which key uniquely identifies a record?",
         "Primary Key", ["Foreign Key", "Candidate Key", "Index Key"]),

        ("Which key references another table?",
         "Foreign Key", ["Primary Key", "Reference Key", "Link Key"]),

        ("Which constraint prevents duplicate values?",
         "UNIQUE", ["DISTINCT", "NO DUPLICATE", "SINGLE"]),

        ("Which constraint prevents NULL values?",
         "NOT NULL", ["NO NULL", "REQUIRED", "EMPTY NO"]),

        ("Which constraint checks a condition?",
         "CHECK", ["VALIDATE", "IF", "CONDITION"]),

        ("Which constraint provides a default value?",
         "DEFAULT", ["VALUE", "AUTO", "STANDARD"]),

        ("Which keyword removes duplicate query results?",
         "DISTINCT", ["UNIQUE", "ONLY", "DIFFERENT"]),

        ("Which operator combines results of two queries?",
         "UNION", ["JOIN", "MERGE", "COMBINE"]),

        ("Which join returns matching records from both tables?",
         "INNER JOIN", ["MATCH JOIN", "COMMON JOIN", "EQUAL JOIN"]),

        ("Which join returns all records from the left table?",
         "LEFT JOIN", ["LEFT OUTER", "ALL LEFT", "OUTER LEFT"]),

        ("Which join returns all records from the right table?",
         "RIGHT JOIN", ["RIGHT OUTER", "ALL RIGHT", "OUTER RIGHT"]),

        ("Which join returns all records from both tables?",
         "FULL OUTER JOIN", ["ALL JOIN", "COMPLETE JOIN", "OUTER ALL"]),

        ("Which join produces every possible combination?",
         "CROSS JOIN", ["FULL JOIN", "COMBINATION JOIN", "ALL JOIN"]),

        ("What is normalization used for?",
         "Reducing data redundancy", ["Increasing duplication", "Deleting databases", "Increasing storage"]),

        ("Which normal form removes repeating groups?",
         "First Normal Form", ["Second Normal Form", "Third Normal Form", "BCNF"]),

        ("Which normal form removes partial dependency?",
         "Second Normal Form", ["First Normal Form", "Third Normal Form", "BCNF"]),

        ("Which normal form removes transitive dependency?",
         "Third Normal Form", ["First Normal Form", "Second Normal Form", "BCNF"]),

        ("What does ACID stand for?",
         "Atomicity, Consistency, Isolation, Durability", ["Accuracy, Control, Integrity, Data", "Access, Consistency, Index, Data", "Atomic, Central, Internal, Durable"]),

        ("Which ACID property means all-or-nothing?",
         "Atomicity", ["Consistency", "Isolation", "Durability"]),

        ("Which ACID property maintains valid database state?",
         "Consistency", ["Atomicity", "Isolation", "Durability"]),

        ("Which ACID property separates transactions?",
         "Isolation", ["Atomicity", "Consistency", "Durability"]),

        ("Which ACID property preserves committed data?",
         "Durability", ["Atomicity", "Consistency", "Isolation"]),

        ("Which command permanently saves a transaction?",
         "COMMIT", ["SAVE", "STORE", "APPLY"]),

        ("Which command reverses a transaction?",
         "ROLLBACK", ["UNDO", "REVERSE", "CANCEL"]),

        ("Which database object speeds up searching?",
         "Index", ["Key", "View", "Trigger"]),

        ("Which database object is a virtual table?",
         "View", ["Index", "Trigger", "Schema"]),

        ("Which object automatically executes when an event occurs?",
         "Trigger", ["Procedure", "Function", "Index"]),

        ("Which object stores reusable SQL statements?",
         "Stored Procedure", ["View", "Index", "Trigger"]),

        ("Which language defines database structure?",
         "DDL", ["DML", "DCL", "TCL"]),

        ("Which language manipulates data?",
         "DML", ["DDL", "DCL", "TCL"]),

        ("Which language controls permissions?",
         "DCL", ["DDL", "DML", "TCL"]),

        ("Which language controls transactions?",
         "TCL", ["DDL", "DML", "DCL"]),

        ("What is a row in a relational table called?",
         "Record", ["Field", "Column", "Attribute"])
    ]
}


# ============================================================
# CHECK DATA
# ============================================================

for subject, questions in DATA.items():

    if len(questions) != 50:
        raise ValueError(
            f"{subject} must have exactly 50 questions. "
            f"Found {len(questions)}."
        )


# ============================================================
# DATABASE CONNECTION
# ============================================================

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


# ============================================================
# DELETE OLD QUESTIONS
# ============================================================

cursor.execute("DELETE FROM question")

print("Old questions deleted.")


# ============================================================
# EXAM IDs
# Existing exams:
# 1 = Python
# 2 = Java
# 3 = HTML
# 4 = DBMS
# ============================================================

exam_ids = {
    "Python": 1,
    "Java": 2,
    "HTML": 3,
    "DBMS": 4
}


# ============================================================
# INSERT QUESTIONS
# ============================================================

question_id = 1

for subject, question_list in DATA.items():

    exam_id = exam_ids[subject]

    for index, item in enumerate(question_list):

        question_text = item[0]
        correct_answer = item[1]
        options = item[2]

        difficulty_list = [
            "Easy",
            "Medium",
            "Hard"
        ]

        difficulty = difficulty_list[index % 3]


        # ----------------------------------------------------
        # MCQ
        # ----------------------------------------------------

        mcq_options = options + [correct_answer]
        random.shuffle(mcq_options)

        option_a = mcq_options[0]
        option_b = mcq_options[1]
        option_c = mcq_options[2]
        option_d = mcq_options[3]

        cursor.execute("""
            INSERT INTO question
            (
                question_id,
                exam_id,
                topic,
                question_text,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                subject,
                difficulty,
                question_type
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            question_id,
            exam_id,
            "General",
            question_text,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            subject,
            difficulty,
            "MCQ"
        ))

        question_id += 1


        # ----------------------------------------------------
        # TRUE / FALSE
        # ----------------------------------------------------

        tf_statement = question_text.replace(
            "Which",
            "The correct answer to the following question is"
        )

        tf_correct = "True"

        cursor.execute("""
            INSERT INTO question
            (
                question_id,
                exam_id,
                topic,
                question_text,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                subject,
                difficulty,
                question_type
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            question_id,
            exam_id,
            "General",
            f"{tf_statement}: {correct_answer}",
            "True",
            "False",
            "",
            "",
            tf_correct,
            subject,
            difficulty,
            "True/False"
        ))

        question_id += 1


        # ----------------------------------------------------
        # FILL IN THE BLANKS
        # ----------------------------------------------------

        fill_question = (
            question_text
            + " Answer: ________"
        )

        cursor.execute("""
            INSERT INTO question
            (
                question_id,
                exam_id,
                topic,
                question_text,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                subject,
                difficulty,
                question_type
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            question_id,
            exam_id,
            "General",
            fill_question,
            "",
            "",
            "",
            "",
            correct_answer,
            subject,
            difficulty,
            "Fill in the Blanks"
        ))

        question_id += 1


# ============================================================
# SAVE
# ============================================================

conn.commit()


# ============================================================
# VERIFY
# ============================================================

total = cursor.execute(
    "SELECT COUNT(*) FROM question"
).fetchone()[0]

print()
print("====================================")
print("QUESTION BANK CREATED")
print("====================================")
print("Total questions:", total)


for subject in exam_ids:

    count = cursor.execute("""
        SELECT COUNT(*)
        FROM question
        WHERE subject = ?
    """, (subject,)).fetchone()[0]

    print(subject, ":", count)


print()
print("Question type counts:")

for qtype in [
    "MCQ",
    "True/False",
    "Fill in the Blanks"
]:

    count = cursor.execute("""
        SELECT COUNT(*)
        FROM question
        WHERE question_type = ?
    """, (qtype,)).fetchone()[0]

    print(qtype, ":", count)


conn.close()

print()
print("600 questions inserted successfully.")