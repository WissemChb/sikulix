
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
    wait("1499787886756.png")
    click("1499787902217.png")

   
    click("1499788183174.png")

    if exists("1499788287163.png"):
        click("1499788294490.png")
        type('root')
        click("1499788301772.png")
    else:
        pass



def add_multinat_address():

    """ Testing the asseignement of NAT address to a device """

    Debug.info("assign a NAT IP address to device should be saved")
    
    click("1499789042284.png")
    click("1499789059828.png")
    click("1499789083362.png")
    click("1499789111197.png")
    click("1499789136539.png")
    click("1499789153565.png")
    addrSelected = find("1499791037960.png").text()
    device = find("1499791191112.png").text()
    click("1499789174732.png")
    click("1499789220095.png")
    if exists("1499789262506.png") and find(Location(859, 766)).text() == addrSelect  and find(Location(530, 764)).text() == device:
        Debug.info('************** Pass ******************)
    else: 
        Debug.info('************** Fail ******************)
        
    



def finish_test():
    App.close('firefox')

try:
    
    if __name__ == '__main__':
        start_test("192.168.1.254")
        add_multinat_address()
except Exception as e:
    Debug.error(e)
finally:
    finish_test()