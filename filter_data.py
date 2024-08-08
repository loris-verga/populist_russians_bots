import csv
import csv
from datetime import datetime
import csv
from datetime import datetime
import os


def filter_csv(input_file, output_file, column_indices, target_column_index, target_value="English"):
    # Open the input file for reading
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        # Read the header
        header = next(reader)

        # Filter the header according to the column indices
        filtered_header = [header[i] for i in column_indices]

        # List to store filtered rows
        filtered_rows = []

        # Process each row in the input file
        for row in reader:
            # Check if the target column has the target value
            if row[target_column_index] == target_value:
                # Filter the row according to the column indices
                filtered_row = [row[i] for i in column_indices]
                filtered_rows.append(filtered_row)


    # Create the output file if it does not exist
    if not os.path.exists(output_file):
        open(output_file, 'w').close()

    # Open the output file for writing
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        # Write the filtered header
        writer.writerow(filtered_header)

        # Write the filtered rows
        writer.writerows(filtered_rows)


# Define the set of column indices to keep
column_indices = {1, 2, 5, 13}


def extract_date_columns(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        # Read the header
        header = next(reader)

        # Find the index of the date column
        date_column_index = 2

        # Create new header without the date column
        new_header = [col for i, col in enumerate(header) if i != date_column_index] + ['year', 'month', 'day']

        # List to store rows with extracted date columns
        rows_with_date_columns = []

        # Process each row in the input file
        for row in reader:
            # Extract the date from the date column
            date_str = row[date_column_index]
            date_obj = datetime.strptime(date_str, '%m/%d/%Y %H:%M')

            # Extract year, month, and day from the date object
            year = date_obj.year
            month = date_obj.month
            day = date_obj.day

            # Append the extracted date columns to the row
            row_with_date_columns = [col for i, col in enumerate(row) if i != date_column_index] + [year, month, day]
            rows_with_date_columns.append(row_with_date_columns)

    # Write the changes to the output file
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        # Write the new header
        writer.writerow(new_header)

        # Write the rows with extracted date columns
        writer.writerows(rows_with_date_columns)


def remove_links_from_text(text):
    # Split the text into words
    words = text.split()

    # Remove words that start with 'http' or 'www'
    words_without_links = [word for word in words if not word.startswith('http') and not word.startswith('www')]

    # Join the words back together
    text_without_links = ' '.join(words_without_links)

    return text_without_links


def remove_links(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        # Read the header
        header = next(reader)

        # Find the index of the text column
        text_column_index = 1

        # List to store rows with removed links
        rows_with_removed_links = []

        # Process each row in the input file
        for row in reader:
            # Get the text from the text column
            text = row[text_column_index]

            # Remove links from the text
            text_without_links = remove_links_from_text(text)

            # Replace the text in the row with the text without links
            row[text_column_index] = text_without_links

            # Append the modified row to the list
            rows_with_removed_links.append(row)

        # Write the changes to the output file
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # Write the header
            writer.writerow(header)

            # Write the rows with removed links
            writer.writerows(rows_with_removed_links)

def convert_to_lowercase(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        # Read the header
        header = next(reader)
        # Find the index of the text column
        text_column_index = 1
        # List to store rows with converted text to lowercase
        rows_with_lowercase_text = []
        # Process each row in the input file
        for row in reader:
            # Get the text from the text column
            text = row[text_column_index]
            # Convert the text to lowercase
            lowercase_text = text.lower()
            # Replace the text in the row with the lowercase text
            row[text_column_index] = lowercase_text
            # Append the modified row to the list
            rows_with_lowercase_text.append(row)
        # Write the changes to the output file
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            # Write the header
            writer.writerow(header)
            # Write the rows with converted text to lowercase
            writer.writerows(rows_with_lowercase_text)
