def func(x):
    return -0.6*x*x + 2.4*x + 5.5 #implement equation here 
    
xlf = 2 #xl value
xu = 6 #xu value
num_of_it = 5 #number of iterations
it = 1
while(1):
    print('#', it)
    d = 0.6180*(xu-xlf)
    print("d=", "(", xu, "-", xlf, ")*0.6180=", d)
    x1 = xlf + d
    x2 = xu - d
    print("x1=", x1, "f(x1)=", func(x1))
    print("x2=", x2, "f(x2)=", func(x2))
    if(func(x1)<=func(x2)):
        xu = x1
        xopt = x2
        print("xu = x1\nxopt = x2")
    else:
        xlf = x2
        xopt = x1
        print("xlf = x2\nxopt = x1")
    print("xleft=", xlf, "xu=", xu, "xopt=", xopt)    
    if(it == num_of_it): 
        break
    it += 1
    
    
    
    
