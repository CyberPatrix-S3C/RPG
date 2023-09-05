import requests, os, sys
repoVersion = ""
currentVersion = ""

def update_func(uname, repo):
	'''
	Function for
	checking if update is
	available or not.
	then update if update is available, and 
	do exit the script if not.
	'''
	try:
		url = f'https://raw.githubusercontent.com/{uname}/{repo}/main/version.txt'
		req = requests.get(url)
		contents = req.text
		
		print(contents)
	except Exception as e:
		print(f'[X] Request//Error: {e}')
	
	try:
		# RepoVersion
		# save output into a file and the read the file content.
		with open('version_line.txt', 'w') as vfc:
			vfc.write(contents)
		with open("version_line.txt", "r") as vfc:
			for line in vfc.readlines():
				repoVersion = line
		os.remove("version_line.txt")
		#print (repoVersion)
		
		#CurrentVersion
		# open version file and read the file content
		with open("version.txt", "r") as vfc:
			for line in vfc.readlines():
				currentVersion = line
		
		
		#  matching both files' contents.
		if repoVersion == currentVersion:
			print ("[-] No Update Available... You are using the current tool's version.")
			sys.exit(1)
		else:
			print ("[+] Update Available... ", end="\n")
			print ("[*] Updating Script...")
			
			os.system (f"""
			cd ..
			rm -rf {repo}
			git clone https://github.com/{uname}/{repo}
			echo "[+] Successfully Updated!"
			echo "[✓] Done!"
			""")
			sys.exit(1)
	except:
		print ("[X] Something went wrong!")
		sys.exit(1)

userName = "CyberPatrix-S3C"
repository = "RPG"

# invoking the update_func() function with the arguments.
update_func(userName, repository)
