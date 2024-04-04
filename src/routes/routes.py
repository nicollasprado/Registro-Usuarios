from src.controllers.controller import *

routes = {
    "indexRoute": "/", "indexRoute_controller": IndexController.as_view("index"),
    "viewRegisteredRoute": "/verCadastrados", "viewRegistered_controller": ViewRegisteredController.as_view("viewRegistered"),
    "viewRegisteredRouteSearch": "/verCadastrados/search", "viewRegisteredSearch_controller": ViewRegisteredSearchController.as_view("viewRegisteredSearch"),
}