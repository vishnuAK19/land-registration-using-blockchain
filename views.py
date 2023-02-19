from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
from Block import *
from Blockchain import *
from hashlib import sha256
import os
from django.core.files.storage import FileSystemStorage

blockchain = Blockchain()
if os.path.exists('blockchain_contract.txt'):
    with open('blockchain_contract.txt', 'rb') as fileinput:
        blockchain = pickle.load(fileinput)
    fileinput.close()

def UserCheck(request):
    if request.method == 'POST':
        reg = request.POST.get('t1', False)
        strdata = '<table border=1 align=center width=100%><tr><th><font size="" color="white">Registration ID</th><th><font size="" color="white">Current Owner Name</th><th><font size="" color="white">Land Details</th>'
        strdata+='<th><font size="" color="white">Current Owner Address</th><th><font size="" color="white">Document Submitted</th><th><font size="" color="white">Document No</th><th><font size="" color="white">Existing Owner Name</th>'
        strdata+='<th><font size="" color="white">Existing Owner Address</th><th><font size="" color="white">Existing Owner Phone</th><th><font size="" color="white">Current Owner Phone</th><th><font size="" color="white">Land Picture</th></tr>'
        for i in range(len(blockchain.chain)):
            if i > 0:
                b = blockchain.chain[i]
                data = b.transactions[0]
                arr = data.split("#")
                if arr[0] == reg:
                    strdata+='<tr><td><font size="" color="white">'+arr[0]+'</td>'+'<td><font size="" color="white">'+arr[1]+'</td>'+'<td><font size="" color="white">'+arr[2]+'</td>'+'<td><font size="" color="white">'+arr[3]+'</td>'+'<td><font size="" color="white">'+arr[4]+'</td>'+'<td><font size="" color="white">'+arr[5]+'</td>'
                    strdata+='<td><font size="" color="white">'+arr[6]+'</td>'+'<td><font size="" color="white">'+arr[7]+'</td>'+'<td><font size="" color="white">'+arr[8]+'</td>'+'<td><font size="" color="white">'+arr[9]+'</td>'
                    strdata+='<td><img src=http://127.0.0.1:8000/static/Photo/'+arr[0]+".png height=300 width=300></img></td></tr>"
        context= {'data':strdata}       
        return render(request, 'UserLandSearch.html', context)   

def AdminLandSearch(request):
    if request.method == 'GET':
        strdata = '<table border=1 align=center width=100%><tr><th><font size="" color="white">Registration ID</th><th><font size="" color="white">Current Owner Name</th><th><font size="" color="white">Land Details</th>'
        strdata+='<th><font size="" color="white">Current Owner Address</th><th><font size="" color="white">Document Submitted</th><th><font size="" color="white">Document No</th><th><font size="" color="white">Existing Owner Name</th>'
        strdata+='<th><font size="" color="white">Existing Owner Address</th><th><font size="" color="white">Existing Owner Phone</th><th><font size="" color="white">Current Owner Phone</th><th><font size="" color="white">Land Picture</th></tr>'
        for i in range(len(blockchain.chain)):
            if i > 0:
                b = blockchain.chain[i]
                data = b.transactions[0]
                arr = data.split("#")
                strdata+='<tr><td><font size="" color="white">'+arr[0]+'</td>'+'<td><font size="" color="white">'+arr[1]+'</td>'+'<td><font size="" color="white">'+arr[2]+'</td>'+'<td><font size="" color="white">'+arr[3]+'</td>'+'<td><font size="" color="white">'+arr[4]+'</td>'+'<td><font size="" color="white">'+arr[5]+'</td>'
                strdata+='<td><font size="" color="white">'+arr[6]+'</td>'+'<td><font size="" color="white">'+arr[7]+'</td>'+'<td><font size="" color="white">'+arr[8]+'</td>'+'<td><font size="" color="white">'+arr[9]+'</td>'
                strdata+='<td><img src=http://127.0.0.1:8000/static/Photo/'+arr[0]+".png height=300 width=300></img></td></tr>"
        context= {'data':strdata}       
        return render(request, 'AdminLandSearch.html', context)    

def RegisterLand(request):
    if request.method == 'GET':
       return render(request, 'RegisterLand.html', {})

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def User(request):
    if request.method == 'GET':
       return render(request, 'User.html', {})


def Admin(request):
    if request.method == 'GET':
       return render(request, 'Admin.html', {})

def AdminLogin(request):
    if request.method == 'POST':
      username = request.POST.get('username', False)
      password = request.POST.get('password', False)
      if username == 'admin' and password == 'admin':
       context= {'data':'welcome '+username}
       return render(request, 'AdminScreen.html', context)
      else:
       context= {'data':'login failed'}
       return render(request, 'Admin.html', context)

def RegisterLandAction(request):
    if request.method == 'POST' and request.FILES['t10']:
      oname = request.POST.get('t1', False)
      ldetails = request.POST.get('t2', False)
      oaddress = request.POST.get('t3', False)
      document = request.POST.get('t4', False)
      documentno = request.POST.get('t5', False)
      ename = request.POST.get('t6', False)
      eaddress = request.POST.get('t7', False)
      ephone = request.POST.get('t8', False)
      cphone = request.POST.get('t9', False)
      myfile = request.FILES['t10']
      fs = FileSystemStorage()
      file_id = len(blockchain.chain) + 1
      file_id = file_id + 6213
      filename = fs.save("C:/Python/LandRealState/RealStateApp/static/Photo/"+'Tel_'+str(file_id)+".png", myfile)
      details = 'Tel_'+str(file_id)+"#"+oname+"#"+ldetails+"#"+oaddress+"#"+document+"#"+documentno+"#"+ename+"#"+eaddress+"#"+ephone+"#"+cphone
      blockchain.add_new_transaction(details)
      hash = blockchain.mine()
      b = blockchain.chain[len(blockchain.chain)-1]
      output = "Land Registration No : "+'Tel_'+str(file_id)+"</br>Blockchain Previous Hash : "+str(b.previous_hash)+"</br>Block No : "+str(b.index)+"</br>Current Hash : "+str(b.hash)
      blockchain.save_object(blockchain,'blockchain_contract.txt')
      context= {'data':output}
      return render(request, 'RegisterLand.html', context)



    
