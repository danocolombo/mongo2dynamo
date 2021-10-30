import os
import json
import glob


def clean_id(toxic):
    # this gets dict value for id
    actual_value = toxic['$oid']
    return actual_value


def analyze_record(record):
    client_info = json.loads(record)
    aws_client = {}
    # ===================================
    # remove connection value
    # ===================================
    if "connection" in client_info:
        client_info.pop("connection")
    # ===============================================
    # get client related information we want to save
    # ===============================================
    client_id = client_info["_id"]["$oid"]
    client_name = client_info["name"]
    client_code = client_info["code"]
    # print(f"******************")
    # print(f"client_id: {client_id}")
    # print(f"client_name: {client_name}")
    # print(f"client_code: {client_code}")

    # ================================================
    # get the user definitions for the client
    # ================================================
    if "users" in client_info:
        client_users = []
        read_users = client_info["users"]
        for x in read_users:
            stripped_id = clean_id(x["_id"])
            group_info = {"userId": {"S": stripped_id}, "role": {"S": x['role']}, "status": {"S": x['status']}}
            client_users.append(group_info)
            
        # print(f"users: {client_users}\n")

    # ================================================
    # get the default groups information
    # ================================================
    if "defaultGroups" in client_info:
        client_groups = []
        read_groups = client_info["defaultGroups"]
        # need to remove the mongo data type for id
        
        for x in read_groups:
            stripped_id = clean_id(x["_id"])
            client_groups.append({"group_id": {"S": stripped_id}, "gender": {"S": x['gender']}, "title": {"S": x['title']}, "location": {"S":x['location']}, "facilitator": {"S": x['facilitator']}})
            
            # client_users.insert(str(f"id: {stripped_id}"))

        # print(f"default_groups: {client_groups}\n")    

    # ================================================
    # now check for mConfigs
    # ================================================
    if "mConfigs" in client_info:
        client_configs = {}
        for x in client_info["mConfigs"]:
            config_setting = {}
            the_config = ""
            the_value = ""
            for k, v in x.items():
                if k == "config":
                    the_config = v
                elif k == "value":
                    the_value = v
            client_configs[the_config] = {"B": the_value}


        # print(f"client_configs:\n{client_configs}\n")


    # ===================================
    # print the original structure
    # ===================================
    # print(f"******************\n{client_info}\n****************")

    # =============================================
    # create the new dict to return
    # =============================================
    aws_client["clientId"] = {"S": client_id}
    aws_client["clientName"] = {"S": client_name}
    aws_client["clientCode"] = {"S": client_code}
    aws_client["clientUsers"] = {"L": client_users}
    aws_client["defaultGroups"] = {"L": client_groups}
    aws_client["clientConfigs"] = {"L": client_configs}
    return aws_client


# This creates output file as array of Meetings in JSON format
def gen_file_name(file_number):
    temp = './json_files/aws-ready-files/clients/aws-clients-file' + \
           str(file_number) + '.json'
    return temp


def write_file_header(fp):
    header_data = "{\"meeter-clients\":[\n"
    fp.writelines(header_data)


def write_file_footer(fp):
    fp.writelines("]}")


def write_record(fp, record, comma):
    if comma:
        end_record = "}},\n"
    else:
        end_record = "}}\n"
    wrapper_start = "{\"PutRequest\": {\"Item\":"

    # record_to_write = "{}{}".format(record, end_record)
    record_to_write = f"{wrapper_start}{record}{end_record}"

    fp.writelines(record_to_write)


def check_input_file(input_directory, input_file_name):
    # this will make sure the input_file exists and the output_dir is clean
    file_confirmation = False
    target = input_directory + input_file_name
    directory_contents = glob.glob(target)
    return len(directory_contents)


def output_directory_confirmed(output_directory):
    # if there are files in the output directory, warn they will be deleted and ask to proceed
    file_count = 0

    try:
        target = output_directory + "/*.*"
        # first see if the directory exists
        if not os.path.isdir(output_directory):
            response = input(
                "Output directory does not exist, do you want to create it?(y/n)")
            if response.upper() != "Y":
                raise Exception(
                    "Output directory non-existent. Operation aborted by user")
            # need to create directory
            os.mkdir(output_directory)
            # verify directory was created
            if not os.path.isdir(output_directory):
                raise Exception("Unable to create output directory")
        with os.scandir(output_directory) as dir_contents:
            for entry in dir_contents:
                file_count += 1
        if file_count > 0:
            response = input(
                f"Output directory {output_directory} is not empty. Proceed?(y/n)")
            if response.upper() == "Y":
                # get the file names and delete
                dir_contents = os.listdir(output_directory)
                for a_file in dir_contents:
                    target = output_directory + "/" + a_file
                    os.remove(target)
                return True
            else:
                return False
        else:
            return True
    except (ZeroDivisionError, TypeError) as err:
        print(f'error: {err}')


def convert_client_definitions():
    # =========================================
    # Set up the definitions for processing
    # =========================================
    file_limit = 25  # number of lines from origin to put in new files
    file_size = 0  # used for writing location
    file_count = 1  # used to create the files names
    file_pointer = 0

    # file to read
    input_directory = "./json_files/mongo-export-files/clients/"
    input_file_name = "mongo-clients-wbc-all.json"
    input_file = f"{input_directory}{input_file_name}"
    # directory location for output files
    output_directory = "./json_files/aws-ready-files/clients"

    if not check_input_file(input_directory, input_file_name):
        # no input file found...
        print(f"\n{input_file} not found, \nPlease confirm input file. aborting")
        return False
    if not output_directory_confirmed(output_directory):
        # directory not found or user elected to abort
        print(f"\nOutput directory not ready to proceed.\n aborting")
        return False

    # get the size of the file
    f = open(input_file)
    num_lines = sum(1 for line in f)
    f.close()
    # now read through the file
    # opent the file to write....
    out_file = open(gen_file_name(file_count), 'w')
    f = open(input_file)
    write_file_header(out_file)
    for x in f:
        file_pointer += 1
        file_record = x.rstrip('\n')
        
        if file_size == 0:
            # write_file_header(out_file)
            junk = True
        if file_size < file_limit:
            add_comma = False
            if file_size == (file_limit - 1) or file_pointer == num_lines:
                add_comma = False
            else:
                add_comma = True
            
            return_value = analyze_record(file_record)
            
            write_record(out_file, json.dumps(return_value), add_comma)
            file_size += 1
            if file_size == file_limit or file_pointer == num_lines:
                # write_file_footer(out_file)
                file_count += 1
                file_size = 0
            # out_file.close()
    write_file_footer(out_file)
    out_file.close()
    f.close()
    return True
