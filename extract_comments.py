# Function to extract comments and save them to comments.txt
def extract_comments(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        # Create a list to store the extracted comments
        comments = []

        # Flag to indicate when to start/stop collecting comments
        collecting_comments = False

        for line in lines:
            # Check if the line starts with "Comment:" to start collecting comments
            if line.strip().startswith("Comment:"):
                collecting_comments = True
                continue
            # Check if we are currently collecting comments and the line is not empty
            if collecting_comments and line.strip():
                comments.append(line.strip())

        # Save the extracted comments to comments.txt
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(comments))

        print(f'Comments extracted and saved to {output_filename}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Input and output file names
input_filename = 'output.txt'
output_filename = 'comments.txt'

# Call the extract_comments function
extract_comments(input_filename, output_filename)
