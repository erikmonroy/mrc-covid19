#SETUP
#import Beautiful Soup, parsing library
import bs4
#import only needed modules
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#PARSING
#replace with HTML file of results
url = input("Enter url of HTML file:")
print("File selected is: " + url + "\n" + "Thank you! One moment please, I'm computing.")
#opening the connection, grabbing the page
uClient = uReq(url)
#offloading content into variable
page_html = uClient.read()
uClient.close()
#parse html
page_soup = soup(page_html, "html.parser")

#grabs all patient records
patients = page_soup.findAll("div",{"class":"patient"})

#open csv
filename = "results.csv"
f = open(filename, "w")

headers = "Reporting Laboratory, Ordering Facility, Ordering Physician, Date Reported to ECLRS, Collection Date, Specimen Received Date, Accession Number\n"

f.write(headers)

#loop and find
for patient in patients:
    #Reporting Laboratory
    data_container = patient.findAll("span", {"class":"data"})
    reporting_lab = data_container[6].text.strip()
    #Ordering Facility
    ordering_container = patient.findAll("div", {"class":"data"})
    ordering_facility_string = ordering_container[1].text.strip()
    ordering_facility_split = ordering_facility_string.split('\n',1)
    ordering_facility = ordering_facility_split[0]
    #Ordering Physician
    ordering_physician_string = ordering_container[2].text.strip()
    ordering_physician_split = ordering_physician_string.split('\n',1)
    ordering_physician = ordering_physician_split[0]
    #Date Reported to ECLRS
    eclrs_date = data_container[7].text.strip()
    #Collection Date
    collection_date = data_container[13].text.strip()
    #Specimen Received Date
    specimen_date = data_container[15].text.strip()
    #Accession Number
    accession_container = patient.findAll("span", {"class":"prioritydata"})
    accession_number =  accession_container[0].text
    #print check
    print("accession_number:    "+accession_number)
    print("ordering_facility:   "+ordering_facility)
    print("ordering_physician: "+ordering_physician)
    print("reporting_lab:   "+reporting_lab)
    print("eclrs_date:  "+eclrs_date)
    print("collection_date: "+collection_date)
    print("specimen_date:   "+specimen_date)
    #each loop, writes data to csv file
    f.write(accession_number + "," + ordering_facility + "," + ordering_physician.replace(",", "|") + "," + reporting_lab + "," + eclrs_date + "," + collection_date + "," + specimen_date + "\n")
f.close()
print("Your CSV file is awaiting in your files. Import into Excel or Google Sheets and you are good to go.")