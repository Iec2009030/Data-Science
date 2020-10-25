
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
                   
  
