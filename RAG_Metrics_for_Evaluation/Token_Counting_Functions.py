## To count the number of tokens in a text document, you can use a tokenizer. 
## The specific tokenizer you use should ideally match the one used by your language model. 
## However, if you don't have access to the exact tokenizer, you can use approximations. 
## Here are a few methods:

### 1. Using the `transformers` library (recommended if you're working with transformer-based models):

### iteration # 1 of this script 
from tqdm import tqdm
from transformers import AutoTokenizer

# Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained("<huggingface_model_ckpt>")

# Function to count tokens
def count_tokens(text):
    return len(tokenizer.encode(text))

# Apply the function with a progress bar
tqdm.pandas(desc="Counting tokens")
df['token_count_text'] = df['text'].progress_apply(count_tokens)

# Display the value counts
print(df['token_count_text'].value_counts())


-------------------------------------------
## iteration #2 of this script 

from transformers import AutoTokenizer

def count_tokens(text, model_name="gpt2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return len(tokenizer.encode(text))

# Example usage
text = "Your text goes here."
token_count = count_tokens(text)
print(f"Number of tokens: {token_count}")

---------------------------------------------------------
### 2. Using a simple whitespace-based tokenization (quick approximation):

def count_tokens_simple(text):
    return len(text.split())

# Example usage
text = "Your text goes here."
token_count = count_tokens_simple(text)
print(f"Approximate number of tokens: {token_count}")

------------------------------------------------------------
### 3. Using the `tiktoken` library (specific to OpenAI models using BPE tokenizer):

import tiktoken

def count_tokens_tiktoken(text, encoding_name="cl100k_base"):
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))

# Example usage
text = "Your text goes here."
token_count = count_tokens_tiktoken(text)
print(f"Number of tokens: {token_count}")

-----------------------------------------------------
### 4. Reading from a file and counting tokens:

from transformers import AutoTokenizer

def count_tokens_from_file(file_path, model_name="gpt2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    total_tokens = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            total_tokens += len(tokenizer.encode(line))
    
    return total_tokens

# Example usage
file_path = "path/to/your/text/file.txt"
token_count = count_tokens_from_file(file_path)
print(f"Total number of tokens in the file: {token_count}")
```

----------------------------------------------------
### Summary 
```
Choose the method that best fits your needs and the specifics of the model you are using. 

1. The `transformers` library method is generally the most accurate for transformer-based models
2. The simple whitespace method is quickest but least accurate. 
3. The `tiktoken` method is specific to OpenAI models.

  Remember that the actual token count may vary slightly depending on the specific tokenizer used by your language model.
```
