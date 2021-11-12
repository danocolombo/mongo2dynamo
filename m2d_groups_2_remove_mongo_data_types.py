import json
import os
import aws_dynamo_utils


def clean_id(toxic):
    # this gets dict value for id
    # we can have two different formats....
    # {'$oid': '60874224194cadb9cca5798c'} #dict
    # ObjectId(5eaf6ef6a97c783041c0ed8b)   #string
    if isinstance(toxic, str):
        # print(f"string")
        actual_value = toxic[9:-1]
    elif isinstance(toxic, dict):
        # print(f"dict")
        actual_value = toxic['$oid']
    # print(f"actual_value now: {actual_value}")

    return actual_value


def clean_meeting_date(toxic):
    # this gets dict value for date and returns the date value
    # dict name is $date and want to only return date of long time stamp
    print(f"toxic_date: {toxic}")
    actual_date = toxic['$date'][:10]
    return actual_date


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


def remove_mongo_data_types():
    file_directory = './json_files/aws-ready-files/groups/'
    aws_files = []
    for entry in os.listdir(file_directory):
        if os.path.isfile(os.path.join(file_directory, entry)):
            # print(entry)
            aws_files.append(entry)

    for aws_file in aws_files:
        data = {}
        the_entry = {}
        dead = False
        try:
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
                # the_group = json.dumps(entry)
                # fresh_group = list(the_group)

                # REMOVE MONGO __v
                if aws_dynamo_utils.search_dict(the_entry, "__v"):
                    the_entry.pop("__v")
                # CLEAN ID
                if aws_dynamo_utils.search_dict(the_entry, "_id"):
                    the_entry['_id'] = clean_id(the_entry['_id'])
                else:
                    print(f"NO _id, now that is not supposed to happen")

                # write the record, add comma unless last record
                write_record(f, the_entry, entry != data['Groups'][-1])
            write_file_footer(f)
            f.close()
        except Exception as err:
            print(f"{err}")
            junk = input('ERROR-THROWN')
            print(f"the_entry:\n{the_entry}")
            dead = True
        finally:
            if dead:
                print(f"finally: \n{the_entry['_id']}")
    return True
