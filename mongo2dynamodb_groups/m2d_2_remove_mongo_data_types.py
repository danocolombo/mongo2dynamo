import json
import os
import mongo2dynamodb.aws_dynamo_utils as aws_dynamo_utils


def clean_id(toxic):
    # this gets dict value for id
    actual_value = toxic['$oid']
    return actual_value



def write_record(fp, record, comma):
    if comma:
        end_record = ",\n"
    else:
        end_record = "\n"
    record_to_write = f"{json.dumps(record)}{end_record}"

    fp.writelines(record_to_write)


def write_file_footer(fp):
    fp.writelines("]}")


def remove_mongo_data_types(table):
    # need to dete
    file_directory = str(f"./json_files/aws-ready-files/{table}/")
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
        aws_dynamo_utils.write_file_header(table, f)

        for entry in data[table]:
            the_entry = entry
            # the_group = json.dumps(entry)

            # REMOVE MONGO __v
            the_entry.pop("__v")
            # CLEAN ID
            the_entry['_id'] = clean_id(the_entry['_id'])

            # write the record, add comma unless last record
            write_record(f, the_entry, entry != data[str.capitalize(table)][-1])
        write_file_footer(f)
        f.close()
    return True
