
""" This file is created by g507954 in 12/07/2017 """


import os


Settings.UserLogs = True
Settings.UserLogPrefix = os.environ["USER"]
Debug.setLogFile("/home/g507954/SikuliWorkSpace/Output/testHH6-6576_Output.log")
Settings.OcrTextSearch = True
Settings.OcrTextRead = True



########### Start Test code ############*

def start_test(url):
    
    """This function contain the basic configuration to running the tests"""
    
    Debug.user(' ################# start Test ######################')
    App.open('firefox --private-window '+url)
    wait("1499845863373.png",10)
    click("1499845872839.png")

   
    click("1499845891908.png")

    if exists("1499845925702.png"):
        click("1499845936983.png")
        type('root')
        click("1499845947105.png")
    else:
        pass



def add_multinat_address():

    """ Testing the asseignement of NAT address to a device """

    Debug.info("assign a NAT IP address to device should be saved")
    
    click("1499845963295.png")
    click("1499845981321.png")
    device = find("1500041672744.png").text().encode('utf-8').lower()
    click("1500041682191.png")
    click("1499846011192.png")
    
    click(Location(925, 574))
    
    addrSelected = find("1499867721220.png").text().encode('utf-8')
    print(addrSelected)
    
    
    click(Location(805, 440))
    
   
    click("1499846237069.png")
    click("1499846274282.png")
    wait(2)

    multiNAT = find("1499853959396.png").text().encode('utf-8').split('\n')

    print("+++++++"+find("1500041716728.png").text().encode('utf-8'))
    if exists("1500025380402.png") and find("1499868318382.png").text().encode('utf-8') == addrSelected  and device == find("1500041738262.png").text().encode('utf-8').lower() and  multiNAT[1] == ' Assigned to MultiNAT':
        Debug.info('************** Pass ******************')                 
    else:
        Debug.info('************** Fail ******************')
        

def test_modif_nat_address():

    Debug.info("changing a NAT IP address for a device should be saved")
    click("1499856375104.png")
    
    click(Location(796, 544))
    click("1499856497271.png")

    wait(3)
    assignAddr = find("1499856646224.png").text().encode('utf-8').split('\n')[1]
    
   
    
    if assignAddr == " Assigned to MultiNAT":
        Debug.info('************** Pass ******************')
    else:
        Debug.info('************** Fail ******************')
    
    
def delete_assigned_nat_address():
     Debug.info("Deleted a NAT IP address for a device should be saved")
     click("1499857830280.png")
     if exists("1499858245997.png"):
         click("1499857869931.png")
     if len(find("1499857970091.png").text().encode('utf-8').split('\n')) == 1:
              Debug.info('************** Pass ******************')
     else:
             Debug.info('************** Fail ******************')
             
             
             


def finish_test():
    App.close('firefox')


# --------------------- Main  -------------------------

try:    
    if __name__ == '__main__':
        start_test("192.168.1.254")
        add_multinat_address()
        test_modif_nat_address()
        delete_assigned_nat_address()
except Exception as e:
    Debug.error(str(e))
    Debug.info('************* Fail ******************')
finally:
    finish_test()