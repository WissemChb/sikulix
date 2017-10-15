""" This file is created by g507954 in 12/07/2017 """


import os
import subprocess

Settings.UserLogs = True
Settings.UserLogPrefix = os.environ["USER"]
Debug.setLogFile("/home/g507954/SikuliWorkSpace/Output/testHH6-6580_Output.log")
Settings.OcrTextSearch = True
Settings.OcrTextRead = True



########### Start Test code ############

def start_test(url):
    
    """This function contain the basic configuration to running the tests"""
    
    Debug.user(' ################# start Test ######################')
    App.open('firefox --private-window '+url)
    wait("1499859035755.png",10)
    click("1499859050127.png")
    click("1499860406404.png")
    if  exists("1499860460744.png"):
        click("1499860468980.png")
        type('root')
        click("1499860496036.png")
    else:
        pass
    wait(3)
    click("1500042448017.png")

    

def enabling_pool_dhcp_test():

    Debug.info("Enabling DHCP should be saved")
    click("1499869448836.png")
    click("1499869500708.png")
    
    run("sudo dhclient -r eno1")
    run("sudo dhclient -v eno1")
    wait(5)
   
    addrCheck = find("1500048800819.png").right(270).text().encode('utf-8')
    print(addrCheck)
    address = str(subprocess.check_output("ifconfig eno1 |  grep 'inet ' |  tr -s ' '   |  cut -d ' ' -f3 |  cut -d ':' -f2", shell=True))
    print(address)
    click("1499869807158.png")
    click("1499869823253.png")
    click("1500280738868.png")
    if exists("1500042519928.png"):
        assignedAddr =  find("1500042533344.png").left(270).text().encode('utf-8')
    else: 
        assignedAddr = ""
    print(assignedAddr)
    if assignedAddr in address and addrCheck in address :
        Debug.info("********************* Pass *********************")
    else:
        Debug.info("********************* Fail ********************")
    
def disabling_dhcp_pool_test():

    Debug.info("Disabling DHCP should be saved")
    click("1499870278482.png")
    click("1499870293830.png")
    wait(5)
    click("1500042448017.png")
    click("1499870354112.png")
    click("1499870361236.png")
    wait(5)
    run("sudo dhclient -r eno1")
    run("sudo dhclient -v eno1")
    wait(2)
    addrCheck = find("1500048800819.png").right(270).text().encode('utf-8')
    print(addrCheck)
    address = str(subprocess.check_output("ifconfig eno1 |  grep 'inet ' |  tr -s ' '   |  cut -d ' ' -f3 |  cut -d ':' -f2", shell=True))
    print(address)
    
    click("1499869807158.png")
    click("1500280896095.png")
    click("1499869834841.png")
    assigned =  find("1499870556012.png").text().encode('utf-8').split('\n')
    if "Assigned to sst-BT-Test" not in assigned and addrCheck in address :
        Debug.info("********************* Pass *********************")
    else:
        Debug.info("********************* Fail ********************")
    

def finish_test():
    App.close('firefox')



# --------------------- Main  -------------------------

try:    
    if __name__ == '__main__':
        start_test("192.168.1.254")
        enabling_pool_dhcp_test()
        disabling_dhcp_pool_test()
except Exception as e:
    Debug.error(str(e))
    Debug.info('************* Fail ******************')
finally:
    finish_test()    
    
    