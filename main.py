# mongo2dynamo conversion
from m2d_meetings_1_json_files import create_json_compliant_files as meetings_json_files
from m2d_meetings_2_remove_mongo_data_types import remove_mongo_data_types as meetings_remove_mongo_types
from m2d_meetings_3_add_dynamodb_data_types import add_dynamo_data_types as meetings_add_dynamo_types
from m2d_meetings_4_rename_fields import change_field_names as meetings_change_fields
from m2d_meetings_5_aws_wrap_each_meeting import dynamodb_wrapper as meetings_dynamo_wrapper
import m2d_groups_1_json_files
import m2d_groups_2_remove_mongo_data_types
import m2d_groups_3_add_dynamodb_data_types
import m2d_groups_4_rename_fields
import m2d_groups_5_aws_wrap_each_meeting
import m2d_clients_0_complete
import m2d_humans_1_json_files
import m2d_humans_2_remove_mongo_data_types
import m2d_humans_3_add_dynamodb_data_types
import m2d_humans_4_rename_fields
import m2d_humans_5_aws_wrap_each_meeting
import m2d_peoples_1_json_files
import m2d_peoples_2_remove_mongo_data_types
import m2d_peoples_3_add_dynamodb_data_types
import m2d_peoples_4_rename_fields
import m2d_peoples_5_aws_wrap_each_meeting

# DO MEETINGS
try:
    # convert the Meetings data
    if meetings_json_files():
        print(f"1. mongo data transformed to json [aws-ready-files produced]")
        # strip out the mongo data types
        if meetings_remove_mongo_types():
            print(f"2. Mongo data types removed")
            if meetings_add_dynamo_types():
                print(f"3. Dynamo data types added")
                if meetings_change_fields():
                    print(f"4. Dynamo fields changed")
                    if meetings_dynamo_wrapper():
                        print(f"5. Dynamo wrappers applied")
                    else:
                        print(f"dynamodb_wrapper(): error")
                else:
                    print(f"change_field_names(): error")
            else:
                print(f"add_dynamo_data_types(): error")
        else:
            print(f"ERROR REMOVING DATA TYPES")
    else:
        raise Exception('create_json_compliant_files(): error')
    # convert the groups data
    # convert the users data

except Exception as err:
    print(f"{err}")

finally:
    print("mongo2dynamo: Meetings converted and ready")

# DO GROUPS
try:
    # convert the Greetings data
    if m2d_groups_1_json_files.create_json_compliant_files():
        print(f"1. mongo data transformed to json [aws-ready-files produced]")
        # strip out the mongo data types
        if m2d_groups_2_remove_mongo_data_types.remove_mongo_data_types():
            print(f"2. Mongo data types removed")
            if m2d_groups_3_add_dynamodb_data_types.add_dynamo_data_types():
                print(f"3. Dynamo data types added")
                if m2d_groups_4_rename_fields.change_field_names():
                    print(f"4. Dynamo fields renamed")
                    if m2d_groups_5_aws_wrap_each_meeting.dynamodb_wrapper():
                        print(f"5. Dynamo wrappers applied")
                    else:
                        print(f"dynamodb_wrapper(): error")
                else:
                    print(f"change_field_names(): error")
            else:
                print(f"add_dynamo_data_types(): error")
        else:
            print(f"ERROR REMOVING DATA TYPES")
    else:
        raise Exception('create_json_compliant_files(): error')
    # convert the groups data
    # convert the users data

except Exception as err:
    print(f"{err}")

finally:
    print("mongo2dynamo: Groups converted and ready")

# DO CLIENTS
try:
    # convert the Client data
    if m2d_clients_0_complete.convert_client_definitions():
        print(f"Client conversion complete")
    else:
        raise Exception('convert_client_definitions(): error')

except Exception as err:
    print(f"{err}")

finally:
    print("mongo2dynamo: Clients converted and ready")

# DO HUMANS
try:
    # convert the Humans data
    if m2d_humans_1_json_files.create_json_compliant_files():
        print(f"1. mongo data transformed to json [aws-ready-files produced]")
        # strip out the mongo data types
        if m2d_humans_2_remove_mongo_data_types.remove_mongo_data_types():
            print(f"2. Mongo data types removed")
            if m2d_humans_3_add_dynamodb_data_types.add_dynamo_data_types():
                print(f"3. Dynamo data types added")
                if m2d_humans_4_rename_fields.change_field_names():
                    print(f"4. Dynamo fields renamed")
                    if m2d_humans_5_aws_wrap_each_meeting.dynamodb_wrapper():
                        print(f"5. Dynamo wrappers applied")
                    else:
                        print(f"dynamodb_wrapper(): error")
                else:
                    print(f"change_field_names(): error")
            else:
                print(f"add_dynamo_data_types(): error")
        else:
            print(f"ERROR REMOVING DATA TYPES")
    else:
        raise Exception('create_json_compliant_files(): error')

except Exception as err:
    print(f"{err}")

finally:
    print("mongo2dynamo: Humans converted and ready")

# DO PEOPLES
try:
    # convert the Peoples data
    if m2d_peoples_1_json_files.create_json_compliant_files():
        print(f"1. mongo data transformed to json [aws-ready-files produced]")
        # strip out the mongo data types
        if m2d_peoples_2_remove_mongo_data_types.remove_mongo_data_types():
            print(f"2. Mongo data types removed")
            if m2d_peoples_3_add_dynamodb_data_types.add_dynamo_data_types():
                print(f"3. Dynamo data types added")
                if m2d_peoples_4_rename_fields.change_field_names():
                    print(f"4. Dynamo fields renamed")
                    if m2d_peoples_5_aws_wrap_each_meeting.dynamodb_wrapper():
                        print(f"5. Dynamo wrappers applied")
                    else:
                        print(f"dynamodb_wrapper(): error")
                else:
                    print(f"change_field_names(): error")
            else:
                print(f"add_dynamo_data_types(): error")
        else:
            print(f"ERROR REMOVING DATA TYPES")
    else:
        raise Exception('create_json_compliant_files(): error')

except Exception as err:
    print(f"{err}")

finally:
    print("mongo2dynamo: Humans converted and ready")
