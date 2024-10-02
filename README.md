# PDF Summarizer

## Table of Contents

- [PDF Summarizer](#pdf-summarizer)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation and Setup](#installation-and-setup)
  - [Customization](#customization)
    - [Adjusting Detail Level](#adjusting-detail-level)
    - [Adding Additional Instructions](#adding-additional-instructions)
    - [Setting Minimum Chunk Size](#setting-minimum-chunk-size)
    - [Changing Chunk Delimiter](#changing-chunk-delimiter)
    - [Enabling Recursive Summarization](#enabling-recursive-summarization)
    - [Verbose Output](#verbose-output)
  - [Modules](#modules)
  - [Acknowledgments](#acknowledgments)

## Introduction

This project allows you to generate concise summaries of PDF documents using OpenAI's GPT models. It extracts text from PDFs, tokenizes and chunks the text efficiently, and then uses the GPT model to create summaries. This can be especially useful for quickly understanding lengthy documents or extracting key information.

The code is based on the OpenAI Cookbook example ["Summarizing long documents"](https://cookbook.openai.com/examples/summarizing_long_documents), and extends it to handle PDF files and batch processing of multiple files.


## Features

- **PDF Extraction:** Extracts text from PDF files.
- **Efficient Tokenization:** Tokenizes text using the `tiktoken` library optimized for OpenAI models.
- **Intelligent Chunking:** Splits text into manageable chunks based on token limits.
- **Summarization:** Generates summaries using OpenAI's GPT models.
- **Batch Processing:** Processes multiple PDF files at once.
- **Configurable Detail Level:** Adjust the level of detail in the summaries.

## Prerequisites

- Python 3.7 or higher
- An OpenAI API key (you can obtain one by signing up at [OpenAI](https://platform.openai.com/signup))

## PDF Files 

Add your PDF-files to the input folder. 

## Installation and Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your_project.git
   cd your_project
   ```
   
## Setup

1. **Clone the Repository:**

```bash
   git clone https://github.com/yourusername/your_project.git
```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set OpenAI API Key:**
Set the OPENAI_API_KEY environment variable.

```bash
export OPENAI_API_KEY='your-api-key'
```

## Customization

You can customize the summarization process by adjusting various parameters in the `summarize` function. Below are the parameters you can modify to fine-tune the summaries according to your needs:

### Adjusting Detail Level
**Parameter:** `detail`  
The `detail` parameter controls the level of detail in the summaries. It accepts a float value between 0 and 1, where:  
- `0` results in the most concise summary.  
- `1` produces the most detailed summary by splitting the text into more chunks.

**Example:**
```python
summary = summarizer.summarize(text, detail=0.5, verbose=True)
```

**Parameter:** `model`
You can specify different OpenAI GPT models by changing the model parameter. The default model is 'gpt-4-turbo', but you can switch to other models like 'gpt-3.5-turbo' for faster responses or to reduce costs.
**Example:**
```python
summary = summarizer.summarize(text, model='gpt-3.5-turbo')
```

### Adding Additional Instructions
**Parameter:** `additional_instructions`
Use this parameter to provide custom instructions to the AI model, guiding the focus or format of the summary. This can be helpful if you want the summary in bullet points or if you want to emphasize certain aspects.
**Example**
```python
summary = summarizer.summarize(
    text,
    additional_instructions="Please provide the summary in bullet points and focus on the key economic impacts."
)
```

### Setting Minimum Chunk Size
**Parameter**: `minimum_chunk_size`
This parameter defines the minimum number of tokens for each text chunk when splitting the document. Increasing this value results in larger chunks, which can affect the granularity of the summarization.
**Example:**
```python
summary = summarizer.summarize(text, minimum_chunk_size=1000)
```

### Changing Chunk Delimiter
**Parameter**: `chunk_delimiter`
By default, the text is split into chunks based on periods ("."). You can change the delimiter to split the text differently, such as by paragraphs or lines.
**Example** (splitting by paragraphs):
```python
summary = summarizer.summarize(text, chunk_delimiter="\n\n")
```

### Enabling Recursive Summarization
**Parameter**: `summarize_recursively`
When set to True, this enables recursive summarization. The AI model will consider previous summaries when processing new chunks, potentially improving coherence and context in the final summary.
**Example**:
```python
summary = summarizer.summarize(text, summarize_recursively=True)
```
### Verbose Output
**Parameter**: `verbose`
Setting this parameter to True enables verbose output, which provides additional information during the summarization process, such as the number of chunks and their token lengths.
**Example:**
```python
summary = summarizer.summarize(text, verbose=True)
```

## Modules
- **pdf_utils.py**: Functions to extract text from PDFs.
- **tokenizer_utils.py**: Functions for text tokenization.
- **chunk_utils.py**: Functions to chunk text efficiently.
- **summarizer.py**: The main summarization class using OpenAI's API.


## Acknowledgments

**Based On:**
This project is based on the OpenAI Cookbook example: Summarizing long documents, and extends it to handle PDF files and batch processing of multiple files.

**Libraries and Tools:**
OpenAI for providing the GPT models.
PyMuPDF for PDF text extraction.
tiktoken for tokenization optimized for OpenAI models.
tqdm for progress bars.
