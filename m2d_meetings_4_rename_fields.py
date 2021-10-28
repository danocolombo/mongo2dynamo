import json
import os

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


def change_field_names():
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
            # the_meeting = json.dumps(entry)
            # fresh_meeting = list(the_meeting)

            # _id => meetingId
            the_entry['meetingId'] = the_entry.pop('_id')

            # attendance => attendanceCount
            the_entry['attendanceCount'] = the_entry.pop('attendance')

            # facilitator => facilitatorContact
            the_entry['facilitatorContact'] = the_entry.pop('facilitator')

            # cafeCoordinator => cafeContact
            the_entry['cafeContact'] = the_entry.pop('cafeCoordinator')

            # children => childrenCount
            the_entry['childrenCount'] = the_entry.pop('children')

            # mealCnt => mealCount
            the_entry['mealCount'] = the_entry.pop('mealCnt')

            # mealCoordinator => mealContact
            the_entry['mealContact'] = the_entry.pop('mealCoordinator')

            # newcomers => newcomersCount
            the_entry['newcomersCount'] = the_entry.pop('newcomers')

            # nursery => nurseryCount
            the_entry['nurseryCount'] = the_entry.pop('nursery')

            # supportRole => supportContact
            the_entry['supportContact'] = the_entry.pop('supportRole')

            # youth => youthCount
            the_entry['youthCount'] = the_entry.pop('youth')

           # write the record, add comma unless last record
            write_record(f,the_entry,entry != data['Meetings'][-1])
        write_file_footer(f)
        f.close()
    return True
