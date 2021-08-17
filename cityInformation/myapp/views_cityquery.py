from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from myapp import models

def query(request):
    provinceList=models.Province.objects.all()
    context={"provinceList":provinceList}
    return(render(request,"myapp/queryPage.html",context))

def from_province_get_city(request,provinceId=1):
    provinceList=models.Province.objects.filter(Id=provinceId)
    cityList=models.City.objects.filter(ProvinceId=provinceList[0].Id)

    cityData=[]
    for ob in cityList:
        cityData.append({"cityId":ob.Id,"cityName":ob.Name})

    #return(JsonResponse({'data':data}))
    return(JsonResponse({"provinceData":{"provinceId":provinceList[0].Id,"provinceName":provinceList[0].Name},"cityData":cityData}))

def from_city_get_district(request,cityId=1):
    cityList=models.City.objects.filter(Id=cityId)
    districtList=models.District.objects.filter(CityId=cityList[0].Id)

    districtData=[]
    for ob in districtList:
        districtData.append({"districtId":ob.Id,"districtName":ob.Name})

    return(JsonResponse({"cityData":{"cityId":cityList[0].Id,"cityName":cityList[0].Name},"districtData":districtData}))