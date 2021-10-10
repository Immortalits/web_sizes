import pickle

# 1. feladat:

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

# ----------------------------------------------------
# 2. feladat:

for i in range(0, len(sites_new)):
    if sites[i]["size"] != sites_new[i]["size"]:
        dif = sites_new[i]["size"] - sites[i]["size"]
        rate = dif / (sites_new[i]["size"] / 100)
        rate = round(rate, 2)
        if rate > 0:
            print(f"{sites_new[i]['domain']} changed by +{rate}%.")
        if rate < 0:
            print(f"{sites_new[i]['domain']} changed by {rate}%.")

# ----------------------------------------------------
# 3. feladat:

empty_sites = 0
for site in sites_new:
    if site["size"] == 0:
        empty_sites += 1

print(f"There are {empty_sites} empty sites.")

# ----------------------------------------------------
# 4. feladat:

for site in sites_new:
    if site["size"] != 0:
        if site["size"] > 1024:
            meret = round(site['size'] / 1024, 2)
            print(f"{site['domain']} is {meret} Gb.")
        else:
            print(f"{site['domain']} is {site['size']} Mb.")
