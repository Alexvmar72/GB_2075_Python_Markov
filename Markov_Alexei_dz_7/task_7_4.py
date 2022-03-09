import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(BASE_DIR, 'some_data')

lght_10 = 0
lght_100 = 0
lght_1000 = 0
lght_10000 = 0
lght_100000 = 0
lght_1000000 = 0

dict_out = {10: lght_10, 100: lght_100, 1000: lght_1000, 10000: lght_10000, 100000: lght_100000, 1000000: lght_1000000}

for root, dirs, files in os.walk(folder):
    for file in files:
        if os.stat(os.path.join(root,file)).st_size <= 10:
            lght_10 += 1
            dict_out[10] = lght_10
        if os.stat(os.path.join(root,file)).st_size <= 100 and os.stat(os.path.join(root,file)).st_size > 10:
            lght_100 += 1
            dict_out[100] = lght_100
        if os.stat(os.path.join(root,file)).st_size <= 1000 and os.stat(os.path.join(root,file)).st_size > 100:
            lght_1000 += 1
            dict_out[1000] = lght_1000
        if os.stat(os.path.join(root,file)).st_size <= 10000 and os.stat(os.path.join(root,file)).st_size > 1000:
            lght_10000 += 1
            dict_out[10000] = lght_10000
        if os.stat(os.path.join(root,file)).st_size <= 100000 and os.stat(os.path.join(root,file)).st_size > 10000:
            lght_100000 += 1
            dict_out[100000] = lght_100000
        if os.stat(os.path.join(root,file)).st_size <= 1000000 and os.stat(os.path.join(root,file)).st_size > 100000:
            lght_1000000 += 1
            dict_out[1000000] = lght_1000000

print(dict_out)
