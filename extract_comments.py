# Function to extract contents between lines starting with "[-]"
def extract_contents(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        # Create a list to store the extracted contents
        comments = []

        # Flag to indicate when to start/stop extracting contents
        comments = False

        for line in lines:
            # Check if the line starts with "[-]" to start extracting contents
            if line.strip().startswith("[-]"):
                if comments:
                    # Stop extracting if we were already extracting
                    comments = False
                else:
                    # Start extracting if not already extracting
                    comments = True
                continue
            # Check if we are currently extracting contents and the line is not empty
            if comments and line.strip():
                comments.append(line.strip())

        # Save the extracted contents to output.txt
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(comments))

        print(f'Contents extracted and saved to {output_filename}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Input and output file names
input_filename = 'output.txt'
output_filename = 'comments.txt'

# Call the extract_contents function
comments(input_filename, output_filename)
