# pip install striprtf
import re
from striprtf.striprtf import rtf_to_text
import glob
import os

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
        text_content, mcq_content, fibq_content = sections[:3]
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



def process_all_rtf_files(folder_path):
    # Use glob to find all RTF files in the folder
    rtf_files = glob.glob(os.path.join(folder_path, '*.rtf'))

    for rtf_filename in rtf_files:
        print(f"Processing {rtf_filename}")
        extract_sections_from_rtf(rtf_filename)

# Call the function with the path to your folder containing RTF files
folder_path = 'C:\\Users\\s224228\\Documents\\Fagpakkeprojekt-Eyes-Modelling\\Text_passges'
process_all_rtf_files(folder_path)
