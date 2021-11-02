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

def donations2pennies(donation):
    # this converts the value to 100th of a dollar
    # first strip the Mondo type off the value
    # actual_value = float(donation['$numberDecimal'])
    pennies = 0
    if isinstance(donation, dict):
        # print(f"It is dict")
        # print(f"dict: >>{donation}<<")
        new_value = donation['$numberDecimal']
        # print(f"new_value: {new_value}")
        pennies = int(float(new_value) * 100)
        # print(f"pennies: {pennies}")
    else:
        # print(f"nope")
        # print(f"donation type: {type(donation)}")
        if isinstance(donation, int):
            if donation == 0:
                pennies = 0
            else:
                pennies = donation * 100
    # pennies = actual_value * 100
    # return pennies
    return pennies
    


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
            if aws_dynamo_utils.search_dict(the_entry, "__v"):
                the_entry.pop("__v")
            # CLEAN ID
            the_entry['_id'] = clean_id(the_entry['_id'])
            # CLEAN meetingDate
            the_entry['meetingDate'] = clean_meeting_date(the_entry['meetingDate'])

            # need to convert values for donations to pennies
            if aws_dynamo_utils.search_dict(the_entry, "donations"):
                the_entry['donations'] = donations2pennies(the_entry['donations'])

            # write the record, add comma unless last record
            write_record(f, the_entry, entry != data['Meetings'][-1])
        write_file_footer(f)
        f.close()
    return True
