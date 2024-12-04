from openai import OpenAI
import os
import openai
import ast
import re

# Initialize the OpenAI client
client = OpenAI(
    api_key = "",
)

def extract_comments_and_code(file_path):
    """
    Extracts comments and associated code blocks from a Python file.
    """
    with open(file_path, 'r') as file:
        source = file.read()

    tree = ast.parse(source)
    comments = []
    code_blocks = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
            docstring = ast.get_docstring(node)
            if docstring:
                comments.append(docstring)
                code_blocks.append(ast.get_source_segment(source, node))

    # Extract inline comments using regex
    inline_comments = re.findall(r'#.*', source)
    comments.extend(inline_comments)
    code_blocks.extend([''] * len(inline_comments))

    return comments, code_blocks

def evaluate_comment_quality(comment, code_block):
    """
    Uses OpenAI's LLM to evaluate the quality of a comment.
    """
    prompt = f"""
    Evaluate the following comment for clarity, relevance, and consistency with the associated code block.

    Comment:
    {comment}

    Code Block:
    {code_block}

    Provide a score from 1 to 5 for each category:
    - Clarity
    - Relevance
    - Consistency

    Also, provide suggestions for improvement if necessary.
    """

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': 'You are an assistant that evaluates code comments.'},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=200,
        temperature=0
    )

    return response.choices[0].message.content.strip()

def main():
    # Path to the code file to analyze
    file_path = 'sample_code.py'

    comments, code_blocks = extract_comments_and_code(file_path)

    for comment, code_block in zip(comments, code_blocks):
        print("Comment:")
        print(comment)
        print("\nAssociated Code Block:")
        print(code_block)
        print("\nLLM Evaluation:")
        evaluation = evaluate_comment_quality(comment, code_block)
        print(evaluation)
        print("\n" + "-"*80 + "\n")

if __name__ == "__main__":
    main()
