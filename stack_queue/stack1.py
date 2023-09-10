# Use a single array to implement three stacks (k stacks)

# this is a space ineffecient implementation

def create_partition(n,k):
    if k > n:
        print("error")
        return
    sizes = []
    value = 0 
    for i in range(k-1):
        value += int(n/k)
        sizes.append(int(n/k))
    sizes.append(n-value)
    return sizes
class MultiStack:
    """ Define a multistack"""
    def __init__(self,n,k):
        self.arr_size = n
        self.partitions = k
        self.array = [0]*n
        self.top = [-1]*k
        self.sizes = create_partition(n, k)
    def push(self,val,sn):
        if self.top[sn] == self.sizes[sn]-1:
            print("Stack is full")
            return
        self.top[sn]+=1
        self.array[sn*self.sizes[sn]+self.top[sn]] = val
        return
    def pop(self,sn):
        if self.top[sn] == -1:
            print("Empty stack")
            return
        val = self.array[sn*self.sizes[sn]+self.top[sn]]
        self.array[sn*self.sizes[sn]+self.top[sn]] = 0
        self.top[sn]-=1
        print(f'{val} Popped')
    def peek(self,sn):
        print(f'{ self.array[sn*self.sizes[sn]+self.top[sn]]} at the top of sn')
ms = MultiStack(12,3)
ms.push(4,0)
ms.push(5,1)
ms.push(6,2)
ms.push(5,2)
ms.push(5,2)
ms.push(5,2)
ms.push(5,2)

ms.pop(2)
ms.push(10,2)
print(ms.array)