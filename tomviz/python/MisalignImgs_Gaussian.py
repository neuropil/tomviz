# Misalign (Random-Poisson) a tomography tilt series
# for testing and reconsruction development
#
# Developed as part of the tomviz project (www.tomviz.com)

def transform_scalars(dataset):        
    from tomviz import utils
    import numpy as np

    #----USER SPECIFIED VARIABLES-----#
    TILT_AXIS  = []     # Specify Tilt Axis Dimensions x=0, y=1, z=2
    SHIFT_EXP  = 0.10   # Specify the Expected (mean) Random % Image Shift (0-1)
    SHIFT_STDDEV = 0.05 # Specify the Standard Deviation as % of Image (0-1)
    np.random.seed(12)  # Set a new seed to get different random alignments
    #---------------------------------#

    data_py = utils.get_array(dataset) # Get data as numpy array.

    if data_py is None: # Check if data exists.
        raise RuntimeError("No data array found!")    

    if TILT_AXIS == []: # If tilt axis is not given, find it.
    # Find the smallest array dimension, assume it is the tilt angle axis.
        if data_py.ndim == 3:
            TILT_AXIS = np.argmin( data_py.shape )
        elif data_py.ndim == 2:
            raise RuntimeError("Data Array is 2 dimensions, it should be 3!")
        else: 
            raise RuntimeError("Data Array is not 2 or 3 dimensions!")

    for i in range(0,np.size(data_py,TILT_AXIS)-1):
        if TILT_AXIS == 2:
            shift_mu    = np.size(data_py,0)*SHIFT_EXP
            shift_sigma = np.size(data_py,0)*SHIFT_STDDEV
            shift0 = int( np.random.normal(shift_mu, shift_sigma) )
            shift1 = int( np.random.normal(shift_mu, shift_sigma) )
            data_py[:,:,i] = np.roll( data_py[:,:,i], shift0, axis = 0)
            data_py[:,:,i] = np.roll( data_py[:,:,i], shift1, axis = 1)
        elif TILT_AXIS == 1:
            shift_mu    = np.size(data_py,0)*SHIFT_EXP
            shift_sigma = np.size(data_py,0)*SHIFT_STDDEV
            shift0 = int( np.random.normal(shift_mu, shift_sigma) )
            shift1 = int( np.random.normal(shift_mu, shift_sigma) )
            data_py[:,i,:] = np.roll( data_py[:,i,:], shift0, axis = 0)
            data_py[:,i,:] = np.roll( data_py[:,i,:], shift1, axis = 1)
        elif TILT_AXIS == 0:
            shift_mu    = np.size(data_py,1)*SHIFT_EXP
            shift_sigma = np.size(data_py,1)*SHIFT_STDDEV
            shift0 = int( np.random.normal(shift_mu, shift_sigma) )
            shift1 = int( np.random.normal(shift_mu, shift_sigma) )
            data_py[i,:,:] = np.roll( data_py[i,:,:], shift0, axis = 0)
            data_py[i,:,:] = np.roll( data_py[i,:,:], shift1, axis = 1)
        else:
            raise RuntimeError("Python Transform Error: Unknown TILT_AXIS.")

    utils.set_array(dataset, data_py)
    print('Misalign Images Complete')
