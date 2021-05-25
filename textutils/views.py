from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def text_analysis(request):
    # Get the text
    djtext = request.POST.get('text','default')
    remove_punc = request.POST.get('remove_punc','off')
    capitalize = request.POST.get('capitalize','off')
    lower_case = request.POST.get('lower_case','off')
    line_remover = request.POST.get('line_remover','off')
    extra_space_remover = request.POST.get('extra_space_remover','off')
    char_counter = request.POST.get('char_counter','off')

    # Analyze the text
    sp_details = []
    if(remove_punc == 'on'):
        analyzed = ""
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punc:
                analyzed += char
        djtext = analyzed
    if(capitalize == 'on'):
        djtext = djtext.upper()
    if (lower_case == 'on'):
        djtext = djtext.lower()
    if(line_remover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
            # else:
            #     analyzed = analyzed + " "
        djtext = analyzed
    if(extra_space_remover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        djtext = analyzed
    if (char_counter == 'on'):
        l = f"The characters in the text are :- {len(djtext)}"
        sp_details.append(l)
    if(remove_punc=='off' and capitalize=='off' and lower_case=='off' and line_remover=='off' and extra_space_remover=='off' and char_counter=='off'):
        sp_details.append("Hey mate ! you made no change in the text.")
        params = {
            'analyzed_text': djtext,
            'special_details': sp_details
        }
        return render(request, "analyze.html", params)
    if(char_counter == 'on'):
        params = {
            'analyzed_text': djtext,
            'special_details' : sp_details
        }
    else:
        params = {
            'analyzed_text': djtext
        }
    return render(request, "analyze.html", params)

def contactus(request):
    return render(request, 'contactus.html')

def aboutus(request):
    return render(request, 'aboutus.html')
