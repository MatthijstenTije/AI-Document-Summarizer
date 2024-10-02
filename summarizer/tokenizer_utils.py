import tiktoken

def tokenize(text: str, model_name: str = 'gpt-4-turbo'):
    """
    Tokenizes the input text using the tiktoken library.
    """
    encoding = tiktoken.encoding_for_model(model_name)
    return encoding.encode(text)
