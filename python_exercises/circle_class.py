from typing import Sequence


class Circle:
    def __init__(self, components: Sequence, element_count: int):
        self.components = components
        self.element_count = element_count


    def __iter__(self):
        result = []
        num_iterations = self.element_count // len(self.components)
        left_over = self.element_count % len(self.components)
        for i in range(num_iterations):
            for j in self.components:
                print(j)
                result.append(j)
        for k in range(left_over):
            result.append(self.components[k])
        print(result)
        return result


c = Circle('abc', 8)

print(list(c))

### better implementation :  


class CircleIterator():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0
 
    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value
 
 
class Circle():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
 
    def __iter__(self):
        return CircleIterator(self.data,
                              self.max_times)