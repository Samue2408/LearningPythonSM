#https://docs.python.org/es/3/library/heapq.html
import heapq

numbers = [1, 4, 2, 100, 20, 50, 32, 150, 8]

print(heapq.nlargest(4, numbers))
print(heapq.nsmallest(4, numbers))