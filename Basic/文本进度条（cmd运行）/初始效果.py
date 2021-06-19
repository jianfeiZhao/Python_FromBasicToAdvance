import time
scale=10
print("--------执行开始--------")
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)
    print("{:<4.0%}[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("--------执行结束--------")
