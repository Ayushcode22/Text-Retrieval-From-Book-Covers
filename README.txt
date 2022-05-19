Submitter name: Ayush Tirpude

Roll No.: 2019csb1078

Course: CS305

=================================

1. What does this program do

This is an implementation of a program where a single or multiple book covers can be scanned and their respective details about author, title,ISBN number
and publisher can be identified. This program uses teseract API for text detection in Images and Named entity recognition for getting details for author and publisher


2. A description of how this program works (i.e. its logic)

This program takes path of the folder where book covers are stored and then scans through it for images.Each image is scanned and details like author, title, ISBN number
and publisher is extracted. Title is extracted from the text by font size. The maximum font size is found and according to it most nearest words with same height(ratio taken 1.2)
are added to title.

For Author and Publisher NER is used which finds out author and Publisher by name_types of "PERSON" and "ORG" respectively.

For ISBN number the text extracted is splitted with a delimiter of new line and lines containing ISBN numbers are shown for all Editions(if present)

Finally all these details are written on the excell file using xlsxwriter to an excell file named "hello.xlsx" 


3. How to compile and run this program

For command line unit testing :-
python -m unittest test.py

For VS code :-
just open test.py an run 


