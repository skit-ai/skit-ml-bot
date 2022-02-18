def get_raw_dataset():
    # Obtain auth token.
    # Request for calls.
    # Get calls/turns data.
    # Format calls/turns data.
    # Upload data to s3.
    # return s3 url
    ...


def tag_dataset():
    # Download data from s3 url.
    # Upload to annotation service.
    # return annotation request status.
    ...


def get_tagged_data():
    # Query annotation service db.
    # Format annotated data.
    # Upload data to s3.
    # return s3 url
    ...


def evaluate_dataset():
    # Download data from s3 url.
    # Get config from db.
    # Evaluate data using eevee
    # return evaluation results.
    ...
