import pickle

pth = '/PATH/TO/YOUR/FOLDER/'  # Has to be defined because of debug bug
def save_pickle(file, data1):
    if '.pkl' not in file:
        file += '.pkl'
    pkl_file = open(pth + file, 'wb')
    pickle.dump(data1, pkl_file)
    pkl_file.close()

def load_pickle(fl_nm):
    if '.pkl' not in fl_nm:
        fl_nm += '.pkl'
    try:
        pkl_file = open(pth + fl_nm, 'rb')
        data1 = pickle.load(pkl_file)
        pkl_file.close()
    except:
        print('Missing pickle table:', fl_nm)
        # pkl_file = open(file, 'wb')
        data1 = ''
    return data1

def enc_decr(f1, f11, f2, ms):
    valid_key = False
    e_ms = [(x**f1)%f2 for x in ms]
    # print(ms**f1)
    # print(e_ms)
    d_ms = [(x**f11)%f2 for x in e_ms]
    # print(e_ms**f11)
    # print(d_ms)   
    if d_ms == ms and e_ms != ms:
        e_ms = [(x**f11)%f2 for x in ms]
        d_ms = [(x**f1)%f2 for x in e_ms]
        if d_ms == ms and e_ms != ms:
            valid_key = True
    return valid_key


def encr(f1, f11, f2, ms):
    e_ms = [(x**f1)%f2 for x in ms]
    d_ms = [(x**f11)%f2 for x in e_ms]
    e_ms2 = [(x**f11)%f2 for x in ms]
    d_ms2 = [(x**f1)%f2 for x in e_ms2]
    print(e_ms, d_ms, e_ms2, d_ms2)


def decr(f1, f11, f2, ms):
    e_ms = [(x**f1)%f2 for x in ms]
    d_ms = [(x**f11)%f2 for x in ms]

    
def enc_decr_other_key(f1, f11, f2, ms, g1, g11, g2):   
    e_ms = [(x**f1)%f2 for x in ms]
    if [(x**g1)%g2 for x in e_ms] == ms:
        return True
    print(e_ms, d_ms)
    if [(x**g11)%g2 for x in e_ms] == ms:
        return True
    
    e2_ms = [(x**f11)%f2 for x in ms]
    if [(x**g1)%g2 for x in e2_ms] == ms:
        return True
    if [(x**g11)%g2 for x in e2_ms] == ms:
        return True

    return False
       
    
keys = []
x = 100
option = 1
if option == 1:
    # create key pairs
    for i0 in range(2, x):
        for i1 in range(i0+1, x):
            for i2 in range(2, i0*i1):
                if enc_decr(i0, i1, i2, [1,2,3,4,5]):
                    print(i0, i1, i2)
                    keys.append([i0, i1, i2])
                    # print(keys)
                    # exit()
    save_pickle('keys4', keys)

elif option == 2:
    # Look for keys which can open it
    dec_keys = {}
    keys = load_pickle('keys4')
    for i in range(len(keys)):
        for j in range(1): #  range(i+1, len(keys)):
            k = keys[i]
            uk = [77, 83, 19] # keys[j] 
            dec_failed = False
            if enc_decr_other_key(k[0], k[1], k[2], [1,2,3,4,5], uk[0], uk[1], uk[2]):
                if str(k) not in dec_keys:
                    dec_keys[str(k)] = [uk]
                else:
                    dec_keys[str(k)].append(uk)
        if i % 100 == 0:
            print(i, len(keys))
    save_pickle('dec_keysfff', dec_keys)

elif option == 3:
    # Count which keys are most succesfull
    dec_keys = load_pickle('dec_keys4')
    # print(len(dec_keys))
    keys_counter = {}
    i = 0
    for key in dec_keys:
        i+=1
        for key2 in dec_keys[key]:
            if str(key2) not in keys_counter:
                keys_counter[str(key2)] = 1
            else:
                keys_counter[str(key2)] += 1
        if i % 100 == 0:
            print(i)

    save_pickle('keys_counter4', keys_counter)

elif option == 4:
    # Print most succesfull keys
    keys_counter = load_pickle('keys_counter4')
    key_list = []
    for key2 in keys_counter:
        key_list.append((keys_counter[key2], key2))
    key_list.sort()
    for key in key_list:
        if ', 6]' not in key[1]:
            print(key)

elif option == 5:
    # 4064, '[83, 87, 66]'
    # Get keys which can be opened by this key
    
    dec_keys = load_pickle('dec_keys3')
    i = 0
    for key in dec_keys:
        if [83, 87, 66] in dec_keys[key]:
            i+=1
            if i%8 == 0:
                print(key)
            else:
                print(key, end = '    ')

    # print(keys)

elif option == 6:
    # encr(83, 95, 5187, [1,2,3,4,5])
    encr(11, 23, 57, [1,2,3,4,5])
    # encr(83, 87, 66, [1,2,3,4,5])
    # decr(77, 83, 19, [1, 53, 48, 16, 44])
    decr(41, 65, 114, [1, 53, 48, 16, 44])

    # [83, 95, 5187], [83, 95, 5567], [83, 95, 6213], [83, 95, 7030], [83, 95, 7410],[77, 83, 19]

elif option == 7:

    # Look for keys which can open it
    dec_keys = {}
    # dec_keys = load_pickle('dec_keysfff')
    # for key in dec_keys:
    #     print(key, end=', ')
    # exit()
    keys = [[5, 11, 19], [5, 11, 38], [5, 29, 19], [5, 29, 38], [5, 29, 57], [5, 29, 95], [5, 29, 114], [5, 29, 133], [5, 47, 19], [5, 47, 38], [5, 47, 57], [5, 47, 114], [5, 47, 133], [5, 65, 19], [5, 65, 38], [5, 65, 57], [5, 65, 95], [5, 65, 114], [5, 65, 133], [5, 65, 190], [5, 65, 247], [5, 65, 266], [5, 65, 285], [5, 83, 19], [5, 83, 38], [5, 83, 57], [5, 83, 114], [5, 83, 133], [5, 83, 266], [5, 83, 399], [11, 23, 19], [11, 23, 38], [11, 23, 57], [11, 23, 95], [11, 23, 114], [11, 23, 133], [11, 23, 190], [11, 23, 247], [11, 41, 19], [11, 41, 38], [11, 41, 57], [11, 41, 114], [11, 41, 133], [11, 41, 209], [11, 41, 266], [11, 41, 399], [11, 41, 418], [11, 59, 19], [11, 59, 38], [11, 59, 57], [11, 59, 95], [11, 59, 114], [11, 59, 133], [11, 59, 190], [11, 59, 247], [11, 59, 266], [11, 59, 285], [11, 59, 399], [11, 59, 494], [11, 59, 570], [11, 77, 19], [11, 77, 38], [11, 77, 57], [11, 77, 114], [11, 77, 133], [11, 77, 266], [11, 77, 399], [11, 77, 798], [11, 95, 19], [11, 95, 38], [11, 95, 57], [11, 95, 95], [11, 95, 114], [11, 95, 133], [11, 95, 190], [11, 95, 247], [11, 95, 266], [11, 95, 285], [11, 95, 399], [11, 95, 494], [11, 95, 570], [11, 95, 665], [11, 95, 703], [11, 95, 741], [11, 95, 798], [23, 29, 19], [23, 29, 38], [23, 29, 57], [23, 29, 114], [23, 29, 133], [23, 29, 266], [23, 29, 399], [23, 47, 19], [23, 47, 38], [23, 47, 57], [23, 47, 95], [23, 47, 114], [23, 47, 133], [23, 47, 190], [23, 47, 209], [23, 47, 247], [23, 47, 266], [23, 47, 285], [23, 47, 399], [23, 47, 418], [23, 47, 494], [23, 47, 570], [23, 47, 589], [23, 47, 627], [23, 47, 665], [23, 47, 703], [23, 47, 741], [23, 47, 779], [23, 47, 798], [23, 47, 1045], [23, 65, 19], [23, 65, 38], [23, 65, 57], [23, 65, 114], [23, 65, 133], [23, 65, 266], [23, 65, 399], [23, 65, 798], [23, 83, 19], [23, 83, 38], [23, 83, 57], [23, 83, 95], [23, 83, 114], [23, 83, 133], [23, 83, 190], [23, 83, 247], [23, 83, 266], [23, 83, 285], [23, 83, 399], [23, 83, 494], [23, 83, 570], [23, 83, 665], [23, 83, 703], [23, 83, 741], [23, 83, 798], [23, 83, 1235], [23, 83, 1330], [23, 83, 1406], [23, 83, 1482], [23, 83, 1729], [29, 41, 19], [29, 41, 38], [29, 41, 57], [29, 41, 95], [29, 41, 114], [29, 41, 133], [29, 41, 190], [29, 41, 247], [29, 41, 266], [29, 41, 285], [29, 41, 399], [29, 41, 437], [29, 41, 494], [29, 41, 570], [29, 41, 665], [29, 41, 703], [29, 41, 741], [29, 41, 798], [29, 41, 874], [29, 59, 19], [29, 59, 38], [29, 59, 57], [29, 59, 114], [29, 59, 133], [29, 59, 209], [29, 59, 266], [29, 59, 361], [29, 59, 399], [29, 59, 418], [29, 59, 589], [29, 59, 627], [29, 59, 722], [29, 59, 798], [29, 59, 1083], [29, 59, 1178], [29, 59, 1254], [29, 59, 1463], [29, 77, 19], [29, 77, 38], [29, 77, 57], [29, 77, 95], [29, 77, 114], [29, 77, 133], [29, 77, 190], [29, 77, 247], [29, 77, 266], [29, 77, 285], [29, 77, 399], [29, 77, 494], [29, 77, 570], [29, 77, 665], [29, 77, 703], [29, 77, 741], [29, 77, 798], [29, 77, 1235], [29, 77, 1330], [29, 77, 1387], [29, 77, 1406], [29, 77, 1482], [29, 77, 1729], [29, 77, 1995], [29, 77, 2109], [29, 95, 19], [29, 95, 38], [29, 95, 57], [29, 95, 114], [29, 95, 133], [29, 95, 266], [29, 95, 399], [29, 95, 798], [29, 95, 1957], [41, 47, 19], [41, 47, 38], [41, 47, 57], [41, 47, 114], [41, 47, 133], [41, 47, 266], [41, 47, 399], [41, 47, 798], [41, 65, 19], [41, 65, 38], [41, 65, 57], [41, 65, 95], [41, 65, 114], [41, 65, 133], [41, 65, 190], [41, 65, 247], [41, 65, 266], [41, 65, 285], [41, 65, 399], [41, 65, 494], [41, 65, 570], [41, 65, 665], [41, 65, 703], [41, 65, 741], [41, 65, 798], [41, 65, 1235], [41, 65, 1330], [41, 65, 1387], [41, 65, 1406], [41, 65, 1482], [41, 65, 1729], [41, 65, 1995], [41, 65, 2109], [41, 65, 2190], [41, 65, 2470], [41, 83, 19], [41, 83, 38], [41, 83, 57], [41, 83, 114], [41, 83, 133], [41, 83, 266], [41, 83, 399], [41, 83, 798], [41, 83, 817], [41, 83, 931], [41, 83, 1634], [41, 83, 1862], [41, 83, 2413], [41, 83, 2451], [41, 83, 2793], [41, 83, 3097], [47, 59, 19], [47, 59, 38], [47, 59, 57], [47, 59, 95], [47, 59, 114], [47, 59, 133], [47, 59, 190], [47, 59, 247], [47, 59, 266], [47, 59, 285], [47, 59, 399], [47, 59, 437], [47, 59, 494], [47, 59, 551], [47, 59, 570], [47, 59, 665], [47, 59, 703], [47, 59, 741], [47, 59, 798], [47, 59, 817], [47, 59, 874], [47, 59, 931], [47, 59, 1102], [47, 59, 1235], [47, 59, 1273], [47, 59, 1311], [47, 59, 1330], [47, 59, 1406], [47, 59, 1482], [47, 59, 1634], [47, 59, 1653], [47, 59, 1729], [47, 59, 1862], [47, 59, 1995], [47, 59, 2109], [47, 59, 2185], [47, 59, 2413], [47, 59, 2451], [47, 59, 2470], [47, 59, 2546], [47, 59, 2622], [47, 59, 2755], [47, 77, 19], [47, 77, 38], [47, 77, 57], [47, 77, 114], [47, 77, 133], [47, 77, 266], [47, 77, 399], [47, 77, 798], [47, 83, 3318], [47, 95, 19], [47, 95, 38], [47, 95, 57], [47, 95, 95], [47, 95, 114], [47, 95, 133], [47, 95, 190], [47, 95, 247], [47, 95, 266], [47, 95, 285], [47, 95, 323], [47, 95, 399], [47, 95, 494], [47, 95, 570], [47, 95, 646], [47, 95, 665], [47, 95, 703], [47, 95, 741], [47, 95, 798], [47, 95, 969], [47, 95, 1235], [47, 95, 1330], [47, 95, 1387], [47, 95, 1406], [47, 95, 1482], [47, 95, 1615], [47, 95, 1729], [47, 95, 1938], [47, 95, 1995], [47, 95, 2109], [47, 95, 2261], [47, 95, 2470], [47, 95, 2774], [47, 95, 3230], [47, 95, 3458], [47, 95, 3515], [47, 95, 3705], [47, 95, 3990], [47, 95, 4161], [47, 95, 4199], [47, 95, 4218], [49, 97, 2382], [53, 77, 3315], [53, 77, 3570], [53, 93, 4094], [59, 65, 19], [59, 65, 38], [59, 65, 57], [59, 65, 114], [59, 65, 133], [59, 65, 266], [59, 65, 399], [59, 65, 798], [59, 83, 19], [59, 83, 38], [59, 83, 57], [59, 83, 95], [59, 83, 114], [59, 83, 133], [59, 83, 190], [59, 83, 247], [59, 83, 266], [59, 83, 285], [59, 83, 323], [59, 83, 399], [59, 83, 494], [59, 83, 570], [59, 83, 646], [59, 83, 665], [59, 83, 703], [59, 83, 741], [59, 83, 798], [59, 83, 969], [59, 83, 1235], [59, 83, 1330], [59, 83, 1387], [59, 83, 1406], [59, 83, 1482], [59, 83, 1615], [59, 83, 1729], [59, 83, 1843], [59, 83, 1938], [59, 83, 1957], [59, 83, 1995], [59, 83, 2109], [59, 83, 2261], [59, 83, 2470], [59, 83, 2603], [59, 83, 2774], [59, 83, 3230], [59, 83, 3458], [59, 83, 3515], [59, 83, 3686], [59, 83, 3705], [59, 83, 3914], [59, 83, 3990], [59, 83, 4161], [59, 83, 4199], [59, 83, 4218], [59, 83, 4522], [59, 83, 4845], [59, 89, 4214], [65, 77, 19], [65, 77, 38], [65, 77, 57], [65, 77, 95], [65, 77, 114], [65, 77, 133], [65, 77, 190], [65, 77, 247], [65, 77, 266], [65, 77, 285], [65, 77, 399], [65, 77, 494], [65, 77, 570], [65, 77, 665], [65, 77, 703], [65, 77, 741], [65, 77, 798], [65, 77, 1235], [65, 77, 1330], [65, 77, 1406], [65, 77, 1482], [65, 77, 1729], [65, 77, 1995], [65, 77, 2109], [65, 77, 2470], [65, 77, 3367], [65, 77, 3458], [65, 77, 3515], [65, 77, 3705], [65, 77, 3885], [65, 77, 3990], [65, 77, 4218], [65, 77, 4810], [65, 77, 4921], [65, 95, 19], [65, 95, 38], [65, 95, 57], [65, 95, 114], [65, 95, 133], [65, 95, 266], [65, 95, 399], [65, 95, 798], [65, 95, 817], [65, 95, 931], [65, 95, 1634], [65, 95, 1862], [65, 95, 2413], [65, 95, 2451], [65, 95, 2793], [65, 95, 4826], [65, 95, 4902], [65, 95, 5586], [65, 95, 5719], [77, 83, 19], [77, 83, 38], [77, 83, 57], [77, 83, 114], [77, 83, 133], [77, 83, 209], [77, 83, 266], [77, 83, 399], [77, 83, 418], [77, 83, 589], [77, 83, 627], [77, 83, 798], [77, 83, 1178], [77, 83, 1254], [77, 83, 1463], [77, 83, 1767], [77, 83, 2926], [77, 83, 3534], [77, 83, 4123], [77, 83, 4389], [83, 95, 19], [83, 95, 38], [83, 95, 57], [83, 95, 95], [83, 95, 114], [83, 95, 133], [83, 95, 190], [83, 95, 247], [83, 95, 266], [83, 95, 285], [83, 95, 399], [83, 95, 494], [83, 95, 570], [83, 95, 665], [83, 95, 703], [83, 95, 741], [83, 95, 798], [83, 95, 1235], [83, 95, 1330], [83, 95, 1406], [83, 95, 1482], [83, 95, 1729], [83, 95, 1995], [83, 95, 2071], [83, 95, 2109], [83, 95, 2470], [83, 95, 3458], [83, 95, 3515], [83, 95, 3705], [83, 95, 3990], [83, 95, 4142], [83, 95, 4218], [83, 95, 4921], [83, 95, 5187], [83, 95, 5567], [83, 95, 6213], [83, 95, 7030], [83, 95, 7410],[77, 83, 19]]
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            k = keys[i]
            uk = keys[j]
            dec_failed = False
            if enc_decr_other_key(k[0], k[1], k[2], [1,2,3,4,5], uk[0], uk[1], uk[2]):
                if str(k) not in dec_keys:
                    dec_keys[str(k)] = [uk]
                else:
                    dec_keys[str(k)].append(uk)
    print(dec_keys)
       

    

# print(len(keys))
# print(keys)
# for key in keys:
##      if not enc_decr(key[0], key[2], key[1], 3):
#        print(key[0], key[2], key[1], False)
#         exit()
#         keys.remove(key)
# print(len(keys))
# save_pickle('keys10', keys)

'''

[[5, 11, 19], [5, 11, 38], 
 [5, 29, 19], [5, 29, 38], [5, 29, 57], [5, 29, 95], [5, 29, 114], [5, 29, 133], 
 [5, 47, 19], [5, 47, 38], [5, 47, 57], [5, 47, 114], [5, 47, 133], 
 [5, 65, 19], [5, 65, 38], [5, 65, 57], [5, 65, 95], [5, 65, 114], [5, 65, 133], [5, 65, 190], [5, 65, 247], [5, 65, 266], [5, 65, 285], 
 [5, 83, 19], [5, 83, 38], [5, 83, 57], [5, 83, 114], [5, 83, 133], [5, 83, 266], [5, 83, 399], 
 [11, 23, 19], [11, 23, 38], [11, 23, 57], [11, 23, 95], [11, 23, 114], [11, 23, 133], [11, 23, 190], [11, 23, 247], 
 [11, 41, 19], [11, 41, 38], [11, 41, 57], [11, 41, 114], [11, 41, 133], [11, 41, 209], [11, 41, 266], [11, 41, 399], [11, 41, 418], 
 [11, 59, 19], [11, 59, 38], [11, 59, 57], [11, 59, 95], [11, 59, 114], [11, 59, 133], [11, 59, 190], [11, 59, 247], [11, 59, 266], [11, 59, 285], [11, 59, 399], [11, 59, 494], [11, 59, 570], 
 [11, 77, 19], [11, 77, 38], [11, 77, 57], [11, 77, 114], [11, 77, 133], [11, 77, 266], [11, 77, 399], [11, 77, 798], 
 [11, 95, 19], [11, 95, 38], [11, 95, 57], [11, 95, 95], [11, 95, 114], [11, 95, 133], [11, 95, 190], [11, 95, 247], [11, 95, 266], [11, 95, 285], [11, 95, 399], [11, 95, 494], [11, 95, 570], [11, 95, 665], [11, 95, 703], [11, 95, 741], [11, 95, 798], 
 [23, 29, 19], [23, 29, 38], [23, 29, 57], [23, 29, 114], [23, 29, 133], [23, 29, 266], [23, 29, 399], [23, 47, 19], [23, 47, 38], [23, 47, 57], [23, 47, 95], [23, 47, 114], [23, 47, 133], [23, 47, 190], [23, 47, 209], [23, 47, 247], [23, 47, 266], [23, 47, 285], [23, 47, 399], [23, 47, 418], [23, 47, 494], [23, 47, 570], [23, 47, 589], [23, 47, 627], [23, 47, 665], [23, 47, 703], [23, 47, 741], [23, 47, 779], [23, 47, 798], [23, 47, 1045], 
 [23, 65, 19], [23, 65, 38], [23, 65, 57], [23, 65, 114], [23, 65, 133], [23, 65, 266], [23, 65, 399], [23, 65, 798], 
 [23, 83, 19], [23, 83, 38], [23, 83, 57], [23, 83, 95], [23, 83, 114], [23, 83, 133], [23, 83, 190], [23, 83, 247], [23, 83, 266], [23, 83, 285], [23, 83, 399], [23, 83, 494], [23, 83, 570], [23, 83, 665], [23, 83, 703], [23, 83, 741], [23, 83, 798], [23, 83, 1235], [23, 83, 1330], [23, 83, 1406], [23, 83, 1482], [23, 83, 1729], 
 [29, 41, 19], [29, 41, 38], [29, 41, 57], [29, 41, 95], [29, 41, 114], [29, 41, 133], [29, 41, 190], [29, 41, 247], [29, 41, 266], [29, 41, 285], [29, 41, 399], [29, 41, 437], [29, 41, 494], [29, 41, 570], [29, 41, 665], [29, 41, 703], [29, 41, 741], [29, 41, 798], [29, 41, 874], 
 [29, 59, 19], [29, 59, 38], [29, 59, 57], [29, 59, 114], [29, 59, 133], [29, 59, 209], [29, 59, 266], [29, 59, 361], [29, 59, 399], [29, 59, 418], [29, 59, 589], [29, 59, 627], [29, 59, 722], [29, 59, 798], [29, 59, 1083], [29, 59, 1178], [29, 59, 1254], [29, 59, 1463], 
 [29, 77, 19], [29, 77, 38], [29, 77, 57], [29, 77, 95], [29, 77, 114], [29, 77, 133], [29, 77, 190], [29, 77, 247], [29, 77, 266], [29, 77, 285], [29, 77, 399], [29, 77, 494], [29, 77, 570], [29, 77, 665], [29, 77, 703], [29, 77, 741], [29, 77, 798], [29, 77, 1235], [29, 77, 1330], [29, 77, 1387], [29, 77, 1406], [29, 77, 1482], [29, 77, 1729], [29, 77, 1995], [29, 77, 2109], 
 [29, 95, 19], [29, 95, 38], [29, 95, 57], [29, 95, 114], [29, 95, 133], [29, 95, 266], [29, 95, 399], [29, 95, 798], [29, 95, 1957], 
 [41, 47, 19], [41, 47, 38], [41, 47, 57], [41, 47, 114], [41, 47, 133], [41, 47, 266], [41, 47, 399], [41, 47, 798],
 [41, 65, 19], [41, 65, 38], [41, 65, 57], [41, 65, 95], [41, 65, 114], [41, 65, 133], [41, 65, 190], [41, 65, 247], [41, 65, 266], [41, 65, 285], [41, 65, 399], [41, 65, 494], [41, 65, 570], [41, 65, 665], [41, 65, 703], [41, 65, 741], [41, 65, 798], [41, 65, 1235], [41, 65, 1330], [41, 65, 1387], [41, 65, 1406], [41, 65, 1482], [41, 65, 1729], [41, 65, 1995], [41, 65, 2109], [41, 65, 2190], [41, 65, 2470], 
 [41, 83, 19], [41, 83, 38], [41, 83, 57], [41, 83, 114], [41, 83, 133], [41, 83, 266], [41, 83, 399], [41, 83, 798], [41, 83, 817], [41, 83, 931], [41, 83, 1634], [41, 83, 1862], [41, 83, 2413], [41, 83, 2451], [41, 83, 2793], [41, 83, 3097], [47, 59, 19], [47, 59, 38], [47, 59, 57], [47, 59, 95], [47, 59, 114], [47, 59, 133], [47, 59, 190], [47, 59, 247], [47, 59, 266], [47, 59, 285], [47, 59, 399], [47, 59, 437], [47, 59, 494], [47, 59, 551], [47, 59, 570], [47, 59, 665], [47, 59, 703], [47, 59, 741], [47, 59, 798], [47, 59, 817], [47, 59, 874], [47, 59, 931], [47, 59, 1102], [47, 59, 1235], [47, 59, 1273], [47, 59, 1311], [47, 59, 1330], [47, 59, 1406], [47, 59, 1482], [47, 59, 1634], [47, 59, 1653], [47, 59, 1729], [47, 59, 1862], [47, 59, 1995], [47, 59, 2109], [47, 59, 2185], [47, 59, 2413], [47, 59, 2451], [47, 59, 2470], [47, 59, 2546], [47, 59, 2622], [47, 59, 2755], [47, 77, 19], [47, 77, 38], [47, 77, 57], [47, 77, 114], [47, 77, 133], [47, 77, 266], [47, 77, 399], [47, 77, 798], [47, 83, 3318], [47, 95, 19], [47, 95, 38], [47, 95, 57], [47, 95, 95], [47, 95, 114], [47, 95, 133], [47, 95, 190], [47, 95, 247], [47, 95, 266], [47, 95, 285], [47, 95, 323], [47, 95, 399], [47, 95, 494], [47, 95, 570], [47, 95, 646], [47, 95, 665], [47, 95, 703], [47, 95, 741], [47, 95, 798], [47, 95, 969], [47, 95, 1235], [47, 95, 1330], [47, 95, 1387], [47, 95, 1406], [47, 95, 1482], [47, 95, 1615], [47, 95, 1729], [47, 95, 1938], [47, 95, 1995], [47, 95, 2109], [47, 95, 2261], [47, 95, 2470], [47, 95, 2774], [47, 95, 3230], [47, 95, 3458], [47, 95, 3515], [47, 95, 3705], [47, 95, 3990], [47, 95, 4161], [47, 95, 4199], [47, 95, 4218], [49, 97, 2382], [53, 77, 3315], [53, 77, 3570], [53, 93, 4094], [59, 65, 19], [59, 65, 38], [59, 65, 57], [59, 65, 114], [59, 65, 133], [59, 65, 266], [59, 65, 399], [59, 65, 798], [59, 83, 19], [59, 83, 38], [59, 83, 57], [59, 83, 95], [59, 83, 114], [59, 83, 133], [59, 83, 190], [59, 83, 247], [59, 83, 266], [59, 83, 285], [59, 83, 323], [59, 83, 399], [59, 83, 494], [59, 83, 570], [59, 83, 646], [59, 83, 665], [59, 83, 703], [59, 83, 741], [59, 83, 798], [59, 83, 969], [59, 83, 1235], [59, 83, 1330], [59, 83, 1387], [59, 83, 1406], [59, 83, 1482], [59, 83, 1615], [59, 83, 1729], [59, 83, 1843], [59, 83, 1938], [59, 83, 1957], [59, 83, 1995], [59, 83, 2109], [59, 83, 2261], [59, 83, 2470], [59, 83, 2603], [59, 83, 2774], [59, 83, 3230], [59, 83, 3458], [59, 83, 3515], [59, 83, 3686], [59, 83, 3705], [59, 83, 3914], [59, 83, 3990], [59, 83, 4161], [59, 83, 4199], [59, 83, 4218], [59, 83, 4522], [59, 83, 4845], [59, 89, 4214], [65, 77, 19], [65, 77, 38], [65, 77, 57], [65, 77, 95], [65, 77, 114], [65, 77, 133], [65, 77, 190], [65, 77, 247], [65, 77, 266], [65, 77, 285], [65, 77, 399], [65, 77, 494], [65, 77, 570], [65, 77, 665], [65, 77, 703], [65, 77, 741], [65, 77, 798], [65, 77, 1235], [65, 77, 1330], [65, 77, 1406], [65, 77, 1482], [65, 77, 1729], [65, 77, 1995], [65, 77, 2109], [65, 77, 2470], [65, 77, 3367], [65, 77, 3458], [65, 77, 3515], [65, 77, 3705], [65, 77, 3885], [65, 77, 3990], [65, 77, 4218], [65, 77, 4810], [65, 77, 4921], [65, 95, 19], [65, 95, 38], [65, 95, 57], [65, 95, 114], [65, 95, 133], [65, 95, 266], [65, 95, 399], [65, 95, 798], [65, 95, 817], [65, 95, 931], [65, 95, 1634], [65, 95, 1862], [65, 95, 2413], [65, 95, 2451], [65, 95, 2793], [65, 95, 4826], [65, 95, 4902], [65, 95, 5586], [65, 95, 5719], [77, 83, 19], [77, 83, 38], [77, 83, 57], [77, 83, 114], [77, 83, 133], [77, 83, 209], [77, 83, 266], [77, 83, 399], [77, 83, 418], [77, 83, 589], [77, 83, 627], [77, 83, 798], [77, 83, 1178], [77, 83, 1254], [77, 83, 1463], [77, 83, 1767], [77, 83, 2926], [77, 83, 3534], [77, 83, 4123], [77, 83, 4389], [83, 95, 19], [83, 95, 38], [83, 95, 57], [83, 95, 95], [83, 95, 114], [83, 95, 133], [83, 95, 190], [83, 95, 247], [83, 95, 266], [83, 95, 285], [83, 95, 399], [83, 95, 494], [83, 95, 570], [83, 95, 665], [83, 95, 703], [83, 95, 741], [83, 95, 798], [83, 95, 1235], [83, 95, 1330], [83, 95, 1406], [83, 95, 1482], [83, 95, 1729], [83, 95, 1995], [83, 95, 2071], [83, 95, 2109], [83, 95, 2470], [83, 95, 3458], [83, 95, 3515], [83, 95, 3705], [83, 95, 3990], [83, 95, 4142], [83, 95, 4218], [83, 95, 4921], [83, 95, 5187], [83, 95, 5567], [83, 95, 6213], [83, 95, 7030], [83, 95, 7410],[77, 83, 19]]'''