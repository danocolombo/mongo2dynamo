import os
import json


def clean_id(toxic):
    # this gets dict value for id
    actual_value = toxic['$oid']
    return actual_value


def clean_meeting_date(toxic):
    # this gets dict value for date and returns the date value
    # dict name is $date and want to only return date of long time stamp
    actual_date = toxic['$date'][:10]
    return actual_date


aws_files = []
try:
    base_path = './json_files/aws-ready-files/'
    for entry in os.listdir(base_path):
        if os.path.isfile(os.path.join(base_path, entry)):
            # print(entry)
            aws_files.append(entry)
    # now process each file
    for aws_file in aws_files:
        full_file_name = './json_files/aws-ready-files/' + aws_file
        file_data = None
        with open(full_file_name) as json_file:
            file_data = json.load(json_file)
            json_file.close()

        # for reading nested data [0] represents
        # the index value of the list
        with open(full_file_name, 'w') as fresh_file:
            fresh_file.writelines("{\"Meetings\": [\n")
            for record in file_data['Meetings']:
                tmpMeeting = record

                tmpMeeting['_id'] = clean_id(tmpMeeting['_id'])
                # remove __v in dict
                tmpMeeting.pop("__v", None)
                tmpMeeting['meetingDate'] = clean_meeting_date(tmpMeeting['meetingDate'])
                record_to_write = f"\t{tmpMeeting}\n"
                fresh_file.writelines(record_to_write)
                print(tmpMeeting)
            fresh_file.writelines("]}")
            fresh_file.close()

except ValueError:
    print("We got a value error")

else:
    print(f'We have {len(aws_files)} files to process')

finally:
    print(f'Done Processing')
