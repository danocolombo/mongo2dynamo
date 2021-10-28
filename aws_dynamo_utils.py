# this file is used to format json components to be dynamodb compliant

# add the S for string values
def label_as_string(field):
    # get string, need to return list
    new_value = {"S": field}
    return (new_value)


def identify_field(field, field_type):
    # get string, need to return list
    new_value = {f"{field_type}": str(field)}
    return (new_value)


def search_dict(table, field):
    # this returns True if field is in dict
    if field in table.keys():
        return True
    else:
        return False
