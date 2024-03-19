# pip install striprtf
import re
from striprtf.striprtf import rtf_to_text
from textwrap import wrap
def extract_sections_from_rtf(rtf_path):
    with open(rtf_path, 'r') as file:
        rtf_content = file.read()
        text = rtf_to_text(rtf_content)

    # Split the text into sections
    sections = re.split(r'Multiple Choice Questions:|Fill-in-the-blank Questions:', text)
    
    # Remove any empty sections or whitespace
    sections = [s.strip() for s in sections if s.strip()]

    # Assume that the sections are in order: text, MCQ, FIBQ
    if len(sections) >= 3:
        # Wrap each section to the specified width
        text_content = '\n'.join(wrap(sections[0], width=wrap_width))
        mcq_content = '\n'.join(wrap(sections[1], width=wrap_width))
        fibq_content = '\n'.join(wrap(sections[2], width=wrap_width))
    else:
        print(f"Not enough sections in file: {rtf_path}")
        return

    base_filename = rtf_path[:-4]  # Remove .rtf extension
    text_filename = base_filename + "_text.txt"
    mcq_filename = base_filename + "_MCQ.txt"
    fibq_filename = base_filename + "_FIBQ.txt"

    # Write contents into separate files
    with open(text_filename, 'w', encoding='utf-8') as f:
        f.write(text_content)
    with open(mcq_filename, 'w', encoding='utf-8') as f:
        f.write(mcq_content)
    with open(fibq_filename, 'w', encoding='utf-8') as f:
        f.write(fibq_content)


# For a single file

# Example usage
rtf_filename = 'C:\\Users\\s224228\\Documents\\Fagpakkeprojekt-Eyes-Modelling\\Text_passges\\AI_HC_P01.rtf' # give the name and path
wrap_width = 80
extract_sections_from_rtf(rtf_filename)