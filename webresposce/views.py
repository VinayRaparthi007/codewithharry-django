from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount=request.POST.get('charcount','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Capatalized Text", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if(charcount == "on"):
        analyzed= djtext
        count = 0
        for char in djtext:
            count = count + 1
        
        params = {'purpose': 'Charector Count', 'analyzed_text': analyzed,'number': count}
       
        # return render(request, 'analyze.html', params) 
    if(removepunc != 'on' and fullcaps != 'on' and extraspaceremover != 'on' and newlineremover != 'on' and charcount !='on'):
        return HttpResponse('<h1>please select any operation Brother</h1>') 

    return render(request, 'analyze.html', params)
    

def bootstrap(request):
    return render(request,"index.html")