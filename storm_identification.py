"""Functions to identify storms in 2d radar reflectivity images """
import collections
import numpy as np

def round_to_nearest_fraction(number, fraction):
    """Round np array to any fraction"""
    factor=1/fraction
    result= np.round(number*factor)/factor
    return result

def thresh_gw(image_radar, res=0.2):
    """Otsu (1979) algorithm for threshold selection from gray level histograms"""
    r_flat= image_radar.flatten() #r for rain
    r_flat=round_to_nearest_fraction(r_flat, res)
    res_array=np.arange(start=r_flat.min(), stop=r_flat.max(),
                        step= res)
    #We calculate the occurence probability of each res_array value in r_flat
    dict_count=collections.Counter(r_flat)
    prob_i=list()
    for elt in res_array:
        if elt in r_flat:
            prob_i.append(dict_count[elt]/r_flat.size)
        else:
            prob_i.append(0)
    mu_t=sum([x*y for x, y in zip(res_array,prob_i)])
    lambda_k=list()
    for key, elt in enumerate(res_array):
        mu_k=sum([x*y for x, y in zip(res_array[:(key+1)],prob_i[:(key+1)])])
        w_k=sum([x for x in prob_i])
        w_1=1-w_k
        mu_0=mu_k/w_k
        mu_1=(mu_t-mu_k)/(1-w_k)
        variance_0=sum( [(y/w_k)*(x-mu_0)**2 for x, y in
        zip(res_array[:(key+1)], prob_i[:(key+1)])])
        variance_1=sum( [(y/w_1)*(x-mu_1)**2 for x, y in
        zip(res_array[(key+1):], prob_i[(key+1):])])
        #Compute lambda_k
        variance_w=w_k*variance_0+w_1*variance_1
        variance_b=w_k*w_1(mu_1-mu_0)
        lambda_k.append(variance_b/variance_w)
    thres= res_array[np.argmin(lambda_k)]
    return thres

def plot_radar(radar_matrix):
    #Read 
    pass
