import json
import os
import aws_dynamo_utils


def clean_id(toxic):
    # this gets dict value for id
    actual_value = toxic['$oid']
    return actual_value


def clean_meeting_date(toxic):
    # this gets dict value for date and returns the date value
    # dict name is $date and want to only return date of long time stamp
    actual_date = toxic['$date'][:10]
    return actual_date


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


def remove_mongo_data_types():
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
            the_meeting = json.dumps(entry)
            fresh_meeting = list(the_meeting)

            # REMOVE MONGO __v
            the_entry.pop("__v")
            # CLEAN ID
            the_entry['_id'] = clean_id(the_entry['_id'])
            # CLEAN meetingDate
            the_entry['meetingDate'] = clean_meeting_date(the_entry['meetingDate'])

            # write the record, add comma unless last record
            write_record(f, the_entry, entry != data['Meetings'][-1])
        write_file_footer(f)
        f.close()
    return True
