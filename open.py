from pypdf import PdfReader
import regex


def get_text():
    reader = PdfReader("teste.pdf")
    page = reader.pages[2]

    e_parts = []
    j_parts = []
    def visitor_body_e(text, cm, tm, font_dict, font_size):
        x = tm[4]
        if x > 300 and x < 900:
            e_parts.append(text)

    def visitor_body_j(text, cm, tm, font_dict, font_size):
        x = tm[4]
        if x <100:
            j_parts.append(text)
    page.extract_text(visitor_text=visitor_body_e)
    print(e_parts)
    page.extract_text(visitor_text=visitor_body_j)
    text_body = "".join(j_parts)
    e_body = "".join(e_parts)
    print(e_body)
    x = text_body.split("\n")
    print(e_body)
    #print(x)
    jp = []
    ro = []
    for count,e in enumerate (x):
        if count % 2 == 0:
            jp.append(e)
        else:
            ro.append(e)
    return jp,ro