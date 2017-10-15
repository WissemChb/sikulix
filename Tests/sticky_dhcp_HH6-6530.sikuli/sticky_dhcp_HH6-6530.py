""" This file is created by g507954 in 12/07/2017 """


import os
import subprocess

Settings.UserLogs = True
Settings.UserLogPrefix = os.environ["USER"]
Debug.setLogFile("/home/g507954/SikuliWorkSpace/Output/testHH6-6530_Output.log")
Settings.OcrTextSearch = True
Settings.OcrTextRead = True



########### Start Test code ############*

def start_test(url):
    
    """This function contain the basic configuration to running the tests"""
    
    Debug.user(' ################# start Test ######################')
    App.open('google-chrome  '+url)
    wait("1501594726051.png",20)
    
    click("1501594739049.png")
    
    click("1499860406404.png")
    if  exists("1499860460744.png"):
        click("1499860468980.png")
        type('root')
        click("1499860496036.png")
    else:
        pass
    wait(3)
    click("1500042036780.png")
    


    
def add_sticky_dhcp_test():

    Debug.info("assign a sticky DHCP IP address to device should be saved")

    click("1499860847422.png")
    click("1499860876307.png")
    click("1499860734728.png")
    click("1499859306356.png")
    click("1499859318863.png")
    click("1499859576916.png")
    wait(5)
    run("sudo dhclient -r eno1")
    run("sudo dhclient -v eno1")
    address = str(subprocess.check_output("ifconfig eno1 |  grep 'inet ' |  tr -s ' '   |  cut -d ' ' -f3 |  cut -d ':' -f2", shell=True))
    click("1499859483220.png")
    click("1499859500556.png")
    if  exists("1499860460744.png"):
        click("1499860468980.png")
        type('root')
        click("1499860496036.png")
    else:
        pass

    click("1500283055517.png")
    assigned =  find("1500041924380.png").text().encode('utf-8').split('\n')
    if len(assigned) == 2 and assigned[0] == address and assigned[1] == " Assigned to sst-BT-Test":
        Debug.info("********************* Pass *********************")
    else:
         Debug.info("********************* Fail ********************")
        
def disabled_sticky_dhcp():
    click("1499861785940.png")
    click("1499861806001.png")
    if  exists("1499860460744.png"):
       click("1499860468980.png")
       type('root')
       click("1499860496036.png")
    else:
        pass

    wait(5)
    click("1500042052860.png")
    
    click("1500026342106.png")
    click("1500026352208.png")
    click("1499861673176.png")
    wait(3)
    run("sudo dhclient -r eno1")
    run("sudo dhclient -v eno1")
    address = str(subprocess.check_output("ifconfig eno1 |  grep 'inet ' |  tr -s ' '   |  cut -d ' ' -f3 |  cut -d ':' -f2", shell=True))
    click("1499859483220.png")
    click("1499859500556.png")
    if  exists("1499860460744.png"):
       click("1499860468980.png")
       type('root')
       click("1499860496036.png")
    else:
        pass

    click("1499859512863.png")
    assigned =  find("1500025977030.png").text().encode('utf-8').split('\n')
    if ' Assigned to sst' not in assigned and address == "192.168.1.65": 
        Debug.info("********************* Pass *********************")
    else:
        Debug.info("********************* Fail ********************")

    


def changing_sticky_dhcp_address():
    Debug.info("changing sticky DHCP IP address of device should be saved")
    click("1499861785940.png")
    click("1499861806001.png")
    wait(5)
    click("1500042075163.png")
    click("1499862205158.png")
    click("1499862226823.png")
    click("1501595640773.png")
    click("1499862261239.png")
    wait(3)
    run("sudo dhclient -r eno1")
    run("sudo dhclient -v eno1")
    address = str(subprocess.check_output("ifconfig eno1 |  grep 'inet ' |  tr -s ' '   |  cut -d ' ' -f3 |  cut -d ':' -f2", shell=True))
    click("1499859483220.png")
    click("1499859500556.png")
    if  exists("1499860460744.png"):
       click("1499860468980.png")
       type('root')
       click("1499860496036.png")
    else:
        pass

    wait(2)
    click("1499859512863.png")
    assigned =  find("1500041984906.png").text().encode('utf-8').split('\n')
    if len(assigned) == 2 and assigned[0] == address and assigned[1] == " Assigned to sst-BT-Test":
        Debug.info("********************* Pass *********************")
    else:
        Debug.info("********************* Fail ********************")

 
        
def finish_test():
    
    App.close('chrome')


# --------------------- Main  -------------------------

try:    
    if __name__ == '__main__':
        start_test("192.168.1.254")
        add_sticky_dhcp_test()
        changing_sticky_dhcp_address()
        disabled_sticky_dhcp()
except Exception as e:
    Debug.error(str(e))
    Debug.info('************* Fail ******************')
finally:
    finish_test()    
    
    
    
    