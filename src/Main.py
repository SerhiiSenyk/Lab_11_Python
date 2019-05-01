# -*- coding: utf-8 -*-  

# @author Serhii Senyk
from models.Size import Size
from models.Material import Material 
from models.Board import Board
from models.Calculator import Calculator
from models.Color import Color
from models.Stapler import Stapler
from models.StationeryKnife import StationeryKnife
from models. OfficeAppliance import  OfficeAppliance
from managers.SortType import SortType
from managers.OfficeAppliancesManager import OfficeAppliancesManager

def print_list(list):
    for  item in list: 
        print(item)

def main():
    board = Board(price = 250,
                  color = Color(128,128,128),
                  weight = 25.5,
                  producer = "Economix",
                  material = Material.METAL,
                  surface = "chalky",
                  size_of_surface = Size(150, 7.5, 100),
                  type_of_frame  = "aluminium")
    calculator = Calculator(price = 300,
                  color = Color(128, 0, 128),
                  weight = 0.2,
                  producer = "Intel",
                  material = Material.PLASTIC,
                  type = "engineering",
                  bit_size = 32,
                  corpus_size = Size(10.0, 5.0, 0.5))
    stapler = Stapler(price = 25.5,
                  color = Color(256, 128, 256),
                  weight = 1.2,
                  producer = "Buromax",
                  material = Material.METAL_PLUS_PLASTIC,
                  staples_size = 0.7,
                  power = 25)
    stationery_knife = StationeryKnife(price = 55.0,
                  color = Color(128, 128, 128),
                  weight = 0.5,
                  producer = "ABC",
                  material = Material.METAL,
                  width_of_blade = 10.8)
    office_appliances = list()
    office_appliances.append(board)
    office_appliances.append(calculator)
    office_appliances.append(stapler)
    office_appliances.append(stationery_knife)
    manager = OfficeAppliancesManager(office_appliances)
    print("List :\n")
    print_list(office_appliances)

    color = Color(red = 128, green = 128, blue = 128)
    print("Selection by color" + str(color))
    print_list(manager.find_by_color(color))

    print("Sort by ascending by price\n")
    manager.sort_by_price(office_appliances,SortType.ASCENDING)
    print_list(office_appliances)

    print("Sort by descending by price\n")
    manager.sort_by_price(office_appliances,SortType.DESCENDING)
    print_list(office_appliances)

    print("Sort by ascending by weight\n")
    manager.sort_by_weight(office_appliances,SortType.ASCENDING)
    print_list(office_appliances)

    print("Sort descending by weight\n")
    manager.sort_by_weight(office_appliances,SortType.DESCENDING)
    print_list(office_appliances)

main()