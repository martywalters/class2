#iterator:
class Iter_example:
    def __iter__(self):
        self.val = 101
        return self
    def __next__(self):
        if self.val <= 90:
            raise StopIteration
        self.val -= 1
        return(self.val)
    
iter_example = Iter_example()
my_iter = iter(iter_example)
for number in my_iter:
    print(number,end=" ")
print()

#generator:
class Gen_example:
    def firstn(self, n):
        num = 0
        while num < n:
            yield num
            num += 1

gen_example = Gen_example()
for i in gen_example.firstn(10):
    print(i,end=' ')
print()
#Context Managers:

class Context_example:
    def __enter__(self):
        print('Building resources')
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print('Releasing class resources')

with Context_example() as resource:
    pass
        
        
