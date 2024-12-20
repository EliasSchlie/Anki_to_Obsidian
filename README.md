# Anki to Obsidian Converter

## Overview
This tool is designed to seamlessly convert exported Anki notes into Markdown files that can be directly imported into [Obsidian](https://obsidian.md). It allows you to manage and review your notes with Obsidian’s powerful markdown and linking capabilities.

## Features
- Converts Anki notes into clean Markdown files.
- Compatible with Obsidian's vault structure.

## Prerequisites
1. **Anki**: Install Anki and ensure your notes are ready for export.
2. **Python**: This tool is built using Python. Make sure you have Python installed on your system.

## Installation
1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/anki-to-obsidian.git
   cd anki-to-obsidian
   ```
2. Install the required dependencies (if any). For example:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Export Notes from Anki**:
   - Open Anki.
   - Go to `File` > `Export`.
   - Choose the `Notes in plain text (*.txt)` format and save the file.

2. **Prepare Input Folder**:
   - Place the exported Anki file(s) into the `exported_notes/` folder.

3. **Run the Script**:
   - Execute the script by specifying the input folder and the desired output folder:
     ```bash
     python anki_to_obsidian.py --input exported_notes --output obsidian_notes
     ```

4. **Load into Obsidian**:
   - Open your Obsidian vault.
   - Import the generated Markdown files into the appropriate folder in your vault.

## Configuration
- Customize the output format and file naming in the script by modifying the parameters in `anki_to_obsidian.py`.
- Add support for additional fields or tags if needed.

## Example
**Input (Anki Exported Notes):**
```
Front: Allele
Back: Each of two or more alternative forms of a gene that arise by mutation and are found at the same place on a chromosome.
```

**Output (Markdown File):**
```markdown
---
Type:: 
  - "[[Word]]"
  - "[[Anki_to_Obsidian]]"
---
# Allele
= Each of two or more alternative forms of a gene that arise by mutation and are found at the same place on a chromosome.
```

## Troubleshooting
- Ensure your Anki export file is correctly formatted as plain text.
- Verify the input and output folder paths are accurate.
- Check for missing Python dependencies and install them using `pip`.

## Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.