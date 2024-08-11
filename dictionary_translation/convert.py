import csv
from openai import OpenAI

client = OpenAI(api_key="")


def get_chatgpt_batch_response(words_batch):
    try:
        # Create the prompt for the batch
        joined_words = "\n".join(words_batch)
        prompt = "Translate the following German regex phrases into simple English phrases without any decomposition or explanation. For instance: Prompt: wirtschaft (.* )?(s(i)?eh(t|en)|schau(t|en)|blick(t|en)) (.* )?(her|hin)(ab|unter) Output: economic outlook downwards. \n Only provide the translated phrases in English as the answer in a linebreak-separated list. \n"

        # Send the request
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": joined_words}
            ]
        )

        # Split the response into a list of translations
        translations = completion.choices[0].message.content.split("\n")
        return translations

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Replace 'dictionary_translation/filtered.csv' with your CSV file path
input_file = 'dictionary_translation/filtered.csv'
output_file = 'dictionary_translation/filtered_with_translation.csv'

# Read from the input file and write to the output file
with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

batch_size = 5
batch = []

# Prepare to collect translated words
translated_rows = []

for i, row in enumerate(rows):
    word = row[0]  # Assuming the word is in the first column
    print(f"Processing word: {word}")
    batch.append(word)

    # If batch is full or it's the last word, send the request
    if len(batch) == batch_size or i == len(rows) - 1:
        translations = get_chatgpt_batch_response(batch)

        if translations:
            for j, translation in enumerate(translations):
                translated_rows.append(rows[i - len(batch) + j + 1] + [translation])
        else:
            for j in range(len(batch)):
                translated_rows.append(rows[i - len(batch) + j + 1] + ['Translation Error'])

        # Clear the batch for the next set of words
        batch = []

# Write the updated rows to the output file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(translated_rows)

print("Translation complete. Updated CSV file saved.")
