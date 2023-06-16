from django.shortcuts import render
from django.http import JsonResponse
import os, openai


#openai.organization = "org-9ge91FBt6iMFTVNwLvML94f2"
openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(   
        model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}],
                max_tokens=2500,
                n=1,
                stop=None,
                temperature=0.0,
        
    )
    
    answer = response.choices[0].message.content.strip()
    return answer



# Create your views here.
def chats(request):
   
    if request.method == 'POST':
        message =request.POST.get("message")
        response = ask_openai(message)
        
        return JsonResponse({"message":message, "response": response})

    
    
    return render(request, "chat/index.html")
