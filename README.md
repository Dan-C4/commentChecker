# Comment Quality and Consistency Checker

An LLM-powered tool to assess and improve the quality and consistency of code comments in codebases.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Experiment Results](#experiment-results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

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
- An OpenAI API key with access to GPT-3.5-Turbo or GPT-4 models

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/comment-quality-checker.git
   cd comment-quality-checker
