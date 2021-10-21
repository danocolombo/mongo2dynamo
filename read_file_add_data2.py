import json

with open('limited-data.txt', 'r') as f:
    meeting_count = 0
    file_count = 1
    for x in f:
        meeting_count += 1
        data_line = f.readline()
        if meeting_count < 5:
            with open('limited-output.txt', 'w') as aws_out:
                aws_out.writelines("{")
                aws_out.writelines('\t\"Meetings\": [')
                aws_out.writelines('{\n\"PutRequest\":{\n\t\"Item\":')
                aws_out.writelines(data_line)
                aws_out.writelines('}}')
                if meeting_count < 4:
                    aws_out.writelines(',')
        else:
            meeting_count = 1

    # aws_out.write(']}')
