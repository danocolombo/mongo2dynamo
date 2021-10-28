import os
import glob


# This creates output file as array of Meetings in JSON format
def gen_file_name(file_number):
    temp = './json_files/aws-ready-files/groups/aws-groups-file' + str(file_number) + '.json'
    return temp


def write_file_header(fp):
    header_data = "{\"Groups\":[\n"
    fp.writelines(header_data)


def write_file_footer(fp):
    footer_data = "]}"
    fp.writelines(footer_data)


def write_record(fp, record, comma):
    if comma:
        end_record = ",\n"
    else:
        end_record = "\n"
    # record_to_write = "{}{}".format(record, end_record)
    record_to_write = f"{record}{end_record}"

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
            response = input("Output directory does not exist, do you want to create it?(y/n)")
            if response.upper() != "Y":
                raise Exception("Output directory non-existent. Operation aborted by user")
            # need to create directory
            os.mkdir(output_directory)
            # verify directory was created
            if not os.path.isdir(output_directory):
                raise Exception("Unable to create output directory")
        with os.scandir(output_directory) as dir_contents:
            for entry in dir_contents:
                file_count += 1
        if file_count > 0:
            response = input(f"Output directory {output_directory} is not empty. Proceed?(y/n)")
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


def create_json_compliant_files():
    # =========================================
    # Set up the definitions for processing
    # =========================================
    file_limit = 25  # number of lines from origin to put in new files
    file_size = 0  # used for writing location
    file_count = 1  # used to create the files names
    file_pointer = 0

    # file to read
    input_directory = "./json_files/mongo-export-files/groups/"
    input_file_name = "mongo-groups-small.json"
    input_file = f"{input_directory}{input_file_name}"
    # directory location for output files
    output_directory = "./json_files/aws-ready-files/groups"

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
    f = open(input_file)
    for x in f:
        file_pointer += 1
        file_record = x.rstrip('\n')
        out_file = open(gen_file_name(file_count), 'a')
        if file_size == 0:
            write_file_header(out_file)
        if file_size < file_limit:
            add_comma = False
            if file_size == (file_limit - 1) or file_pointer == num_lines:
                add_comma = False
            else:
                add_comma = True
            write_record(out_file, file_record, add_comma)
            file_size += 1
            if file_size == file_limit or file_pointer == num_lines:
                write_file_footer(out_file)
                file_count += 1
                file_size = 0
            out_file.close()
    f.close()
    return True
