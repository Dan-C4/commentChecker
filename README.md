# Comment Quality and Consistency Checker

One team member Daniel Chandler
An LLM-powered tool to assess and improve the quality and consistency of code comments in codebases.

## Introduction

This project leverages Large Language Models (LLMs) to evaluate the quality and consistency of comments in codebases. By analyzing comments for clarity, relevance, and consistency, the tool provides actionable feedback to help developers maintain high documentation standards.

Clear and consistent comments improve code readability and maintainability, which are crucial for collaboration and scaling in software development.

## Features

- Parses code files to extract comments and associated code blocks.
- Uses an LLM (e.g., GPT-4) to assess comment quality.
- Assigns scores based on clarity, relevance, and consistency.
- Provides suggestions for improving comments.
- Supports Python codebases (extensible to other languages).

## Prerequisites

- Python 3.6 or higher
- OpenAI Python library
- An OpenAI API key with access to GPT-4 models

## Installation

1. **Clone the repository**
2. **Navigate to the project directory**
3. **pip install openai**

## Usage Guide

1. Paste you OpenAI API into:
   9 client = OpenAI(
    api_key = "API GOES HERE",
   )
2. Make sure the program you want to Code Check is in the same directory
3. Rename your program to sample_code.py or change the name in the code here:
   72 file_path = 'sample_code.py'
4. Use the following command to run the program:
   python comment_quality_checker.py
