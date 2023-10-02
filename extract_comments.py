# Function to filter and save non-matching lines to comments.txt
def filter_and_save_comments(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        # Create a list to store the lines that don't start with "[–]"
        comments = []

        for line in lines:
            # Check if the line doesn't start with "[–]" (you can adjust the text as needed)
            if not line.strip().startswith("[–]"):
                comments.append(line.strip())

        # Save the filtered lines to comments.txt
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(comments))

        print(f'Non-matching lines saved to {output_filename}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Input and output file names
input_filename = 'output.txt'
output_filename = 'comments.txt'

# Call the filter_and_save_comments function
filter_and_save_comments(input_filename, output_filename)
