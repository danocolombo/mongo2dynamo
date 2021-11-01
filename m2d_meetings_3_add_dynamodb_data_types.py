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
    return True
    file_directory = './json_files/aws-ready-files/meetings/'
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
            if aws_dynamo_utils.search_dict(the_entry, "_id"):
                the_entry['_id'] = aws_dynamo_utils.label_as_string(the_entry['_id'])
            if aws_dynamo_utils.search_dict(the_entry, "facilitator"):
                the_entry['facilitator'] = aws_dynamo_utils.identify_field(the_entry['facilitator'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "announcementsContact"):
                the_entry['announcementsContact'] = aws_dynamo_utils.identify_field(the_entry['announcementsContact'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "attendance"):
                the_entry['attendance'] = aws_dynamo_utils.identify_field(the_entry['attendance'], "N")
            if aws_dynamo_utils.search_dict(the_entry, "avContact"):
                the_entry['avContact'] = aws_dynamo_utils.identify_field(the_entry['avContact'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "cafeCoordinator"):
                the_entry['cafeCoordinator'] = aws_dynamo_utils.identify_field(the_entry['cafeCoordinator'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "cafeCount"):
                the_entry['cafeCount'] = aws_dynamo_utils.identify_field(the_entry['cafeCount'], "N")
            if aws_dynamo_utils.search_dict(the_entry, "children"):
                the_entry['children'] = aws_dynamo_utils.identify_field(the_entry['children'], "N")
            if aws_dynamo_utils.search_dict(the_entry, "childrenContact"):
                the_entry['childrenContact'] = aws_dynamo_utils.identify_field(the_entry['childrenContact'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "cleanupContact"):
                the_entry['cleanupContact'] = aws_dynamo_utils.identify_field(the_entry['cleanupContact'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "closingContact"):
                the_entry['closingContact'] = aws_dynamo_utils.identify_field(the_entry['closingContact'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "donations"):
                the_entry['donations'] = aws_dynamo_utils.identify_field(the_entry['donations'], "N")
            if aws_dynamo_utils.search_dict(the_entry, "greeterContact1"):
                the_entry['greeterContact1'] = aws_dynamo_utils.identify_field(the_entry['greeterContact1'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "greeterContact2"):
                the_entry['greeterContact2'] = aws_dynamo_utils.identify_field(the_entry['greeterContact2'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "meal"):
                the_entry['meal'] = aws_dynamo_utils.identify_field(the_entry['meal'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "mealCnt"):
                the_entry['mealCnt'] = aws_dynamo_utils.identify_field(the_entry['mealCnt'], "N")
            if aws_dynamo_utils.search_dict(the_entry, "mealCoordinator"):
                the_entry['mealCoordinator'] = aws_dynamo_utils.identify_field(the_entry['mealCoordinator'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "meetingDate"):
                the_entry['meetingDate'] = aws_dynamo_utils.identify_field(the_entry['meetingDate'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "meetingType"):
                the_entry['meetingType'] = aws_dynamo_utils.identify_field(the_entry['meetingType'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "newcomers"):
                the_entry['newcomers'] = aws_dynamo_utils.identify_field(the_entry['newcomers'], "N")
            if aws_dynamo_utils.search_dict(the_entry, "notes"):
                the_entry['notes'] = aws_dynamo_utils.identify_field(the_entry['notes'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "nursery"):
                the_entry['nursery'] = aws_dynamo_utils.identify_field(the_entry['nursery'], "N")
            if aws_dynamo_utils.search_dict(the_entry, "nurseryContact"):
                the_entry['nurseryContact'] = aws_dynamo_utils.identify_field(the_entry['nurseryContact'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "resourceContact"):
                the_entry['resourceContact'] = aws_dynamo_utils.identify_field(the_entry['resourceContact'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "securityContact"):
                the_entry['securityContact'] = aws_dynamo_utils.identify_field(the_entry['securityContact'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "setupContact"):
                the_entry['setupContact'] = aws_dynamo_utils.identify_field(the_entry['setupContact'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "supportRole"):
                the_entry['supportRole'] = aws_dynamo_utils.identify_field(the_entry['supportRole'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "tenantId"):
                the_entry['tenantId'] = aws_dynamo_utils.identify_field(the_entry['tenantId'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "title"):
                the_entry['title'] = aws_dynamo_utils.identify_field(the_entry['title'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "transportationContact"):
                the_entry['transportationContact'] = aws_dynamo_utils.identify_field(the_entry['transportationContact'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "transportationCount"):
                the_entry['transportationCount'] = aws_dynamo_utils.identify_field(the_entry['transportationCount'], "N")
            if aws_dynamo_utils.search_dict(the_entry, "worship"):
                the_entry['worship'] = aws_dynamo_utils.identify_field(the_entry['worship'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "youth"):
                the_entry['youth'] = aws_dynamo_utils.identify_field(the_entry['youth'], "N")
            if aws_dynamo_utils.search_dict(the_entry, "youthContact"):
                the_entry['youthContact'] = aws_dynamo_utils.identify_field(the_entry['youthContact'], "S")

            # write the record, add comma unless last record
            write_record(f, the_entry, entry != data['Meetings'][-1])
        write_file_footer(f)
        f.close()
    return True
