logo='''
╔╦╗╔═╗╔╦╗╔═╗╔═╗╦═╗╔═╗╔╦╗╦ ╦╦═╗╔═╗╔═╗
 ║ ║╣ ║║║╠═╝║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝╠═╣╚═╗
 ╩ ╚═╝╩ ╩╩  ╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═╩ ╩╚═╝
'''
print(logo)
for c in range(0,101,10):
    celsius=c
    fahrenheit=c*1.8+32
    print(f'   {celsius}\t\t{fahrenheit}   ')