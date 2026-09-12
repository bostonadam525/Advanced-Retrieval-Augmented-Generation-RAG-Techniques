# Pydantic in LangGraph Agents


---
# Why use Pydantic with LangGraph?

1. **Data Validation & Parsing**
   - Defines how data should be structured using standard Python type checks, automatically enforcing these rules.
   - LLM gives output in unstructured data --> Pydantic validates these outputs

2. **Type Hint Integration**
   - Python type annotations are used to define schemas.
   - This reduces the need for verbose validation code.

3. **Fast Performance**
   - Core validation engine written in RUST -- VERY FAST!

4. **Strict and Lax Modes**
   - Supports BOTH strict mode (enforcing strict types) AND lax mode (attempting to coerce data -- converting "1" to 1)

5. **Clear Error Handling**
   - Provides detailed errors when data validation fails.
  
6. **JSON Schema Generation**
   - Pydantic models can easily generate JSON schemas for documentation or validation in other languages.
