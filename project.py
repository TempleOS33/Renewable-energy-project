import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("data.csv")
data = data.dropna()
list=[]

def fun3():
    print("hello world")



def fun1():
    x = input("Please input the energy type here: ").lower()
    match x:
        case "roof top pv":
            x = "rooftoppv_gwh"
        case "csp":
            x = "csp_gwh"
        case "on shore wind":
            x = "onshorewind_gwh"
        case "off shore wind":
            x = "offshorewind_gwh"
        case "solid biopower":
            x = "biopowersolid_gwh"
        case "gaseous biopower":
            x = "biopowergaseous_gwh"
        case "geothermal and hydrothermal":
            x = "geothermalhydrothermal_gwh"
        case "enhanced geothermal systems":
            x = "egsgeothermal_gwh"
        case "hydropower":
            x = "hydropower_gwh"
        case "urban utility":
            x = "urbanUtilityScale"
    if x=="onshorewind_gwh":
        for i in data.values:
            list.append(i[12])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[12] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="offshorewind_gwh":
        for i in data.values:
            list.append(i[15])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[15] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="urbanUtilityScale":
        for i in data.values:
            list.append(i[1])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[1] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="rooftoppv_gwh":
        for i in data.values:
            list.append(i[7])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[7] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="csp_gwh":
        for i in data.values:
            list.append(i[9])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[9] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="biopowersolid_gwh":
        for i in data.values:
            list.append(i[18])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[18] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="biopowergaseous_gwh":
        for i in data.values:
            list.append(i[21])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[21] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="geothermalhydrothermal_gwh":
        for i in data.values:
            list.append(i[24])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[24] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="egsgeothermal_gwh":
        for i in data.values:
            list.append(i[26])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[26] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="hydropower_gwh":
        for i in data.values:
            list.append(i[28])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[28] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="geothermalhydrothermal_gwh":
        for i in data.values:
            list.append(i[24])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[24] == a:
                c = i[0]
                print(c, a)
                continue
    elif x == "q":
        print("you exited the program")
    else:
        print("Try again, make sure to get the correct name")

def fun2():
    user_pick_state = input("What state do you want to look at? ")
    search_states_energy = input(f"What energy source do you want to look at in {user_pick_state}? ").lower()
    list=[]
    match search_states_energy :
        case "roof top pv":
            search_states_energy = "rooftoppv_gwh"
        case "csp":
            search_states_energy = "csp_gwh"
        case "on shore wind":
            search_states_energy = "onshorewind_gwh"
        case "off shore wind":
            search_states_energy = "offshorewind_gwh"
        case "solid biopower":
            search_states_energy = "biopowersolid_gwh"
        case "gaseous biopower":
            search_states_energy = "biopowergaseous_gwh"
        case "geothermal and hydrothermal":
            search_states_energy = "geothermalhydrothermal_gwh"
        case "enhanced geothermal systems":
            search_states_energy = "egsgeothermal_gwh"
        case "hydropower":
            search_states_energy = "hydropower_gwh"
        case "urban utility":
            search_states_energy = "urbanUtilityScale"
    for i in data.values:
        if i[0]== user_pick_state:
            if search_states_energy == "onshorewind_gwh":
                print(i[12])
            elif search_states_energy == "offshorewind_gwh":
                print(i[15])
            elif search_states_energy == "urbanUtilityScale":
                print(i[1])
            elif search_states_energy == "rooftoppv_gwh":
                print(i[7])
            elif search_states_energy == "csp_gwh":
                print(i[9])
            elif search_states_energy == "biopowersolid_gwh":
                print(i[18])
            elif search_states_energy == "biopowergaseous_gwh":
                print(i[21])
            elif search_states_energy == "geothermalhydrothermal_gwh":
                print(i[24])
            elif search_states_energy == "egsgeothermal_gwh":
                print(i[26])
            elif search_states_energy == "hydropower_gwh":
                print(i[28])
            else:
                print("Try Again.")

y = input("what function do you want to use?")

if y == "1":
    fun1()

if y == "2":
    fun2()

