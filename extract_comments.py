# Function to extract comments from a Reddit data text file and save to 'comments.txt'
def extract_comments_and_save(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        comments_section = False
        comments = []

        for line in lines:
            line = line.strip()

            # Check if we are inside the comments section
            if line == "Comments:":
                comments_section = True
                continue

            if comments_section and line:
                comments.append(line)

        if comments:
            # Save the comments to 'comments.txt'
            output_file = 'comments.txt'
            with open(output_file, 'w', encoding='utf-8') as out_file:
                for comment in comments:
                    out_file.write(comment + '\n')
            
            print(f"Extracted comments saved to {output_file}")
        else:
            print("No comments found in the file.")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    input_file = "output.txt"  # Replace with the path to your saved Reddit data text file
    extract_comments_and_save(input_file)
