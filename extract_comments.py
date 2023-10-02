def extract_comments(input_file="output.txt", output_file="comments.txt"):
    try:
        # Read the content from the input file
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()

        # Split the content into separate comments
        comments = content.split('\n\n')

        # Filter out any empty comments
        comments = [comment.strip() for comment in comments if comment.strip()]

        # Combine the comments into a single string
        comments_text = "\n\n".join(comments)

        # Save the comments to the output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(comments_text)

        print(f"Extracted comments successfully and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
