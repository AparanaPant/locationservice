import json
import os
import time

import requests

daraz_url = "https://member.daraz.com.np/locationtree/api/getSubAddressList?countryCode=NP"


def get_province():
    response = requests.get(daraz_url)
    provinces = response.json().get('module')
    for province in provinces:
        get_cities_for_each_province(province.get('id'))
        province.pop("isSupportDgCod")
        province.pop("parentId")
        province.pop("name")
        province['reference_id'] = province.pop('id')
    with open('provinces.txt', 'w') as f:
        json.dump(provinces, f, ensure_ascii=False)


def get_cities_for_each_province(province_id):
    time.sleep(120)
    response = requests.get(f"{daraz_url}&addressId={province_id}")
    cities = response.json().get('module')
    for city in cities:
        get_areas_for_each_city(city.get('id'))
        city.pop("isSupportDgCod")
        city.pop("name")
        city['reference_id'] = city.pop('id')
        create_or_append('cities.txt', city)


def get_areas_for_each_city(city_id):
    time.sleep(60)
    response = requests.get(f"{daraz_url}&addressId={city_id}")
    areas = response.json().get('module')
    for area in areas:
        area.pop("isSupportDgCod")
        area.pop("name")
        area['reference_id'] = area.pop('id')
        create_or_append('areas.txt', area)


def create_or_append(path, data):
    if not os.path.exists(path):
        with open(path, 'w') as f:
            json.dump([data], f, ensure_ascii=False)
    else:
        json_data = json.load(open(path))
        json_data.append(data)
        with open(path, 'w') as f:
            json.dump(json_data, f, ensure_ascii=False)


get_province()
