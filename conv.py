
def conv2d(X, F, stride=1, padding=0):

  #initialize the values
  res = []
  (irow, icol) = X.shape
  (row, col) = F.shape
  
  (new_row, new_col) = ((irow-row + 2* padding)/stride + 1, (icol-col + 2* padding)/stride + 1)
  
  #perform conv operation
  for i in range(0, irow, stride):
    for j in range(0, icol, stride):
      inp = X[i:i+row, j:j+col]
      if (X.shape == F.shape)
        res.append(np.sum(np.multiply(inp, F))
  
  # reshape and return
  res = np.asarray(res).reshape((new_row, new_col))
  return res
  
  
def pooling_operation(X, W, type="max", stride=1):
  
  #initialize the values
  res = []
  (irow, icol) = X.shape
  (new_row, new_col) = ((irow-W)/stride + 1, (icol-W)/stride + 1)
  
  #perform pooling operation
  for i in range(0, irow):
    for j in range(0, icol):
      inp = X[i:i+W, j:j+W]
      if (inp.shape[0] == W and inp.shape[1] == W):
        res.append(np.max(inp))
        
  #reshape and return
  res = np.asarray(res).reshape((new_row, new_col))
  return res
                               
def apply_padding(X, padding=0):
   (row, col) = X.shape
   a = np.zeros((row + 2*padding, col + 2*padding))
   a[padding:padding+row, padding: padding+col] = X
   return a

                   
def get_iou(X, Y):
  res =[None]*4
  res[0] = max(X[0], y[0])
  res[2] = min(X[2], y[2])
  res[1] = max(X[1], Y[1])
  res[3] = min(X[3], y[3])
                   
  # get the area
  total_area = get_area(X) + get_area(Y)
  inter_area = get_area(res)
                   
  return inter_arae/total_area
                   
def inverted_dropout(prev_layer, keep_prob = 0.7):
    keep_prob = keep_prob
    drop_mat = np.random.rand(prev_layer.shape[0], prev_layer.shape[1]) > keep_prob
    prev_layer = np.multiply(prev_layer, drop_mat)
    prev_layer = prev_layer/keep_prob
                   
    return prev_layer

                   
def conv_2D(X, F, stride=1, padding=0):

  #input shape 
  res = []
  (inp_channel, inp_row, inp_col) = X.shape
  (out_channel, inp_channel, filt_row, filt_col) = F.shape

  # new shape
  out_row = (inp_row - filt_row + 2* padding)/stride + 1
  out_col = (inp_col- filt_col + 2*padding)/stride + 1
  rres = []

  # convolve
  for l in range(0, out_channel):
    for i in range(0, inp_row):
      for j in range(0, inp_col):
        sum = 0
        for k in range(0, inp_channel):
          inter_mat = X[k, i: i+filt_row, j:j + filt_col]
          if (inter_mat.shape[0] == filt_row and inter_mat.shape[1] == filt_col):
            sum = sum + np.sum(np.multiply(inter_mat, F[l,k,:,:]))
          else:
            break
        res.append(sum)
    a = np.asarray(res).reshape((out_row, out_col))
    a.tolist()
    rres.append(a)
    res = []

  rres = np.asarray(rres)
  return rres
