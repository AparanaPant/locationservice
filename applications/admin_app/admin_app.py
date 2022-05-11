from flask import Blueprint
from flask_restful import Api

from applications.admin_app.resources.area_resource import AreaResource
from applications.admin_app.resources.areas_resource import AreasResource
from applications.admin_app.resources.cities_resource import CitiesResource
from applications.admin_app.resources.city_resource import CityResource
from applications.admin_app.resources.province_resource import ProvinceResource
from applications.admin_app.resources.provinces_resource import ProvincesResource, Test

admin_app = Blueprint('admin_app', __name__)
api = Api(admin_app)

api.add_resource(ProvincesResource, "/provinces")
api.add_resource(Test, "/test")
api.add_resource(CitiesResource, "/cities")
api.add_resource(AreasResource, "/areas")
api.add_resource(ProvinceResource, "/province/<province_id>")
api.add_resource(CityResource, "/city/<city_id>")
api.add_resource(AreaResource, "/area/<area_id>")

