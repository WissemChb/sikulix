""" This file is created by g507954 in 10/07/2017 ,  it works only when the BT is in reset mode """




import os


Settings.UserLogs = True
Settings.UserLogPrefix = os.environ["USER"]
Debug.setLogFile("/home/g507954/SikuliWorkSpace/Output/testHH6-6525_Output.log")
Settings.OcrTextSearch = True
Settings.OcrTextRead = True

address = {
        '0.0.0.0':"Enter Default address should be not possible",
        '127.0.0.1':"Enter localhost address should be not possible",
        '10.0.0.1':"Enter private 10.0.0.0 address should be not possible",
        '172.16.0.5':"Enter private 172.16.0.0 address should be not possible",
        '192.168.0.4':"Enter private 192.168.0.0 address should be not possible",
        '224.0.0.10': "Enter multicast address should be not possible",
        '100.64.0.20': "Enter public  address 100.64.0.0 should not be  possible",
        '169.254.0.50': "Enter public  address 169.254.0.0 should not be  possible",
        '192.88.99.100': "Enter public  address 192.88.99.0 should not be  possible",
        }


########### Start Test code ############



def start_test(url): 

    """This function contain the basic configuration to running the tests"""
    
    Debug.user(' ################# start Test ######################')
    App.open('firefox --private-window '+url)
    wait("1501595436606.png", 10)

    click("1501595453560.png")

    if exists():
        
        click()
    else:
        click()
        


    if exists("1499781534684.png"):
        click("1499781552298.png")
        type('root')
        click("1499781563870.png")
    else:
        pass
    click("1499781591282.png")

def valid_address_saved(addr,message):

    """ This function test the valid IP address will be saved """
    
    adr = addr.split('.')
    Debug.info(message)
    doubleClick(Location(728, 516))
    paste(str(adr[0]))
    if len(adr[0])< 3:
       type(Key.TAB)
    else:
        type ("a",KeyModifier.CTRL)
    paste(str(adr[1]))
    if len(adr[1]) < 3 : 
        type(Key.TAB)
    else:
        type ("a",KeyModifier.CTRL)
    paste(str(adr[2]))
    if len(adr[2]) < 3:
        type(Key.TAB)
    else:
        type ("a",KeyModifier.CTRL)
    paste(str(adr[3]))

    click("1499781780453.png")
    wait(1)
    print( find("1500027780522.png").text().encode('utf-8'))
    if  find("1500027790420.png").text().encode('utf-8') == addr:
       Debug.info('************ Pass ******************')  
    else:
       Debug.info('************ Fail ******************')
       
    

def public_static_ip_range_tab_screen(n1,n2,n3,n4, message): 

    """ Test the unvalid IP address """
     
    Debug.info(message)
    doubleClick(Location(728, 516))
    paste(str(n1))
    if len(n1)< 3:
       type(Key.TAB)
    else:
        type ("a",KeyModifier.CTRL)
    paste(str(n2))
    if len(n2) < 3 : 
        type(Key.TAB)
    else:
        type ("a",KeyModifier.CTRL)
    paste(str(n3))
    if len(n3) < 3:
        type(Key.TAB)
    else:
        type ("a",KeyModifier.CTRL)
    paste(str(n4))
    
    if exists("1499781844930.png"):
        Debug.info('************ Pass ******************')    
    else:
        Debug.info('************ Fail ******************')
        
                

def address_blank_test():

    """ Test a popup should be open when we enter IP address """
    
    Debug.info('Enter an IP address should not be possible')

    click("1499782256475.png")
    if exists("1499782281377.png"):
        Debug.info('************ Pass ******************')
        click("1499782294209.png")
        
    else: 
        Debug.info('************ Fail ******************')
        click("1499782317985.png") 



def finish_test():
    App.close('firefox')


try:
    if __name__ == "__main__":
        start_test("192.168.1.254")
        address_blank_test()
        
        for i in address.keys():
            adr = i.split('.')
            public_static_ip_range_tab_screen(adr[0],adr[1],adr[2],adr[3],address[i])
            
        valid_address_saved("100.35.118.20", "Enter a valid  address should be saved")
except Exception as e: 
     Debug.error(str(e))
     Debug.info('************ Fail ******************')
finally:
    finish_test()
    
    


    



 


   
    










