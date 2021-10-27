import json
import os


def write_file_header(fp):
    header_data = "{\"meeter-meetings\":[\n"
    fp.writelines(header_data)


def write_record(fp, record, comma):
    if comma:
        end_record = "}},\n"
    else:
        end_record = "}}\n"
    wrapper_start = "{\"PutRequest\": {\"Item\":"

    # record_to_write = "{}{}".format(record, end_record)
    record_to_write = f"{wrapper_start}{json.dumps(record)}{end_record}"

    fp.writelines(record_to_write)


def write_file_footer(fp):
    fp.writelines("]}")


def dynamodb_wrapper():
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

            # write the record, add comma unless last record
            write_record(f, the_entry, entry != data['Meetings'][-1])
        write_file_footer(f)
        f.close()
    return True
