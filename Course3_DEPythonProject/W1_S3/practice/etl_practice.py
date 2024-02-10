import pandas as pd
from datetime import datetime
import xml.etree.ElementTree as ET
import glob

log_file = "logs/log_file.txt" 
target_file = "output/transformed_data.csv" 

### EXTRACT
def extract_csv(filename):
	return pd.read_csv(filename)

def extract_json(filename):
	return pd.read_json(filename, lines=True)

def extract_xml(filename):
	df = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
	tree = ET.parse(filename)
	root = tree.getroot()
	for entry in root:
		model = entry.find("car_model").text
		year = entry.find("year_of_manufacture").text
		price = round(float(entry.find('price').text), 2)
		fuel = entry.find('fuel').text
		df = pd.concat([df, pd.DataFrame([{'car_model':model, 'year_of_manufacture':year, 'price':price, 'fuel':fuel}])], ignore_index=True)
	return df

def extract():
	extracted_data = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])

	for csvfile in glob.glob("data/*.csv"):
		extracted_data = pd.concat([extracted_data, extract_csv(csvfile)], ignore_index=True)

	for jsonfile in glob.glob("data/*.json"):
		extracted_data = pd.concat([extracted_data, extract_json(jsonfile)], ignore_index=True)

	for xmlfile in glob.glob("data/*.xml"):
		extracted_data = pd.concat([extracted_data, extract_xml(xmlfile)], ignore_index=True)

	return extracted_data

def load_data(filename, transformed_data):
	transformed_data.to_csv(filename)

def log_progress(message):
	timestamp_format = '%Y-%h-%d-%H:%M:%S'
	now = datetime.now()
	timestamp = now.strftime(timestamp_format) 
	with open(log_file,"a") as f:
		f.write(timestamp + ',' + message + '\n') 

def main():
	log_progress("ETL Beginning")

	log_progress("Extracting")
	extracted_data = extract()

	log_progress("Finished Extraction")

	# log_progress("Beginning transformation")
	# # transformed_data = transform(extracted_data)
	# log_progress("Finished transformation")

	log_progress("Beginning loading")
	load_data(target_file, extracted_data)
	log_progress("Finished loading")


main()

### TRANSFORM