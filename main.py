# mongo2dynamo conversion
import m2d_1_json_files
import m2d_2_remove_mongo_data_types
import m2d_3_add_dynamodb_data_types
import m2d_4_rename_fields

try:
    # create json compliant files
    if m2d_1_json_files.create_json_compliant_files():
        print(f"1. mongo data transformed to json [aws-ready-files produced]")
        # strip out the mongo data types
        if m2d_2_remove_mongo_data_types.remove_mongo_data_types():
            print(f"2. Mongo data types removed")
            if m2d_3_add_dynamodb_data_types.add_dynamo_data_types():
                print(f"3. Dynamo data types added")
                if m2d_4_rename_fields.change_field_names():
                    print(f"4. Dynamo fields renamed")
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
    print("mongo2dynamo utility complete")
