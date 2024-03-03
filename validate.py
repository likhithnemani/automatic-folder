import requests
import pandas as pd

# Assuming your dataset is in a CSV file named "dataset.csv"
# df = pd.read_csv("final_dataset.csv")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Make the query
# output = query({
#     "inputs": "## Instruction Check if the input passage answers the above questions answered. If all of them are answered give the o/p as yes or else print the missing ones. 1) Tech stack is mentioned or not ? 2) Name of the project mentioned or not ? 3) Project description mentioned or not ? ## Input: " + df['Project Description'][25] + " Output (Yes/No):"
# })

output = query({
    "inputs": "Sample one ..."
})

# Extract project description from the generated text
generated_text = output[0]['generated_text']
print(generated_text)