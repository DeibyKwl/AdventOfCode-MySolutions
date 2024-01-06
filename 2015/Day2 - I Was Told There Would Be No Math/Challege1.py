# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

with open('input.txt', 'r') as f:
    text = f.readlines()

paper_sizes_lst = []

for line in text:
    l,w,h = line.split('x')
    l,w,h = int(l), int(w), int(h.strip())

    smallest_area = min(l*w, w*h, h*l)
    paper_sizes_lst.append(2*l*w + 2*w*h + 2*h*l + smallest_area)

total_size = sum(paper_sizes_lst)
print(total_size)