# This reads one file and makes numerous resultant files, based on configuration
def gen_file_name(filenum):
    temp = 'output-file' + str(filenum) + '.json'
    return temp


def write_file_header(fp):
    header_data = "{\"Meetings\":[\n"
    fp.writelines(header_data)


def write_file_footer(fp):
    fp.writelines("]}")


def write_record(fp, record):
    front_record = "{\"PutRequest\":{\"Item\":"
    end_record = "}}\n"
    record_to_write = "{}{}{}".format(front_record, record, end_record)
    fp.writelines(record_to_write)


file_size = 0  # used for writing location
file_limit = 10  # number of lines from origin to put in new files
file_count = 1  # used to create the files names

# file to read
input_file = "mongo-meetings-small.json"
# get the size of the file
f = open(input_file)
num_lines = sum(1 for line in f)
f.close()

# now read through the file
f = open(input_file)
for x in f:
    file_record = f.readline().rstrip('\n')
    out_file = open(gen_file_name(file_count), 'a')
    if file_size == 0:
        write_file_header(out_file)
    if file_size < file_limit:
        write_record(out_file, file_record)
        file_size += 1
        if file_size == file_limit:
            write_file_footer(out_file)
            file_count += 1
            file_size = 0
        out_file.close()
f.close()
