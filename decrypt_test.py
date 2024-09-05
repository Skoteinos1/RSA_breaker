import pickle

pth = '/PATH/TO/YOUR/FOLDER/'  # Has to be defined because of debug bug
def save_pickle(file, data1):
    if '.pkl' not in file:
        file += '.pkl'
