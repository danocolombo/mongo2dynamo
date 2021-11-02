# mongo2dynamo
This takes a file export from MongoDB and gets it to Amazon DynamoDB tables

It needs to be noted that the files from Mongo export are NOT JSON compliant, and will need to be modified.  

1. make JSON compliant file(s)
2. use configuration setting to define how many records we want per file.  If there are more records than the "file_limit", multiple json files will be created.
3. MongoDB has specific data types that are included in the json file and will need to be adapted for AWS
4. Change fields and data types as needed
5. Create output files that are array of records.

To accomplish this effort, we break the conditioning down into separate files at this time.

## Input Data Files (json_files/mongo-export-files/{table}
These are actual mongo export files from the collections in MongoDB. Some collections are large, so small versions were created for development and testing purposes. The actual file used is defined in each json_files python file. Examples:
- mongo-meetings.json (exported table from mongodb)
- mongo-meetings-small.json (smaller version of above)

## Output files
When running main.py the process will get the defined files and produce array of records in the json_files/aws-ready-files directory associated with the specific dataabase tables (collections). Those files can be consumed by AWS lambda function outlined in the aws_lambda_sample.txt file.

