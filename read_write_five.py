import json

with open('aws-meetings.json', 'w') as aws_out:
    aws_out.writelines("{")
    aws_out.writelines('\t\"Meetings\": [')
    meeting_count = 0
    with open('mongo-meetings.json', 'r') as f:
        for x in f:
            meeting_count += 1
            data_line = f.readline()
            if meeting_count < 5:
                aws_out.writelines('{\n\"PutRequest\":{\n\t\"Item\":')
                aws_out.writelines(data_line)
                aws_out.writelines('}}')
                if meeting_count < 4:
                    aws_out.writelines(',')


    aws_out.write(']}')
