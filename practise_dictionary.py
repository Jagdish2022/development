# dict = {
# 1: 'Jagdish',
# 2:  'Ramesh',
# 3:  'Rohit'
# }

# print(dict)
# print(dict[3])
# print(dict.get(2))

# for key, value in dict.items():
#     if key == 1:
#         print(value)

dics = {
'Sunil Kumar': {
    "Father_name": 'Ramesh Kumar',
    "Age":  35,
    "Gender": "M"
},
'Kamal Kumar': {
    "Father_name": 'Bimlesh Kumar',
    "Age":  22,
    "Gender": "M"
},

'Vinod Kumar':{
    "Father_name": 'Kala Kumar',
    "Age":  32,
    "Gender": "M"
    }
}


enter_name = str(input('Please enter the employee name '))

try:
    print(f"{enter_name} father is {dics[enter_name]['Father_name']}")
except:
    print("Sorry ! Please enter the valid name ")


print(dics['Sunil Kumar'])
# print(dics.get(5)['Name'])
# print(dics[5]['Gender'])

##this is the new change that i made to save the new version of repo
##this is the new version
##this is a new version 01/17/2022

##this is a new version 01/17/2022___211