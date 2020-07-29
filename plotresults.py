import matplotlib.pyplot as plt
import pandas 

#=========================================
def plotnow(simname = None, NbChannels=6):
#=========================================

	if not simname:
		titleadd=""
		simadd = ''
	else:
		titleadd=simname
		simadd = titleadd + '_'

	labels=["D1","D2","STN","GPe","GPi"]
	# with open('log\\' + simadd + 'BG_customCBG', 'rt') as theFile: #windows
	with open('log/' + simadd + 'BG_customCBG', 'rt') as theFile: # linux or mac
		reader = pandas.read_csv(theFile, sep=' ', header=None)

	fig = plt.figure()		
	plt.plot(range(reader.shape[0]),reader[:][0])
	plt.xlabel('Time Step')
	plt.ylabel('FS Cell Response')
	plt.title(titleadd)

	for i in range(1,reader.shape[1]):
		if (i-1)%NbChannels==0:
			fig = plt.figure()		
		plt.plot(range(reader.shape[0]),reader[:][i],label='Channel #'+ str((i-1)%NbChannels +1))
		if i%NbChannels==0 or i==(reader.shape[1]-1):
			plt.xlabel('Time Step')
			plt.ylabel(labels[int((i-1)/NbChannels)] + ' Cell Response')
			plt.legend()
			plt.title(titleadd)

	plt.show()
