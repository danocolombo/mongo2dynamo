import json
import os


def write_file_header(fp):
    header_data = "{\"Clients\":[\n"
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


def change_field_names():
    file_directory = './json_files/aws-ready-files/clients/'
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
        for entry in data['Clients']:
            the_entry = entry
            the_entry['clientId'] = the_entry.pop('_id')

            # mid => meetingId
            the_entry['clientName'] = the_entry.pop('name')

            # write the record, add comma unless last record
            write_record(f, the_entry, entry != data['Clients'][-1])
        write_file_footer(f)
        f.close()
    return True
