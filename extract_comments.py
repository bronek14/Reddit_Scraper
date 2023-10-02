# Function to extract contents between lines starting with "[-]"
def extract_contents(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        # Create a list to store the extracted contents
        extracted_contents = []

        # Flag to indicate when to start/stop extracting contents
        extracting_contents = False

        for line in lines:
            # Check if the line starts with "[-]" to start extracting contents
            if line.strip().startswith("[-]"):
                if extracting_contents:
                    # Stop extracting if we were already extracting
                    extracting_contents = False
                else:
                    # Start extracting if not already extracting
                    extracting_contents = True
                continue
            # Check if we are currently extracting contents and the line is not empty
            if extracting_contents and line.strip():
                extracted_contents.append(line.strip())

        # Save the extracted contents to output.txt
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(extracted_contents))

        print(f'Contents extracted and saved to {output_filename}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Input and output file names
input_filename = 'output.txt'
output_filename = 'extracted_contents.txt'

# Call the extract_contents function
extract_contents(input_filename, output_filename)
