import os
import csv
from dateutil import parser


location = '..\\..\\..\\Desktop\\Saarah\\'
state_file = 'state_abbreviations.csv'
test_file = 'test.csv'


def import_data(file):
	data = {}
	with open(location+file) as f:
		csvReader = csv.reader(f)
		headers = csvReaders.__next__()
		for head in headers:
			data[head] = list()
		for row in csvReader:
			for ind in range(len(header)):
				title = headers[ind] 
				data[title].append(row[ind])
	f.close()
	return data

def string_cleaning(data, tag):
	bio = data[tag].copy()
	cleaned = []
	for ind in bio:
		temp = bio[ind].split()
		for val in temp:
			if temp.startswith(" ") or temp.endswith(" "):
				temp = temp.rstrip(" ")
			else:
				continue
		fixed = " ".join(temp)
		cleaned.append(fixed)
	return cleaned

def get_abbreviations(file):
	abbs = {}
	with open(location+file) as f:
		csvReader = csv.reader(f)
		for row in csvReader:
			abbs[row[0]] = row[1]
	f.close()
	return abbs

def code_swap(data, tag):
	abbs = get_abbreviations('state_abbreviations.csv')
	states = data[tag].copy()
	fixed_states = []
	for state in states:
		fixed_states.append(abbs[state])
	return fixed_states

def month_mapping():
	numerics = {}
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	for month in months:
		numerics[month] = months.index(month)
	return numerics


def date_offset(data, tag):
	dates = data[tag].copy()
	numerics = month_mapping()
	valid = []
	invalid []
	for date in dates:
		for month in numerics:
			if date.startswith(month) or date.startswith(numerics[month]):
				temp_date = parser.parse(date).date()
				fixed_date = str(temp_date.year) + '-' + str(temp_date.month) + '-' + str(temp_date.day)
				date = fixed_date
			else:
				date = 'NA'
	return dates


def data_cleaning():
	data = import_data(state_file)
	fixed_bio = data_cleaning(data, 'bio')
	fixed_states = code_swap(data, 'state')
	fixed_dates = date_offset(date, 'start_date')
	data['bio'] = fixed_bio
	data['state'] = fixed_states
	data['start_date'] = fixed_dates
	return data
