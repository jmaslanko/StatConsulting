import random
import pandas as pd

print('Enter the following input values:')

# Input values needed
S = int(input('Subjects Per Site: ')) #subjects per site
T = int(input('Sites: ')) #sites
B = int(input('Block size: ')) #Block size
N = int(input('Treatments: ')) #treatments
D = int(input('Control: ')) #Control

# Initialize sites/blocks, assuming only 4 possible sites
SITES = ['AAA', 'BBB', 'CCC', 'DDD']
NUM_BLOCKS = int(S/B)

# Lists to append to from loops
final_list = []
site_list = []

# Loop through sites and blocks to create number of values needed
for site in range(0, T):
    site_list.extend([SITES[site] + str(i).zfill(2) for i in range(1, S+1)])
    for block in range(1, NUM_BLOCKS+1):
        num_t = ['T' for _ in range(1, (int(B*N/(N+D)))+1)]
        num_c = ['C' for _ in range(1, (int(B*D/(N+D)))+1)]
        all = num_c + num_t
        
        # After getting number of 'T' and 'C', randomly shuffle in block
        random.shuffle(all)
        final_list.extend(all)

# Join lists for final output
output = []
for i, j in zip(site_list, final_list):
    print(i + j)
    output.append(i + j)

# Export to desktop as CSV
df = pd.DataFrame(output)
df.to_csv('~/RandomData.csv')
