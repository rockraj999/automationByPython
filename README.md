# Project1

## Automated Transaction/Order File Validation System

###Project Overview:
The Automated Transaction/Order File Validation System is a Python-based solution that automates the validation process for transaction/order files received from a mart. The system applies predefined rules to ensure data accuracy and compliance with business requirements. By leveraging Python and pandas, the project streamlines the validation process, reduces manual efforts, save time, and improves data quality assurance.

### Technical skills:
1. Python
2. pandas
3. os (for reading/writing from the specific folder)
4. shutil (to copy the file) 
5. csv (for CSV file handling)
6. Modularised the code 

### Workflow Overview:
1. File Import: The system receives transaction/order files in various formats (Excel, CSV) from the mart.
   Read all thefilese from the folder Mart->incomingFiles->YYYYMMDD folder
2. Data Loading: The files are loaded into a dictionary/list or pandas df for further processing.
3. Rule Application: Predefined rules are applied to the transaction/order data. These rules check for the following: 
   valid product_id - product_id should be present in product master table.
   valid order_date - order_date should not be in future.
   emptiness - all field should not be empty
   valid city - orders should be from Mumbai and Banglore only.
   valid sale calculation - total sale amount should be product price from product master table*quantity.
     
4. Data Validation: To validate the rule I created a validation module where the code performs data checks, flagging any discrepancies or violations of the predefined rules within the transaction/order files.
5. Error Reporting: Validation files are generated, highlighting the identified errors or anomalies against each row. The file provide detailed information about the errors, such as the affected rows and specific rule violations.
6. Error Handling: The system handles errors or exceptions encountered during the validation process, ensuring the smooth execution of the automation. for this used try and except code block.
7. Output Generation: The validation reports are saved as Excel or CSV files for easy sharing and review.
   files with no error should go to Mart->successFiles->YYYYMMDD folder
   if any single orders validation fails then full file should be rejected and go to Mart->rejectedFiles->YYYYMMDD folder
   for each rejected file one more file should be created(file_name_error.csv) in the same folder. and in this file only those order 
   records will be there which failed the validation along with reason of rejection in reason column.
8. after processing an email should be sent to business which specify total file processed, success files and rejected files.  




