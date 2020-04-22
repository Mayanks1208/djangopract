# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')


    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    # fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # charcounter = request.POST.get('charcounter', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' :'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analized.html', params)
    if(fullcaps=="on"):
        analyze=""
        for char in djtext:
            analyze = analyze + char.upper()

        params = {'purpose': 'FULL CAPS', 'analyzed_text': analyze}
        djtext = analyzed
        # return render(request, 'analized.html', params)

    if (newlineremover == "on"):
        analyze = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyze = analyze + char


        params = {'purpose': 'New Line remover', 'analyzed_text': analyze}
        djtext = analyzed
        # return render(request, 'analized.html', params)

    if (extraspaceremover=="on"):
        analyze = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]  ==" " and djtext[index+1] ==" "):
                analyze = analyze + char


        params = {'purpose': 'extraspaceremover', 'analyzed_text': analyze}
        # djtext = analyzed
        # return render(request, 'analized.html', params)

    if (removepunc !="on" and newlineremover !="on" and extraspaceremover!="on" and fullcaps !="on"):
        return HttpResponse("please select any one operator!")

    return render(request, 'analized.html', params)
    # elif  (charcounter=="on"):
    #     analyze = ""
    #     for  char in djtext:
    #         analyze = len(djtext)
    #
    #
    #     params = {'purpose': 'charcounter', 'analyzed_text': analyze}
    #     return render(request, 'analized.html', params)
    #
    #
    # else:
    #     return HttpResponse("Error")


# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")



