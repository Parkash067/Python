result = []
_dic = {}
inventory_logs = [
    {'item_code':101, 'item_name':'Keypad', 'sale_count':10, 'purchase_count':0},
    {'item_code':102, 'item_name':'Smoke Detector', 'sale_count':0, 'purchase_count':10},
    {'item_code':103, 'item_name':'Door Contact', 'sale_count':5, 'purchase_count':0},
    {'item_code':104, 'item_name':'Flush Mount', 'sale_count':25, 'purchase_count':0},
    {'item_code':105, 'item_name':'DSC', 'sale_count':0, 'purchase_count':100}
]

remaining_count = [
    {'item_code': 101, 'remain':50, 'item_name':'Keypad'},
    {'item_code': 102, 'remain':60, 'item_name':'Smoke Detector'},
    {'item_code': 103, 'remain':17, 'item_name':'Door Contact'},
    {'item_code': 104, 'remain':80, 'item_name':'Flush Mount'},
    {'item_code': 105, 'remain':70, 'item_name':'DSC'},
    {'item_code': 106, 'remain':25, 'item_name':'Smart Lock'},
    {'item_code': 107, 'remain':49, 'item_name':'Alexa'},
    {'item_code': 108, 'remain':55, 'item_name':'Philips Hue'},
    {'item_code': 109, 'remain':63, 'item_name':'Google Assistant'},
    {'item_code': 110, 'remain':74, 'item_name':'Motion Sensor'},
]

for remain in remaining_count:
    for count in inventory_logs:
        if remain['item_code'] == count['item_code']:
            result.append(
                {'item_code': count['item_code'],
                 'item_name': count['item_name'],
                 'opening': remain['remain'],
                 'sale_count': count['sale_count'],
                 'purchase_count': count['purchase_count'],
                 'sale_return':0,
                 'purchase_return':0,
                 'total': remain['remain'] - count['sale_count'] + count['purchase_count'],
                 })

for i in result:
    print str(i['item_code'])+"\t"+i['item_name']+"\t"+str(i['opening'])+"\t"+str(i['sale_count'])+\
          "\t"+str(i['purchase_count'])+"\t"+str(i['sale_return'])+"\t"+str(i['purchase_return'])+"\t"+str(i['total'])



