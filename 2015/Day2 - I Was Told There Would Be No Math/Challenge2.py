# How many total feet of ribbon should they order?

with open('input.txt', 'r') as f:
    text = f.readlines()

paper_sizes_lst = []

for line in text:
    l,w,h = line.split('x')
    l,w,h = int(l), int(w), int(h.strip())

    # Find the 2 smallest dimensions
    tmp_lst = [l,w,h]
    side_one = min(tmp_lst)
    tmp_lst.pop(tmp_lst.index(side_one))
    side_two = min(tmp_lst)

    ribbon_bow = l*w*h
    ribbon_present = side_one + side_one + side_two + side_two

    paper_sizes_lst.append(ribbon_present + ribbon_bow)

total_size = sum(paper_sizes_lst)

print(total_size)