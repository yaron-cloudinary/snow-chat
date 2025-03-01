import openai
import os
import re
import sys
from string import Template

def read_file_instructions(foldername, filename, instruction_template):
    with open(f'{foldername}/{filename}', 'r') as file:
        placeholder = filename.removesuffix(".csv")
        templateObj = Template(instruction_template)
        instructions = templateObj.substitute(filename=placeholder)
        return f"{instructions}\n{file.read()}\n"


def read_folder_instructions(foldername, instruction_template):
    appendix = ""
    for filename in os.listdir(foldername):
        if filename.endswith(".csv"):
            appendix += read_file_instructions(foldername, filename, instruction_template)
    return appendix


def query_chatgpt(question):
    # Initialize the OpenAI client
    api_key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI(api_key=api_key)


    # Read the instruciton files 
    with open('./instructions.txt', 'r') as file:
        instructions = file.read()

    #Read additional instructions from the schemas and lookup folder
    appendix = ""
    appendix += read_folder_instructions('./schemas', "Below is a list that describes the ${filename} database table.  Each row describes a column.   The first word is the database column name. Then it is followed by a column type. The rest of the row is a comment.  Not all have comments.  The comment describes the column.:")
    appendix += read_folder_instructions('./lookup', "Where the ${filename} column is described in this csv:")

    # Define the conversation
    messages = [
        {"role": "system", "content": f"{instructions}\n\nBelow are further instructions that describe the schemas.\n\n{appendix}"},
        {"role": "user", "content": f"{question}"},

    ]

    # Send the message to ChatGPT
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=5000,
        temperature=0.7
    )

    return (messages, response)










def extract_sql_blocks(text):
    """
    Extracts only the SQL code blocks from the given text and removes everything else.
    """
    pattern = r"```sql(.*?)```"  # Regex pattern to match SQL code blocks
    matches = re.findall(pattern, text, re.DOTALL)  # Find all SQL code blocks
    if matches:
        # Return only the first SQL code block
        return matches[0].strip()
    else:
        return "No SQL code blocks found."
    



