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
        newResumeTxtFile.write(fileContent)
        lst=re.findall('\S+@\S+',fileContent)
        print(lst)
        def email_filtering(fileContent):
            if(re.findall('\S+@\S+',fileContent)):
                return True
            else:
                return False
        print(email_filtering(fileContent))
        def linkld_filtering(fileContent):
            if(fileContent.find('www.linkedin.com') != -1):
                print ("Contains given substring ")
            else:
                print ("Doesn't contains given substring")
        linkld_filtering(fileContent)
        skillDataset = pd.read_csv(r"D:\Users\sahil\Desktop\Project\SRS\companies_data.csv")
        skills = list(skillDataset['comp_skills'])
        cleanedskillList = [x for x in skills if str(x) != 'nan']
        cleanedskillList = [i.split()[0] for i in skills]
		

        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')




