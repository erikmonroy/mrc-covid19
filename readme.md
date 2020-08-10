# HTML to CSV Parser

## PYTHON SCRIPT FOR DUTCHESS COUNTY COVID-19 DATA

### This was made for the Dutchess County Department of Behavioral and Community Health in service of the Medical Reserve Corp. It attempts to translate COVID-19 test results data from HTML files to CSV format.

#### Prerequisites

Before you continue, ensure you have met the following requirements:

* You have installed the latest version of Python
* You have downloaded the data as a HTML file
* You have a basic understanding of how to edit an HTML document and how to use your command line

#### Steps

1. Download the mrc.py script
2. Preprocess the HTML file with a text editor or IDE and save (Further instructions below)
3. Copy the url of the HTML file opened
4. Open your command line from the folder in which your mrc.py script is stored and run the script!

##### Preprocessing the HTML manually
I am not a professional software engineer, so this was the quickest solution I could come up with.

The file needs div containers around each patient to parse it. To place those without code:
1. Find and replace all:
`<p style="page-break-after: always">&nbsp;</p>`
with
`</div><div class="patient">`
2. Add
`<div class="patient">`
right after the beginning `</h1>` tag
3. Delete the final hanging `</div>` tag at the end, as it causes an Index Error. NOTE: not performing this step will still result in a perfectly functional CSV

#### Authors
Erik Spangenberg, 
MRC Volunteer, 
Vassar Colleget Student

Contact at: espangenberg@vassar.edu