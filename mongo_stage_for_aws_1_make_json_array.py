# This creates output file as array of Meetings in JSON format
def gen_file_name(file_number):
    temp = './json_files/aws-ready-files/aws-input-file' + str(file_number) + '.json'
    return temp


def write_file_header(fp):
    header_data = "{\"Meetings\":[\n"
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


# =========================================
# Set up the definitions for processing
# =========================================
file_limit = 25  # number of lines from origin to put in new files
file_size = 0  # used for writing location
file_count = 1  # used to create the files names
file_pointer = 0

# file to read
input_file = "./json_files/mongo-export-files/mongo-meetings-small.json"
# get the size of the file
f = open(input_file)
num_lines = sum(1 for line in f)
f.close()
print(f"records: {num_lines}")
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
