import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# creating a list of profiles
profiles = []

# traverse the data
for i in data:
    # find "All User Profile" in each item
	if "All User Profile" in i :
            
        # if found
		# split the item
		i = i.split(":")
            
        # item at index 1 will be the wifi name    
		i = i[1]
            
        # formatting the name
		# first and last character is use less
		i = i[1:-1]
            
        # appending the wifi name in the list
		profiles.append(i)

# printing heading
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("----------------------------------------------")

# traversing the profiles
for i in profiles:
    # try catch block begins
	# try block
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        # finding password from the result list
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        
        # if there is password it will print the pass word
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))

        # else it will print blank in front of pass word
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    
    # called when this process get failed
    except subprocess.CalledProcessError:
	    print("Encoding Error Occured")  
