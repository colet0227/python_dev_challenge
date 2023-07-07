# define the Cloud Function
def process_payload(request):
    # parse the incoming JSON request

    # get the 'captions' list from the data
    captions = get captions

    # if captions is empty return error message
    if not captions:
        return error message

    # get the start frame of the first word
    # since captions is a python list we can constant index it
    first = captions[0][start frame]

    # get the end frame of the last word
    last = captions[-1][end frame]

    # return the start_frame of the first word and the end_frame of the last word
    return (first, last)
