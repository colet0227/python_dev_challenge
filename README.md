## Welcome! 👋

Well done for making it this far! This is the final step in the application process for the **Python Developer** role at **OSSA**.

Make sure to read the instructions carefully and follow them to the letter. We will be reviewing your submission and looking for the following:

- **Code quality**: We want to see clean, well-structured, and well-documented code.
- **Problem-solving**: We want to see how you approach problems and how you think about solutions.
- **Attention to detail**: We want to see that you can follow instructions and pay attention to the little things.

## The Challenge
Your task is to write a function that can be deployed as a Google Cloud Function.

The function accepts a `request` containing a JSON payload that *should* be in the following structure:
```json
  {
    "phrase": "Why do people say crypto is too VOLATILE to invest in? It's a LIE.",
    "captions": [
      { "word": "why", "start_frame": 0, "end_frame": 6 },
      { "word": "do", "start_frame": 6, "end_frame": 12 },
      { "word": "people", "start_frame": 12, "end_frame": 18 },
      { "word": "say", "start_frame": 18, "end_frame": 24 },
      { "word": "crypto", "start_frame": 24, "end_frame": 36 }
      // ...etc
    ]
  }
```

See `payload.json` for the full request body.

Each word in `phrase` corresponds to an object in the `captions` array.

The function should return a response that contains the `start_frame` of the first word in the `phrase`, and the `end_frame` of the last word in the phrase.

## Instructions

1. Fork this repository.
2. Clone the forked repository to your local machine.
3. Create and swap to a new branch called `psuedo-code`.
4. Create a new file called `get_frames.py`.
5. Write your pseudo-code in `get_frames.py`. Commit your changes.
6. Create and swap to a new branch called `solution`.
7. Implement your solution in `get_frames.py`. Commit your changes.
8. *Optional*: Create and switch to a new branch called `bonus`. Add in anything else you think would be useful. Commit your changes.