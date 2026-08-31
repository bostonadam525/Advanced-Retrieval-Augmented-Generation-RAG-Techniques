# Asynchronous Programming for AI Agents
- The key concepts here are: Subroutines vs. Co-routines


## Subroutine
- As an example we may have two functions:
```
def fetch_data():

def main():
  ## calling inside main function
  fetch_data()
```
- **key points:**
  - you have to wait for `fetch_data()` to finish its tasks then remaining code in main() function can continue/complete

---
## Co-routines
- This using asynchronous programming.
- Using the example above, we have two functions again, this time one uses `async`

```
async def fetch_data():

def main():
  fetch_data()
```

- **key points:**
  - difference here is that using ASYNC the code in `def main()` can execute without having to wait for the `def fetch_data()` code tasks to complete.



---
# Resources
- [Creating asynchronous AI agents with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/creating-asynchronous-ai-agents-with-amazon-bedrock/)
- [7 Async Patterns for Running Agents Concurrently in Python](https://machinelearningmastery.com/7-async-patterns-for-running-agents-concurrently-in-python/)
