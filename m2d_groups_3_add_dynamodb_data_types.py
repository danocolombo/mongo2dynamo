import json
import os
import aws_dynamo_utils


def write_file_header(fp):
    header_data = "{\"Groups\":[\n"
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
    file_directory = './json_files/aws-ready-files/groups/'
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
        for entry in data['Groups']:
            the_entry = entry
            if aws_dynamo_utils.search_dict(the_entry, "_id"):
                the_entry['_id'] = aws_dynamo_utils.label_as_string(the_entry['_id'])
            if aws_dynamo_utils.search_dict(the_entry, "gender"):
                the_entry['gender'] = aws_dynamo_utils.identify_field(the_entry['gender'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "mid"):
                the_entry['mid'] = aws_dynamo_utils.identify_field(the_entry['mid'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "title"):
                the_entry['title'] = aws_dynamo_utils.identify_field(the_entry['title'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "attendance"):
                the_entry['attendance'] = aws_dynamo_utils.identify_field(the_entry['attendance'], "N")
            if aws_dynamo_utils.search_dict(the_entry, "cofacilitator"):
                the_entry['cofacilitator'] = aws_dynamo_utils.identify_field(the_entry['cofacilitator'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "facilitator"):
                the_entry['facilitator'] = aws_dynamo_utils.identify_field(the_entry['facilitator'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "location"):
                the_entry['location'] = aws_dynamo_utils.identify_field(the_entry['location'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "notes"):
                the_entry['notes'] = aws_dynamo_utils.identify_field(the_entry['notes'], "S")

            # write the record, add comma unless last record
            write_record(f, the_entry, entry != data['Groups'][-1])
        write_file_footer(f)
        f.close()
    return True
