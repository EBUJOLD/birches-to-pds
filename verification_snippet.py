# Verification Snippet
# This code does simple verifaction of Lunar Ice-Cube data

##############   READ IN DATA   ############## 
# Don't currently know how to read data or where it comes from

dataSet = open(filename, 'r')

############## CHECK FOR ZEROES ############## 
# Read each byte in the dataset, check for zeros
# Since we don't know where data comes from, the read in is probably wrong
while dataSet.read()
	if dataSet == 0:
		zero_counter = zero_counter + 1

# At this time, the threshhold number of zeros has not been identified
# 10 is a dummy
if zero_counter > 10:
	print('Too many zeroes')

############## CHECK ROUGH SLOPE ############## 
# Group 1 (skip) is 1024*4 bytes
# Groups 2-4 (average each individually) are 1024*8 (8192) bytes each
# Then compare the averaged values. A good result is 2 > 3 > 4

# Read in 8192 bytes in for each group
group2_data = read()
group3_data = read()
group4_data = read()

# Add them together and then divide by 8192 
avg_group2 = (sum(group2_data)/8192)
avg_group3 = (sum(group3_data)/8192)
avg_group4 = (sum(group4_data)/8192)

if avg_group2 > avg_group3:
	# Group 2 should be greater than group 3
	if avg_group3 > avg_group4:
		# Group 3 should be greater than group 4
		print ('Data passes slope check')
	else 
		print ('Data fails slope check')
else 
	print ('Data fails slope check')

print ('Average of group 2 = %r') %avg_group2
print ('Average of group 3 = %r') %avg_group3
print ('Average of group 4 = %r') %avg_group4