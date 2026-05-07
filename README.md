# Automated CSV Data Processing Pipeline

A Python-based automation pipeline that processes CSV files, cleans data, generates summaries, and organizes files into structured folders with error handling and validation.

## Features
(i) Automatic CSV file detection
(ii) Structured workflow pipeline
(iii) Data cleaning (duplicates + missing values)
(iv) Summary report generation
(v) Fault-tolerant processing
(vi) Error handling with failed file routing
(vii) Archive management to prevent reprocessing


## Folder Structure

```text
csv-automation-pipeline/
│
├── Input/ (New CSV files)
├── Processing/ (Files currently being processed)
├── Output/ (Cleaned data + Summaries)
├── Failed/ (Files that fails validation)
├── Archive/ (Files that has been summarised)
├── main.py
├── README.md
└── .gitignore
```

## Workflow Logic
For each CSV file:
1. Move file to Processing 
2. Read data
3. Clean dataset
4. Validate required fields
5. Generate summary report
6. Save Outputs
7. Move files to:
	- Archive(if success)
	- Failed (if error occured)

## Data Cleaning Performed
(i) Removes duplicate rows
(ii) Removes rows with missig values
(iii) Validates required columns

## Summary Generated
Example:
|Internship|Avg Stipend|
|---------|----------|
|    AI       |    10500   |
|    Web     |      8500   |
--------------------

## Technologies Used
(i) Python
(ii) Pandas
(iii) OS
(iv) Shutil Module

## How to Run
1. Place the CSV files inside "Input/"
2. Run:
	python main.py
3. Check results inside "Ouput/"

## Error Handling
If a file :
	has missing columns
	has invalid data 
	cannot be rea
It will automatically move to "Failed/"
This ensures pipeline stability

## Purpose of project
This project demonstrates:
(i) Automation scripting
(ii) File system handling
(iii) Data processing
(iv) Backend logic thinking

## Future Improvements
Logging system
API data ingestion
Database storage
CLI arguments

## Author
Nandini Dhalia
GitHub: https://github.com/NandiniDhalia
