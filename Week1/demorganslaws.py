a = set(["A","B","C","D"])
b = set(["C","D","E","F"])
sample_space = set(["A","B","C","D","E","F","G"])

#print(a.intersection(b))
#set(['C', 'D'])
#print(a.difference(b)) #A Intersect Not(B)
#set(['A', 'B'])
#print(a.union(b)) # A Union B
#set(['A', 'B', 'C', 'D', 'E', 'F'])
#complement_a = sample_space.difference(a) #sample_space Intersect Not(B)
#print(complement_a)
#set(['E', 'F','G'])

#part1 (complement of the union of two sets)
part1 = sample_space.difference(a.union(b))


#part2 (the intersection of their complements)
part2 = sample_space.difference(a.union(b))


print(part1)
print(part2)
print(part1==part2)
