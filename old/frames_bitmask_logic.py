pickle_name2 = 'frames.p'

if os.path.isfile(pickle_name2):
    print("loading pickle")
    with open(pickle_name2, 'r') as f:
        frames = pickle.load(f)
else:
    print("creating pickle...")
    print("this will take some time...")
    frames = []
    for row in df.iloc[:,1:].iterrows():
        frames.append(np.flip((np.array(row[1:]).reshape(8,8).astype('float').T),0))


    with open(pickle_name2, 'wb') as f:
        pickle.dump(frames, f)


# a: x centre point of kernel
# a: x centre point of kernel
# r1: length of kernel
# r2: width of kernel
# n: dimension of array (assuming square matrix)
def bitmask_2d_square(a,b,n,r1,r2):
    # n = dimension matrix
    # m = dimension of kernel
    y,x = np.ogrid[-a:n-a, -b:n-b]
    #mask = x*x+y*y > r*r                               #CIRCLE
    #mask = (np.maximum(abs(x),abs(y)) < r1)             #SQUARE
    mask = abs((x/r1)+(y/r2)) + abs((x/r1)-(y/r2)) < 2  #RECTANGLE
    return mask


# %%notify
# Which threshold do you want?

### --- MUST BE 4 CHARACTERS i.e. 24.0 NOT 24 ---
#temperature average that is considered to be a person
threshold = 23.5
### ---------------------------------------------

pickle_name1 = 'df_tempMeans_'+str(threshold)[0:2]+'_'+str(threshold)[3]+'.p'
pickle_name2 = 'df_tempMeans_thresh_'+str(threshold)[0:2]+'_'+str(threshold)[3]+'.p'


if os.path.isfile(pickle_name1) and os.path.isfile(pickle_name2):
    print("loading pickles")
    df_tempMeans = pd.read_pickle(pickle_name1)
    df_tempMeans_thresh = pd.read_pickle(pickle_name2)
else:
    print("creating pickle...")
    print("this will take some time...")
    # frames is a list of 2D arrays
    # t is the instantaneous time point
    # frames[t][0][0] is the top left pixel
    # frames[t][7][7] is the bottom right pixel
    # 31.75 is the maximum, 20.5 is the minimum temp
    #
    # u1   u2   u3
    #    |    |    |
    #    |    |    |
    #    |    |    |

    #----------VARIABLES----------
    u3 = 5 #centre of rectangle right
    u2 = 2 #centre of rectangle middle
    u1 = -1 #centre of rectangle left
    ux = [u1,u2,u3]
    kw = 3 #Kernel width
    kernel_area = 15 #Area of kernel = 15 pixels

    n = 8 #
    temps_thresh = []
    temps = []
    # for all frames
    for t in tnrange(len(frames)-1):
        temp_thresh = [0,0,0]
        temp = [0,0,0]
        for centrex in range(3):
            mask = bitmask_2d_square(kw,ux[centrex],n,3,5)
            array = np.zeros((n, n))
            # create bitmask
            array[mask] = 1
            if centrex == 0:
                mean_temp = (np.multiply(frames[t],array).sum())/10
            else:
                mean_temp = (np.multiply(frames[t],array).sum())/kernel_area
            temp[centrex] = mean_temp
            if mean_temp > threshold:
                temp_thresh[centrex] = 1
            else:
                temp_thresh[centrex] = 0

        temps_thresh.append(temp_thresh)
        temps.append(temp)

    df_tempMeans = pd.DataFrame(temps)
    df_tempMeans_thresh = pd.DataFrame(temps_thresh)
    df_tempMeans.to_pickle(pickle_name1)
    df_tempMeans_thresh.to_pickle(pickle_name2)
