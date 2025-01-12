import os
from gencontent import generate_page, extract_title
from src.markdown_blocks import markdown_to_html_node

import os

import os


def generate_pages_recursive(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")

    for dirpath, dirnames, filenames in os.walk(from_path):
        for filename in filenames:
            # Input file: full path to the file
            input_file = os.path.join(dirpath, filename)
            print(input_file)

            # Read the content of the input markdown file
            with open(input_file, "r") as from_file:
                markdown_content = from_file.read()

            # Read the template file
            with open(template_path, "r") as template_file:
                template = template_file.read()

            # Convert markdown content to HTML (assuming markdown_to_html_node is defined)
            node = markdown_to_html_node(markdown_content)
            html = node.to_html()

            # Extract the title from the markdown content (assuming extract_title is defined)
            title = extract_title(markdown_content)

            # Replace placeholders in the template
            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", html)

            # Compute the destination path
            relative_dirpath = os.path.relpath(dirpath, from_path)
            output_dir = os.path.join(dest_path, relative_dirpath)
            os.makedirs(output_dir, exist_ok=True)  # Create directories if they don't exist

            # Change the file extension to .html
            output_filename = os.path.splitext(filename)[0] + '.html'

            # Define the full output file path
            output_file_path = os.path.join(output_dir, output_filename)

            # Write the generated HTML to the output file
            with open(output_file_path, "w") as to_file:
                to_file.write(template)
