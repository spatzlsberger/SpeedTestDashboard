
import speedtest
import time

servers = []

threads = None
#return speed test results
s = speedtest.Speedtest()
s.get_servers
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

results_dict = s.results.dict()
#format results
download = results_dict['download']
upload = results_dict['upload']
ping = results_dict['ping']

print(str(download) + " " + str(upload) + " " + str(ping))

localtime = time.asctime( time.localtime(time.time()) )
print(localtime)

#output to csv
f = open("C:/Users/Shane Patzlsberger/source/repos/SpeedTestApp/SpeedTest/outputNetworkStatistics.csv","a")
f.write(str(localtime) + "," + str(download) + "," + str(upload) + "," + str(ping) + "\n")
f.close()
