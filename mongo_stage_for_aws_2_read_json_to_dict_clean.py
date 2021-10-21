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


# Opening JSON file
with open('aws-input-file1.json') as json_file:
    data = json.load(json_file)

    # for reading nested data [0] represents
    # the index value of the list

    for i in data['Meetings']:
        tmpMeeting = i

        tmpMeeting['_id'] = clean_id(tmpMeeting['_id'])
        # remove __v in dict
        tmpMeeting.pop("__v", None)
        tmpMeeting['meetingDate'] = clean_meeting_date(tmpMeeting['meetingDate'])
        print(tmpMeeting)