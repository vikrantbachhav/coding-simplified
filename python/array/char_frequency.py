from collections import defaultdict
l = 'gggeeksforgeeks'
#l = ['c','c','c','a','a','b','d','e','e']

d = defaultdict(str)

for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

vk = defaultdict(list)
for k, v in d.items():
    vk[v].append(k)

print("d items: ", d.items())
print("d max item: ", max(d.items()))
print("d min item: ", min(d.items()))
print("d max item: ", max(d.values()))
print("d min item: ", min(d.values()))
print(max(d, key=d.get))
print(max(d, key=lambda k: d.get(k)))
print(max(d.items(), key=lambda k: k[1]))

print("vk items: ", vk.items())
print("vk max item: ", max(vk.items()))
print("vk min item: ", min(vk.items()))
print("vk max item: ", max(vk.values()))
print("vk min item: ", min(vk.values()))
print(max(vk, key=vk.get))
print(max(vk, key=lambda k: vk.get(k)))
print(max(vk.items(), key=lambda k: k[0]))