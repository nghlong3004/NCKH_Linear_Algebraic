import numpy as np

# Transition matrix
A = np.array([[0.92, 0.04], 
              [0.08, 0.96]])

x = np.array([[200],[350]])

print("a) :", A)
print("b) :", np.dot(A,x)[0])
print("c) :", np.dot(np.dot(A, np.dot(A,A)), x)[1])
