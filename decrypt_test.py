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