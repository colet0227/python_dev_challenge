import json

def process_payload_from_file(file_path):
    # Read the payload from the file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Check if captions are present in data
    if 'captions' not in data:
        return json.dumps({
            'status': 'error',
            'message': 'No captions found in the request.'
        }), 400

    captions = data['captions']

    # check if captions is not empty
    if not captions:
        return json.dumps({
            'status': 'error',
            'message': 'Captions array is empty.'
        }), 400

    # get the start frame of the first word
    start_frame_first_word = captions[0]['start_frame']

    # get the end frame of the last word
    end_frame_last_word = captions[-1]['end_frame']

    return (json.dumps({
           'start_frame_first_word': start_frame_first_word,
           'end_frame_last_word': end_frame_last_word
           }), 200)


print(process_payload_from_file('payload.json'))
