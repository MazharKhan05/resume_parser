from django.shortcuts import render;
import json # will be needed for saving preprocessing details
import numpy as np # for data manipulation
import pandas as pd # for data manipulation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django import forms
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
import string
from tika import parser
from nltk.tokenize import word_tokenize 
from django.http import HttpResponseRedirect
import json
from django.core.paginator import Paginator
import csv
@csrf_protect





def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        uploaded_file_path = fs.path(filename)
        uploaded_file_url = fs.url(filename)
        newResumeTxtFile=open('sample','w',encoding='utf-8')
        resumeFile=uploaded_file_path
        resumeFileData=parser.from_file(resumeFile)
        fileContent = resumeFileData['content']
        fileContent=fileContent.strip()
        fileContent=fileContent.split()
        print(type(fileContent))
        print(len(fileContent))
        n=len(fileContent)
        #ResumeData = []
        #ResumeData.append(fileContent)
        #print(type(fileContent) )
        def email_filtering(fileContent):
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            for i in range(0,n):
                if(re.fullmatch(regex,fileContent[i])):
                    return True
                else:
                    return False
        def linkdn_filtering(fileContent):
            for i in range(0,n):
                print(fileContent[i])
                #p = re.compile('(http(s?)://|[a-zA-Z0-9\-]+\.|[linkedin])[linkedin/~\-]+\.[a-zA-Z0-9/~\-_,&=\?\.;]+[^\.,\s<]')
                if(fileContent[i].startswith("linkedin.com")):
                    return True
                else:
                    return False
                   
        print(email_filtering(fileContent))
        print(linkdn_filtering(fileContent))
        #newResumeTxtFile.write(fileContent)
        
        #print(ResumeData)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')




