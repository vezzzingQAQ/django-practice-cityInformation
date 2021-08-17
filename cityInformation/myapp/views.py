from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    return(render(request,"myapp/index.html"))

def demo1(request):
    context={}
    context["name"]="Meiiing"
    context["a"]=[10,20,30]
    context["stu"]={"name":"Vezz","age":20}
    data=[
        {"name":"xinnas","sex":1,"age":40,"state":0},
        {"name":"huihui","sex":0,"age":12,"state":2},
        {"name":"derder","sex":1,"age":10,"state":1},
        {"name":"sdaihui","sex":0,"age":22,"state":2},
    ]
    context["dlist"]=data
    context["time"]=datetime.now
    context["m1"]=100
    context["m2"]=20
    return(render(request,"myapp/demo1.html",context))

def demo2(request):
    return(render(request,"myapp/demo2.html"))