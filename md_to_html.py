import argparse
import sys

def md_to_html(markdown):
    html = []
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            html.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith('## '):
            html.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith('### '):
            html.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith('- '):
            html.append(f"<li>{line[2:]}</li>")
        else:
            html.append(f"<p>{line}</p>")
    return '\n'.join(html)

def md_to_ansi(markdown):
    ansi = []
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            ansi.append(f"\033[1m{line[2:]}\033[0m")  # Bold for H1
        elif line.startswith('## '):
            ansi.append(f"\033[1m{line[3:]}\033[0m")  # Bold for H2
        elif line.startswith('### '):
            ansi.append(f"\033[1m{line[4:]}\033[0m")  # Bold for H3
        elif line.startswith('- '):
            ansi.append(f"\033[7m{line[2:]}\033[0m")  # Inverted for list items
        else:
            ansi.append(f"\033[7m{line}\033[0m")      # Inverted for preformatted text
    return '\n'.join(ansi)

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to HTML.')
    parser.add_argument('input_file', help='Path to the input Markdown file')
    parser.add_argument('--out', help='Path to the output HTML file')
    parser.add_argument('--format', choices=['html', 'ansi'], default='ansi', help='Output format: "html" for HTML file, "ansi" for terminal output')

    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            markdown = f.read()
    except FileNotFoundError:
        sys.stderr.write(f"Error: The file {args.input_file} does not exist.\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        sys.exit(1)

    html = md_to_html(markdown)

    if args.out:
        try:
            with open(args.out, 'w', encoding='utf-8') as f:
                f.write(html)
        except Exception as e:
            sys.stderr.write(f"Error: {str(e)}\n")
            sys.exit(1)
    else:
        print(html)

if __name__ == "__main__":
    main()
