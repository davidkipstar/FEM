

def test_x_or_y(output,A,b):
  if output[0]:
    x = output[1]
    for i in range(len(A)):
      if sum(A[i][j]*x[j] for j in range(len(x)))<b[i]:
        return False
  if not output[0]:
    y = output[1]
    for i in range(len(y)):
      if y[i] < 0:
        return False
    for j in range(len(A[0])):
      ytransposedai = sum(y[i]*A[i][j] for i in range(len(y)))
      if ytransposedai < -0.00000000000001 or ytransposedai > 0.00000000000001:
        return False
    if sum(y[i]*b[i] for i in range(len(y))) <= 0:
      return False
  return True

