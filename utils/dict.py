def user_data_to_dict(data):
    return {'id':data[0],
                        'first_name':data[1],
                        'last_name':data[2],
                        'email_id':data[3],
                        'contact_no':data[4]
                         }
def unicode_to_str(args):
    args = {str(k):str(v) for k,v in args.items()}
    return [args['first_name'],args['last_name'],args['email_id'],args['contact_no']]

def fill_all_field_in_arg(args,data):
    if 'first_name' not in args:
        args['first_name'] = data[0][1]
    if 'last_name' not in args:
        args['last_name'] = data[0][2]
    if 'email_id' not in args:
        args['email_id'] = data[0][3]
    if 'contact_no' not in args:
        args['contact_no'] = data[0][4]
    return args