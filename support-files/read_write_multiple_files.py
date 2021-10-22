
# this reads mongo file and creates multiple smaller files ready for aws dynamodb

file_size = 0   # this is number of entries in current file being written
file_count = 1  # this is used to increment file name
file_name = 'output' + str(file_count) + '.json'

# open file to convert
with open('mongo-meetings.json', 'r') as f:
    for x in f:
        # set file_name, open for writing and start wth header data
        if file_size == 0:
            file_name = 'output' + str(file_count) + '.json'
            with open(file_name, 'w') as aws_out:
                aws_out.writelines("{")
                aws_out.writelines('\t\"Meetings\": [')
                data_line = f.readline()
                aws_out.writelines('{\n\"PutRequest\":{\n\t\"Item\":')
                aws_out.writelines(data_line)
                aws_out.writelines('}}')
                if x > f:
                    aws_out.writelines(',')
            file_count += 1
        else:
            # file is being processed
            with open(file_name, 'a') as aws_out:
                # append the next line
                aws_out.writelines("{")
                aws_out.writelines('\t\"Meetings\": [')
                data_line = f.readline()
                aws_out.writelines('{\n\"PutRequest\":{\n\t\"Item\":')
                aws_out.writelines(data_line)
                aws_out.writelines('}}')
                if x > f:
                    aws_out.writeline
            file_count += 1
        if x = f:
            # we are done reading the file
    aws_out.write(']}')
