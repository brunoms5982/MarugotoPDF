import pdfplumber
import pandas as pd
import tabula
import regex as re

# Replace 'your_pdf_file.pdf' with the path to your PDF file


pdf_path = 'MarugotoonlineA2B1-1_Vocabulary.pdf'

# Read PDF into list of DataFrame
# dataframe = tabula.read_pdf(pdf_path, pages='all', guess=False, stream=True, pandas_options={'header': None}, lattice=False)
# Specify the PDF file you want to extract tables from

# Define a list of areas to extract
areas = [
    (82.276, 34.058, 135.85, 306.524),
    (138.912, 34.058, 174.118, 300.401),
    (184.833, 35.589, 223.866, 301.932),
    (230.754, 34.824, 270.553, 306.524),
    (277.441, 34.824, 324.127, 304.228),
    (327.189, 33.293, 368.518, 302.697),
    (320.301, 307.29, 366.222, 578.225),
    (368.518, 308.82, 409.847, 580.521),
    (373.11, 35.589, 415.204, 303.463),
    (418.266, 36.354, 461.126, 301.932),
    (412.143, 310.351, 458.83, 577.459),
    (467.248, 37.12, 507.812, 299.636),
    (461.891, 308.82, 503.22, 578.225),
    (507.812, 304.228, 556.03, 582.052),
    (516.996, 32.528, 553.733, 297.34),
    (558.326, 310.351, 603.481, 579.755),
    (561.387, 33.293, 607.308, 303.463),
    (609.604, 34.824, 654.76, 301.167),
    (605.778, 309.586, 650.933, 577.459),
    (656.291, 31.762, 700.681, 298.871),
    (653.995, 313.412, 698.385, 577.459),
    (702.212, 34.058, 747.368, 302.697),
    (701.447, 308.055, 745.837, 578.225),
    (748.899, 35.589, 794.055, 304.993),
    (748.133, 309.586, 795.585, 578.225),
]


# Initialize an empty list to store the extracted DataFrames
extracted_dataframes = []

# Loop through the defined areas and extract tables
for area in areas:
    df = tabula.read_pdf(pdf_path, pages='all', lattice=True,area=area, pandas_options={'header': None})
    extracted_dataframes.extend(df)

df = pd.concat(extracted_dataframes, axis=0, ignore_index=True)
# Now, extracted_dataframes contains DataFrames extracted from the specified areas
# Define a function to extract Japanese characters
def extract_japanese(text):
    pattern = re.compile(r'([\p{IsHan}\p{IsBopo}\p{IsHira}\p{IsKatakana}ー~]+)', re.UNICODE)
    if pd.notna(text):
        output = pattern.findall(text)
        if output:
            return ' /'.join(output)
    return ''

def extract_english(text):
    pattern = re.compile(r'([\p{IsHan}\p{IsBopo}\p{IsHira}\p{IsKatakana}ー~]+)', re.UNICODE)
    if pd.notna(text):
        text =  re.sub(pattern, '', text)
        text = text.replace('\r', '')
        # Remove empty parentheses ()
        text = text.replace('()', '')
        # Remove \
        text = text.replace('\\', '')
        return text

    return ''
# Apply the function to the DataFrame
df['japanese_column'] = df[0].apply(extract_japanese)
df['english_column'] = df[0].apply(extract_english)

df.dropna(how="all",axis=1,inplace=True)