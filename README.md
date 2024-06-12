# MD to HTML Converter

This is a simple console application that converts a subset of Markdown to HTML.

## How to build and run the project

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/md_to_html_converter.git
    cd md_to_html_converter
    ```

2. Run the script with a Markdown file as input:
    ```sh
    python md_to_html.py samples/example.md
    ```

3. Optionally, specify an output file:
    ```sh
    python md_to_html.py samples/example.md --out output.html
    ```

## Usage

- `python md_to_html.py <input_file> [--out <output_file>]`

## [Revert commit](https://github.com/Akella22/Mtrpz-Lab-1/commit/bea1adc1536c30cb85b6b1a819c6d7dbc91ca1b4)

## [Failed tests commit](https://github.com/Akella22/Mtrpz-Lab-1/pull/1/commits/7805e21e593fb2bc9d37db08e88bc5c9490fedc8)

## [Succeded tests commit](https://github.com/Akella22/Mtrpz-Lab-1/pull/1/commits/2fc4c2f4c276524b415ee3c185a96a5b6c587dae)

# Висновки

Хоча тести допомогли виявити деякі помилки у програмному коді, вони не виявили всі можливі проблеми. Наприклад, один із тестів не врахував відсутність символу нового рядка в кінці згенерованого HTML, що призвело до невідповідності між очікуваним та фактичним результатами. Таким чином, хоча тести відіграли важливу роль у забезпеченні якості програмного забезпечення, вони не змогли виявити всі потенційні проблеми, які можуть виникнути в процесі роботи програми.
