import json
import os
import aws_dynamo_utils

def write_file_header(fp):
    header_data = "{\"Meetings\":[\n"
    fp.writelines(header_data)


def write_record(fp, record, comma):
    if comma:
        end_record = ",\n"
    else:
        end_record = "\n"
    # record_to_write = "{}{}".format(record, end_record)
    record_to_write = f"{json.dumps(record)}{end_record}"

    fp.writelines(record_to_write)

def write_file_footer(fp):
    fp.writelines("]}")


def add_dynamo_data_types():
    file_directory = './json_files/aws-ready-files/'
    aws_files = []
    for entry in os.listdir(file_directory):
        if os.path.isfile(os.path.join(file_directory, entry)):
            # print(entry)
            aws_files.append(entry)
    for aws_file in aws_files:
        full_file_name = file_directory + aws_file
        # Opening JSON file
        f = open(full_file_name, )

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        f.close()
        # Iterating through the json
        # list
        f = open(full_file_name, "w")
        write_file_header(f)
        for entry in data['Meetings']:
            the_entry = entry
            # the_meeting = json.dumps(entry)
            # fresh_meeting = list(the_meeting)

            # id =
            the_entry['_id'] = aws_dynamo_utils.label_as_string(the_entry['_id'])
            the_entry['facilitator'] = aws_dynamo_utils.identify_field(the_entry['facilitator'],"S")
            the_entry['announcementsContact'] = aws_dynamo_utils.identify_field(the_entry['announcementsContact'], "S")
            the_entry['attendance'] = aws_dynamo_utils.identify_field(the_entry['attendance'], "N")
            the_entry['avContact'] = aws_dynamo_utils.identify_field(the_entry['avContact'], "S")
            the_entry['cafeCoordinator'] = aws_dynamo_utils.identify_field(the_entry['cafeCoordinator'], "S")
            the_entry['cafeCount'] = aws_dynamo_utils.identify_field(the_entry['cafeCount'], "N")
            the_entry['children'] = aws_dynamo_utils.identify_field(the_entry['children'], "N")
            the_entry['childrenContact'] = aws_dynamo_utils.identify_field(the_entry['childrenContact'], "S")
            the_entry['cleanupContact'] = aws_dynamo_utils.identify_field(the_entry['cleanupContact'], "S")
            the_entry['closingContact'] = aws_dynamo_utils.identify_field(the_entry['closingContact'], "S")
            the_entry['donations'] = aws_dynamo_utils.identify_field(the_entry['donations'], "N")
            the_entry['greeterContact1'] = aws_dynamo_utils.identify_field(the_entry['greeterContact1'], "S")
            the_entry['greeterContact2'] = aws_dynamo_utils.identify_field(the_entry['greeterContact2'], "S")
            the_entry['meal'] = aws_dynamo_utils.identify_field(the_entry['meal'], "S")
            the_entry['mealCnt'] = aws_dynamo_utils.identify_field(the_entry['mealCnt'], "N")
            the_entry['mealCoordinator'] = aws_dynamo_utils.identify_field(the_entry['mealCoordinator'], "S")
            the_entry['meetingDate'] = aws_dynamo_utils.identify_field(the_entry['meetingDate'], "S")
            the_entry['meetingType'] = aws_dynamo_utils.identify_field(the_entry['meetingType'], "S")
            the_entry['newcomers'] = aws_dynamo_utils.identify_field(the_entry['newcomers'], "N")
            the_entry['notes'] = aws_dynamo_utils.identify_field(the_entry['notes'], "S")
            the_entry['nursery'] = aws_dynamo_utils.identify_field(the_entry['nursery'], "N")
            the_entry['nurseryContact'] = aws_dynamo_utils.identify_field(the_entry['nurseryContact'], "S")
            the_entry['resourceContact'] = aws_dynamo_utils.identify_field(the_entry['resourceContact'], "S")
            the_entry['securityContact'] = aws_dynamo_utils.identify_field(the_entry['securityContact'], "S")
            the_entry['setupContact'] = aws_dynamo_utils.identify_field(the_entry['setupContact'], "S")
            the_entry['supportRole'] = aws_dynamo_utils.identify_field(the_entry['supportRole'], "S")
            the_entry['tenantId'] = aws_dynamo_utils.identify_field(the_entry['tenantId'], "S")
            the_entry['title'] = aws_dynamo_utils.identify_field(the_entry['title'], "S")
            the_entry['transportationContact'] = aws_dynamo_utils.identify_field(the_entry['transportationContact'], "S")
            the_entry['transportationCount'] = aws_dynamo_utils.identify_field(the_entry['transportationCount'], "N")
            the_entry['worship'] = aws_dynamo_utils.identify_field(the_entry['worship'], "S")
            the_entry['youth'] = aws_dynamo_utils.identify_field(the_entry['youth'], "N")
            the_entry['youthContact'] = aws_dynamo_utils.identify_field(the_entry['youthContact'], "S")


           # write the record, add comma unless last record
            write_record(f,the_entry,entry != data['Meetings'][-1])
        write_file_footer(f)
        f.close()
    return True
