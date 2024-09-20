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
