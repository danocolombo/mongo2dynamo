# mongo2dynamo
This takes a file export from MongoDB and gets it to Amazon DynamoDB tables

It needs to be noted that the files from Mongo export are NOT JSON compliant, and will need to be modified.  Also, the AWS DynamoDB import process only accepts 50 entries at a time.  So this process will do a few things.

1. make JSON compliant file(s)
2. use configuration setting to define how many records we want per file.  If there are more records than the "file_limit", multiple json files will be created.
3. MongoDB has specific data types that are included in the json file and will need to be adapted for AWS
4. AWS input requires some extra structure for the insert AND also need data types added

To accomplish this effort, we break the conditioning down into separate files at this time.

## Data Files
- mongo-meetings.json (exported table from mongodb)
- mongo-meetings-small.json (smaller version of above)

## Process Order & Descriptions
___
- **mongo_stage_for_aws_1_make_json_files.py**
To make the file JSON compliant, make Meetings array, and put a , (comma) after each record, and close the file properly. NOTE: we need to save a config file that lets us know how many files we created.
- **mongo_stage_for_aws_2_format_records.py**
Now loop through each record and clean up the data types
- **mongo_stage_for_aws_3_add_ddb_data_types.py**
