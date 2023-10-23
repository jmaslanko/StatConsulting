import random

print('Enter the following input values:')

S = int(input('Subjects Per Site: ')) #subjects per site
T = int(input('Sites: ')) #sites
B = int(input('Block size: ')) #Block size
N = int(input('Treatments: ')) #treatments
D = int(input('Control: ')) #Control

SITES = ['AAA', 'BBB', 'CCC', 'DDD']
NUM_BLOCKS = int(S/B)

final_list = []
site_list = []

for site in range(0, T):
    site_list.extend([SITES[site] + '0' + str(i) for i in range(1, S+1)])
    for block in range(1, NUM_BLOCKS+1):
        num_t = ['T' for _ in range(1, (int(B*N/(N+D)))+1)]
        num_c = ['C' for _ in range(1, (int(B*D/(N+D)))+1)]
        all = num_c + num_t
        
        random.shuffle(all)
        final_list.extend(all)


for i, j in zip(site_list, final_list):
    print(i + j)
