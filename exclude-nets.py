#!/usr/bin/env/python3

# Generate list of /24 subnets with specific exclusions applied
#  - i.e. exclude 10.x.5.x (10.0-255.5.0-255)
#  - i.e. exclude 172.16.10.x and 172.17.15.x

##  Define exclusions for each private IP range

###   10.x.x.x   ###
# [ 10.x.x.x 2ND OCTET EXCLUSIONS ] - this will apply exclusion to entire 3rd + 4th octet ranges, i.e. 5 = 10.5.0-255.0-255
exclusions10_2nd = {}
# [ 10.x.x.x 3RD OCTET EXCLUSIONS ]
exclusions10_3rd = {}
# [ 10.x.x.x FULL EXCLUSIONS ] - specific 2nd + 3rd octet exclusions, assuming 4th octet is always /24 full net
exclusions10_full = {}

###   172.x.x.x   ###
# [ 172.x.x.x 2ND OCTET EXCLUSIONS ] - remember, range is 172.16.x.x - 172.31.255.255!!
exclusions172_2nd = {}
# [ 172.x.x.x 3RD OCTET EXCLUSIONS ] 
exclusions172_3rd = {}
# [ 172.x.x.x FULL EXCLUSIONS ] - specify 2nd + 3rd octet
exclusions172_full = {}

###   192.168.x.x   ###
# [ 192.168.x.x EXCLUSIONS ] - only care about 3rd octet since first two are fixed and assume class C
exclusions192_3rd = {}

##### EXAMPLES #####
# exclusions10_2nd = {5, 6}   # exclude 10.5.x.x and 10.6.x.x
# exclusions172_2nd = {18, 20}   # exclude 172.18.x.x and 172.20.x.x (only private 172 range for everything else)
# exclusions10_full = {(5, 7), (5, 8)}   # exclude 10.5.7.x and 10.5.8.x
# exclusions172_full = {(16, 10), (17, 15)}   # for 172.16.10.x and 172.17.15.x
# exclusions192 = {0, 5, 8, 12}

# Function to generate list of /24 subnets while avoiding exclusions
def generate_subnets(filename, base, max2nd, exclusions2nd, exclusions3rd, exclusionsFull):
    with open(filename, "w") as f:
        for i in range(max2nd + 1): #iterate 2nd octet
            if i in exclusions2nd:
                continue #skip full 2nd octet exclusions
            for j in range(256): #iterate 3rd octet
                if j in exclusions3rd or (i, j) in exclusionsFull:
                    continue #skip specific exclusions
                f.write(f"{base}.{i}.{j}.0/24\n")

# Generate subnets for 10.x.x.x and 172.16.x.x - 172.31.x.x
generate_subnets("10_nets.txt", "10", 255, exclusions10_2nd, exclusions10_3rd, exclusions10_full)
generate_subnets("172_nets.txt", "172", 31, exclusions172_2nd, exclusions172_3rd, exclusions172_full)
# only 172.16 - 172.31

# special case: 192.168.x.x (only modifying 3rd octet)
with open("192_nets.txt", "w") as f:
    for j in range(256):
        if j not in exclusions192_3rd
            f.write(f"192.168.{j}.0/24\n")

print("Subnet lists generated successfully.")
