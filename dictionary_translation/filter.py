import csv


def filter_csv_columns(input_file_path, output_file_path, column_indices):
    """
    Reads a CSV file, keeps only the columns specified by the indices in the dictionary,
    and writes the filtered output to a new file.

    Parameters:
    input_file_path (str): The path to the input CSV file.
    output_file_path (str): The path to the output CSV file.
    column_indices (set): A set with the desired column indices

    """
    try:
        # Open the input file for reading
        with open(input_file_path, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            # Open the output file for writing
            with open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)

                for row in reader:
                    # Filter the row to keep only the desired columns
                    filtered_row = [row[i] for i in column_indices]
                    # Write the filtered row to the output file
                    writer.writerow(filtered_row)

        print(f"Filtered CSV has been written to {output_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# filter
INPUT_PATH = "./gruendl-populism-dict_0.1.1_2020-01-28.csv"
OUTPUT_PATH = "./filtered.csv"
indices = {1, 2,3, 4}
filter_csv_columns(INPUT_PATH, OUTPUT_PATH, indices)