import sys, os, re, subprocess

def runRegress(config):
	for eachURL in config:
		testURL = eachURL['url']
		testDB = eachURL['database']
		testMethod = eachURL['method']
		testData = eachURL['data']
		
		if testDB.strip() != '' :
			switchDB = " --dbms %s"%testDB
		else :
			switchDB = ""

		if testMethod != 'GET' :
			switchMethod = " --data '%s'"%testData
		else :
			switchMethod = ""

		print "****************************************************************************************"
		print "*TESTING %s ON URL %s*"%(testDB, testURL)
		print "****************************************************************************************"
		#print "python lib/src/sqlmap.py --url '%s'%s%s --batch --flush-session"%(testURL, switchDB, switchMethod)
		subProc = subprocess.Popen(["python lib/src/sqlmap.py --url '%s'%s%s --batch --flush-session"%(testURL, switchDB, switchMethod)], stdout=subprocess.PIPE, shell=True)
		(output, errors) = subProc.communicate()
		if re.search('---', output) :
			print output.split('---')[0].split('\n')[-1]
			print output.split('---')[1]
		else :
			print "URL Safe"

def main(argv):
	filename = sys.argv[1]
	configModule = __import__("%s"%filename, -1)	
	runRegress(configModule.site_config)


if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))

