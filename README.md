# Apple-iBooks-Highlighted-Text-Exporter 📚 ![StatusBadge](https://badgen.net/badge/Status/Completed/green) 

### This Python script exports all **notes, books and authors** from the *iBooks database* to a *private database*

This application also manages *authors and books* by creating **records and automatic links** in the private database.

For each book, author and note, the script will create a **new record with all possible important fields.**

The script **automatically handles already existing notes, books and authors.**

**The structure of the database** where the notes will be stored *is available in the repository*.

___

## **FEATURES:**
- Automatically extract every single important information of every note, book and author from iBooks Databases.
- Automatic links between tables.
- Automatic formatting of the content of each note to ensure full compatibility with the Database.

---

## **USAGE:**
 1. Download the latest release of *Python*.
 2. Download the latest release of the project. 
 3. Insert a copy of the two iBooks Databases in the "Database" folder. (You can use my [Apple-iBooks-Database-Exporter](https://github.com/NIK4658/Apple-iBooks-Database-Exporter) project to export the two databases). 
 4. Create the private Database using the same structure found in the repository.
 5. Add Database credentials in the first part of "TextExtractor.py".
 4. **Run TextExtractor.py**.
 5. ALL the notes, books and authors records will be created in the private Database.

---

## **DATABASE REQUIREMENTS:**
 
The private Database MUST be created with the same structure as the one in "Database" folder.

---

## **COMPATIBILITY:**

This script **can be run on any operating system**.

Databases **must first be exported** from a *Mac computer*.

---

## **CHECK ALSO:**

### [Apple-iBooks-Database-Exporter](https://github.com/NIK4658/Apple-iBooks-Database-Exporter):
Automatic script that **locate and generate a copy** of the two iBooks Databases.

### [Apple-iBooks-Highlighted-Text-Parser](https://github.com/NIK4658/Apple-iBooks-Highlighted-Text-Parser):
This project extracts notes from iBooks databases and **formats them, creating a txt file for each book found**.

---
