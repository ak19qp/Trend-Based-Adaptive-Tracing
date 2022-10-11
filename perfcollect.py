import os


sample_period = 1
sample_collection = 5

for i in range(sample_collection):
	os.system('sudo perf record -F 99 -ag -o perf'+str(i)+'.data sleep '+str(sample_period))
	os.system('sudo chmod 777 perf'+str(i)+'.data')



for i in range(sample_collection):
	os.system('sudo perf report -i perf'+str(i)+'.data --stdio > perf'+str(i)+'.txt')
	os.system('sudo chmod 777 perf'+str(i)+'.txt')
