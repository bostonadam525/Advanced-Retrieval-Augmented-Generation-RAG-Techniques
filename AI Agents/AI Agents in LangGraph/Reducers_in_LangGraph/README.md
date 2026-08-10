# Reducers in LangGraph
- A Reducer in LangGraph is a function that takes in multiple inputs, like messages, states, or results from different parts of your graph, and reduces them into a single, unified output.
- Programmatically it looks like this: `Inputs → Node A / Node B / Node C → Reducer → Final Output`


## Types of Reducers
1. Built in reducers
   - `operator.add`: : The core built-in utility designed for chat histories. It appends new messages while automatically deduplicating or updating messages with matching IDs.
   - `add_messages`: Standard Python operator used to concatenate lists or combine numeric tallies when multiple parallel nodes write to a shared state key.
  
2. Custom Reducers
   - User-defined functions: Custom logic written via def my_reducer(current_value, new_value) to implement specific rules.
   - Unique item lists: Filter incoming updates so that a state list retains only distinct entries without duplicates.
   - Capped length lists: Restrict a log or history array to a maximum number of items by dropping older elements.
   - Dictionary merging: Combine incoming partial dictionary updates key-by-key rather than performing a flat replacement of the root dictionary




---
# References
1. https://dev.to/aiengineering/a-beginners-guide-to-getting-started-with-reducers-in-langgraph-38ii
2. https://shafiqulai.github.io/blogs/blog_9.html
3. https://www.skakarh.com/blog/langgraph-reducers-best-practices
