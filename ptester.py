import PriorityQueue
import Waiter
import aStar
import constants
import info

# import anytree
# print(constants.REST[2][9])
# # 4,6 -> 6,6 kelener porusza sie po constants.REST
# star=aStar.aStar([4,6,0,0,0,""],[6,6,0,0,0,""])
# print("WYNIK")
# result=star.astar()
# result2= result.parent
# order=[]
# while True:
#     order=[result.name[5]]+order
#     result=result.parent
#     if result.parent is None:
#         break
# print(result2)
# print(order)
# class elo():
#     i=5
#     c=3
#
# zd=xd= elo()
# zd.i=10
# print(zd.i , " ", xd.i)


waiter = Waiter.Waiter(1, 1, 1)
print(waiter)
waiter.ordersqueue.put("FORWARD")
waiter.ordersqueue.put("FORWARD")
waiter.ordersqueue.put("FORWARD")
waiter.do()
print(waiter)
waiter.do()
print(waiter)
