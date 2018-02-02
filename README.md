# Little Lexicographer

Whenever we publish new data on the [Western Pennsylvania Regional Data Center](https://www.wprdc.org)'s [open data portal](https://data.wprdc.org), we include a data dictionary to describe all the fields. To make this easier, I created a simple Python script that takes as a command-line argument the filename for a CSV file, scans its field values to try to infer the type, and then creates a data dictionary file (also in CSV format) with one row for each of the first file's fields, an example value for each field, and blanks for field descriptions and optional additional notes. 

If example.csv contains this text:

```
numbers,letters,constants,truth_values
34,y,2.7182818284,True
5001,A,3.141592653589793,false
-1,k,-1.61803,
```

corresponding to this table:

numbers|letters|constants|truth_values
-------|-------|---------|------------
34|y|2.7182818284|True
5001|A|3.141592653589793|false
-1|k|-1.61803|

then running lil_lex.py on it like so, 

```
> python lil_lex.py example.csv
```

will generate a file in the same directory as example.csv called example-data-dictionary.csv. Its tabular form looks kind of like this:

field_name|type|description|example|notes
----------|----|-----------|-------|-----
numbers|int||34|"This is an example note I added, just to demonstrate the importance of putting quotes around any field value that contains a comma, lest it be interpreted as more fields than one."
letters|text||y|
constants|float||2.7182818284|
truth_values|bool||True|

Then all you have to do is check that the types are right and fill in the blanks. (Values can easily be inserted into CSVs in your favorite text editor of course, but I enjoy using [VisiData](https://github.com/saulpw/visidata) for editing CSV files since it makes viewing and manipulating CSV files in a terminal window so easy (so long as you're willing to learn some keyboard shortcuts).)

field_name|type|description|example|notes
----------|----|-----------|-------|-----
numbers|int|This field contains integers.|34|"This is an example note I added, just to demonstrate the importance of putting quotes around any field value that contains a comma, lest it be interpreted as more fields than one."
letters|text|Single letters, randomly sampled from the alphabet.|y|
constants|float|These are all well-known mathematical constants.|2.7182818284|
truth_values|bool|Boolean values.|True|

Once your data dictionary file is filled in, it's ready for uploading to CKAN.
