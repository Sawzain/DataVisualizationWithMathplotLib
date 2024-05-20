# # ................multiple inheritance
# class a1:
#     def __init__(self,a):
#         self.a = a
        
#     def show(self,a):
#         print("hello",a)
# class a2:
#     def show1(self):
#         print("hi")
        
# class person(a1,a2):
#     def show2(self):
#         print("123")
        
# p1=person(1)
# p1.show(1)
# p1.show1()
# p1.show2()

# # ..........multilevel inheritance
# class a:
#     def a1(self):
#         print("a2")
# class b(a):
#     def b1(self):
#         print("b2")
# class c(b):
#     def c1(self):
#         print("c2")        
# p1=c()
# p1.a1()
# p1.b1()
# p1.c1()

# # .............super() __init__
# class a():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class b(a):
#     def __init__(self, x, y, c):
#         super().__init__(a, b)
#         self.c = c
#     def prnt(self, x, y, c):
#         print(y, x, c)
        
# ob1 = b(1,2,3)
# ob1.prnt(1,2,3)


# #......................... must learn
# 1) mean, medain, Mode
# 2) normal distribution
# 3) naye bayes
# 4) entropy
# 5) frequency and cumilative frequency
# 6) z-test,p-test,chi2test
# 7) sample of population
# 8) integration, derivative
# 9) matrix
# 10) co-ordinates
# 11) regression, correlation  
# 12) descision tree


# # .................types of machine learning
# i. supervised : label data set
# a.regression : for continuous value
# 1.linear regression
# 2.svm(support vector machine)
# 3.multiple regression
# 4.descision tree regression 
# 5. randon forest regression
# b.classification : for values are are categorized or in classes 
# 1.logistic
# 2.knn
# 3.svm classification
# 4.descision tree classification
# 5.naive bayes

# ii. unsupervised : unlabeled data predicts from color, shape and size
# 1.clustering
# a.k-mean algorithm
# 2.association
      

# iii. reinforcement