import json
import os
import aws_dynamo_utils


def write_file_header(fp):
    header_data = "{\"Humans\":[\n"
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
    file_directory = './json_files/aws-ready-files/humans/'
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

        f = open(full_file_name, "w")
        write_file_header(f)
        for entry in data['Humans']:
            the_entry = entry
            if aws_dynamo_utils.search_dict(the_entry, "_id"):
                the_entry['_id'] = aws_dynamo_utils.label_as_string(the_entry['_id'])
            if aws_dynamo_utils.search_dict(the_entry, "name"):
                the_entry['name'] = aws_dynamo_utils.identify_field(the_entry['name'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "tenantId"):
                the_entry['tenantId'] = aws_dynamo_utils.identify_field(the_entry['tenantId'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "active"):
                the_entry['active'] = aws_dynamo_utils.identify_field(the_entry['active'], "B")
            if aws_dynamo_utils.search_dict(the_entry, "birthday"):
                the_entry['birthday'] = aws_dynamo_utils.identify_field(the_entry['birthday'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "email"):
                the_entry['email'] = aws_dynamo_utils.identify_field(the_entry['email'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "gender"):
                the_entry['gender'] = aws_dynamo_utils.identify_field(the_entry['gender'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "phone"):
                the_entry['phone'] = aws_dynamo_utils.identify_field(the_entry['phone'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "service"):
                the_entry['service'] = aws_dynamo_utils.identify_field(the_entry['service'], "S")
            if aws_dynamo_utils.search_dict(the_entry, "shirtSize"):
                the_entry['shirtSize'] = aws_dynamo_utils.identify_field(the_entry['shirtSize'], "S")

            # write the record, add comma unless last record
            write_record(f, the_entry, entry != data['Humans'][-1])
        write_file_footer(f)
        f.close()
    return True
