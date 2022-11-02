Scourgify

    “Ah, well,” said Tonks, slamming the trunk’s lid shut, “at least it’s all in. That could do with a bit of cleaning, too.”
    She pointed her wand at Hedwig’s cage. “Scourgify.” A few feathers and droppings vanished.
    — Harry Potter and the Order of the Phoenix

Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format.
Consider, for instance, this CSV file of students, before.csv, below:

Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name), 
escaped with double quotes, with last name and first name separated by a comma and space. Not ideal if Hogwarts wants to send a form letter 
to each student, as via mail merge, since it’d be strange to start a letter with:

    Dear Potter, Harry,

Rather than with, for instance:

    Dear Harry,

In a file called scourgify.py, implement a program that:

    Expects the user to provide two command-line arguments:
        the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
        the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
    Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both
    a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit
via sys.exit with an error message.
