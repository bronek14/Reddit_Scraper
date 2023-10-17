#The functionality of this Module is to access the Data stored in the Raw subfolder of Data and futher refine it, throwing out any data that isnt strickly a user comment. This new set of data 
# will be stored in the Processed subfolder to Data.
# expected inputs include: the output.txt file that is stored in Data\\Raw\\


# Function to filter and save non-matching lines to comments.txt
def filter_and_save_comments(input_filename, output_file):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        # Create a list to store the lines that don't start with "[–]"
        comments = []

        for line in lines:
            # Check if the line doesn't start with "[–]" 
            if not line.strip().startswith("[–]"):
                comments.append(line.strip())

        # Save the filtered lines to comments.txt
        with open(output_file, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(comments))

        print(f'Data Successfully filtered and saved to comments.txt')
    except Exception as e:
        print(f'An error occurred: {str(e)}')


