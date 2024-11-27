import yaml
from pathlib import Path


def load_yaml(file_path):
    """Load data from a YAML file."""
    with file_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_header(header_file):
    """Load header content from a Markdown file."""
    header_path = Path(header_file)
    if header_path.exists():
        with header_path.open("r", encoding="utf-8") as file:
            return file.read().strip()
    return None


def generate_markdown(data, header=None):
    """Generate Markdown content from structured data."""
    markdown = ""

    # Add header content if provided
    if header:
        markdown += f"{header}\n\n"

    for section, content in data.items():
        markdown += f"## {section}\n\n"
        markdown += "::::::{tab-set}\n"

        # Role holders tab
        markdown += ":::::{tab-item} Role holders\n"
        markdown += "::::{grid} 1 2 3 4\n:gutter: 3\n\n"
        for role_holder in content.get('role_holders', []):
            markdown += f":::{{grid-item-card}} {role_holder['name']}\n{role_holder['period']}\n:::\n\n"
        markdown += "::::\n:::::\n\n"

        # Past role holders tab
        if content.get('past_role_holders'):
            markdown += ":::::{tab-item} Past role holders\n"
            markdown += "::::{grid} 1 2 3 4\n:gutter: 3\n\n"
            for past_holder in content['past_role_holders']:
                markdown += f":::{{grid-item-card}} {past_holder['name']}\n{past_holder['period']}\n:::\n\n"
            markdown += "::::\n:::::\n\n"

        # Role description tab
        markdown += ":::::{tab-item} Role description\n\n"
        markdown += f"{content.get('role_description', '')}\n"
        markdown += ":::::\n::::::\n\n"

    return markdown


def save_markdown(file_path, content):
    """Save the generated Markdown content to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def main(input_file, output_file, header_file=None):
    input_path = Path(input_file)
    output_path = Path(output_file)

    # Load YAML data
    data = load_yaml(input_path)

    # Load header content
    header = load_header(header_file) if header_file else None

    # Generate Markdown content
    markdown_content = generate_markdown(data, header=header)

    # Save Markdown content
    save_markdown(output_path, markdown_content)
    print(f"Markdown file generated: {output_file}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert YAML to Markdown with optional header file.")
    parser.add_argument("input_file", help="Path to the input YAML file.")
    parser.add_argument("output_file", help="Path to save the generated Markdown file.")
    parser.add_argument("--header_file", help="Path to the header Markdown file.", default=None)
    args = parser.parse_args()

    main(args.input_file, args.output_file, header_file=args.header_file)
