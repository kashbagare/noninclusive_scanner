# noninclusive_scanner
The main purpose of this program is to scan a data dictionary for any database and identify all object names.
The current version only connects to a PostgresSQL instance. Future versions of this will include scanning other data sources.

### Installation instructions
Download all files to a directory (downloaded_dir). Please download the **database.ini** and **noninclusive_words.txt** from the certs folder.
Make sure that you designate a folder on your local (config_dir).

### config_dir
This is the placeholder directory for your database connection ini file (database.ini) and non-inclusive keyword file (noninclusive_words.txt).

###  noninclusive_words.txt
This file contains all the Non-inclusive keyword listing. You can edit to include any other non-inclusive keywords that your organization may want to track.

### database.ini
This file has list of all your database connections. The section name is very important. The program looks for section name to establish connection with desired database technology. In this example, we have only tested this for Postgres database.
For the test run, we are using a section named **SCANNER** in database.ini.

````
cd ~/downloaded_dir/noninclusive_scanner
python setup.py install
````

### Run the program in wrapper python script as

````
config_dir = "/Users/kashbagare/projectdir/python/certs"
section_name = "SCANNER"
init_scan(config_dir, section_name)
````

### Output
```
  table_schema       table_name  table_type     column_name
0  test_schema  blacklist_table  base table              c1
1  test_schema  blacklist_table  base table              c2
2  test_schema  blacklist_table  base table  master_details
3  test_schema           table1  base table      white_list
5  test_schema        some_view        view  master_details
```

### Future work
I plan to encrypt the passwords in database.ini and also introduce other technologies.
I will also be tuning the program for performance and use multi-threading (if we intend to scan multiple technologies at a time).

I also think that this use case can also be applied for identifying PII data elements.

 
