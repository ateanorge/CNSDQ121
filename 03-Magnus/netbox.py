import requests
import json

#netbox vars
netbox_token = ""
baseUrl = "http://192.168.111.39:8000/api/"

#dcim
sites = {}
racks = {}
manufacturers = {}
deviceTypes = {}
devices = {}
deviceRoles = {}

#Virtualization
clusterTypes = {}
clusters = {}
vms = {}




#headers
headers = {
      'Accept': 'application/json',
      'Authorization': 'Token '+netbox_token,
      'Content-Type': 'application/json',
    }

def getList(dict): 
    return list(dict.keys()) 

def get_netbox_sites():
    urn = "dcim/sites/"

    get_sites = requests.get(baseUrl+urn, headers=headers).json()

    for site in get_sites["results"]:
        sites[site["name"]] = site["id"]

def get_netbox_racks():
    urn = "dcim/racks/"

    get_racks = requests.get(baseUrl+urn, headers=headers).json()

    #print(get_racks)
    for site in get_racks["results"]:
        racks[site["name"]] = site["id"]

def get_netbox_manufacturers():
    urn = "dcim/manufacturers/"

    get_manufacturers = requests.get(baseUrl+urn, headers=headers).json()

    #print(get_manufacturers)
    for manufacturer in get_manufacturers["results"]:
        manufacturers[manufacturer["name"]] = manufacturer["id"]



def get_netbox_deviceRoles():
    urn = "dcim/device-roles/"

    get_deviceRoles = requests.get(baseUrl+urn, headers=headers).json()

    #print(get_manufacturers)
    for deviceRole in get_deviceRoles["results"]:
        deviceRoles[deviceRole["name"]] = deviceRole["id"]
  
def get_netbox_devices():
    urn = "dcim/devices/"

    get_devices = requests.get(baseUrl+urn, headers=headers).json()

    for device in get_devices["results"]:
        devices[device["name"]] = device["id"]

def get_netbox_deviceTypes():
    urn = "dcim/device-types/"
    get_deviceTypes = requests.get(baseUrl+urn, headers=headers).json()
    #deviceTypes = {}
    for  x in list(manufacturers.keys()):
        deviceTypes[x] = []
    
    listOfDevices = []
    for deviceType in get_deviceTypes["results"]:
        device_manufacturer = deviceType["manufacturer"]["name"]
        devicDict = {}
        devicDict[deviceType["model"]]= deviceType["id"]
        deviceTypes[device_manufacturer].append(devicDict)
        

def get_clusterTypes():
    urn = "virtualization/cluster-types/"

    get_clusterTypes = requests.get(baseUrl+urn, headers=headers).json()

    for clusterType in get_clusterTypes["results"]:
        clusterTypes[clusterType["name"]] = clusterType["id"]

def get_clusters():
    urn = "virtualization/clusters/"

    get_clusters = requests.get(baseUrl+urn, headers=headers).json()

    for cluster in get_clusters["results"]:
        clusters[cluster["name"]] = cluster["id"]

def get_vms():
    urn = "virtualization/virtual-machines/"

    get_vms = requests.get(baseUrl+urn, headers=headers).json()

    for vm in get_vms["results"]:
        vms[vm["name"]] = vm["id"]

#print(sites)
#print(racks)
#print(manufacturers)
#print(deviceTypes)
#print(devices)
#print(deviceRoles)


#//////////////// User input \\\\\\\\\\\\\\\\\\\\\

def netboxApp():
    get_netbox_sites()
    get_netbox_racks()
    get_netbox_manufacturers()
    get_netbox_deviceRoles()
    get_netbox_devices()
    get_netbox_deviceTypes()
    get_clusterTypes()
    get_clusters()
    get_vms()


    #print(sites)
    #print(racks)
    #print(manufacturers)
    #print(deviceTypes)
    #print(devices)
    #print(deviceRoles)
    #print(clusterTypes)
    #print(clusters)
    #print(vms)


    print("---------Welcom to my Nextbox APP----------")
    print("What do you wanna do?")
    print("1) Add a device to Netbox?")
    print("2) Add a deviceType to Netbox?")
    print("3) Add a deviceRole to Netbox?")
    print("4) Add a manufacturer to Netbox?")
    print("5) import devices via CSV file")
    print("10) Set vmware vcenter settings")
    print("11) import vmware cluster")
    print("12) import vmware VM's")



    tasks = input("number: ")

    if tasks == "1":
        add_device()
    elif tasks == "2":
        print("this funcsion is to ready jet")
        netboxApp()
    elif tasks == "3":
        print("this funcsion is to ready jet")
        netboxApp()
    elif tasks == "4":
        print("this funcsion is to ready jet")
        netboxApp()
    elif tasks == "5":
        print("this funcsion is to ready jet")
        netboxApp()
    elif tasks == "10":
        print("this funcsion is to ready jet")
        netboxApp()
    elif tasks == "11":
        select_clusterTypes()
        print("this funcsion is to ready jet")
        netboxApp()
    elif tasks == "12":
        print("this funcsion is to ready jet")
        netboxApp()

    else:
        print("not a vaild input or featcure not ready jet")
        netboxApp()

def select_manufacturer():
    print("Select manufacturer:")
    counter = 0
    for manufacturer in getList(manufacturers):
        print(str(counter) +") " +manufacturer)
        counter +=1 
    print("x) add new manufacturer \nq) to quit")
    user_select_manufacturer = input("number: ")
    if user_select_manufacturer.isnumeric():
        #res = {list(manufacturers.keys())[int(user_select_manufacturer)]: manufacturers[list(manufacturers.keys())[int(user_select_manufacturer)]]}
        res = list(manufacturers.keys())[int(user_select_manufacturer)]
        return res
    elif user_select_manufacturer.lower() == "x":
        new_manufacturer_name = make_netbox_manufacturers()
        get_netbox_manufacturers()
        return new_manufacturer_name
    elif user_select_manufacturer.lower() == "q":
        netboxApp()
    else:
        print("selectet invalid input")


def select_deviceTypes(selected_manufacturer):
    print("Select model:")
    counter = 0
    #print(deviceTypes[selected_manufacturer])
    if len(deviceTypes[selected_manufacturer]) != 0:
        for deviceType in deviceTypes[selected_manufacturer]:
            print(str(counter) + ") "+ list(deviceType.keys())[0])
            counter +=1

    print("x) add new model \nq) to quit")

    user_select_model = input("number: ")
    if user_select_model.isnumeric():
        #print("a model was selectet")
        #res = deviceType
        res = next(iter(deviceType.values()))
        return res
    elif user_select_model.lower() == "x":
        new_device_id = make_netbox_deviceTypes(selected_manufacturer)
        get_netbox_manufacturers()
        return new_device_id
    elif user_select_model.lower() == "q":
        netboxApp()
    else:
        print("invalid input")

def select_deviceRoles():
    print("Select device role")
    counter = 0
    for deviceRole in deviceRoles:
        #print(deviceRole)
        print(str(counter) + ") "+ deviceRole)
        counter +=1
    print("x) add new role \nq) to quit")
    user_select_model = input("number: ")
    if user_select_model.isnumeric():
        print(list(deviceRoles.keys())[int(user_select_model)])
        return deviceRoles[list(deviceRoles.keys())[int(user_select_model)]] 
    elif user_select_model.lower() == "x":
        pass
    elif user_select_model.lower() == "q":
        netboxApp()
    else:
        print("invalid input")


def select_clusterTypes():
    print("Select cluster types:")
    counter = 0
    for clusterType in getList(clusterTypes):
        print(str(counter) +") " +clusterType)
        counter +=1 
    print("x) add new cluster types \nq) to quit")
    user_select_clusterTypes = input("number: ")
    if user_select_clusterTypes.isnumeric():
        #res = {list(manufacturers.keys())[int(user_select_manufacturer)]: manufacturers[list(manufacturers.keys())[int(user_select_manufacturer)]]}
        res = list(clusterTypes.keys())[int(user_select_clusterTypes)]
        return res
    elif user_select_clusterTypes.lower() == "x":
        pass
        #new_manufacturer_name = make_netbox_manufacturers()
        #get_netbox_manufacturers()
        #return new_manufacturer_name
    elif user_select_clusterTypes.lower() == "q":
        netboxApp()
    else:
        print("selectet invalid input")




#////// Add stuff to netbox

def make_netbox_manufacturers():
    urn = "dcim/manufacturers/"

    #template
    inputData = {
        "manufacturer": "",
        "slug":""
        }

    name = input("Name of manufacturer: ")
    inputData["name"] = name
    inputData["slug"] = name.replace(" ","-").lower()

    payload = json.dumps(inputData)

    make_manufacturers = requests.post(baseUrl+urn, headers=headers, data = payload).json()
    return make_manufacturers["name"]
    #print(make_manufacturers)



def make_netbox_deviceTypes(manufacturer_id):
    urn = "dcim/device-types/"

    if manufacturer_id.isnumeric() == False:
        manufacturer_id = manufacturers[manufacturer_id]
    #template
    inputData = {
        "manufacturer": manufacturer_id,
        "model": "", 
        "slug":"",
        "u_height": "",
        "is_full_depth": None,

        }

    model = input("Enter model: ")
    inputData["model"] = model
    inputData["slug"] = model.replace(" ","-").lower()
    inputData["u_height"] = input("How many unit is the model: ")
    face = input("Is the model full depth? Y/N: ")
    if face.lower() == "y":
        inputData["is_full_depth"] = True
    else:
        inputData["is_full_depth"] = False

    payload = json.dumps(inputData)

    make_deviceTypes = requests.post(baseUrl+urn, headers=headers, data = payload).json()
    return make_deviceTypes["id"]

#make_netbox_deviceTypes("1")
#print(make_netbox_deviceTypes("HP"))
#make_netbox_deviceTypes("2","DL560",2,True)

def add_device():
    urn = "dcim/devices/"
    
    #template
    inputData = {"name": "",
    "device_type": "", 
    "device_role": "", 
    "site":"1",
    "rack": "1",
    "position": "",
    "face": ""}


    #updated template with usefull data
    inputData["name"] = input("Enter device name: ")
    print("")
    inputData["device_role"] = select_deviceRoles()
    print("")
    inputData["device_type"] = select_deviceTypes(select_manufacturer())
    print("")
    inputData["position"] = input("Enter the lowest rack position: ")
    face = input("Rack face front? Y/N: ")
    if face.lower() == "y":
        inputData["face"] = "front"
    else:
        inputData["face"] = "rear"


    payload = json.dumps(inputData)
    add_device = requests.post(baseUrl+urn, headers=headers, data = payload).json()
    print(add_device)
    netboxApp()
    

netboxApp()
