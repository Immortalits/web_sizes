import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

sum_size = 0
avg_size = 0

for site in sites_new:
    sum_size += site["size"]

sum_size = sum_size / 1024
sum_size = round(sum_size, 2)

print(f"Total size is: {sum_size} Gb.")

avg_size = sum_size / len(sites)
avg_size = round(avg_size, 2)

print(f"Avarage size is: {avg_size} Gb.")