from win32printing import *


font = {
    "height": 10,
    #"width":40
}

with Printer(linegap=0) as printer:
    printer.text("مؤسسة عالم الخليج للمواد الغذائية", font_config={"height": 20})
    printer.text("__________________________________________________________________", font_config=font)
    printer.text("الصنف : ملاعق بلاستيك", font_config={"height": 15})
    printer.text("السعر بدون الضريبة : 10", font_config={"height": 15})
    printer.text("الضريبة : 1.5", font_config={"height": 15})
    printer.text("الاجمالي : 11.5", font_config={"height": 15})
    printer.text("__________________________________________________________________", font_config=font)
    printer.text("__________________________________________________________________", font_config=font)




