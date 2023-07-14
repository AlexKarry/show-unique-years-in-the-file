file = open("FF_data.txt")  # 'file' object

unique_years = set()  # empty set

for items in file:
    items = items.strip()  # str, "19260701    0.09    0.22    0.30   0.009"
    split_items = items.split()  # str, ["19260701", "0.09", "0.22", "0.30", "0.009"]
    years = split_items[0]  # str, 19260701
    year_cut = years[0:4]  # str, 1926
    unique_years.add(year_cut)  # class 'set', {'1992', '1984', ...}

sorted_list = sorted(unique_years)  # class 'list', ['1926', '1927' ...]
count = len(unique_years)  # int, 87

print(sorted_list)
print(f"{count} unique years found")
