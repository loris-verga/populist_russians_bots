import csv

dic_rooduijn_pauwels = {"elit",
                        "consensus",
                        "undemocratic",
                        "referend",
                        "corrupt",
                        "propagand",
                        "politici",
                        "deceit",
                        "deceiv",
                        "betray",
                        "shame",
                        "scandal",
                        "truth",
                        "dishonest",
                        "establishm",
                        "ruling"}


def extract_grundle_translation_dictionary(populism_criteria):

    """
    This method extract a dictionary from a csv file
    Args:
           file_path: the path of the csv file
           populism_criteria: the criteria associated with the specific dictionary

    Returns:

    """
    FILE_PATH = "./dictionary_translation/filtered_with_translation.csv"
    POPULISM_CRIT_COLUMN = 3
    EXPRESSION_COLUMN = 4

    result_set = set()  # Initialize an empty set to store the values

    # Open and read the CSV file
    with open(FILE_PATH, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Ensure the row has enough columns
            if len(row) >= 5:
                # Check if the fourth column matches the specified value
                if row[POPULISM_CRIT_COLUMN] == populism_criteria:
                    # Add the value from the fifth column to the set
                    result_set.add(row[EXPRESSION_COLUMN])

    return result_set
