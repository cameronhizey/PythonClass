# What I did
# sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]
# sample_list.reverse()
# chunk1 = sample_list[-3:]
# chunk2 = sample_list[3:-3]
# chunk3 = sample_list[0:3]
# print(f"Chunk-1 = {chunk1}")
# print(f"Chunk-2 = {chunk2}")
# print(f"Chunk-3 = {chunk3}")

# What guy in video did
sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]
chunk_size = int(len(sample_list)/3)
end = chunk_size
start = 0
for i in range(1, 4):
    chunk = sample_list[start:end]
    print(f"Chunk-{i} = {list(reversed(chunk))}")
    start = end
    end += chunk_size
