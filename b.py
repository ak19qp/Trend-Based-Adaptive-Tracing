
from pandas import read_csv
from sklearn.metrics import mean_squared_error
from math import sqrt
from random import randrange
import statistics
import statsmodels.api as sm
import time


def event_list(action):
	events = ""

	for x in action:
		
	    if x =="cpu_percent":
	        events = events + "module_load\nmodule_free\nmodule_get\nmodule_put\nmodule_request\npower_cpu_idle\npower_cpu_frequency\npower_machine_suspend\nrcu_utilization\nsched_kthread_stop\nsched_waking\nsched_wakeup\nsched_wakeup_new\nsched_switch\nsched_migrate_task\nsched_process_free\nsched_process_exit\nsched_wait_task\nsched_process_wait\nsched_process_fork\nsched_process_exec\nsched_stat_wait\nsched_stat_sleep\nsched_stat_iowait\nsched_stat_blocked\nsched_stat_runtime\n"
	    if x =="memory_shared":
	        events = events + "kmem_kmalloc\nkmem_cache_alloc\nkmem_kmalloc_node\nkmem_cache_alloc_node\nkmem_kfree\nkmem_cache_free\nkmem_mm_page_free\nkmem_mm_page_free_batched\nkmem_mm_page_alloc\nkmem_mm_page_alloc_zone_locked\nkmem_mm_page_pcpu_drain\nkmem_mm_page_alloc_extfrag\n"
	    if x =="disk_usage_percent":
	        events = events + "writeback_dirty_page\nwriteback_write_inode_start\nwriteback_exec\nwriteback_wait\nwriteback_congestion_wait\nwriteback_thread_start\nwriteback_thread_stop"
	return events
	

df = read_csv('/home/research/Desktop/dump.txt')

cpu_percent = df['cpu_percent']


# split into train and test sets
X = df
size = int(len(cpu_percent) * 0.4)
train = X[0:size]

######################################
sampleSize = 10
randStartIndex = size
sampling = 150
errorUpperBound = 0.03
errorLowerBound = 0.03
betaVal = 0.5
samplingFrequency = 1.0
samplingGap = 20
anomalyScoreThresholdLearnAfter = 3
######################################

anomalyScore = []
samplingCounter = 0
anomalyScoreThreshold = []


for x in df:
	anomalyScore.append(0)
	anomalyScoreThreshold.append(0)






#predictions = list()







while samplingCounter < sampling:

	time.sleep(1)

	actionList = ""
	actionListArray = []

	


	indexArr = -1

	nextSample = samplingGap
	#nextSample = round(samplingGap * samplingFrequency)
	randNum = randrange(randStartIndex, randStartIndex + nextSample)
	if randNum + nextSample <= len(X) - sampleSize:
		randStartIndex = randNum + nextSample
		print (randStartIndex)
	else:
		print ("End of data")
		break

	for x in df:
		indexArr = indexArr+1
		print(x)


		


		selectedSample = X[x][randNum:randNum + sampleSize]



		meanPredDif = []


		history = X[x][0 : randNum + sampleSize]

		model = sm.tsa.ARIMA(history, order=(1,1,1))
		model_fit = model.fit()
		output = model_fit.forecast()
		
		yhat = output[randStartIndex-10]

		

		#predictions.append(yhat)
		obs = X[x][randNum + sampleSize+1]

		meanOfSample = statistics.mean(selectedSample)
		sdOfSample = statistics.stdev(selectedSample)
		meanAndPredictionDifference = abs(yhat - meanOfSample) / meanOfSample

		isAnomaly = 0

		if (samplingCounter == anomalyScoreThresholdLearnAfter):
			anomalyScoreThreshold[indexArr] = anomalyScoreThreshold[indexArr] / anomalyScoreThresholdLearnAfter

		if(samplingCounter > anomalyScoreThresholdLearnAfter):
			if yhat > (meanOfSample + (errorUpperBound * meanOfSample)) or yhat < (meanOfSample - (errorLowerBound * meanOfSample)):
		  		isAnomaly = 1
		else:
			anomalyScoreThreshold[indexArr] = anomalyScoreThreshold[indexArr] + meanAndPredictionDifference 


		anomalyScore[indexArr] = (betaVal * isAnomaly) + ((1 - betaVal) * anomalyScore[indexArr])

		takeAction = 0
		if anomalyScore[indexArr] >= anomalyScoreThreshold[indexArr]:
			takeAction = 1
			actionList = actionList + x + "\n"
			actionListArray.append(x)

		samplingFrequency =  1 - anomalyScore[indexArr]
		meanPredDif.append(meanAndPredictionDifference)



		print('predicted=%f, actual=%f, mean_of_sample=%f, meanAndPredictionDifference=%f, flagged=%i, anomalyScore=%f, sampling_Freq=%f, takeAction=%i' % (yhat, obs, meanOfSample, meanAndPredictionDifference, isAnomaly, anomalyScore[indexArr], samplingFrequency, takeAction))
		


	f = open("action_list.txt", "w")
	f.write(actionList)
	f.close()

	f = open("event_list.txt", "w")
	f.write(event_list(actionListArray))
	f.close()

	samplingCounter = samplingCounter + 1



