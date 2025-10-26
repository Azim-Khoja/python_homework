"""
Review Exercises
1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.

2. Populate your new table with the following values:

Name	Species	Age
Benjamin Sisko	Human	40
Jadzia Dax	Trill	300
Kira Nerys	Bajoran	29

3. Update the Name of Jadzia Dax to be Ezri Dax

4. Display the Name and Age of everyone in the table classified as Bajoran.
"""

import sqlite3

with sqlite3.connect("Roster.db") as conn:
    cursor = conn.cursor()

    cursor.execute(
        """
        create table if not exists Roster(
            name text,
            species text,
            age integer
        )
        """
    )

    roster = [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ]

    cursor.executemany(
        "insert into Roster values (?,?,?)", roster
    )

cursor.execute("""
    update Roster
    set name = 'Ezri Dax'
    where species = 'Trill'
    """)

cursor.execute(
    """
    SELECT name, age FROM Roster
    WHERE species = 'Bajoran'
    """)
print(cursor.fetchone())
















































