from django.http.response import HttpResponse
from django.shortcuts import render
#Practising pull
# Create your views here.

def index(request):
    display_list=["sourav","sachin","dravid","laxman","sehvag","yuvraj","kumble","agarkar","raina","dhoni","srinath"]
    disp_dict={"key1":"abcd123456","key2":"abcd1234567","key3":"abcd666622"}
    return render(request,"personal_navigator/index.html",{"disp":display_list, "dic":disp_dict})

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc',"off")
    capitalize=request.POST.get('capitalize',"off")
    newlineremover=request.POST.get('newlineremover',"off")
    spaceremover=request.POST.get('extraspaceremover',"off")
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed+=i
        
        print(analyzed)
        params={'purpose':"Remove Punchation",'analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,"personal_navigator/analyze.html",params)
    
    if capitalize=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':"convert into uppercase",'analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,"personal_navigator/analyze.html",params)

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed+=char
        params={'purpose':"Remove New Line",'analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,"personal_navigator/analyze.html",params)
    
    if spaceremover=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):    
                analyzed+=char
        params={'purpose':"Remove New Line",'analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,"personal_navigator/analyze.html",params)
    
    if removepunc!="on" and spaceremover!="on" and newlineremover!="on" and capitalize!="on":
        return HttpResponse("Error page.")

    return render(request,"personal_navigator/analyze.html",params)
    # else:
    #     return HttpResponse("Error")
