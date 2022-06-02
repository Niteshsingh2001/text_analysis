# This File is made by Human - Nitesh Singh
from django.http import HttpResponse
from django.shortcuts import render
import re

meta = {"site_name" : "Text Analysis"}

def index(request):
    return render(request, "index.html", meta)


def analyze(request):
    get_text = request.GET.get("all_text", "default")
    punc = request.GET.get("check1", "off")
    cap = request.GET.get("check2", "off")
    count = request.GET.get("check3", "off")
    extra = request.GET.get("check4", "off")
    cap_head = request.GET.get("check5", "off")

    punc_lst = '''.,\\';[]`~!@/$%^&**()_-=+{}":|<>?*-+'''



    analyze_text = ""
    purpose = []


    if punc == "on":
        purpose.append("Remove Punctuation")
        for char in get_text:
            if char not in punc_lst:
                analyze_text = analyze_text + char

    if cap == "on":
        purpose.append("Capitalize")
        if analyze_text == "":
            analyze_text = get_text
        analyze_text = analyze_text.capitalize()

    if extra == "on":
        purpose.append("Removing extra space")
        if analyze_text == "":
            analyze_text = get_text
        analyze_text = analyze_text.rstrip()
        analyze_text = analyze_text.lstrip()

    if cap_head == "on":
        purpose.append("Capitalize Headings")
        if analyze_text == "":
            analyze_text = get_text
        regex = r"#([^/]+)#"
        test_str = analyze_text
        matches = re.findall(regex, test_str)

        for i in matches:
            analyze_text = analyze_text.replace(i,' '.join(x.capitalize() for x in i.split(' ')))

                

    params = {"text": analyze_text, "motive": purpose,"site_name":meta.get("site_name")}

    if count == "on":
        purpose.append("Count")

        space = 0
        word = 0
        if analyze_text == "":
            analyze_text = get_text
        for i in analyze_text:
            if i == " ":
                space += 1
            else:
                word += 1
        params["count"] = f"Your text contain {space} spaces and {word} Characters"

    if punc == "off" and cap == "off" and count == "off" and extra == "off" and cap_head == "off":
        return HttpResponse(" !! **Error** Please selct any one option !! ")

    return render(request,"analyzed.html",params)




