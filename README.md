# Campus Lost & Found Tracker

## 1. Project Overview

The Campus Lost & Found Tracker is a beginner-level Python command-line project that enables the reporting and search for lost and found items on a college campus.

The project illustrates fundamental programming constructs including:

Input/output

Variable declaration

Conditional

Loops

Functions

Lists

Linear search

Nested loops

Modular programming

The project offers options to:

1. Report a lost item

2. Report a found item

3. View all lost items

4. View all found items

5. Search for an item

6. Find possible matches between lost and found items

7. Exit the program

The project comprises of the following files:

```text

Campus_Lost_and_Found/

│

├── main.py

├── lost.py

├── found.py

├── search.py

├── match.py

└── display.py

```

### File Description

main.py

Contains the main menu and controls the execution of the program.

lost.py

Contains the functions for reporting and displaying lost items.

found.py

Contains the functions for reporting and displaying found items.

search.py

Contains the linear-search functionality for finding an item by name.

match.py

Compares lost and found item names and displays possible matches.

display.py

Contains the common function used to display item information.

The project requires:

Python 3.x

A command-line terminal

No external Python libraries are required.

To install the project, the user must:

### Step 1: Install Python

Install Python 3 from the official Python website if it is not already installed.

### Step 2: Download or Clone the Repository

Clone the GitHub repository or download the project folder.

### Step 3: Open the Project Folder

Open a terminal and navigate to the project directory.

Example:

```bash

cd Campus_Lost_and_Found

```

The user can run the project by entering the command:

```bash

python main.py

```

If the system uses `python3`, the command is:

```bash

python3 main.py

```

The main menu will appear in the terminal.

The program can be used by:

### Report Lost Item

Selecting option `1` and entering the item name, location, date and description.

### Report Found Item

Selecting option `2` and entering the details of the found item.

### View Items

Options `3` and `4` display the currently recorded lost and found items.

### Search

Selecting option `5` and entering an item name, the program searches through the recorded lost and found items.

### Find Possible Matches

Selecting option `6`, the program compares lost-item names with found-item names and displays possible matches.

### Exit

Selecting option `7` to exit the program.

An example includes:

```text

======================================

CAMPUS LOST & FOUND TRACKER

======================================

1. Report Lost Item

2. Report Found Item

3. View Lost Items

4. View Found Items

5. Search for an Item

6. Find Possible Matches

7. Exit

======================================

Enter your choice:

```

The project uses algorithms including:

### Linear search

The search operation checks the stored item names one by one until a matching item is found. The worst-case time complexity for linear search is given by:

```text

O(n)

```

### Matching

The matching operation uses nested loops to compare lost items with found items. If there are n lost items and m found items, the comparisons require up to:

```text

O(n × m)

```

The project has the following limitations:

Data is stored only while the program is running.

The project is command-line based.

Matching is primarily based on the item name.

There is no graphical user interface or database.

The project can be extended in the future by adding:

Permanent data storage

Student/user identification

More detailed matching criteria

A graphical interface

Database support

Login functionality

The project illustrates the use of basic Python programming constructs to solve a campus problem. The programming concepts applied in the project include functions, conditional, loops, lists, searching and modular programming to create a simple command-line application.