# li = [10,20,30,"ram"]


# li.append(40)

# print (li)

# li[0]="ram"

# li.insert(0,50)
# print(li)

# len(li)
# print(li)
# x = len(li)
# print (x)

# ti = (10,20)
# ti[0]=30
# print(ti)

# si = {10,20,30,10}

# si.add(60)
# si.discard(30)
# print (si)

# di = {'1':'ram','2':'hari','3':'shyam' }
# print ("student ", di['1'])

# a = int(input( "enter number"))
# b = int(input( "enter number"))

# if a>b :
#     print ("a is greater")
# elif b>a :
#     print ("b is greater")

# for i in range(6):print (i) 
 

# li = [ 10,20,30,40 ] 

# for i in li:
#      if i == 30:
#          break
#      print (i)

# li = [ 10,20,30,40 ] 

# for i in li:
#      if i == 30:
#          continue
#      print (i)

# li = [10,70,30,90,50,60]
# print(li)
# li.sort(reverse=True)
# print(li)

# def fun(a,b):
#     print(f"{a+b}")
    
# # fun(1,2)
# a = int(input( "enter number:"))
# def fun(a):
#     if a%5==0:
#         print("a is divisible by 5")
        
#     else:
#         print("a is not divisible by 5")
        
# a = int(input( "enter number a:"))
# b = int(input( "enter number b:"))
# def fun(a,b):
#     return a+b,a-b,a*b,a/b
# c,d,e,f=fun(a,b)
# print("the sum is:",c)
# print("the sub is:",d)
# print("the mul is:",e)
# print("the div is:",f)
def fun(a,b,op):
    '''this is fun'''
    if op=="+":
        c=a+b
        print("the sum is:",c)
    # elif op="-":
    #     c=a-b
    
    # print("the sum is",c)