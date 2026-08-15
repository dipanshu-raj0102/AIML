def zscore_normalization(X):

    mu = np.mean(X, axis = 0)
    sigma = np.std(X. axis = 0)
    X_norm = (X - mu)/ sigma 
    return(X_norm, mu , sigma)


