from django.urls import path
from myapp import views
from myapp import views_cityquery

urlpatterns = [
    path("",views.index,name="index"),#首页
    path("demo1",views.demo1,name="demo1"),#模板语法测试
    path("demo2",views.demo2,name="demo2"),#模板继承测试

    path("queryPage",views_cityquery.query,name="querypage"),
    path("queryCity/<int:provinceId>",views_cityquery.from_province_get_city,name="querycity"),#Ajax加载城市信息
    path("queryDistrict/<int:cityId>",views_cityquery.from_city_get_district,name="querydistrict"),#Ajax加载城市信息
]
