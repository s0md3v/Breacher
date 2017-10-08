import requests
import threading
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-u", help="target url", dest='target')
parser.add_argument("--type", help="set the type i.e. html, asp, php", dest='type')
parser.add_argument("--fast", help="uses multithreading", dest='fast', action="store_true")
args = parser.parse_args()
target = args.target
print """\033[1;34m______   ______ _______ _______ _______ _     _ _______  ______
|_____] |_____/ |______ |_____| |       |_____| |______ |_____/
|_____] |    \_ |______ |     | |_____  |     | |______ |    \_

                          \033[37mMade with \033[91m<3\033[37m By D3V\033[1;m"""

print """\n  I am not responsible for your shit and if you get some error while
 running Breacher, there are good chances that target isn't responding.\n"""
print "\033[1;31m--------------------------------------------------------------------------\033[1;m\n"
target = target.replace('https://', '')
target = target.replace('http://', '')
target = target.replace('/', '')
target = 'http://' + target
def scan(links):
	for link in links:
		link = target + link
		r = requests.get(link, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0'})
		http = r.status_code
		if http == 200:
			print '  \033[1;32m[+]\033[0m Admin panel found: %s'% link
		if http == 404:
			print '  \033[1;31m[-]\033[1;m %s'% link
		else:
			http = str(http)
			first = http[:1]
			if first == '3':
				print '  \033[1;32m[+]\033[0m Potential EAR vulnerability found : ' + link
			else:
				print '  \033[1;31m[-]\033[1;m %s'% link
paths = []
def get_paths(type):
    try:
        with open('paths.txt','r') as wordlist:
            for path in wordlist:
                path = str(path.replace("\n",""))
                try:
            		if 'asp' in type:
            			if 'html' in path or 'php' in path:
            				pass
                		else:
               	 			paths.append(path)
                	if 'php' in type:
                		if 'asp' in path or 'html' in path:
                			pass
                		else:
                			paths.append(path)
                	if 'html' in type:
                		if 'asp' in path or 'php' in path:
                			pass
                		else:
                			paths.append(path)
                except:
                	paths.append(path)
    except IOError:
        print"\033[1;31m[-]\033[1;m Wordlist not found!"
        quit()
if args.fast == True:
	type = args.type
	get_paths(type)
	paths1 = paths[:len(paths)/2]
	paths2 = paths[len(paths)/2:]
	def part1():
		links = paths1
		scan(links)
	def part2():
		links = paths2
		scan(links)
	t1 = threading.Thread(target=part1)
	t2 = threading.Thread(target=part2)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
else:
	type = args.type
	get_paths(type)
	links = paths
	scan(links)
