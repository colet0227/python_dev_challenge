## Welcome! 👋

Well done for making it this far! This is the final step in the application process for the **Python Developer** role at **OSSA**.

If you do well on this challenge then we will setup an interview with you to discuss your application and the next steps.

Make sure to read the instructions carefully and follow them to the letter. We will be reviewing your submission and looking for the following:

- **Code quality**: We want to see clean, well-structured, and readable code.
- **Problem-solving**: We want to see how you approach problems and how you think about solutions.
- **Attention to detail**: We want to see that you can follow instructions and pay attention to the little things (such as edge cases, error handling, etc.)

## The Challenge
Your task is to write a Google Cloud Function.

The function accepts a `request` containing a JSON payload that ***should*** adhere to the structure below:
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

> See `payload.json` for the full request body.

Each word in `phrase` corresponds to an object in the `captions` array.

The function should return a response that contains the `start_frame` of the first word in the `phrase`, and the `end_frame` of the last word in the `phrase`.

## Instructions

1. Fork this repository.
2. Clone the forked repository to your local machine.
3. Create and swap to a new branch called `psuedo-code`.
4. Create a new file called `get_frames.py`.
5. Write your pseudo-code in `get_frames.py`. Commit your changes.
6. Create and swap to a new branch called `solution`.
7. Write your code solution in `get_frames.py`. Commit your changes.
8. *Optional* - Create and switch to a new branch called `bonus`. Add in anything else you think would be useful. Commit your changes.
9. Record a loom video that explains your solution. Describe your thought process and any challenges or bugs you encountered, and how you solved them. If you added bonus features then explain what you added, why you added it, and how you implemented the feature. Title the loom video `Product: Python Dev Onboarding Challenge by <first_name> <last_name>`.
11. *Optional* - Record a second loom introducing yourself to the team. Describe why you want this position, talk about past experience, and how you can add value to the team. Title the loom video `Product: Python Dev Introduction by <first_name> <last_name>`.
12. Go to `<LINK>` and submit your application.