import re
import pandas as pd
import os
import io
################# This code is use for global styling ####################################################
global_style = """
<style>
th {
    background-color: blue;
    color: white;
    text-align: left;
}

.table {
    border-collapse: collapse;
}
.table td {
    padding: 5px;
    position:relative;
}
.shobhit{
position:absolute;top:0;left:0;bottom:0;right:0; display:flex;justify-content:center;align-items:center; widht:100%; height:100% ;
}




</style>
"""

#################### this code is use for write data in a file #######################################################
open('out.html', 'w').close()

def write_html_table(html_table):
    # Write the HTML table to a file
    with open('out.html', 'a') as html_file:
        html_file.write(f'<pre> {html_table} </pre>')


def write_html_table_front(html_table):

    f = open('out.html','r')
    data=f.read()
    f.close()
    print(data,'datadtadtadatad')

    f = open('final.html','w+')
    
    f.write(html_table + data)
    
    f.close()
    # with open('out.html', 'a') as html_file :
    #     html_file.seek(0,0)
    #     html_file.write(f'<pre> {html_table} </pre>')

##########################################################################################################################

global_summary = {
    "Item": ['RSSI', 'VSWR', 'VSWR Delta', 'Alarms', 'RET', 'RET Labels', 'TMA', 'SFP', 'Fiber Loss', 'SDIR', 'RRU Status', 'Cell Status', 'Other'],

}


global_summ_df = pd.DataFrame(global_summary)

global_summ_df["Status"]=""
global_summ_df["Comment"]=""



# drd=pd.DataFrame(global_summ_df)
# html_table =  drd.to_html(escape=False, index=False,
#                                                             table_id='styled_table',
#                                                             classes='table table-striped table-bordered')
# write_html_table("\n<h2>-----:NODE INFO:-----:</h2>\n"+html_table)


def addDataintoglobalDf(colname,column1):

    changeIndex=global_summ_df[global_summ_df["Item"]==colname].index[0]

                # global_summ_df.iloc[1]["Status"]="Gelo"

    global_summ_df.loc[changeIndex, 'Comment'] = ", ".join(column1)
    if(len(column1)>0):
        global_summ_df.loc[changeIndex, 'Status'] = "NOK"

    else:
        global_summ_df.loc[changeIndex, 'Status'] = "OK"

    # print(global_summ_df)
  




# dasdashdksajlda

###########################################################################################################################


# data = {'Item': ['RSSI', 'VSWR', 'VSWR Delta', 'Alarms', 'RET', 'RET Labels', 'TMA', 'SFP', 'Fiber Loss', 'SDIR', 'RRU Status', 'Cell Status', 'Other'],
#         'Status': ['NOK', 'NOK', 'NOK', 'NOK', 'NOK', 'OK', 'NA', 'OK', 'NOK', 'OK', 'OK', 'NOK', 'OK'],
#         'Content': [None] * 13}

# df = pd.DataFrame(data)






# Initialize the column1 variable


############# This code is use for find siteid #################################################################
file_path='C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
def siteIdGetter(pattern):
    with open(file_path, 'r') as file:
        input_string = file.read()
        
    matches = re.findall(pattern, input_string, re.MULTILINE)
    strid=""

    for i in matches:
        if(i.split(">")[0]!=""):
            strid=i.split(">")[0]
    return strid

pattern = r".*pmr -m 3 -r 206 \| egrep -i '\(Int_RadioRecInterference\)'.*$"

globalSiteId=siteIdGetter(pattern)
# print(globalSiteId)

###############################################################################################################

#############  This code is use for find siteid #################################################################
file_path='C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt'
def second_siteIdGetter(pattern):
    with open(file_path, 'r') as file:
        input_string = file.read()
        
    matches = re.findall(pattern, input_string, re.MULTILINE)
    strid=""

    for i in matches:
        if(i.split(">")[0]!=""):
            strid=i.split(">")[0]
    return strid

pattern = r"^.*ManagedElement=.*managedElementType.*MEId.*$"

globalSiteId_2=second_siteIdGetter(pattern)
# print(globalSiteId_2)
#########################################################################################################################

#############  This code is use for find siteid #################################################################

file_path='C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt'
def third_siteIdGetter(pattern):
    with open(file_path, 'r') as file:
        input_string = file.read()
        
    matches = re.findall(pattern, input_string, re.MULTILINE)
    strid=""

    for i in matches:
        if(i.split(">")[0]!=""):
            strid=i.split(">")[0]
    return strid

pattern = r"^.*sts.*"

globalSiteId_3=third_siteIdGetter(pattern)
# print(globalSiteId_3,'globalSiteId_3')

#############  This code is use for find siteid #################################################################


#############  This code is use for find siteid #################################################################

file_path='C:/Users/LENOVO/Desktop/dataframework/find_data/fifth_data.txt'
def fifth_siteIdGetter(pattern):
    with open(file_path, 'r') as file:
        input_string = file.read()
        
    matches = re.findall(pattern, input_string, re.MULTILINE)
    strid=""

    for i in matches:
        if(i.split(">")[0]!=""):
            strid=i.split(">")[0]
    return strid

pattern = r"^.*lst lst VA61251A.*"

globalSiteId_5=fifth_siteIdGetter(pattern)
# print('globalSiteId_5::::::::::::',globalSiteId_5,'globalSiteId_5')

#############################################################################################################################
#############  This code is use for find siteid #################################################################

file_path='C:/Users/LENOVO/Desktop/dataframework/find_data/seventh_data.txt'
def SEVENTH_siteIdGetter(pattern):
    with open(file_path, 'r') as file:
        input_string = file.read()
        
    matches = re.findall(pattern, input_string, re.MULTILINE)
    strid=""

    for i in matches:
        if(i.split(">")[0]!=""):
            strid=i.split(">")[0]
    return strid

pattern = r"^.*alt.*"

globalSiteId_7=SEVENTH_siteIdGetter(pattern)
# print('globalSiteId_7::::::::::::',globalSiteId_7)

#############################################################################################################################

file_path = "C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"

def NODE(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        if content:

            start_marker = """=====================================================================================================================================
ID RiL                Type Res MO1-MO2           BOARD1-BOARD2         AlmIDs Cells (States)                                          Issue (Failed checks)
====================================================================================================================================="""
            end_marker = """=====================================================================================================================================
FRU   ;LNH    ;BOARD          ;ST ;FAULT ;OPER ;MAINT ;STAT ;PRODUCTNUMBER   ;REV     ;SERIAL        ;DATE     ;PMTEMP ; TEMP ; UPT ;SW                  ;
====================================================================================================================================="""

            start_index = content.find(start_marker)
            end_index = content.find(end_marker)

            if start_index != -1 and end_index != -1:
                extracted_data = content[start_index:end_index]

                # Define the regular expression pattern
                # pattern = r'Node:\s+(.*?)\s+(.*?)\s+\(.*?\)\s+(.*?)\s+(.*?)\s+(.*?)\s+$'
                pattern = r'Node:\s+(\w+\s+\w+)\s+(\w+\d+/\d+_\w+\s*\(\d+\.\w+\))'


                # Use re.search with re.DOTALL flag to find the matches
                match = re.search(pattern, extracted_data, re.DOTALL)

                if match:
                    # Extract the parsed elements
                    node_name = match.group(1)
                    serial_number = match.group(2)
                    # version = match.group(3)
                    # technology = match.group(4)
                    # technology = match.group(5)

                    print("Node Name:", node_name)
                    print("Serial Number:", serial_number)
                    # print("Version:", version)
                    # print("Technology:", technology)
                    
                else:
                    print("No match found.")
            else:
                print("Start and/or end markers not found in the content.")
            
            
            start_marker = """ hget . allowedplmnlist"""
            end_marker = """=================================================================================================================
MO
================================================================================================================="""
            
            start_index = content.find(start_marker)
            end_index = content.find(end_marker)
            print(start_index,end_index)
            
            if start_index != -1 and end_index != -1:
                extracted_data = content[start_index:end_index]
                # print(extracted_data)

                # Define the regular expression pattern
                # pattern = r'Node:\s+(.*?)\s+(.*?)\s+\(.*?\)\s+(.*?)\s+(.*?)\s+(.*?)\s+$'
                pattern = r'(\d+\.\d+\.\d+\.\d+)'


                # Use re.search with re.DOTALL flag to find the matches
                match = re.search(pattern, extracted_data, re.DOTALL)

                if match:
                    # Extract the parsed elements
                    ONM_1 = match.group(1)
                    # serial_number = match.group(2)
                    # version = match.group(3)
                    # technology = match.group(4)
                    # technology = match.group(5)

                    print("	ONM IP:", ONM_1)
                    # gfdhdrhttkuykuft
                    # print("Serial Number:", serial_number)
                    # print("Version:", version)
                    # print("Technology:", technology)
                else:
                    print("No match found.")
            else:
                print("Start and/or end markers not found in the content.")

################################################################################################################
    file_path2 = "C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path2, 'r') as file:
        content2 = file.read()
        # print(content2)
        # if content2:
        start_marker2 = """*************************************************************************************************************************************"""
        end_marker2 = """=====================================================================================================================================
FRU   ;LNH      ;BOARD       ;ST ;FAULT ;OPER ;MAINT ;STAT ;PRODUCTNUMBER   ;REV     ;SERIAL        ;DATE     ;PMTEMP ; TEMP ; UPT ;SW                   ;
====================================================================================================================================="""

        start_index2 = content2.find(start_marker2)
        end_index2 = content2.find(end_marker2)

        if start_index2 != -1 and end_index2 != -1:
            extracted_data2 = content2[start_index2:end_index2]

            # Define the regular expression pattern
            # pattern = r'Node:\s+(.*?)\s+(.*?)\s+\(.*?\)\s+(.*?)\s+(.*?)\s+(.*?)\s+$'
            pattern2 = r'Node:\s+(\w+\s+\w+)\s+(\w+\d+/\d+_\w+\s*\(\d+\.\w+\))'


            # Use re.search with re.DOTALL flag to find the matches
            match2 = re.search(pattern2, extracted_data2, re.DOTALL)

            if match2:
                # Extract the parsed elements
                node_name2 = match2.group(1)
                serial_number2 = match2.group(2)
                # version = match.group(3)
                # technology = match.group(4)
                # technology = match.group(5)

                print("Node Name2:", node_name2)
                print("Serial Number2:", serial_number2)
                # print("Version:", version)
                # print("Technology:", technology)
            else:
                print("No match found.")
        else:
            print("Start and/or end markers not found in the content.")
        

        start_marker3 = """NIE04225A2> scg"""
        end_marker3 = """===========================================================
Namespace  SystemConstants
==========================================================="""

        start_index3 = content2.find(start_marker3)
        end_index3 = content2.find(end_marker3)

        # if start_index3 != -1 and end_index3 != -1:
        extracted_data3 = content2[start_index3:end_index3]
        # print('asdflkjh',extracted_data3)

            # Define the regular expression pattern
            # pattern = r'Node:\s+(.*?)\s+(.*?)\s+\(.*?\)\s+(.*?)\s+(.*?)\s+(.*?)\s+$'
            # pattern3 = r'(\d+\.\d+\.\d+\.\d+)'
        pattern3=r'(\d+\.\d+\.\d+\.\d+)'



        match3 = re.search(pattern3, extracted_data3, re.MULTILINE)

        if match3:

            ONM_2 = match3.group(0)

            print("	ONM IP2:", ONM_2)
        else:
            print("No match found.")

#############################################################################
    file_path3 = "C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content2 = file.read()
        # print(content2)
        # if content2:
        start_marker2 = """=====================================================================================================================================
ID RiL Type Res MO1-MO2          BOARD1-BOARD2    AlmIDs Cells (States)                         Issue (Failed checks)
====================================================================================================================================="""
        end_marker2 = """=====================================================================================================================================
FRU     ;LNH      ;BOARD     ;ST ;FAULT ;OPER ;MAINT ;STAT ;PRODUCTNUMBER   ;REV     ;SERIAL        ;DATE     ;PMTEMP ; TEMP ; UPT ;
====================================================================================================================================="""

        start_index2 = content2.find(start_marker2)
        end_index2 = content2.find(end_marker2)

        if start_index2 != -1 and end_index2 != -1:
            extracted_data2 = content2[start_index2:end_index2]

            # Define the regular expression pattern
            # pattern = r'Node:\s+(.*?)\s+(.*?)\s+\(.*?\)\s+(.*?)\s+(.*?)\s+(.*?)\s+$'
            pattern2 = r'Node:\s+(\w+\s+\w+)\s+(\w+\d+/\d+_\w+\s*\(\d+\.\w+\))'


            # Use re.search with re.DOTALL flag to find the matches
            match2 = re.search(pattern2, extracted_data2, re.DOTALL)

            if match2:
                # Extract the parsed elements
                node_name3 = match2.group(1)
                serial_number3 = match2.group(2)
                # version = match.group(3)
                # technology = match.group(4)
                # technology = match.group(5)

                print("Node Name3:", node_name3)
                print("Serial Number3:", serial_number3)
                # print("Version:", version)
                # print("Technology:", technology)
            else:
                print("No match found.")
        else:
            print("Start and/or end markers not found in the content.")
        

        start_marker3 = """pst"""
        end_marker3 = """.............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
===================================================================================================="""

        start_index3 = content2.find(start_marker3)
        end_index3 = content2.find(end_marker3)

        # if start_index3 != -1 and end_index3 != -1:
        extracted_data3 = content2[start_index3:end_index3]
        # print('asdflkjh',extracted_data3)

            # Define the regular expression pattern
            # pattern = r'Node:\s+(.*?)\s+(.*?)\s+\(.*?\)\s+(.*?)\s+(.*?)\s+(.*?)\s+$'
            # pattern3 = r'(\d+\.\d+\.\d+\.\d+)'
        pattern3=r'(\d+\.\d+\.\d+\.\d+)'



        match3 = re.search(pattern3, extracted_data3, re.MULTILINE)

        if match3:

            ONM_3 = match3.group(0)

            print("	ONM IP3:", ONM_3)
        else:
            print("No match found.")

###############################################################################################################################################

    file_path3 = "C:/Users/LENOVO/Desktop/dataframework/find_data/fifth_data.txt"
    with open(file_path3, 'r') as file:
        content2 = file.read()
        # print(content2)
        # if content2:
        start_marker2 = """Collecting TN data..."""
        end_marker2 = """=====================================================================================================================================
SMN APN  BOARD    SWALLOCATION  S  FAULT OPER MAINT   c/p   d  PRODUCTNUMBER  REV   SERIAL     DATE     MO
====================================================================================================================================="""

        start_index2 = content2.find(start_marker2)
        end_index2 = content2.find(end_marker2)

        if start_index2 != -1 and end_index2 != -1:
            extracted_data2 = content2[start_index2:end_index2]
            print(extracted_data2)
            # Define the regular expression pattern
            # pattern = r'Node:\s+(.*?)\s+(.*?)\s+\(.*?\)\s+(.*?)\s+(.*?)\s+(.*?)\s+$'
            # pattern2 = r'Node:\s+(\w+\s+\w+)\s+(\w+\d+/\d+_\w+\s*\(\d+\.\w+\))'
            pattern2 = r'Node:\s(\S+)\s+(CXP\d+/\d+_\S+)'  # (CXP\S+)\s(W\d+\.\d+\.\d+\.\d+)\s\((C\d+\.\d+-EP\d+)\
            # pattern = r'Node:\s(\S+)\s(CXP\S+)\s(W\d+\.\d+\.\d+\.\d+)\s\((C\d+\.\d+-EP\d+)\)'
            # Use re.search with re.DOTALL flag to find the matches
            match2 = re.search(pattern2, extracted_data2, re.MULTILINE)

            if match2:
                # Extract the parsed elements
                node_name5 = match2.group(1)
                serial_number5 = match2.group(2)
                # version = match.group(3)
                # technology = match.group(4)
                # technology = match.group(5)

                print("Node Name5:", node_name5)
                print("Serial Number5:", serial_number5)
                # print("Version:", version)
                # print("Technology:", technology)
            else:
                print("No match found.")
        else:
            print("Start and/or end markers not found in the content.")
        

        start_marker3 = """get . dis"""
        end_marker3 = """=================================================================================================================
MO                                                      Attribute         Value
================================================================================================================="""

        start_index3 = content2.find(start_marker3)
        end_index3 = content2.find(end_marker3)
        print(start_index3,end_index3)


        # if start_index3 != -1 and end_index3 != -1:
        extracted_data3 = content2[start_index3:end_index3]
        # print('asdflkjh',extracted_data3)

            # Define the regular expression pattern
            # pattern = r'Node:\s+(.*?)\s+(.*?)\s+\(.*?\)\s+(.*?)\s+(.*?)\s+(.*?)\s+$'
            # pattern3 = r'(\d+\.\d+\.\d+\.\d+)'
        pattern3=r'(\d+\.\d+\.\d+\.\d+)'



        match3 = re.search(pattern3, extracted_data3, re.MULTILINE)

        if match3:

            ONM_5= match3.group(0)

            print("	ONM IP4:", ONM_5)
        else:
            print("No match found.")
##########################################################################################################

    file_path4 = "C:/Users/LENOVO/Desktop/dataframework/find_data/fourth_data.txt"
    with open(file_path4, 'r') as file:
        content2 = file.read()
        lines = content2.split('\n')
        first_line = lines[0]
        print('First Line:', first_line)
        global last_word
        words = content2.split()[::-1] 
        last_word = words[0]
        
        print('Last Word from First Line:', last_word)

        # print(content2)
        # if content2:
        start_marker2 = """<RXTCP:MOTY=RXOTG,CELL=CLA411A;
RADIO X-CEIVER ADMINISTRATION
TG TO CHANNEL GROUP CONNECTION DATA"""
        end_marker2 = """<RXTCP:MOTY=RXOTG,CELL=CLA411B;
RADIO X-CEIVER ADMINISTRATION
TG TO CHANNEL GROUP CONNECTION DATA"""

        start_index2 = content2.find(start_marker2)
        end_index2 = content2.find(end_marker2)

        if start_index2 != -1 and end_index2 != -1:
            extracted_data2 = content2[start_index2:end_index2]
            # print(extracted_data2)
            # Define the regular expression pattern
            # pattern = r'Node:\s+(.*?)\s+(.*?)\s+\(.*?\)\s+(.*?)\s+(.*?)\s+(.*?)\s+$'
            # pattern2 = r'Node:\s+(\w+\s+\w+)\s+(\w+\d+/\d+_\w+\s*\(\d+\.\w+\))'
            pattern2 = r'(\w+\-\d+)\s+(\S+)\s+(\d+)'  # (CXP\S+)\s(W\d+\.\d+\.\d+\.\d+)\s\((C\d+\.\d+-EP\d+)\
            # pattern = r'Node:\s(\S+)\s(CXP\S+)\s(W\d+\.\d+\.\d+\.\d+)\s\((C\d+\.\d+-EP\d+)\)'
            # Use re.search with re.DOTALL flag to find the matches
            # match2 = re.findall(pattern2, extracted_data2, re.MULTILINE)

            match = re.search(pattern2, extracted_data2)
          
            if match:
                cl1a0 = match.group(0)
                cl1a1 = match.group(1)
                cl1a2 = match.group(2)
                cl1a2=cl1a2.rstrip('A')
                print(cl1a2)
            else:
                print("No IP address found.")
           

            # if match2:
            #     columns = ['MO', 'CELL', 'CHGR']
            #     table_df = pd.DataFrame(match2, columns=columns)
            #     # cl1a=table_df['CELL']
            #     cl1a=table_df['CELL'].str.rstrip('A')
            #     print(cl1a,'cl1a')

            # else:
            #     print("No match found.")
        else:
            print("Start and/or end markers not found in the content.")

        
        

        start_marker2 = """IP                NETMASK          BLOCK   CPSB     IOSTOC"""
        end_marker2 = """ETHERNET          GATEWAY          RP"""

        start_index2 = content2.find(start_marker2)
        end_index2 = content2.find(end_marker2)

        if start_index2 != -1 and end_index2 != -1:
            extracted_data2 = content2[start_index2:end_index2]
            # print(extracted_data2,'extracted_data2extracted_data2')
            # Define the regular expression pattern
            # pattern = r'Node:\s+(.*?)\s+(.*?)\s+\(.*?\)\s+(.*?)\s+(.*?)\s+(.*?)\s+$'
            # pattern2 = r'Node:\s+(\w+\s+\w+)\s+(\w+\d+/\d+_\w+\s*\(\d+\.\w+\))'
            pattern2 = r'(\d+\.\d+\.\d+\.\d+)'  # (CXP\S+)\s(W\d+\.\d+\.\d+\.\d+)\s\((C\d+\.\d+-EP\d+)\
            # pattern = r'Node:\s(\S+)\s(CXP\S+)\s(W\d+\.\d+\.\d+\.\d+)\s\((C\d+\.\d+-EP\d+)\)'
            # Use re.search with re.DOTALL flag to find the matches
            # match2 = re.findall(pattern2, extracted_data2, re.MULTILINE)
            match = re.search(pattern2, extracted_data2)
            # if match2:
            #     columns = ['IP']
            #     table_df = pd.DataFrame(match2,columns=columns)
            #     onm_6=table_df['IP']
            if match:
                ip_address = match.group(0)
                print(ip_address)
            else:
                print("No IP address found.")
                
        #     else:
        #         print("No match found.")
        # else:
        #     print("Start and/or end markers not found in the content.")

        data = {'SiteID': (globalSiteId,globalSiteId_2,globalSiteId_3,globalSiteId_7,cl1a2),
        'RNC': ('N/A',"N/A","N/A",globalSiteId_5,last_word),
        'Node': (node_name,node_name2,node_name3,node_name5,"N/A"),
        'Software Version': (serial_number,serial_number2,serial_number3,serial_number5,"N/A"),
        'ONM IP': (ONM_1,ONM_2,ONM_3,ONM_5,ip_address),
    }
        df = pd.DataFrame(data)
        print('dfdfdfdfdfdfdfdfdfdfdf',df)

        html_table = global_style + df.to_html(escape=False, index=False,
                                                            table_id='styled_table',
                                                            classes='table table-striped table-bordered')

        write_html_table("\n<h2>-----:NODE INFO:-----:</h2>\n"+html_table)

NODE(file_path)
####################################################################################################################   




################# this code create df for node info ########################################################################
# def table_data():
#     data = {'SiteID': (globalSiteId,globalSiteId_2,globalSiteId_3,globalSiteId_5,globalSiteId_7),
#             'RNC': ('N/A',"N/A","N/A","N/A","N/A"),
#             'Node': ('RadioNode LN',"RadioNode N",'RadioNode L',"",""),
#             'Software Version': ('CXP9024418/15_R74C54 (23.Q2)',"CXP2010174/1_R71C54 (23.Q2)",'CXP9024418/15_R37C36 (21.Q3)',"",""),
#             'ONM IP': ('11.244.16.43',"11.244.16.42",'11.170.49.212',"",""),
#         }
#     df = pd.DataFrame(data)
#     # print(df)
#     # global_style = "<style>td { text-align: left; }</style>"
#     html_table = global_style + df.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#     write_html_table("\n<h2>-----:NODE INFO:-----:</h2>\n"+html_table)
# table_data()
############################################################################################################################

####################################  VSWR ###################################################################
final_col_for_data_vswr=[]


file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"

def VSWR(file_path,marketPlace):
    

    with open(file_path, 'r') as file:
        content = file.read()
        # print('ccccccccccc', content)

##############################

        start_marker = "hget (^FieldReplaceableUnit=|^AuxPlugInUnit=|^PlugInUnit=) administrativeState|operationalstate|product|isshared"
        end_marker = "hget rilink RiLinkId|linkRate|operationalState|riPortRef1|riPortRef2"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]

        if extracted_data:
            table_pattern = r"^(FieldReplaceableUnit=\S+)\s+(\d+\s+\(\w+\)|\s*)\s+(\S+)\s+(\d+\s+\(\w+\)|\s*)\s+(.+?)\s+(.+?)\s+(.+?)\s+(\S+)\s+(\S+)$"

            # table_pattern = r"^(FieldReplaceableUnit=\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\S+)\s+(\d+\s+\(\w+\)|\s*)\s+(.+?)\s+(.+?)\s+(.+?)\s+(\S+)\s+(\S+)$"

            # table_pattern = r"^(FieldReplaceableUnit=\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\S+)\s+(\d+\s+\(ENABLED\))\s+(.+?)\s+(.+?)\s+(.+?)\s+(\S+)\s+(\S+)$"  ##  (\d+\s+\(\w+\)|\s*)\s

            table_matches = re.findall(table_pattern, extracted_data, re.MULTILINE)

            if table_matches:
                columns = ['MO', 'administrativeState', 'isSharedWithExternalMe', 'operationalState', 'productName', 'productNumber', 'productRevision', 'productionDate', 'serialNumber']
                table_df = pd.DataFrame(table_matches, columns=columns)
                # print("8th log::\n", table_df)

                serial= table_df["serialNumber"]
                sn1=serial[0]
                sn2=serial[1]
                sn3=serial[3]

                # print('llaaa\n',sn1,sn2,sn3)

                stat= table_df["operationalState"]
                print(stat,'operationalsuu')
                
                state=stat.replace("1","")
                op1=state[0]
                op1= op1.replace('(', '').replace(')', '').replace('1', '').replace('0', '')
                print(op1,'operationalsuu')
                op2=state[1]
                op2= op2.replace('(', '').replace(')', '').replace('1', '').replace('0', '')
                print(op2,'operationalsuu')
            
                op3=state[3]
                op3= op3.replace('(', '').replace(')', '').replace('1', '').replace('0', '')
                print(op2,'operationalsuu')
                # asdfgh
            if extracted_data:
                start_marker = """sdir"""
                end_marker = """hget . allowedplmnlist"""

                start_index = content.find(start_marker)
                end_index = content.find(end_marker)
                extracted_data = content[start_index:end_index]
                # print(extracted_data,'lllll')
                pattern1 = r'\b\d{2}:\d{2}:\d{2}-\d{4}\b'
                table_matches1 = re.findall(pattern1, extracted_data, re.MULTILINE)

                if table_matches1:
                    for time_string in table_matches1:
                        print("VSWR:Extracted time string:", time_string)
                else:
                    print("Time string not found in the data.")
            if extracted_data:
                table_pattern12 = r'^(\d+-\d+)\s*;(\S+)\s*;(\S+)\s*;([^;]+);([^;]+);([^;]+);(\d+\.\d+\s+\(\d+\.\d+\))\s*;([^;]+);([^;]+);([^;]+)$(?!\s*[-]+)'
                table_matches12 = re.findall(table_pattern12, extracted_data, re.MULTILINE)#, re.MULTILINE

                if table_matches12:
                    columns = ['FRU' , 'LNH', 'BOARD', 'RF', 'BP', 'TX (W/dBm)','VSWR (RL)','RX (dBm)','UEs/gUEs','Sector/AntennaGroup/Cells (State:CellIds:PCIs)']  ##  
                    table_df12 = pd.DataFrame(table_matches12, columns=columns,)
                    # print(table_df12)

            if extracted_data:
                pattern = r'(FDD=\S+ FDD=\S+ NRC=\S+)\s'

                table_matches = re.findall(pattern, extracted_data, re.MULTILINE)
                if table_matches:

                    columns1 = ['Sector/AntennaGroup/Cells (State:CellIds:PCIs)']  ##,'RX (dBm)'  

                
                    table = pd.DataFrame(table_matches, columns=columns1,)#,
                    # print('lkjhg',table)

                    global c1,c2,c3
                    
                    c1 = table.iloc[0]
                    c1=c1.to_string(index=False)
                    # print(c1)
                    c2 = table.iloc[1] #
                    c2=c2.to_string(index=False)
                    # print(c2)
                    c3 = table.iloc[2] 
                    c3=c3.to_string(index=False)
                    # print(c3)
                    # print('c1,c2,c3',c1,c2,c3)

                    fru_column = table_df12['FRU']#.drop_duplicates()
                    # print("FRU Column1:\n", fru_column)

                    f1=fru_column[0]
                    # print('1',f1)

                    f2=fru_column[4]
                    # print('2',f2)

                    f3=fru_column[8]
                    # print('2',f3)


                    BOARD_column = table_df12['BOARD']#.drop_duplicates()
                    # print("BOARD Column1:\n", BOARD_column)
                    b1=BOARD_column[0]
                    # print('1',b1)

                    b2=BOARD_column[1]
                    # print('2',b2)

                    b3=BOARD_column[2]
                    # print('3',b3)

                    VSWR_column = table_df12['VSWR (RL)']
                    # print("VSWR (RL) Column:\n",VSWR_column)
                    A=VSWR_column[0]
                    A1= float(A.split()[0]) 
                    # print('a',A1)

                    B=VSWR_column[1]
                    B1 = float(B.split()[0])
                    # print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",delta1)

                    C=VSWR_column[2]
                    C1 = float(C.split()[0])
                    # print('c',C)

                    delta1= abs(A1-C1)
                    
                    # delta1.__abs__()
                    # print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",delta1)

                    D=VSWR_column[3]
                    D1= float(D.split()[0])
                    # print('d',D)
                    delta2= abs(B1-D1)
                    
                    # print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",delta2)

                    E=VSWR_column[4]
                    # print(e)
                    E11= float(E.split()[0]) 
                    # print('e',E11)

                    F=VSWR_column[5]
                    # print(f)
                    F11= float(F.split()[0]) 


                    G=VSWR_column[6]
                    G11= float(G.split()[0])
                    # print('g',G)
                    delta3=abs( E11-G11)
                    


                    H=VSWR_column[7]
                    H11= float(H.split()[0])

                    delta4= abs(F11-H11)
                    delta4.__abs__()
                    K=VSWR_column[8]
                    K13= float(K.split()[0]) 


                    L=VSWR_column[9]
                    L13= float(L.split()[0]) 

                    M=VSWR_column[10]
                    M13= float(M.split()[0])

                    delta5= abs(K13-M13)
                    delta5.__abs__()
                    print(delta5,'azsxdcfvg')

                    N=VSWR_column[11]
                    N13= float(N.split()[0])

                    delta6= abs(L13-N13)
                    delta6.__abs__()
                    cell_column = table_df12['Sector/AntennaGroup/Cells (State:CellIds:PCIs)']
                    table_df12 = table_df12['VSWR (RL)'].transpose()

    file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"

    with open(file_path, 'r') as file:
        content = file.read()
        if content :
            start_marker21= """sdir"""
            end_marker21= """cvls"""

            start_index21 = content.find(start_marker21)
            end_index21 = content.find(end_marker21)
            extracted_data21= content[start_index21:end_index21]
            # print("nnn",extracted_data21)

            if extracted_data21:

                pattern1 = r'\b\d{2}:\d{2}:\d{2}-\d{4}\b'
                table_matches1 = re.findall(pattern1, extracted_data21, re.MULTILINE)

                if table_matches1:
                    for time_string1 in table_matches1:
                        print("VSWR:Extracted time string:", time_string1)
                else:
                    print("Time string not found in the data.")
            

            if extracted_data21:

                if extracted_data21:
                    
                    table_pattern22 = r'^(\d+-\d+)\s*;(\S+)\s*;(\S+)\s*;([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+)$(?!\s*[-]+)'   ######;(\d+\.\d+\s+\(\d+\.\d+\))\s*;([^;]+);([^;]+);([^;]+)$(?!\s*[-]+)
              

                    table_matches22 = re.findall(table_pattern22, extracted_data21, re.MULTILINE)#, re.MULTILINE
                    # print(';;;',table_matches22)
                    if table_matches22:

                        columns = ['FRU','LNH','BOARD','RF','BP', 'TX (W/dBm)','VSWR (RL)','RX (dBm)','UEs/gUEs','Sector/AntennaGroup/Cells (State:CellIds:PCIs)']  ## '  

                    
                        table_df22 = pd.DataFrame(table_matches22, columns=columns,)#,

                if extracted_data21:
                    # pattern23 = r'([^;]+)$'
                    pat=( r'(NRC=\S+)')
                    # if pat in pattern23:
                    table_matches23 = re.findall(pat, extracted_data21, re.MULTILINE)
                    # print(',,,,,',table_matches23)
                    if table_matches23:

                        # columns = ['Sector/AntennaGroup/Cells (State:CellIds:PCIs)']  ##,'RX (dBm)'  

                    
                        table23= pd.DataFrame(table_matches23)#,, columns=columns

                        global a,b,c
                        # print(a,b,c,'a,b,ca,b,ca,b,ca,b,ca,b,c')
                        a = table23.iloc[0:2]
                        # print("Column a:\n", a.to_string(index=False))
                        a=a.to_string(index=False)
                        
                        b = table23.iloc[2:4]
                        # print("Column b:\n", b.to_string(index=False))
                        b=b.to_string(index=False)

                        c = table23.iloc[4:6]
                        # print("Column c:\n", c.to_string(index=False))
                        c=c.to_string(index=False)

                        a = a.replace("\n", " ")
                        b = b.replace("\n", " ")
                        c = c.replace("\n", " ")

                        a = a.lstrip('0 ')
                        b = b.lstrip('0 ')
                        c = c.lstrip('0 ')
                        print(a,b,c,'a,b,ca,b,ca,b,ca,b,ca,b,c')


                        fru_column = table_df22['FRU']#.drop_duplicates()
                        # print("FRU Column:\n", fru_column)

                        fr1=fru_column[0]
                        # print('1',fr1)

                        fr2=fru_column[1]
                        # print('2',fr2)

                        fr3=fru_column[2]
                        # print('2',fr3)


                        BOARD_column = table_df22['BOARD']#.drop_duplicates()
                        # print("BOARD Column:\n", BOARD_column)

                        br1=BOARD_column[0]
                        # print('2',br1)

                        br2=BOARD_column[1]
                        # print('2',br2)

                        br3=BOARD_column[2]
                        # print('2',br3)

###############################################
                    site_Id1=globalSiteId
                    

                    data2 = {
                        "Site_Id":site_Id1,
                        'DATETIME': time_string,
                        "CELL":(c1,c2,c3),
                        "BOARD":(b1,b2,b3),
                        'FRU': (f1,f2,f3),
                        "VSWR1":(A1,E11,K13),
                        "VSWR2":(B1,F11,L13),
                        "VSWR3":(C1,G11,M13),
                        "VSWR4":(D1,H11,N13),
                        "VSWR5":"-",
                        "VSWR6":"-",
                        "VSWR7":"-",
                        "VSWR8":"-",
                        "DELTA1":(delta1,delta3,delta5),
                        "DELTA2":(delta2,delta4,delta6),
                        "DELTA3":"-",
                        "DELTA4":"-",
                        "Serial_Number":(sn1,sn2,sn3),
                        "FAULTS":"-",
                        "Op.State":(op1,op2,op3),
                        "STATUS":"-"    
                    }
                    
                    df = pd.DataFrame(data2)
                    print('asd',df)
                    
                    site_Id2=globalSiteId_2
                    data3={
                        "Site_Id":site_Id2,
                        'DATETIME': time_string1,
                        "CELL":(a,b,c),
                        "BOARD":(br1,br2,br3),
                        'FRU': (fr1,fr2,fr3),
                        "VSWR1":"-",
                        "VSWR2":"-",
                        "VSWR3":"-",
                        "VSWR4":"-",
                        "VSWR5":"-",
                        "VSWR6":"-",
                        "VSWR7":"-",
                        "VSWR8":"-",
                        "DELTA1":"-",
                        "DELTA2":"-",
                        "DELTA3":"-",
                        "DELTA4":"-",
                        "Serial_Number":"-",
                        "FAULTS":"-",
                        "Op.State":"-",
                        "STATUS":"-"     
                    }

                    df1 = pd.DataFrame(data3 )

######################################################################################################################################################################
    file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content3 = file.read()
        if content3:
            start_marker3= """ sdir"""
            end_marker3= """ pst"""

            start_index3 = content3.find(start_marker3)
            end_index3 = content3.find(end_marker3)
            extracted_data3= content3[start_index3:end_index3]
            # print("nnn",extracted_data3)

            if extracted_data3:

                pattern3 = r'\b\d{2}:\d{2}:\d{2}\b'
                table_matches3 = re.findall(pattern3, extracted_data3, re.MULTILINE)

                if table_matches3:
                    for time_string3 in table_matches3:
                        print("VSWR:third file time string:", time_string3)
                else:
                    print("Time string not found in the data.")
            

            if extracted_data3:
                # table_pattern4 =r"^(RRU-\d+-\d+)\s*;(BXP_\d+)\s*;(\S+)\s*;\s*(A|B)\s*;\s*(\S+)\s*;\s*(-|\d+\.\d+ \(\d+\.\d+\)|N/A)\s*;\s*(-|\d+\.\d+ \(\d+\.\d+\)|N/A)\s*;\s*(-|\d+\.\d+ \(\d+\.\d+\)|N/A)\s*"

                
                table_pattern4 = r'^(:?RRU\-\d+-\d+)\s*;(BXP\_\d+)\s*;(\S+)\s*;\s*(A|B)\s*;\s*(\S+)\s*;\s*(-|N/A)\s*;\s*(\d+\.\d+ \(\d+\.\d+\)|N/A|-)\s*;\s*()\s*;\s*(\d+/-)\s*;\s*(SE=\d+ AG=\d+ FDD=\S+ NIOT=\S+|\d+:\d+:\d+)'   ##  ;\s*(SE=(\d+) AG=(\d+) FDD=([A-Z0-9]+) NIOT=([A-Z0-9]+) \(([^,]+), ([^,]+), ([^)]+)\))
            

                table_matches4 = re.findall(table_pattern4, extracted_data3, re.MULTILINE)#, re.MULTILINE
                # print(';;;',table_matches4)
                if table_matches4:

                    columns = ['FRU', 'LNH', 'BOARD','RF', 'BP', 'TX (W/dBm)','VSWR (RL)','RX (dBm)','UEs/gUEs','Sector/AntennaGroup/Cells (State:CellIds:PCIs)']  ##     

                
                    table_df4 = pd.DataFrame(table_matches4, columns=columns,)#,
                    table_df4['Sector/AntennaGroup/Cells (State:CellIds:PCIs)'] = table_df4['Sector/AntennaGroup/Cells (State:CellIds:PCIs)'].str.replace(r'SE=\d+ AG=\d+', '', regex=True)
                    f3=table_df4['FRU'].str.replace('RRU-','')
                    f31=f3[0]
                    f32=f3[4]
                    f33=f3[8]
                    # print(f31,f32,f33,'asddfffjfjjjjj')
                    b3=table_df4['BOARD']
                    b31=b3[0]
                    b32=b3[4]
                    b33=b3[8]
                    # print(b31,b32,b33,'asddfffjfjjjjj')
                    global cell31,cell32,cell33
                    cell3=table_df4['Sector/AntennaGroup/Cells (State:CellIds:PCIs)']
                    # cell3=cell3.replace(r'SE=\d+ AG=\d+','')
                    cell31=cell3[0]
                    cell32=cell3[4]
                    cell33=cell3[8]
                    # print(cell31,cell32,cell33,'asddfffjfjjjjj')

                    # print(table_df4)

                    data23={
                    "Site_Id":globalSiteId_3,
                    'DATETIME': time_string3,
                    "CELL":(cell31,cell32,cell33),
                    "BOARD":(b31,b32,b33),
                    'FRU': (f31,f32,f33),
                    "VSWR1":"-",
                    "VSWR2":"-",
                    "VSWR3":"-",
                    "VSWR4":"-",
                    "VSWR5":"-",
                    "VSWR6":"-",
                    "VSWR7":"-",
                    "VSWR8":"-",
                    "DELTA1":"-",
                    "DELTA2":"-",
                    "DELTA3":"-",
                    "DELTA4":"-",
                    "Serial_Number":"-",
                    "FAULTS":"-",
                    "Op.State":"-",
                    "STATUS":"-"     
                }
                    print(data23,'asdflkjhg')

                    df4 = pd.DataFrame(data23 )
                    # print(df4,'asdflkjhg4321')
##################################################################################################################################################################################
                    
                    combined_table_df = pd.concat([df, df1,df4], ignore_index=True)
                    print(combined_table_df,'vswr')
                    
                    col_listing=combined_table_df.columns.to_list()[4:]
                    # print(col_listing,'collkjhgfdvbnn')
                    # dataReq=[]

                    color_thresholds = {
                        'CT': [ 1.36],
                        'UPNY_Direct': [ 1.38],
                        'UPNY_Rullex': [1.38],
                        'PH': [1.38],
                        'VA': [1.3],
                    }


                    

                    # newcoll=""
                    main_col=[]
                    def app_color(val):
                        if type(val)== type('hello'):

                            if val.strip() == 'DISABLED': 
                                # main_col.append(column['CELL'])
                                # bhjjk
                                
                                return f'<span class="shobhit" style="background-color: rgb(250, 9, 9);color:white;">{val}</span>'
                            else:
                                return ''
                    combined_table_df["Op.State"] = combined_table_df["Op.State"].apply(app_color)
                    print(main_col,'lkkjjj')


                    
                    arr_col=[]
                    for i in range(1,9):
                        arr_col.append('VSWR'+str(i))
                    
                    for i in range(1,5):
                        arr_col.append('DELTA'+str(i))

                    final_col_for_data=[]

                    def apply_colorNew(val):
                        for i in val:
                            if(type(i)==type("str")):
                                if("background-color: rgb(250, 9, 9);color:white;" in i):
                                    if(val["CELL"] not in final_col_for_data_vswr):
                                        final_col_for_data_vswr.append(val["CELL"])

                    final_col_for_data__delta=[]
                    def apply_colorNew__delta(val):
                        for i in val:
                            if(type(i)==type("str")):
                                if("background-color: rgb(250, 9, 9);color:white;" in i):
                                    if(val["CELL"] not in final_col_for_data__delta):
                                        final_col_for_data__delta.append(val["CELL"])

                        
                    def apply_color(val, column, start_end):
                        # print(type(val),val != '-',column[0]=='V',val > start_end[0],'lklklkl')
                        value=""
                        if column[0]=='V':
                            if val != '-':
                                val = float(val)
                            
                                if val > start_end[0]:
                                    value = f'background-color: rgb(250, 9, 9);color:white;' ### ,{Summary(column1)}
                                else:
                                    value = ""
                            else:
                                value = ""
                    
                        print("value =",value)


                        if column[0]=='D':
                            # xcvbnm,
                            if val != '-':
                                print(column)
                                val = float(val)
                                print(val,'zmhfnxbcv')

                                # xcvbnm
                                if val >5:
                                    value = f'background-color: rgb(250, 9, 9);color:white;'

                                else:
                                    value = ""
                        
                        return value
                    
                    
                    columns_to_style = col_listing
                    print(columns_to_style,'shobhitpppppp')
                    # brjjh
                    # Apply styling to the specified columns
                    for column in arr_col:
                        # print(column,'klkkkkk')

                        # print()


                        combined_table_df[column] = combined_table_df[column].apply(lambda x: f'<span class="shobhit" style="{apply_color("{:.2f}".format(x) if x!="-" else "-",column,color_thresholds[marketPlace])}">{"{:.2f}".format(x) if x!="-" else "-"}</span>')


                        # combined_table_df[column] = combined_table_df[column].apply(lambda x: f'<span class="shobhit" style="{apply_color(x,column,color_thresholds[marketPlace])}">{x}</span>')
                        
                    # print(combined_table_df["VSWR1"],'combined_table_dfcombined_table_dfcombined_table_df')

                    # addDataintoglobalDf("RSSI",column)
                    combined_table_df2 = combined_table_df.apply(apply_colorNew,axis=1)
                    combined_table_ = combined_table_df[["CELL","DELTA1","DELTA2","DELTA3","DELTA4"]].apply(apply_colorNew__delta,axis=1)
                    # combined_table_ = combined_table_df.apply(apply_colorNew__delta,axis=1)
                    # print(final_col_for_data__delta,'apply_colorNew__deltaapply_colorNew__delta')

                    addDataintoglobalDf('VSWR Delta',final_col_for_data__delta )
                    html_table = combined_table_df.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')
                    
                            
                        
                        # addDataintoglobalDf("VSWR",dataReq["CELL"].to_list())
                        # dsahkdsajdlksa
                    write_html_table("\n<h2>-----:VSWR:-----:</h2>\n \n" + html_table)

                else:
                    print("No matching table data found.")  
            else:
                print("No extracted data found.")

marketPlace = 'CT'
VSWR(file_path,marketPlace)
# bjjh
# brhh
# brbrbr
###########################################################################################################################################################
# column21=[]
# def testing(val):
#     column21.append(val)
#     print(column21,"sdjsagdjhgsadjhgdsaj")
# print("dhasgdsafslkjhfdslkjfdshjkdasdd",column21)
############################ RSSI ###############################################################################################################
file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
def RSSI(file_path):
    with open(file_path, 'r') as file:
        input_string = file.read()

        start_marker = r"""pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'"""
        end_marker = r"pst"

        start_index = input_string.find(start_marker)
        end_index = input_string.find(end_marker)
        extracted_data =input_string[start_index:end_index]
        # print('extracted_data',extracted_data)
        if extracted_data:
            start_marker1 = r"""pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'"""
            end_marker1 = globalSiteId+"> pmr -m 3 -r 206 | egrep -i 'Acc_InitialERabEstabSuccRate|Acc_InitialErabSetupSuccRate|Acc_InitialUEContextEstabSuccRate|Acc_RrcConnSetupSuccRate|Acc_S1SigEstabSuccRate|Ret_ERabRetainabilityRate|Ret_ErabRelAbnormal'"
            start_index = input_string.find(start_marker1)
            end_index = input_string.find(end_marker1)
            extracted_data =input_string[start_index:end_index]
            # print('extracted_data',extracted_data)

        if extracted_data:
                pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
                table_matche = re.findall(pattern, extracted_data, re.MULTILINE)
                if table_matche:
                    date = table_matche[0]
                    # print('date:::',date)
        if extracted_data:
            pattern = r'\b(\d{2}:\d{2})\s+(\w+_\w+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s'
            # print(extracted_data.find("Time  Counter"))
            
            table_matches1=extracted_data[extracted_data.find("Time  Counter"):]
            # print(table_matches1,"table_matches1")
            # vnvmjmjb
            # dsadsadsad
            # table_matches1= re.findall(pattern, extracted_data, re.MULTILINE)
            if table_matches1: 

                # print(table_matches1,"table_matches1")
                # columns = ['Time','Counter ','DIE04225A11','DIE04225A21','DIE04225A31','EIE04225A11','EIE04225A21','EIE04225A31'] #  
                table_df = pd.read_csv(io.StringIO(table_matches1), delim_whitespace=True)
                            
                table_df.insert(0, 'Date', date)
                col1=table_df.columns[3:]
                # print(col1,'col1col1col1col1col1')
                # table_df['Site Id']=globalSiteId
                # table_df = table_df[['Site Id','Time','Counter','DVA61251A11','DVA61251A21','DVA61251A31','LVA61251A11','LVA61251A21','LVA61251A31']]
####################################################################################################
    file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content = file.read()
        # print(content)

        start_marker = """pmr -m .5 -r 206 | egrep '(Int_RadioRecInterference)'"""
        end_marker = """pmxe -m 2 NRCellDU= Int_AvgRadioRecInterferencePwr$"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print("lkjihih",extracted_data)


        if extracted_data:
            pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
            table_matche = re.findall(pattern, extracted_data, re.MULTILINE)
            if table_matche:
                date = table_matche[0]
                # print('date:::',date)
        if extracted_data:
            pattern1 = r'\b(\d{2}:\d{2})\s+(\w+_\w+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s'
            
            table_matches1= re.findall(pattern1, extracted_data, re.MULTILINE)

            if table_matches1:
                columns = ['Time','Counter','DVA61251A11','DVA61251A21','DVA61251A31','LVA61251A11','LVA61251A21','LVA61251A31'] # 
                
                table_df1 = pd.DataFrame(table_matches1, columns=columns)
                
                # table_df['DVA61251A11']
                # print( list(table_df['DVA61251A11']),'++++++++++++++++++Shobhit++++++++++++++++')       
                table_df1.insert(0, 'Date', date)
                print(table_df, table_df1)



                threeCol=table_df.columns[:3].to_list()
                oneCol=table_df.columns[3:].to_list()
                twoCol=table_df1.columns[3:].to_list()

                print(threeCol,oneCol,twoCol)

                completeData=[]

                for i in threeCol:
                    completeData.append((i,""))

                
                for i in oneCol:
                    completeData.append((f"<div style='text-align:center;'>{globalSiteId}</div>",i))

                
                for i in twoCol:
                    completeData.append((f"<div style='text-align:center;'>{globalSiteId_3}</div>",i))

                print(completeData)
                # dwjdlksajlds
                combined_table_df = pd.concat([table_df, table_df1], ignore_index=True)
                for col in combined_table_df.columns:
                    print(col,'mnbzxc')
                    if 'NaN' in col:
  
                        combined_table_df[col] = combined_table_df[col].fillna('')

                # print(combined_table_df,"dsadsadsa")
                fkcol=""
                column1=[]
                def highlight_red(val):

                    print(val,fkcol,'shobhitpppa')
                    # val = float(val)
                    # dsadsadasdas
                    # print(val,val > -110 or val < -121,"highlight_red")
                    try:
                        # global column1
                        # column1 =[]
                        if fkcol[0]=="D" or fkcol[0]=="E":
                            print(column,'shobhitpppa')
                            val = float(val)
                            # dsadsadasdas
                            if val > -110 or val < -121:
                                column1.append(column)
                                # testing(column)
                                # print('global column222',column1)
                                # 'global column'
                                return f'<span class="shobhit" style="background-color: rgb(250, 9, 9);color:white;">{val}</span>' ### ,{Summary(column1)}
                            
                            else:
                                return val
                        else:

                            val = float(val)
                            if  val > -112.0 or val < -121.0 : ## val > -119.4 or
                                column1.append(column)
                                # testing(column)
                                # print('global column222',column1)
                                # 'global column'
                                return f'<span class="shobhit" style="background-color: rgb(250, 9, 9);color:white;">{val}</span>'
                            else:
                                return val
                    except ValueError:
                        return val

                col_listing=combined_table_df.columns.to_list()[2:]
                print('col_listingcol_listingcol_listing',col_listing)

                # ldasjdsjalkdlsajl
                columns_to_style = col_listing

                combined_table_df=combined_table_df.fillna('')



                # Apply styling to the specified columns
                for column in columns_to_style:

                    print(column)
                    fkcol=column
                    # if column.startswith("DIE") and column.startswith("EIE"):
                    combined_table_df[column] =combined_table_df[column].apply(highlight_red)



                addDataintoglobalDf("RSSI",column1)

                
                # dsadsadsadasdsadsa

                # table_dfnew1 = pd.DataFrame(columns=table_df.columns)

                # combined_table_df.columns = pd.MultiIndex.from_product([['Result'], table_df.columns],[['Result'], table_df.columns])
                
                print(combined_table_df.columns,completeData)
                combined_table_df.columns = pd.MultiIndex.from_tuples(completeData)
                

                html_tableFinal = combined_table_df.to_html(escape=False, index=False, table_id='styled_table', classes='table table-striped table-bordered')


                print(html_tableFinal)
                html_tableFinal=html_tableFinal.replace('<th>Date</th>','<th rowspan="2">Date</th>')
                html_tableFinal=html_tableFinal.replace('<th>Time</th>','<th rowspan="2">Time</th>')
                html_tableFinal=html_tableFinal.replace('<th>Counter</th>','<th rowspan="2">Counter</th>')
                html_tableFinal=html_tableFinal.replace('<th></th>','')
                print(html_tableFinal)
                # Replace the '<td>' tags to include 'style' attribute
                # html_tableFinal = html_table.replace('<td>', '<td style="text-align: center;">')
                # create_excel(combined_table_df,"RSSI")
                write_html_table("\n<h2>--------:RSSI--------:</h2>\n \n"+html_tableFinal)

RSSI(file_path)
# kkjjlki
############################################################################################################################################
 
 ###############--------:RSSI--------(LVA61251A):#######################################################################################################
# file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
# def alt(file_path3):
#         # file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
#     with open(file_path3, 'r') as file:
#         content = file.read()
#         # print(content)

#         start_marker = """pmr -m .5 -r 206 | egrep '(Int_RadioRecInterference)'"""
#         end_marker = """pmxe -m 2 NRCellDU= Int_AvgRadioRecInterferencePwr$"""

#         start_index = content.find(start_marker)
#         end_index = content.find(end_marker)
#         extracted_data = content[start_index:end_index]
#         # print("lkjihih",extracted_data)


#         if extracted_data:
#             pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
#             table_matche = re.findall(pattern, extracted_data, re.MULTILINE)
#             if table_matche:
#                 date = table_matche[0]
#                 # print('date:::',date)
#         if extracted_data:
#             pattern1 = r'\b(\d{2}:\d{2})\s+(\w+_\w+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s'
            
#             table_matches1= re.findall(pattern1, extracted_data, re.MULTILINE)

#             if table_matches1:
#                 columns = ['Time','Counter ','DVA61251A11','DVA61251A21','DVA61251A31','LVA61251A11','LVA61251A21','LVA61251A31'] # 

#                 table_df = pd.DataFrame(table_matches1, columns=columns)
#                 # table_df['DVA61251A11']
#                 # print( list(table_df['DVA61251A11']),'++++++++++++++++++Shobhit++++++++++++++++')
#                 table_df.insert(0, 'Date', date)
#                 # print('lklklk;;;;;;;',table_df)

#                 html_table = global_style + table_df.to_html(escape=False, index=False,
#                                                             table_id='styled_table',
#                                                             classes='table table-striped table-bordered')

#                 write_html_table("<h2>--------:RSSI--------(LVA61251A):</h2>"+html_table)

#                     # print("RSSI:\n", table_df)

# alt(file_path3) 
#######################################################################################################################################################################################################

############## X2 Link Status Start#############################################################################################################################
def X2_Link_Status_Start(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "hget ^TermPointToGNodeB= ip|administrativeState|operationalState"
        end_marker = "lst AntennaNearUnit"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print( extracted_data)

        if extracted_data:
            # table_pattern = r"^(\S)\s=(\S)\s"
            table_pattern = r"(NRNetwork=\d+,\w+=\w+,\w+=\w+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
            
            table_matches = re.findall(table_pattern, extracted_data, re.MULTILINE)

            if table_matches:
                columns = ['MO', 'administrativeState', 'ipsecEpAddress', 'ipv4Address', 'ipv6Address', 'operationalState', 'upIpAddress', 'usedIpAddress']
                table_df = pd.DataFrame(table_matches, columns=columns)
                # print("16th log:\n", table_df
                
                # print("16th log:\n", table_df)

                num_rows = len(table_df)
                # print(f"Number of rows: {num_rows}")


                ENABLED_count1 = 0
                DISABLED_count2 = 0

                for i in table_df['upIpAddress']:
                    if i == '(ENABLED)':
                        ENABLED_count1 += 1
                    elif i == '(DISABLED)':
                        DISABLED_count2 += 1
                    else:
                        print("Data not available")

                # print('Count of (ENABLED):',ENABLED_count1)
                # print('Count of (DISABLED):', DISABLED_count2)

                data= {"SiteID":[globalSiteId],
                    "Total No. of X2 Links":[num_rows],
                    "Total No.of Disabled X2 Link":[DISABLED_count2],
                    "ENABLED_count2":[ENABLED_count1]

                }

                df = pd.DataFrame(data)
                # print('ppp',df)

##################################
    file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path1, 'r') as file:
        content = file.read()

        start_marker1 = "hget ^TermPointToGNodeB= ip|administrativeState|operationalState"
        end_marker1 = "NIE04225A2> sts"

        start_index1 = content.find(start_marker1)
        end_index1 = content.find(end_marker1)
        extracted_data1 = content[start_index1:end_index1]
        # print('eeeeeeeeee', extracted_data1)

        if extracted_data1:
            # table_pattern = r"^(\S)\s=(\S)\s"
            table_pattern1 = r"(NRNetwork=\d+,\w+=\w+,\w+=\w+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
            
            table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

            if table_matches1:
                columns = ['MO', 'administrativeState', 'ipsecEpAddress', 'ipv4Address', 'ipv6Address', 'operationalState', 'upIpAddress', 'usedIpAddress']
                table_df1 = pd.DataFrame(table_matches1, columns=columns)
                # print("ooooooooooooooo:\n", table_df)
                
                print("ooooooooooooooo:\n", table_df1)

                num_rows1 = len(table_df1)
                # print(f"Number of rows: {num_rows1}")


                ENABLED_count3 = 0
                DISABLED_count4 = 0

                for i in table_df1['operationalState']:
                    print(i)
                    if i == '1':
                        ENABLED_count3 += 1
                    elif i == '0':
                        DISABLED_count4 += 1
                    else:
                        print("Data not available")

                # print('Count of (ENABLED)NIE04225A2>:',ENABLED_count3)
                # print('Count of (DISABLED)NIE04225A2>:', DISABLED_count4)

                data1= {"SiteID":[globalSiteId_2],
                    "Total No. of X2 Links":[num_rows1],
                    "Total No.of Disabled X2 Link":[DISABLED_count4],
                    "ENABLED_count2":[ENABLED_count3]

                }

                df1 = pd.DataFrame(data1)
                # print('pppppppppppppppp',df1)
######################################
                combined_table_df = pd.concat([df, df1], ignore_index=True)
                html_table = global_style +combined_table_df.to_html(escape=False, index=False,
                                                              table_id='styled_table',
                                                              classes='table table-striped table-bordered')

                write_html_table("\n<h2>-----:X2 Link Status Start:----:</h2>\n"+html_table)

            else:
                print("No matching table data found.")
        else:
            print("No extracted data found.")

X2_Link_Status_Start(file_path)
#####################################################################################################################################################

################# GNR CELL STATUS ##############################################################################################################################
final_col_for_data_pc=[]
file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
def GNR_CELL_STATUS(file_path):

    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"
        end_marker = "hget ^EUtranCellFDD|TDD|NBIOT cellid|rachroo|tac|earfcnd|earfcnul|cellrange|dlChannelBandwidth$|ulChannelBandwidth$"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print('table_matches',extracted_data)
        if extracted_data:
            table_pattern= r"(?:NRCellDU=(\S+))\s+(\d+\s+\(\w+\)|\s*)\s+(?:i\[1\] = (\d+))\s+(\d+\s+\(\w+)\)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+)\s+(?:\[1\] = (NRSectorCarrier=\S+))\s+(\d+)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+)"

            table_matches = re.findall(table_pattern, extracted_data, re.MULTILINE)
            # print("table_matches",table_matches)
            if table_matches:
                columns = ['MO', 'administrativeState', 'bandList', 'cellBarred', 'cellReservedForOperator','nRPCI' ,'nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']  ### 
                table_df = pd.DataFrame(table_matches, columns=columns)
                table_df['operationalState'] = table_df['operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df['administrativeState'] = table_df['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df['cellBarred'] = table_df['cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df['cellReservedForOperator'] = table_df['cellReservedForOperator'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')

                table_df['Site Id'] = globalSiteId
                table_df['cellRange'] = ''
                table_df = table_df[['Site Id','MO', 'administrativeState', 'bandList', 'cellBarred','cellRange', 'cellReservedForOperator','nRPCI','nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']]
                # print('(((((())))))',table_df)

    file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path1, 'r') as file:
        content = file.read()

        start_marker1 = "hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"
        end_marker1 = "hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"

        start_index1 = content.find(start_marker1)
        end_index1 = content.find(end_marker1)
        extracted_data1 = content[start_index1:end_index1]
        # print(extracted_data1)
        if extracted_data1:
            table_pattern1= r"(?:NRCellDU=(\S+))\s+(\d+\s+\(\w+\)|\s*)\s+\s*(?:i\[2\] = (\d+\s+\d+\s+))\s*+(\d+\s+\(\w+)\)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+)\s+(?:\[1\] = (NRSectorCarrier=\S+))\s+(\d+)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+)" ##  (\d+\s+\(\w+\)|\s*)

            # table_pattern1= r"(NRCellDU=\S+)\s+(\d+\s+\(UNLOCKED\))\s+\s*(?:i\[2\] = (\d+\s+\d+\s+))\s*+(\d+\s+\(\w+)\)\s+(\d+\s+\(NOT_RESERVED\))\s+(\d+)\s+(?:\[1\] = (NRSectorCarrier=\S+))\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\d+)"
            table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

            if table_matches1:
                columns = ['MO', 'administrativeState', 'bandList', 'cellBarred', 'cellReservedForOperator','nRPCI' ,'nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency'] 
                table_df1 = pd.DataFrame(table_matches1, columns=columns)
                table_df1['operationalState'] = table_df1['operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df1['administrativeState'] = table_df1['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df1['cellBarred'] = table_df1['cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df1['cellReservedForOperator'] = table_df1['cellReservedForOperator'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '') 
                table_df1['Site Id'] = globalSiteId_2
                table_df1['cellRange'] = ''
                

                table_df1 = table_df1[['Site Id','MO', 'administrativeState', 'bandList', 'cellBarred','cellRange', 'cellReservedForOperator','nRPCI','nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']]
               
                combined_table_df = pd.concat([table_df, table_df1], ignore_index=True)
                # print('combined_table_df',combined_table_df)
                # final_col_for_dat=[]
                def apply_colorNew(val):
                    for i in val :
                        if(type(i)==type("str")):
                            if("background-color: rgb(250, 9, 9); color:white;" in i) or ("background-color: orange;" in i) or ("background-color: rgb(250, 9, 9);" in i)  :
                                if(val["Site Id"]+" "+val["MO"] not in final_col_for_data_pc ):
                                    final_col_for_data_pc.append(val["Site Id"]+" "+val["MO"])
                                else:
                                    print('lkjhgfdsa')
                
                def apply_color(val):
                    if val.strip() == 'BARRED' or val.strip() == 'RESERVED':
                        return 'background-color: rgb(250, 9, 9); color:white;'
                    else:
                        return ''
                combined_table_df[['cellBarred', 'cellReservedForOperator']] = combined_table_df[['cellBarred', 'cellReservedForOperator']].applymap(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')
                # combined_table_df['cellBarred'], combined_table_df['cellReservedForOperator'] = combined_table_df['cellBarred'] or combined_table_df['cellReservedForOperator'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')

                def apply_color(row):
                    if row['administrativeState'].strip() == 'LOCKED' and row['operationalState'].strip() == 'DISABLED':
                        return 'background-color: orange;color:white;'
                    if not row['administrativeState'].strip() == 'LOCKED' and row['operationalState'].strip() == 'DISABLED':
                        return 'background-color: rgb(250, 9, 9);color:white;'
                    # if row['cellBarred'].strip() == 'BARRED':
                    #     return 'background-color: red;'
                    
                    else:
                        return ''

                combined_table_df['operationalState'] = combined_table_df.apply(lambda row: f'<span class="shobhit" style="{apply_color(row)}">{row["operationalState"]}</span>', axis=1)
                print(combined_table_df,'plmoknijb')
                combined_table_df2 = combined_table_df.apply(apply_colorNew,axis=1)
                print(final_col_for_data_pc,'final_col_for_data_pcfinal_col_for_data_pc')
                # bgcrd/
                # combined_table_df['cellBarred'] = combined_table_df['cellBarred'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')
                # if combined_table_df['administrativeState']
                # combined_table_df['operationalState'] = combined_table_df['operationalState'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')
                
                # styled_df =combined_table_df.style.apply(color_rows, axis=1)
                # print(styled_df,'styled_df')


                # html_table = combined_table_df.to_html(escape=False, index=False,
                #                                     table_id='styled_table',
                #                                     classes='table table-striped table-bordered')
                
                
                # addDataintoglobalDf('Cell Status',final_col_for_dat )

                html_table = combined_table_df.to_html(escape=False, index=False,
                                              table_id='styled_table',
                                              classes='table table-striped table-bordered')
                write_html_table("\n<h2>-----:5GNR CELL STATUS:-----:</h2>\n \n" + html_table)
            else:
                print("No matching table data found.")
        else:
            print("No extracted data found.")

GNR_CELL_STATUS(file_path)


############################################################################################################################################

###################### 5GNR ALARMS #####################################################################################################################

file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
def ALARMS(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "alt"
        end_marker = "get (^ENodeBFunction=1$|^GNBDUFunction=) ^gNBId$|^gNBIdLength$|^eNBId$"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print(extracted_data)
        if extracted_data:
            table_pattern =  r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w)\s+(..*Failure)\s+(.*)'
            # table_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(m)\s+(.+)\s+\(([^)]+)\)"
            # table_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'

            table_matches = re.findall(table_pattern, extracted_data, re.MULTILINE)

            if table_matches:
                columns = ['Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']  ### 
                table_df = pd.DataFrame(table_matches, columns=columns)

                table_df['Site Id'] = globalSiteId
                table_df = table_df[['Site Id','Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']]  ### 
                
                
                print("]]]]]]]]]]]]]]]]]]]]]\n",table_df)

    file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker1 = "alt"
        end_marker1 = "get (^ENodeBFunction=1$|^GNBDUFunction=) ^gNBId$|^gNBIdLength$|^eNBId$"

        start_index1 = content.find(start_marker1)
        end_index1 = content.find(end_marker1)
        extracted_data1 = content[start_index1:end_index1]
        # print(extracted_data1)
        if extracted_data1:
            # Define regex pattern to extract data
            table_pattern1= r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w)\s+(.*.*Failure)\s+(.*)'  #+\(([^)]+)\)
            # table_pattern1 = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(m)\s+(\S+)\s+(.+)\s+\(([^)]+)\)"

            # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))?\s+(\d+\s+\(\w+\))?\s+(.*)$'

            # table_pattern1 = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s;(\w+)\s; (\w+ \w+ \w+)\s;(.+)'

            # Find matches using the regex pattern
            table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

            if table_matches1:
                columns = ['Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']  ### 
                table_df1 = pd.DataFrame(table_matches1, columns=columns)

                table_df1['Site Id'] = globalSiteId_2
                table_df1 = table_df1[['Site Id','Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']]  ### 
                
    file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content = file.read()
        if content:
            start_marker2= "alt"
            end_marker2 = "get (^ENodeBFunction=1$|^GNBDUFunction=) ^gNBId$|^gNBIdLength$|^eNBId$"

            start_index2 = content.find(start_marker2)
            end_index2 = content.find(end_marker2)
            extracted_data2 = content[start_index2:end_index2]
            # print(extracted_data1)
            if extracted_data2:
                # Define regex pattern to extract data
                table_pattern2 =  r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w)\s+(.*.*Failure)\s+(.*)'

                table_matches2 = re.findall(table_pattern2, extracted_data2, re.MULTILINE)

                if table_matches2:
                    columns = ['Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']  ### 
                    table_df2 = pd.DataFrame(table_matches2, columns=columns)

                    table_df2['Site Id'] = globalSiteId_3
                    table_df2 = table_df2[['Site Id','Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']]  ### 
                    
                    combined_table_df = pd.concat([table_df, table_df1,table_df2], ignore_index=True)
                    # print('z,mnbxvxmmcmnm',combined_table_df)
                # print(combined_table_df.columns,'///////')


                    # print(len(combined_table_df),'mkmkmk')
                    
                    if len(combined_table_df)>0:
                        filtered=combined_table_df[combined_table_df["Specific Problem"]!="External Link Failure"]
                        addDataintoglobalDf('Alarms', [filtered.to_string(index=False, header=False).replace("\n","<br>")])
                        
                    #     addDataintoglobalDf('Alarms', [combined_table_df.to_string(index=False, header=False)).replace("\n","<br>")])
                    #     print('ALARMS', combined_table_df)
                    # else:
                    #     print('no')

                html_table = combined_table_df.to_html(escape=False, index=False,
                                              table_id='styled_table',
                                              classes='table table-striped table-bordered')
                write_html_table("\n<h2>-----:-----:ALARMS:-----::-----:</h2>\n \n" + html_table)
   

            else:
                print("No matching table data found.")
        else:
            print("No extracted data found.")


ALARMS(file_path)
# fgjljug
#####################################################################################################################################

#################### 5GNR GPS AND SYNC #########################################################################################################
def extract_data18(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "st sync"
        end_marker = "get . noofsat"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]

        if extracted_data:  ##   (\d+\s+\(UNLOCKED\)|[^;])\s
            table_pattern = r'(\d+)\s+(\d+\s+\(\w+\)|\s*)\s+\s*(\d+\s+\(\w+\)|\s*)\s+(.*)$'

            # table_pattern = r'(\d+)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+\s+\(\w+\)|\s*)\s+(.*)$'
            # table_pattern = r'(\d+)\s+(\S+\s+\(.*\)|\s*)\s+(\S+\s+\(.*\)|\s*)\s+(.*)$'
            # table_pattern = r'^(\d+)\s+(\d+\s+\(UNLOCKED\)|\d+\s+\(ENABLED\)|"-")\s+(\d+\s+\(UNLOCKED\)|\d+\s+\(ENABLED\)|"-")\s+(.*)$'

            # Define regex pattern to extract data
            # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))\s+(\d+\s+\(\w+\))?\s+(.*)$'
            # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))?\s+(\d+\s+\(\w+\))?\s+(.*)$'

            
            table_matches = re.findall(table_pattern, extracted_data, re.MULTILINE)

            if table_matches:
                columns = ['Proxy', 'Adm State', 'Op. State', 'MO']

                table_df = pd.DataFrame(table_matches, columns=columns)
                table_df['Adm State'] = table_df['Adm State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df['Op. State'] = table_df['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df['Site Id'] = globalSiteId
                table_df = table_df[['Site Id','Proxy', 'Adm State', 'Op. State', 'MO']]
                # table_df['Adm State'] = table_df.apply(lambda row: row['Adm State'] if 'UNLOCKED' in row['Op. State'] else '', axis=1)
                # table_df['Op. State'] = table_df.apply(lambda row: row['Op. State'] if 'ENABLED' in row['Adm State'] else '', axis=1)
                # print("18th log:")
                # print("]]]]]]]]]]]]]]]]]]]]]\n",table_df)


############
    file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path1, 'r') as file:
        content = file.read()

        start_marker1 = "st sync"
        end_marker1 = "get . noofsat"

        start_index1 = content.find(start_marker1)
        end_index1 = content.find(end_marker1)
        extracted_data1 = content[start_index1:end_index1]
        # print('aaaaaaaaaa',extracted_data1)
        if extracted_data1:
            # Define regex pattern to extract data
            
            # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))?\s+(\d+\s+\(\w+\))?\s+(.*)$'
            # table_pattern1 = r'(\d+)\s+(\d+\s+\(\w+\))\s+(\d+\s+\(\w+\))\s+(.*)$'
            # table_pattern1 = r'(\d+)\s+(\d+\s+\(UNLOCKED\)|[^;])\s+(\d+\s+\(ENABLED|DISABLED\))\s+(.*)$'  #  (\d+\s+\(ENABLED\)|\(DISABLED\))\s+(.*)$

            # table_pattern1 = r'(\d+)\s+(\d+\s+\(UNLOCKED\)|[^;])\s+(\d+\s+\(ENABLED\)|\(DISABLED\))\s\s+(.*)$'

            table_pattern1 = r'^\s*(\d+)\s*(\d+\s+\(UNLOCKED\)|[^;])\s+(\d+\s+\(\w+\)|\s*)\s+(.*)$'  ## (\d+\s+\(\w+\)|\s*)(\d+\s+\(\w+)\)

            # table_pattern1 = r'(\d+)\s+(\d+\s+\(UNLOCKED\)|[^;])\s+(\d+\s+\(ENABLED|DISABLED\))\s+(.*)$'


            # Find matches using the regex pattern
            table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

            # print(table_matches1)
            if table_matches1:
                columns = ['Proxy', 'Adm State', 'Op. State', 'MO']   
                table_df1 = pd.DataFrame(table_matches1, columns=columns) 

                table_df1['Adm State'] = table_df1['Adm State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df1['Op. State'] = table_df1['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')  
                # print('table_df1\n',table_df1)

                table_df1['Adm State'] = table_df1['Adm State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df1['Op. State'] = table_df1['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df1['Site Id'] = globalSiteId_2
                table_df1 = table_df1[['Site Id','Proxy', 'Adm State', 'Op. State', 'MO']]  ### 
                
                # print("18th log:")
                # print("]]]]]]]]]]]]]]]]]]]]]\n",table_df1)

##########################################################
    file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content = file.read()
        # print('content',content)
        start_marker2 = "st sync"
        end_marker2 = "get ^RadioEquipmentClock= ^radioClockState$"

        start_index2 = content.find(start_marker2)
        end_index2 = content.find(end_marker2)
        extracted_data2 = content[start_index2:end_index2]
        # print('aaaaaaaaaa',extracted_data2)
        if extracted_data2:


            # table_pattern2 = r'(\d+)\s+()\s+(\d+\s+\(ENABLED\))\s(.*)'

            table_pattern2 = r'(\d+)\s+()\s+(\d+\s+\(\w+\)|\s*)\s(.*)'

            table_matches2 = re.findall(table_pattern2, extracted_data2, re.MULTILINE)

            if table_matches2:
                columns = ['Proxy', 'Adm State', 'Op. State', 'MO']   ### 
                table_df2 = pd.DataFrame(table_matches2, columns=columns)  ##
                table_df2['Adm State'] = table_df2['Adm State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df2['Op. State'] = table_df2['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df2['Site Id'] = globalSiteId_3
                table_df2 = table_df2[['Site Id','Proxy', 'Adm State', 'Op. State', 'MO']]  ### 
                
                # print("18th log:")
                # print("]]]]]]]]]]]]]]]]]]]]]\n",table_df2)

                

                combined_table_df = pd.concat([table_df, table_df1,table_df2], ignore_index=True)
                # print(combined_table_df,'eeeeerrrooorr')

                def apply_color(row):
                    if row['Adm State'].strip() == 'LOCKED' and row['Op. State'].strip() == 'DISABLED':
                        return 'background-color: orange;color:white;'
                    if not row['Adm State'].strip() == 'LOCKED' and row['Op. State'].strip() == 'DISABLED':
                        return 'background-color:rgb(250, 9, 9);color:white;'
                    # if row['cellBarred'].strip() == 'BARRED':
                    #     return 'background-color: red;'
                    
                    else:
                        return ''

                # Apply the function to the DataFrame
                combined_table_df['Op. State'] = combined_table_df.apply(lambda row: f'<span class="shobhit" style="{apply_color(row)}">{row["Op. State"]}</span>', axis=1)

                
                # def apply_color(val):

                #     if val.strip() == 'ENABLED':
                #         return 'background-color: red;'
                #     if val.strip() == 'DISABLED':
                #         return 'background-color: green;'
                #     else:
                #         return ''
                # combined_table_df['Op. State'] = combined_table_df['Op. State'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')

                # combined_table_df['Op. State'] = combined_table_df['Adm State']

                # # Remove the unnecessary characters from 'Adm State'
                # combined_table_df['Adm State'] = combined_table_df['Adm State'].str.replace(r'^\d+\s+\((\w+)\)$', r'\1', regex=True)

                # Print the modified DataFrame
                # print(combined_table_df)

#############



                html_table = combined_table_df.to_html(escape=False, index=False,
                                              table_id='styled_table',
                                              classes='table table-striped table-bordered')
                # print('qqqqqqqq',html_table)
                write_html_table("\n<h2>-----: GPS AND SYNC:-----:</h2>\n \n" + html_table)
                # secondLog = table_df.to_string(index=False)
                # write_data("\n-----:5GNR GPS AND SYNC:-----:\n" + secondLog)
            else:
                print("No matching table data found.")
        else:
            print("No extracted data found.")
extract_data18(file_path)

#################################################################################################################################

################ ALARMS ####################################################################################################################

def ANTENNANEARUNIT(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
####################################################################

        start_marker1 = """lst AntennaNearUnit"""
        end_marker1 = """hget ^AntennaNearUnit= ^rfPortRef$|^onUnitUniqueId$|^uniqueId$"""

        start_index1 = content.find(start_marker1)
        end_index1 = content.find(end_marker1)
        extracted_data1 = content[start_index1:end_index1]
        # print(extracted_data)


        if extracted_data1:
            table_pattern11= r'(\d+)\s+(\d+\s+\([^)]+\))\s+(\d+\s+\([^)]+\))\s+([^\n]+)(?:\s+RetSubUnit=\d+)?'
            # table_pattern11 =r'^\s*(\d+)\s+(\d+ \(\w+\)|\s*)' ## +(\d+\s+((LOCKED)|(UNLOCKED))\s*)\s+(\d+\s+\(\w+\)|\s*)\s+(.*)$
            # table_pattern11 = r"^(\d+)\s*;(\d+\s+\(\w+\)|\s*)\s*;\s*(\d+\s+\(\w+\)|\s*)\s*;(.*)\s"
            
            table_matches11= re.findall(table_pattern11, extracted_data1, re.MULTILINE)

            if table_matches11:
                columns = ['Proxy','Adm State','Op. State','MO'] # ,'Op. State','MO'
 
                table_df1 = pd.DataFrame(table_matches11, columns=columns)
                adm=table_df1['Adm State'] = table_df1['Adm State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                op=table_df1['Op. State'] = table_df1['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                print(adm,"\n",op,'llllkkkmmmnnbb')
                print(table_df1,'antennanearunit45436')

#############################################################################

        start_marker = """hget ^AntennaNearUnit= ^rfPortRef$|^onUnitUniqueId$|^uniqueId$"""
        end_marker = """hget ^RetSubUnit= ^electricalAntennaTilt$|^iuantAntennaModelNumber$|^iuantBaseStationId$|^maxTilt$|^minTilt$|^operationalState$|^tiltChangeStatus$|^userLabel$"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print(extracted_data)


        if extracted_data:
            table_pattern1 = r"^(AntennaUnitGroup=\d+-\d+,AntennaNearUnit=\d+).*(RF\d+-\w+).*(FieldReplaceableUnit=\d-\d).*(RfPort=\w+\s+RF\d+-\w+)$"
            
            table_matches1= re.findall(table_pattern1, extracted_data, re.MULTILINE)

            if table_matches1:
                columns = ['MO ','onUnitUniqueId','rfPortRef','uniqueId'] #,'rfPortRef','uniqueId'
 
                table_df = pd.DataFrame(table_matches1, columns=columns)
                # print(table_df)


                table_df['Site Id'] = globalSiteId
                table_df['Adm State'] = adm
                table_df['Op. State']=op
                table_df['iuantDeviceType']=''
                table_df['ProductNumber']=''
                table_df['SerialNumber']=''
            # Reorder columns
                table_df = table_df[[ 'Site Id','MO ','Adm State','Op. State','iuantDeviceType','onUnitUniqueId','rfPortRef','uniqueId','ProductNumber','SerialNumber']]
                def apply_color(row):
                    if row['Adm State'].strip() == 'LOCKED' and row['Op. State'].strip() == 'DISABLED':
                        return 'background-color: orange;color:white;'
                    if not row['Adm State'].strip() == 'LOCKED' and row['Op. State'].strip() == 'DISABLED':
                        return 'background-color:rgb(250, 9, 9);color:white;'
                    # if row['cellBarred'].strip() == 'BARRED':
                    #     return 'background-color: red;'
                    
                    else:
                        return ''

                # Apply the function to the DataFrame
                table_df['Op. State'] = table_df.apply(lambda row: f'<span class="shobhit" style="{apply_color(row)}">{row["Op. State"]}</span>', axis=1)
                # print(table_df)
                html_table = global_style + table_df.to_html(escape=False, index=False,
                                                          table_id='styled_table',
                                                          classes='table table-striped table-bordered')

                write_html_table("<h2>-----: ANTENNANEARUNIT:-----:</h2>"+html_table)

            else:
                print("No matching table data found.")
        else:
            print("No extracted data found.")


ANTENNANEARUNIT(file_path)
############################################################################################################################################################################

##################### RET ############################################################################################################################################################

def ret(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = """hget ^RetSubUnit= ^electricalAntennaTilt$|^iuantAntennaModelNumber$|^iuantBaseStationId$|^maxTilt$|^minTilt$|^operationalState$|^tiltChangeStatus$|^userLabel$"""
        end_marker = """hget ^TmaSubUnit= ^tmaType$|^iuantAntennaModelNumber$|^iuantBaseStationId$|^dlAttenuation$|^dlTrafficDelay$|^operationalState$|^ulGain$|^userLabel$|^ulTrafficDelay$"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print(extracted_data)

        if extracted_data:
            table_pattern1 = r'(AntennaUnitGroup=\d+-\d+,AntennaNearUnit=\d+,RetSubUnit=\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+\s+\(\w+\)|\s*)\s+(\S+)'
            
            table_matches1= re.findall(table_pattern1, extracted_data, re.MULTILINE)

            if table_matches1:
                columns = ['MO','electricalAntennaTilt','iuantAntennaModelNumber','iuantBaseStationId','maxTilt','minTilt','operationalState','tiltChangeStatus',' userLabel'] #,'rfPortRef','uniqueId'
                
                table_df = pd.DataFrame(table_matches1, columns=columns)
                # print(table_df) 
                table_df['operationalState'] = table_df['operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df['tiltChangeStatus'] = table_df['tiltChangeStatus'].str.replace(r'(', '').str.replace(')', '').str.replace('3', '')

                table_df['Site Id'] = globalSiteId

                table_df = table_df[[ 'Site Id','MO','electricalAntennaTilt','iuantAntennaModelNumber','iuantBaseStationId','maxTilt','minTilt','operationalState','tiltChangeStatus',' userLabel']]

                final_col_for_data=[]


                def apply_colorNew(val):
                    for i in val:
                        if(type(i)==type("str")):
                            if("background-color: rgb(250, 9, 9);color:white;" in i):
                                if(val["Site Id"]+" "+val["MO"] not in final_col_for_data):
                                    final_col_for_data.append(val["Site Id"]+" "+val["MO"])

                    

                def apply_color(val):

                    if val.strip() == 'DISABLED' or val.strip() == 'abcd' :
                        return 'background-color: rgb(250, 9, 9);color:white; '
                    else:
                        return ''
                table_df['operationalState'] = table_df['operationalState'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')
                table_df['tiltChangeStatus'] = table_df['tiltChangeStatus'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')

                column=table_df.columns.to_list()
                # print(column,'columnnhgnnnnnnnnn')

                # print(table_df)
                # if table_df['operationalState'] == "'background-color: rgb(250, 9, 9);color:white;' " or table_df['tiltChangeStatus'] == "'background-color: rgb(250, 9, 9);color:white;' ":

                # print(table_df['operationalState'])
                # table_df['substring_found'] =table_df['operationalState'].str.contains("background-color")

                
                combined_table_df2 = table_df.apply(apply_colorNew,axis=1)
                # print(table_df['substring_found'])

                print(final_col_for_data)
                
                addDataintoglobalDf("RET",final_col_for_data)
                # dsadsadsadsadsa
                # condition = pd.concat([table_df['background-color: rgb(250, 9, 9);color:white;' in table_df['operationalState'].str.strip()],table_df[ 'background-color: rgb(250, 9, 9);color:white;' in table_df['tiltChangeStatus'].str.strip()]])
                # print(condition,'condition')

                # filtered_rows = table_df[condition]
                # print(filtered_rows,'filtered_rows')
                # site_ids = filtered_rows['Site Id']
                # print(site_ids,'mlnjbffcssza')







                html_table = table_df.to_html(escape=False, index=False,
                                                          table_id='styled_table',
                                                          classes='table table-striped table-bordered')

                write_html_table("<h2>-----: RET Status:-----:</h2>\n"+html_table)

                # # print("RetSubUnit:\n", table_df)

            else:
                print("No matching table data found.")
        else:
            print("No extracted data found.")

ret(file_path)

############################################################################################################################################################

###################### SECTOR STATUS ################################################################################################################################

def SECTOR_STATUS(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"
        end_marker = "hget ^SectorEquipmentFunction= administrativeState|operationalState|availableHwOutputPower|reservedBy"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        data_lines = []
        lines = extracted_data.strip().split('\n')

        for line in lines:
            if not line.startswith('#'):
                data_lines.append(line)
            # print("djwifhuhkjdjhbhbjf",line)
        data_text = '\n'.join(data_lines)
        # print( data_text)
# extract_data(file_path)        

        for i,li in enumerate(data_lines):
            
            if(li=="================================================================================================================="):
                # print(f"Line index: {i}")
                # print(li, "data_lines")

                if i == 6 :
                    table_pattern = r"(\S+)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+\s+\(\w+\)|\s*)\s\s+(?:\[1\]\s*=\s*( ))"  ### (\d+\s+\(\w+\)|\s*)
                    # table_pattern = r"(\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(?:\[1\]\s*=\s*( ))"
                    table_matches = re.findall(table_pattern, content, re.MULTILINE)
                    if table_matches:
                        columns = ['MO', 'administrativeState', 'arfcnDL', 'arfcnUL', 'bSChannelBwDL', 'bSChannelBwUL', 'configuredMaxTxPower', 'operationalState', 'reservedBy']
                        table_df = pd.DataFrame(table_matches, columns=columns)
                        table_df['administrativeState'] = table_df['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                        table_df[ 'operationalState'] = table_df[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                        table_df['Site Id'] = globalSiteId

                # Reorder columns
                        table_df = table_df[[ 'Site Id','MO', 'administrativeState', 'arfcnDL', 'arfcnUL', 'bSChannelBwDL', 'bSChannelBwUL', 'configuredMaxTxPower', 'operationalState', 'reservedBy']]
    file_path = "C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker1 = "hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"
        end_marker1 = "hget ^SectorEquipmentFunction= administrativeState|operationalState|availableHwOutputPower|reservedBy"

        start_index1 = content.find(start_marker1)
        end_index1 = content.find(end_marker1)
        extracted_data1 = content[start_index1:end_index1]
        data_lines = []
        lines = extracted_data1.strip().split('\n')

        for line in lines:
            if not line.startswith('#'):
                data_lines.append(line)
            # print("djwifhuhkjdjhbhbjf",line)
        data_text = '\n'.join(data_lines)
        # print( data_text)
# extract_data(file_path)        

        for i,li in enumerate(data_lines):
            
            if(li=="================================================================================================================="):
                # print(f"Line index: {i}")
                # print(li, "data_lines")

                if i == 6 :
                    table_pattern1 = r"(\S+)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+\s+\(\w+\)|\s*)\s+(?:\[1\]\s*=\s*(NRCellDU=\S+))"  ##  (\d+\s+\(\w+\)|\s*)

                    # table_pattern1 = r"(\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(?:\[1\]\s*=\s*(NRCellDU=\S+))"
                    table_matches1 = re.findall(table_pattern1, content, re.MULTILINE)
                    if table_matches1:
                        columns = ['MO', 'administrativeState', 'arfcnDL', 'arfcnUL', 'bSChannelBwDL', 'bSChannelBwUL', 'configuredMaxTxPower', 'operationalState', 'reservedBy']
                        table_df1 = pd.DataFrame(table_matches1, columns=columns)
                        table_df1['administrativeState'] = table_df1['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                        table_df1[ 'operationalState'] = table_df1[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                # table_df1['Op. State'] = table_df1['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                        table_df1['Site Id'] = globalSiteId_2
                        # print('12222222222222222222@@@@@@@@@@',table_df1)
                        combined_table_df = pd.concat([table_df, table_df1], ignore_index=True)

                        def apply_color(row):
                            if row['administrativeState'].strip() == 'LOCKED' and row['operationalState'].strip() == 'DISABLED':
                                return 'background-color: orange;color:white;'
                            if not row['administrativeState'].strip() == 'LOCKED' and row['operationalState'].strip() == 'DISABLED':
                                return 'background-color: rgb(250, 9, 9);color:white;'
                            else:
                                return ''

                        # Apply the function to the DataFrame
                        combined_table_df['operationalState'] = combined_table_df.apply(lambda row: f'<span class="shobhit" style="{apply_color(row)}">{row["operationalState"]}</span>', axis=1)

                        # table_df['operationalState'] = table_df['operationalState'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')

                # Add global styles if needed
                        # global_style = '<style>/* Your global CSS styles here */</style>'



                        html_table = global_style + combined_table_df.to_html(escape=False, index=False,
                                                              table_id='styled_table',
                                                              classes='table table-striped table-bordered')

                        write_html_table("\n<h2>-----:-----:NR SECTOR CARRIER STATUS:-----::-----:</h2>\n \n"+html_table)
                        # print("6th log::\n", combined_table_df)
                        

                    else:
                        print("No matching data found.")


SECTOR_STATUS(file_path)

###########################################################################################################################################
#################### LTE SECTOR CARRIER STATUS ############################################################################
def LTE_SECTOR(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = """hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""
        end_marker = """hget sec noof"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print(extracted_data)

        if extracted_data:
            table_pattern1 = r'(SectorCarrier=\d+\-\d+\-\d+)\s+(\d{5})\s+(\d+\s+\(\w+\)|\s*)\s+(?:\[2\]\s*=\s*(.*)$)'
            # table_pattern1 = r'(SectorCarrier=\d+\-\d+\-\d+)\s+(\d{5})\s+(\d+\s+\(\w+\)|\s*)\s+(\[2\]\s*=\s*(.*)$)' ######  \s+(?:\[1\]\s*=\s*))
            
            table_matches1= re.findall(table_pattern1, extracted_data, re.MULTILINE)

            if table_matches1:
                columns = ['MO','configuredMaxTxPower','operationalState','reservedBy'] #  
                
                table_df = pd.DataFrame(table_matches1, columns=columns)
                print(table_df,'sssjsjiuiwuiehebshdh')
                table_df['operationalState'] = table_df['operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df['Site Id'] = globalSiteId
                table_df = table_df[[ 'Site Id','MO','configuredMaxTxPower','operationalState','reservedBy']]
######################################################################################################################################\

    file_path3 = "C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content2 = file.read()

        start_marker2 = """hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""
        end_marker2 = """hget ^SectorEquipmentFunction= administrativeState|operationalState|availableHwOutputPower|reservedBy"""

        start_index2 = content2.find(start_marker2)
        end_index2 = content2.find(end_marker2)
        extracted_data2 = content2[start_index2:end_index2]
        # print(extracted_data2,'22222')

        if extracted_data2:
            table_pattern2 = r'(SectorCarrier=\d+)\s+(\d{5})\s+(\d+\s+\(\w+\)|\s*)\s+(?:\[\d+\]\s*=\s*(.*)$)'

            # table_pattern2 = r'(SectorCarrier=\d+)\s+(\d{5})\s+(\d+\s+\(\w+\)|\s*)\s+(?:\[(3|2)\]\s*=\s*(.*)$)'
            # table_pattern2 = r'(SectorCarrier=\d+)\s+(\d{5})\s+(\d+\s+\(\w+\)|\s*)\s+(?:\[(3|2)\]\s*=\s*(.*)$)'
            # table_pattern1 = r'(SectorCarrier=\d+\-\d+\-\d+)\s+(\d{5})\s+(\d+\s+\(\w+\)|\s*)\s+(\[2\]\s*=\s*(.*)$)' ######  \s+(?:\[1\]\s*=\s*))
            
            table_matches2= re.findall(table_pattern2, extracted_data2, re.MULTILINE)

            if table_matches2:
                columns = ['MO','configuredMaxTxPower','operationalState','reservedBy'] #  
                
                table_df2 = pd.DataFrame(table_matches2, columns=columns)
                print(table_df2,'sssjsjiuiwuiehebshdh')
                table_df2['operationalState'] = table_df2['operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df2['Site Id'] = globalSiteId_3
                table_df2 = table_df2[[ 'Site Id','MO','configuredMaxTxPower','operationalState','reservedBy']]
##################################################################################################################################################
                combined_table_df = pd.concat([table_df, table_df2], ignore_index=True)

                def apply_color(val):

                    if val.strip() == 'DISABLED':
                        return 'background-color: rgb(250, 9, 9);color:white; '
                    else:
                        return ''
                combined_table_df['operationalState'] = combined_table_df['operationalState'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')
                html_table = global_style + combined_table_df.to_html(escape=False, index=False,
                                                          table_id='styled_table',
                                                          classes='table table-striped table-bordered')

                write_html_table("<h2>-----:LTE SECTOR CARRIER STATUS:-----:</h2>\n"+html_table)

                # # print("RetSubUnit:\n", table_df)

            else:
                print("No matching table data found.")
        else:
            print("No extracted data found.")

LTE_SECTOR(file_path)


#########################################################################################################################################

#####################  5GNR RILINK  ######################################################################################################


def RILINK(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "hget rilink RiLinkId|linkRate|operationalState|riPortRef1|riPortRef2"
        end_marker = "hget sfp prod"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data1 = content[start_index:end_index]

        if extracted_data1:
            table_pattern1 = r"(.+?)\s+(\d+)\s+(\d+\s+\(\w+\)|\s*)\s+(.+?)\s+(.+?)\s+(.+)$"
            table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

            columns = [ 'MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']
            table_df1 = pd.DataFrame(table_matches1, columns=columns)
            table_df1[ 'operationalState'] = table_df1[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
            table_df1['Site Id'] = globalSiteId
            table_df1 = table_df1[['Site Id','MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']]

    file_path = "C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "hget rilink RiLinkId|linkRate|operationalState|riPortRef1|riPortRef2"
        end_marker = "hget sfp prod"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data2 = content[start_index:end_index]
        # print('lllllll', extracted_data2)



    if extracted_data2:
        table_pattern2 = r"(.+?)\s+(\d+)\s+(\d+\s+\(\w+\)|\s*)\s+(.+?)\s+(.+?)\s+(.+)$"
        table_matches2 = re.findall(table_pattern2, extracted_data2, re.MULTILINE)

        if table_matches2:
            table_df2 = pd.DataFrame(table_matches2, columns=columns)  # Use the same columns as table_df1
            table_df2[ 'operationalState'] = table_df2[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
            # print('klllllllkklklk', table_df2)
            table_df2['Site Id'] = globalSiteId_2

            combined_table_df = pd.concat([table_df1, table_df2], ignore_index=True)

            # def apply_color(val):

            #     if val.strip() == 'DISABLED':
            #         return 'background-color:rgb(250, 9, 9);color:white; '
            #     else:
            #         return ' '
            # combined_table_df['operationalState'] = combined_table_df['operationalState'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')

            # html_table = combined_table_df.to_html(escape=False, index=False, table_id='styled_table',
            #                                         classes='table table-striped table-bordered')

            # write_html_table("\n<h2>-----:RILINK:-----:</h2>\n \n" + html_table)

        else:
            print("No matching table data found.")
    else:
        print("No extracted data found.")
#########################################################################################
    file_path3 = "C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content3 = file.read()

        start_marker = "hget ^RiLink= fronthaulDeviceLineRate|linkRate|operationalState|riPortRef1|riPortRef2|transportType"
        end_marker = "get EUtranCellRelation esCellCaConfigurationAvail 3"

        start_index = content3.find(start_marker)
        end_index = content3.find(end_marker)
        extracted_data2 = content3[start_index:end_index]
        # print('lllllll', extracted_data2)



    if extracted_data2:
        table_pattern3 = r"(RiLink=\d+)\s+(\d+\s+\(\w+\))\s+(\d+)\s+(\d+\s+\(\w+\)|\s*)\s+(FieldReplaceableUnit=\d+,RiPort=\w+)\s+(FieldReplaceableUnit=\S+,RiPort=\S+)"
        table_matches3 = re.findall(table_pattern3, extracted_data2, re.MULTILINE)

        if table_matches2:
            columns=['MO','fronthaulDeviceLineRate','linkRate','operationalState','riPortRef1','riPortRef2']
            table_df3 = pd.DataFrame(table_matches3, columns=columns)  # Use the same columns as table_df1
            table_df3[ 'operationalState'] = table_df3[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
            qw=table_df3['MO'].str.replace('RiLink=','')
            table_df3.drop(columns=['fronthaulDeviceLineRate'], inplace=True)
            table_df3['Site Id'] = globalSiteId_3
            table_df3['riLinkId'] = qw

            # table_df3.to_csv("dsadsada.csv")

            # print(table_df3['fronthaulDeviceLineRate'])

            # print(table_df3)
            # saSasASas
            
            table_df3 = table_df3[['Site Id','MO','linkRate','riLinkId','operationalState','riPortRef1','riPortRef2']]
            # print('klllllllkklklk\n', table_df3)
            

            combined_table_df = pd.concat([table_df1, table_df2,table_df3], ignore_index=True)
            # print(combined_table_df)

            def apply_color(val):

                if val.strip() == 'DISABLED':
                    return 'background-color:rgb(250, 9, 9);color:white; '
                else:
                    return ' '
            combined_table_df['operationalState'] = combined_table_df['operationalState'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')

            html_table = combined_table_df.to_html(escape=False, index=False, table_id='styled_table',
                                                    classes='table table-striped table-bordered')

            write_html_table("\n<h2>-----:RILINK:-----:</h2>\n \n" + html_table)

        else:
            print("No matching table data found.")
    else:
        print("No extracted data found.")
#################################################################################################################

RILINK(file_path)
######################################################################################################################################################

####################  _+_+_+_+_+_+_+_+_+_+:----- #######################################################################################
final_col_for_data_loss=[]

def extract_data455(file_path,marketPlace):
    # print(marketPlace ,"______")
  
    
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = """ sdir"""
        end_marker = """ hget . allowedplmnlist"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]   
        # print( "lkkhh",extracted_data)

        if extracted_data:
            start_marker1 = """..........
+--------+                  +----------------+"""
            end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

            
hget . allowedplmnlist"""
            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]
            # print( "lllllmmmmmnnnn\n",extracted_data1)

            if extracted_data1:
                table_pattern21="^(\d+)\s*;(\w+)\s*;([A-Za-z0-9-]+)\s*;([\d.]+)\s*;(\d+C)\s*;(\d+%)\s* ;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([\d.]+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*(\d+m)\s*;\s*(\d+)"   ### ;\s*([A-Za-z0-9-]+)\s*;\s*;\s*([\d.]+)\s*;\s*([\d.%-]+)\s*;\s*([\d.-]+)\s*;\s*([\d.-]+)\s*;\s*(\d+)\s*;\s*([\d.]+)\s*;\s*([\d.]+)\s*;\s*([\d.%-]+)\s*;\s*([\d.-]+)\s*;\s*([\d.-]+)\s*;\s*(\d+)\s*;\s*(-?\d+(\.\d+)?)\s*;\s*(\d+m)\s*;\s*(\d+)$

                table_matches21 = re.findall(table_pattern21, extracted_data1, re.MULTILINE)

                if table_matches21:
                    global c1,c2,c3
                    # print(c1,'c1c1c1')
                    columns = [ 'ID', 'LINK', 'RiL', 'WL1', 'TEMP1', 'TXbs1','TXdBm1','RXdBm1' ,'BER1','WL2','TEMP2','TXbs2','TXdBm2','RXdBm2','BER2','DlLoss','UlLoss','LENGTH','TT']   ## 
                    table_df21 = pd.DataFrame(table_matches21, columns=columns)
                    table_df21['Site Id'] = globalSiteId
                    table_df21['Cell'] = (c1,c2,c3)

                    table_df21 = table_df21[['Site Id' ,'Cell','ID', 'LINK', 'RiL', 'WL1', 'TEMP1', 'TXbs1','TXdBm1','RXdBm1','BER1','WL2','TEMP2','TXbs2','TXdBm2','RXdBm2','BER2','DlLoss','UlLoss','LENGTH','TT']]
                    print('table_df21',table_df21)
                    # if marketPlace == 'CT':
##################################################################
    file_path2="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path2, 'r') as file:
        content = file.read()

        start_marker2 = """ sdir"""
        end_marker2 = """ cvls"""

        start_index2 = content.find(start_marker2)
        end_index2 = content.find(end_marker2)
        extracted_data2 = content[start_index2:end_index2]   
        # print( "lkkhh",extracted_data2)

        if extracted_data2:
            start_marker3 = """...........
+--------+               +-------------+"""
            end_marker3 = """ """+globalSiteId_2+"""> cvls"""
            start_index3 = content.find(start_marker3)
            end_index3 = content.find(end_marker3)
            extracted_data3 = content[start_index3:end_index3]
            # print( "lllllmmmmmnnnn\n",extracted_data3)

            if extracted_data3:
                table_pattern3="\s*(\d+)\s*;\s*(Up)\s*;\s*(\w+\-\d+\-\w+\-\d+\-\d+\-\S+)\s*;\s*(\d+\.\d+)\s*;\s*(\d+C)\s*;\s*(\d+%)\s*;\s*(-?\d+\.\d+)\s*;\s*(-?\d+\.\d+)\s*;\s*(\d+/\d+|\d+)\s*;\s*(\d+\.\d+)\s*;\s*(\d+C)\s*;\s*(\d+%)\s*;\s*(-?\d+\.\d+)\s*;\s*(-?\d+\.\d+)\s*;\s*(\d+/\d+|\d+)\s*;\s*(-?\d+\.\d+)\s*;\s*(-?\d+\.\d+)\s*;\s*(\d+m|)\s*;\s*(\d+)\s*"
                # table_pattern3 = r"\b(\d+)\s+;(\w+)\s+(\S+)\s+(\d+\.\d+)"  ##  ;\s*([^;]+)\s*;([\d.]+)\s*;(\w+)\s*;([\d.%-]+)\s*;([-.\d]+)\s*;([-.\d]+)\s*;([^;]+)\s*;([\d.]+)\s*;(\w+)\s*;([-.\d]+)\s*;([-.\d]+)\s*;([^;]+)\s*;([^;]+)\s*;([-.\d]+)\s*;([-.\d]+)\s*;([-.\w]+)\s*;(\d+)
                # table_pattern3="^(\d+)\s*;(\w+)\s*;([A-Za-z0-9-]+)\s*;([\d.]+)\s*;(\d+C)\s*;(\d+%)\s* ;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([\d.]+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*(\d+m)\s*;\s*(\d+)"   ### ;\s*([A-Za-z0-9-]+)\s*;\s*;\s*([\d.]+)\s*;\s*([\d.%-]+)\s*;\s*([\d.-]+)\s*;\s*([\d.-]+)\s*;\s*(\d+)\s*;\s*([\d.]+)\s*;\s*([\d.]+)\s*;\s*([\d.%-]+)\s*;\s*([\d.-]+)\s*;\s*([\d.-]+)\s*;\s*(\d+)\s*;\s*(-?\d+(\.\d+)?)\s*;\s*(\d+m)\s*;\s*(\d+)$

                table_matches3 = re.findall(table_pattern3, extracted_data3, re.MULTILINE)
                # print(table_matches3)
                if table_matches3:
                    global a,a,b,b,c,c
                    # print(a,'c1c1c1')
                    columns = [ 'ID', 'LINK', 'RiL', 'WL1', 'TEMP1', 'TXbs1','TXdBm1','RXdBm1' ,'BER1','WL2','TEMP2','TXbs2','TXdBm2','RXdBm2','BER2','DlLoss','UlLoss','LENGTH','TT']   ##   
                    table_df3 = pd.DataFrame(table_matches3, columns=columns)
                    table_df3['Site Id'] = globalSiteId_2
                    table_df3['Cell'] = (a,a,b,b,c,c) #,'Cell'

                    table_df3 = table_df3[['Site Id','Cell' ,'ID', 'LINK', 'RiL', 'WL1', 'TEMP1', 'TXbs1','TXdBm1','RXdBm1','BER1','WL2','TEMP2','TXbs2','TXdBm2','RXdBm2','BER2','DlLoss','UlLoss','LENGTH','TT']]
                    # print('lkjhgffdssa;',table_df3)
#####################################################################################################################

    file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content3 = file.read()

        start_marker3 = """ sdir"""
        end_marker3 = """LVA61251A> pst"""

        start_index3 = content3.find(start_marker3)
        end_index3 = content3.find(end_marker3)
        extracted_data3 = content3[start_index3:end_index3]   
        print( "lkkhh",extracted_data3)

        if extracted_data3:
            start_marker4= """.............................
+--------+                         +----------+"""
            end_marker4= """ LVA61251A> pst"""
            start_index4 = extracted_data3.find(start_marker4)
            end_index4 = extracted_data3.find(end_marker4)
            extracted_data4 = extracted_data3[start_index4:end_index4]
            # print( "lllllmmmmmnnnn\n",extracted_data4)

            if extracted_data4:
                # print('qwertyuiop')
                # brbrbrbrbrb
                table_pattern4="\s*(\d+)\s*;\s*(Up)\s*;\s*(\d+)\s*;\s*(\d+\.\d+)\s*;\s*(\d+C)\s*;\s*(\d+%)\s*;\s*(-?\d+\.\d+)\s*;\s*(-?\d+\.\d+)\s*;\s*(\d+)\s*;\s*(\d+\.\d+)\s*;\s*(\d+C)\s*;\s*(\d+%)\s*;\s*(-?\d+\.\d+)\s*;\s*(-?\d+\.\d+)\s*;\s*(\d+)\s*;\s*(-?\d+\.\d+)\s*;\s*(-?\d+\.\d+)\s*" ##;\s*(\d+)\s*
                # table_pattern3 = r"\b(\d+)\s+;(\w+)\s+(\S+)\s+(\d+\.\d+)"  ##  ;\s*([^;]+)\s*;([\d.]+)\s*;(\w+)\s*;([\d.%-]+)\s*;([-.\d]+)\s*;([-.\d]+)\s*;([^;]+)\s*;([\d.]+)\s*;(\w+)\s*;([-.\d]+)\s*;([-.\d]+)\s*;([^;]+)\s*;([^;]+)\s*;([-.\d]+)\s*;([-.\d]+)\s*;([-.\w]+)\s*;(\d+)
                # table_pattern3="^(\d+)\s*;(\w+)\s*;([A-Za-z0-9-]+)\s*;([\d.]+)\s*;(\d+C)\s*;(\d+%)\s* ;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([\d.]+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*(\d+m)\s*;\s*(\d+)"   ### ;\s*([A-Za-z0-9-]+)\s*;\s*;\s*([\d.]+)\s*;\s*([\d.%-]+)\s*;\s*([\d.-]+)\s*;\s*([\d.-]+)\s*;\s*(\d+)\s*;\s*([\d.]+)\s*;\s*([\d.]+)\s*;\s*([\d.%-]+)\s*;\s*([\d.-]+)\s*;\s*([\d.-]+)\s*;\s*(\d+)\s*;\s*(-?\d+(\.\d+)?)\s*;\s*(\d+m)\s*;\s*(\d+)$

                table_matches4 = re.findall(table_pattern4, extracted_data4, re.MULTILINE)
                # print(table_matches4,'table_matches4table_matches4table_matches4')
                if table_matches4:
                    # global a,a,b,b,c,c
                    # print(a,'c1c1c1')
                    columns = [ 'ID', 'LINK', 'RiL', 'WL1', 'TEMP1', 'TXbs1','TXdBm1','RXdBm1' ,'BER1','WL2','TEMP2','TXbs2','TXdBm2','RXdBm2','BER2','DlLoss','UlLoss']   ##    
                    table_df4 = pd.DataFrame(table_matches4, columns=columns)
                    table_df4['Site Id'] = globalSiteId_3
                    table_df4['Cell'] = (cell31,cell31,cell32,cell32,cell33,cell33,cell31,cell32,cell33) #,'Cell'
                    table_df4['LENGTH'] = ''
                    table_df4['TT'] = ''

                    table_df4 = table_df4[['Site Id','Cell' ,'ID', 'LINK', 'RiL', 'WL1', 'TEMP1', 'TXbs1','TXdBm1','RXdBm1','BER1','WL2','TEMP2','TXbs2','TXdBm2','RXdBm2','BER2','DlLoss','UlLoss','LENGTH','TT']]
                    print('lkjhgfdsa',table_df4)


                    combined_table_df = pd.concat([ table_df21,table_df3,table_df4], ignore_index=True)
                    # print(combined_table_df)
##############################################################

                    color_thresholds = {
                        'CT': [-3, 3],
                        'UPNY_Direct': [-2, 2],
                        'UPNY_Rullex': [-2, 2],
                        'PH': [-3, 3],
                        'VA': [-3, 3],
                    }


                    def apply_color_Global(val, column_name,startend):
                            
                        val = val.strip()
                        # print(val,"valvalval")
                        if column_name in ['BER1', 'BER2']:
                            if val != '0' and val != '0/0' :
                                return 'background-color: rgb(250, 9, 9);color:white;'
                        elif column_name in['DlLoss','UlLoss']:
                            if float(val) < startend[0] or float(val) > startend[1]:
                                return 'background-color: red;color:white;'
                        # elif column_name == 'VSWR (RL)':
                        #     if val.strip() == 'AIR21' or (float(val) < 1.5 and float(val) >= 0):
                        #         return 'background-color: red;color:white;'
                        return ''
                         
                    print(color_thresholds[marketPlace])
                    
                    combined_table_df['BER1'] = combined_table_df['BER1'].apply(lambda x: f'<span class="shobhit" style="{apply_color_Global(x, "BER1",color_thresholds[marketPlace])}">{x}</span>')
                    combined_table_df['BER2'] = combined_table_df['BER2'].apply(lambda x: f'<span class="shobhit"style="{apply_color_Global(x, "BER2",color_thresholds[marketPlace])}">{x}</span>')
                    combined_table_df['DlLoss'] = combined_table_df['DlLoss'].apply(lambda x: f'<span class="shobhit" style="{apply_color_Global(x, "DlLoss",color_thresholds[marketPlace])}">{x}</span>')
                    combined_table_df['UlLoss'] = combined_table_df['UlLoss'].apply(lambda x: f'<span class="shobhit" style="{apply_color_Global(x, "DlLoss",color_thresholds[marketPlace])}">{x}</span>')


                    final_col_for_data=[]
                    def apply_colorNew(val):
                        for i in val:
                            if(type(i)==type("str")):
                                if("background-color: rgb(250, 9, 9);color:white;" in i):
                                    if(val["Site Id"]+" "+val["Cell"] not in final_col_for_data_loss):
                                        final_col_for_data_loss.append(val["Site Id"]+" "+val["Cell"])

                    # print(combined_table_df)
                    combined_table_df2 = combined_table_df.apply(apply_colorNew,axis=1)

                    
                    # addDataintoglobalDf("Fiber Loss",final_col_for_data)
                    html_table = combined_table_df.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')
                    # print(html_table)


                    

                    write_html_table("<h2>-----:LTE FiberLOss:-----:</h2>\n" +html_table)
marketPlace = 'CT' 
# marketPlace = ['CT','UPNY_Direct','UPNY_Rullex','UPNY_Rullex','PH','VA']
extract_data455(file_path,marketPlace)

########################################################################################################################################################
# if len(final_col_for_data_loss)>0:
#     final_col_for_data_loss.append('<br>')
# if len(final_col_for_data_vswr)>0:
#     final_col_for_data_vswr.append('<br>')

file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/fifth_data.txt" 
def fifth_file3(file_path3):
    with open(file_path3, 'r') as file:
        content3 = file.read()
        # print("lllll12",content3)
        if content3:
            start_marker = """invrxb"""
            end_marker = """get . dis"""

            start_index = content3.find(start_marker)
            end_index = content3.find(end_marker)
            extracted_data = content3[start_index:end_index]   
            # print( "lkkhh",extracted_data)

            if extracted_data:
#                 start_marker1 = """=====================================================================================================================================
# ID LINK WL1  TEMP1 TXbs1 TXdBm1 RXdBm1 BER1   WL2  TEMP2 TXbs2 TXdBm2 RXdBm2 BER2   DlLoss UlLoss
# ====================================================================================================================================="""
#                 end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

# =====================================================================================================================================
# ID BOARD       SFPLNH             PORT VENDOR  VENDORPROD       REV  SERIAL         DATE     ERICSSONPROD   WL   TEMP  TXbs  TXdBm  RXdBm   BER
# ====================================================================================================================================="""
#                 start_index1 = content3.find(start_marker1)
#                 end_index1 = content3.find(end_marker1)
#                 extracted_data1 = content3[start_index1:end_index1]   
                # print( "lkkhh",extracted_data1)

            # if extracted_data1:
                # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                table_pattern1 = r"(\d+)\s+(Up)\s+(\d+)\s+(\d+C)\s+(\d+%)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(\d+)\s+(\d+)\s+(\d+C)\s+(\d+%)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s"  #(\d+)\s+

                # if re.match(table_pattern1, extracted_data1):
                #     print("Pattern matches extracted data1")
                

                table_matches1 = re.findall(table_pattern1, extracted_data, re.MULTILINE)

                columns = ['ID','LINK','WL1','TEMP1','TXbs1','TXdBm1','RXdBm1','BER1','WL2','TEMP2','TXbs2','TXdBm2','RXdBm2','BER2','DlLoss','UlLoss']   #
                table_df1 = pd.DataFrame(table_matches1, columns=columns)
                # print(table_df1)
                a1 =table_df1['ID'] 
                a2 =table_df1['BER1'] 
                a3 =table_df1['BER2'] 
                a4 =table_df1['DlLoss'] 
                a5 =table_df1['UlLoss']
############
            if extracted_data:
#                 start_marker2 = """=====================================================================================================================================
# AuxPiu    LNH                  BOARD       RF  TX (W/dBm)  VSWR (RL)    Sector/Cells (localCellIds/CellIds,PCIs)
# ====================================================================================================================================="""
#                 end_marker2 = """-------------------------------------------------------------------------------------------------------------------------------------
# Tip: use option "g" to print graphical view of CPRI connections and RF connections.

# UVA61251A2> get . dis"""
#                 start_index2 = content3.find(start_marker2)
#                 end_index2 = content3.find(end_marker2)
#                 extracted_data2 = content3[start_index2:end_index2]   
                # print( "ppppp",extracted_data2)

            # if extracted_data2:
                # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                table_pattern2 = r'(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+([0-9.]+ \(\d+\.\d+\))\s+(\S+)\s+((?:SR=\d+ \S+ \(\d+\))|(?:N/A))\s'

                # if re.match(table_pattern1, extracted_data1):
                #     print("Pattern matches extracted data1")
                

                table_matches2 = re.findall(table_pattern2, extracted_data, re.MULTILINE)

                columns = ['AuxPiu','LNH','BOARD','RF','TX (W/dBm)','VSWR (RL)','Sector/Cells (localCellIds/CellIds,PCIs)']   #
                table_df2 = pd.DataFrame(table_matches2, columns=columns)
                b1=table_df2['VSWR (RL)']
                b2=table_df2['Sector/Cells (localCellIds/CellIds,PCIs)']
                    # print(table_df2)
#####################

##########################
            if extracted_data:
                start_marker3 = """=====================================================================================================================================
ID T BOARD1      LNH1 PORT R LINK RATE   BER BOARD2      LNH2               PORT R LINK RATE   BER MO1 - MO2
====================================================================================================================================="""
                end_marker3 = """-------------------------------------------------------------------------------------------------------------------------------------

=====================================================================================================================================
ID LINK VENDOR1 VENDORPROD1      REV1 SERIAL1        DATE1    ERICSSONPROD1  VENDOR2 VENDORPROD2      REV2 SERIAL2        DATE2    ERICSSONPROD2 
====================================================================================================================================="""
                start_index3 = content3.find(start_marker3)
                end_index3 = content3.find(end_marker3)
                extracted_data3 = content3[start_index3:end_index3]   
                # print( "ppppp",extracted_data3)

                if extracted_data3:
                    ####### jab na parse ho to is tarike se pattern bnao#######################################################################
                    table_pattern3 = r'\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.*)\s'
                    # table_pattern3 = r'\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+\s*-\s*\S+)'

                    # if re.match(table_pattern1, extracted_data1):
                    #     print("Pattern matches extracted data1")
                    

                    table_matches3 = re.findall(table_pattern3, extracted_data3, re.MULTILINE)

                    columns = ['ID','T','BOARD','LNH1','PORT','R','LINK','RATE','BER','BOARD2','LNH2','PORT','R','LINK','RATE','BER','MO1 - MO2']   # 
                    table_df3 = pd.DataFrame(table_matches3, columns=columns)
                    # table_df3['LNH2']
                    # c=table_df3['LNH2'] = table_df3['LNH2'].str.replace('000100/', '')
                    table_df3['BOARD2']
                    c=table_df3['BOARD2'].str.replace('B2AB4P',"")
                    # print(c,'ccccccccccccccccccccccccccccccc')
                        # b1=table_df2['VSWR (RL)']
                        # b2=table_df2['Sector/Cells (localCellIds/CellIds,PCIs)']
                        # print(table_df3)

###########################
#######################
    file_path6="C:/Users/LENOVO/Desktop/dataframework/find_data/seventh_data.txt"
    with open(file_path6, 'r') as file:
        content = file.read()
        if content:
            start_marker1 = """get UtranCell=.*(VA61251A).* ^cellreserved$|^accessClassNBarred$|^accessClassesBarredCs$|^accessClassesBarredPs$|^cId"""
            # print(start_marker1)
            end_marker1 = """ """+globalSiteId_5+"""> alt"""

            start_index1 = content.find(start_marker1)
            # print('nbbbnb',start_index1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]
            # print('aaaaaaaaaa',extracted_data1)
            if extracted_data1:
            
            #     # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))?\s+(\d+\s+\(\w+\))?\s+(.*)$'
                table_pattern1 = r'(?:UtranCell=(\S+))\s+(cId )\s+(\d+)'

            #     table_pattern1 = r'(\d+)\s+(\S+\s+\(.*\)|\s*)\s+(\S+\s+\(.*\)|\s*)\s+(.*)$'

            #     # Find matches using the regex pattern
                table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

                if table_matches1:
                    columns = ['MO','Attribute','value']   ### 
                    table_df4 = pd.DataFrame(table_matches1, columns=columns)  ##
                    t1= table_df4['MO']
                    # print(t1,'t1')  #table_df4['MO']+table_df4['value'].apply(lambda x: f'({x})')
                    t2=table_df4['Attribute']
                    # t3=table_df4['value']
                    # add=[f'({t1}+\n({t3}))']
                    
            #         table_df1['Site Id'] = 'NIE04225A2'
            #         table_df1 = table_df1[['Site Id','Proxy', 'Adm State', 'Op. State', 'MO']]  ### 
                    
                    # print(" log:\n",table_df1)

#############################

                    data={
                        "RNC":globalSiteId_7,
                        'Site Id':globalSiteId_5,
                        'Cell':t1,                       
                        'BER1':a2,
                        'BER2':a3,
                        'DlLoss':a4,
                        'UlLoss':a5,
                        'VSWR (RL)':c,
                       
                        # 'value':t3

                    }

                    table_df=pd.DataFrame(data)
                    final_col_for_data=[]
                    def apply_colorNew(val):
                        print(val[["VSWR (RL)"]])

                
                    # # print(';l;l;l;l',table_df)
                    final_col_for_data=[]
                    def apply_colorNew(val,):

                        print(val)

                        print(val[["BER1","BER2","DlLoss","UlLoss"]])
                        # dsafsdsadad
                        for i in val[["BER1","BER2","DlLoss","UlLoss"]]: 
                            if(type(i)==type("str")):
                                print(i)
                                if("background-color: rgb(250, 9, 9);color:white;" in i):
                                    if(val["Site Id"]+" "+val["Cell"] not in final_col_for_data_loss):
                                        final_col_for_data_loss.append(val["Site Id"]+" "+val["Cell"])


                        
                        for i in val[["VSWR (RL)"]]:
                            if(type(i)==type("str")):
                                if("background-color: rgb(250, 9, 9);color:white;" in i):
                                    if(val["Site Id"]+" "+val["Cell"] not in final_col_for_data_vswr):
                                        final_col_for_data_vswr.append(val["Site Id"]+" "+val["Cell"])


                    def apply_color(val, column_name):
                        val = val.strip()
                        if column_name in ['BER1', 'BER2']:
                            if val != '0':
                                return 'background-color: rgb(250, 9, 9);color:white;'
                        elif column_name in['DlLoss','UlLoss']:
                            if float(val) < -3 or float(val) > 3:
                                return 'background-color: rgb(250, 9, 9);color:white;'
                        elif column_name == 'VSWR (RL)':
                            if val.strip() == 'AIR21' or (float(val) < 1.5 and float(val) >= 0):
                                return 'background-color: rgb(250, 9, 9);color:white;'
                            
                        return ''

                    # Apply the function to each column separately
                    table_df['BER1'] = table_df['BER1'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x, "BER1")}">{x}</span>')
                    table_df['BER2'] = table_df['BER2'].apply(lambda x: f'<span class="shobhit"style="{apply_color(x, "BER2")}">{x}</span>')
                    table_df['DlLoss'] = table_df['DlLoss'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x, "DlLoss")}">{x}</span>')
                    table_df['UlLoss'] = table_df['UlLoss'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x, "DlLoss")}">{x}</span>')
                    table_df['VSWR (RL)'] = table_df['VSWR (RL)'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x, "VSWR (RL)")}">{x}</span>')

                    combined_table_df2 = table_df.apply(apply_colorNew,axis=1)
       

                    html_table = global_style + table_df.to_html(escape=False, index=False,
                                                              table_id='styled_table',
                                                              classes='table table-striped table-bordered')

                    write_html_table("\n<h2>-----:UMTS Fiber Loss:-----:</h2>\n" + html_table)
                    

                    # print('qws',a)
                    # else:
                    #     print("Pattern does not match extracted data1")
                    # # table_df1['Site Id'] = 'UVA61251A2'
                    # # table_df1 = table_df1[['Site Id','MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']]
                    # print('table_df1',table_df1)
fifth_file3(file_path3)

print(final_col_for_data_vswr)

# dsadsadsadsa
addDataintoglobalDf('Fiber Loss',final_col_for_data_loss )
addDataintoglobalDf("VSWR",final_col_for_data_vswr)

########################################################################################################################################################################
 ###############


def extract_data456(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = """sdir"""
        end_marker = """hget . allowedplmnlist"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]   
        # print( "lkkhh",extracted_data)

        if extracted_data:
            start_marker1 = """..........
+--------+                  +----------------+"""
            end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

globalSiteId>

globalSiteId> hget . allowedplmnlist"""
            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]
            # print( "lllllmmmmmnnnn\n",extracted_data1)

            if extracted_data1:
                table_pattern2="^(\d+)\s*;([A-Za-z0-9-]+)\s*;(\S+)\s*;(\S+)\s*;\s*(\d+)\s*;(\S+)\s*;(\S+)\s*;(\w+)\s*;(\S+)\s*;(\d+)\s*;(\w+/\d+ R1A)\s*;(\d+\.\d+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*"   ###   ;(\w+)\s*;([\d.]+)\s*;(\d+C)\s*;(\d+%)\s* ;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([\d.]+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([^;]+)\s*;\s*(\d+\.\d+)\s*;\s*(\d+m)\s*;\s*(\d+)

                table_matches2 = re.findall(table_pattern2, extracted_data1, re.MULTILINE)

                # print(table_matches2)

                if table_matches2:
                    
                    global c1,c2,c3
                    columns = [ 'ID', 'RiL','BOARD','SFPLNH','PORT','VENDOR','VENDORPROD','REV','SERIAL','DATE','ERICSSONPROD','WL','TEMP','TXbs','TXdBm','RXdBm',' BER']   ##  , 'LINK', 'RiL', 'WL1', 'TEMP1', 'TXbs1','TXdBm1','RXdBm1' ,'BER1','WL2','TEMP2','TXbs2','TXdBm2','RXdBm2','BER2','DlLoss','UlLoss','LENGTH','TT'
                    table_df2 = pd.DataFrame(table_matches2, columns=columns)
                    # print('table_df2',table_df2)
                    table_df2['Site Id'] = globalSiteId
                    # print('table_df2\n',table_df2)
                    table_df2['Cell'] = (c1,c2,c3,c1,c2,c3)
                    table_df2 = table_df2[['Site Id','Cell','ID', 'RiL','BOARD','SFPLNH','PORT','VENDOR','VENDORPROD','REV','SERIAL','DATE','ERICSSONPROD','WL','TEMP','TXbs','TXdBm','RXdBm',' BER']]
                    # print('table_df2\n',table_df2)
##########################################################################################################################################################################################################################
    filepath2="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(filepath2, 'r') as file:
            content2 = file.read()

            start_marker2= """sdir"""
            end_marker2 = """ """+globalSiteId_2+"""> cvls"""

            start_index2 = content2.find(start_marker2)
            end_index2 = content2.find(end_marker2)
            extracted_data2 = content2[start_index2:end_index2]   
            # print( "lkkhh",extracted_data2)

            if extracted_data2:
                start_marker3 = """...........
+--------+               +-------------+"""
                end_marker3 = """ """+globalSiteId_2+"""> cvls"""
                start_index3 = content2.find(start_marker3)
                end_index3 = content2.find(end_marker3)
                extracted_3 = content2[start_index3:end_index3]
                # print( extracted_3,'aslkdkhfhgj' )

                if extracted_3:
                    table_pattern3="(\d+)\s;([A-Za-z0-9-]+)\s*;(\S+)\s*;(\S+)\s*;\s*(\d+)\s*;(\S+)\s*;(\S+)\s*;(\w+)\s*;(\S+)\s*;(\d+)\s*;(\w+/\d+ R1A)\s*;(\d+\.\d+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*"   ###   ;([A-Za-z0-9-]+)\s*;(\S+)\s*;(\S+)\s*;\s*(\d+)\s*;(\S+)\s*;(\S+)\s*;(\w+)\s*;(\S+)\s*;(\d+)\s*;(\w+/\d+ R1A)\s*;(\d+\.\d+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*

                    table_matches3 = re.findall(table_pattern3, extracted_3, re.MULTILINE)

                    # print(table_matches3,'l;l;kk;l')

                    if table_matches3:
                        
                        # global a,b,c
                        columns = [ 'ID' , 'RiL','BOARD','SFPLNH','PORT','VENDOR','VENDORPROD','REV','SERIAL','DATE','ERICSSONPROD','WL','TEMP','TXbs','TXdBm','RXdBm',' BER']   ##   , 'RiL','BOARD','SFPLNH','PORT','VENDOR','VENDORPROD ','REV','SERIAL','DATE','ERICSSONPROD','WL','TEMP','TXbs','TXdBm','RXdBm',' BER'
                        table_df3 = pd.DataFrame(table_matches3, columns=columns)
                        
                        # # print('table_df2',table_df2)
                        table_df3['Site Id'] = globalSiteId_2
                        print('table_df3\n',table_df3)
                        table_df3['Cell'] = (a,a,b,b,c,c,a,a,b,b,c,c)
                        table_df3 = table_df3[['Site Id','Cell','ID', 'RiL','BOARD','SFPLNH','PORT','VENDOR','VENDORPROD','REV','SERIAL','DATE','ERICSSONPROD','WL','TEMP','TXbs','TXdBm','RXdBm',' BER']]
                        # print('table_df3\n',table_df3)

#################################################################################################################################################################################################

    filepath3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(filepath3, 'r') as file:
            content3 = file.read()

            start_marker3= """sdir"""
            end_marker3 = """pst"""

            start_index3 = content3.find(start_marker3)
            end_index3 = content3.find(end_marker3)
            extracted_data3 = content3[start_index3:end_index3]   
            # print( "lkkhh",extracted_data3)

            if extracted_data3:
                start_marker4 = """=====================================================================================================================================
ID ;RiL ;BOARD     ;SFPLNH  ;PORT ;VENDOR       ;VENDORPROD       ;REV  ;SERIAL          ;DATE     ;ERICSSONPROD   ;WL      ;TEMP  ;TXbs  ;TXdBm  ;RXdBm  ; BER
====================================================================================================================================="""
                end_marker4 = """=====================================================================================================================================
BOARD  ;LNH    ;PORT ;T ;S ;OpMode  ;AutoNeg ;MacAddress        ;VlanIds   ;LOS ;BER
====================================================================================================================================="""
                start_index4 = content3.find(start_marker4)
                end_index4 = content3.find(end_marker4)
                extracted_4 = content3[start_index4:end_index4]
                # print('aslkdkhfhgj', extracted_4,'aslkdkhfhgj' )

                if extracted_4: ## [A-Za-z0-9-]+
                    table_pattern4=r"\s*(\d+)\s*;\s*(\d+)\s*;\s*(\S+)\s*;\S*(\d{6}|BXP_\d+)\s*;\s*(\d+)\s*;\s*(\w+)\s*;\s*(\S+)\s*;\s*(\S+)\s*;\s*(\S+)\s*;\s*(\d+)\s*;\s*(\w+/\d+\s+\S+)\s*;\s*(\d+\.\d+)\s*;\s*(\d+C)\s*;\s*(\d+%)\s*;\s*(-\d+\.\d+)\s*;\s*(-\d+\.\d+)\s*;\s*(\d+)\s*" ## \s*;\s*(\d+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*(\d+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*(\d+)\s*$

                    # table_pattern4="(\d+)\s;(\d+)\s*;(\S+)\s*;(\d+)\s*;\s*(\d+)\s*;(\w+)\s*;(\S+)\s*;((\d+\.\d+)|)\s*;(\S+)\s*;(\d+)\s*;(\S+/\d+ R1A)\s*;(\d+\.\d+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*"   ###   ;([A-Za-z0-9-]+)\s*;(\S+)\s*;(\S+)\s*;\s*(\d+)\s*;(\S+)\s*;(\S+)\s*;(\w+)\s*;(\S+)\s*;(\d+)\s*;(\w+/\d+ R1A)\s*;(\d+\.\d+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*

                    table_matches4 = re.findall(table_pattern4, extracted_4, re.MULTILINE)

                    # print(table_matches4,'l;l;kk;l')

                    if table_matches4:                        
                        # global a,b,c
                        columns = [ 'ID','RiL','BOARD','SFPLNH','PORT','VENDOR','VENDORPROD','REV','SERIAL','DATE','ERICSSONPROD','WL','TEMP','TXbs','TXdBm','RXdBm',' BER' ]   ##  
                        table_df4 = pd.DataFrame(table_matches4, columns=columns)
                        
                        # # print('table_df2',table_df2)
                        table_df4['Site Id'] = globalSiteId_3
                        # print('table_df4\n',table_df4)
                        table_df4['Cell'] = (cell31,cell32,cell33,cell31,cell32,cell33,cell31,cell32,cell33,cell31,cell32,cell33,cell31,cell32,cell33,cell31,cell32,cell33)
                        table_df4 = table_df4[['Site Id','Cell','ID', 'RiL','BOARD','SFPLNH','PORT','VENDOR','VENDORPROD','REV','SERIAL','DATE','ERICSSONPROD','WL','TEMP','TXbs','TXdBm','RXdBm',' BER']]
                        print('table_df3table123\n',table_df4.columns,table_df3.columns,table_df2.columns)
                        
                        combined_table_df = pd.concat([table_df2,table_df3,table_df4], ignore_index=True)
                        print(combined_table_df)
# ######################################################################################################################################################################################################################################
                    html_table = combined_table_df.to_html(escape=False, index=False,
                                                    table_id='styled_table',
                                                    classes='table table-striped table-bordered')

                    write_html_table(f"<h2>-----:SFP Details:-----:</h2>\n{html_table}")
                      
extract_data456(file_path)

######################################################################################################################################################

####################### LTE CELL STATUS ########################################################################################################################
# if len(final_col_for_data_pc)>0:
#     final_col_for_data_pc.append('<br>')
def third_file1(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # print("lllll12",content3)
        if content:
            start_marker2 = """hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
            end_marker2 = """ hget ^EUtranCellFDD|TDD|NBIOT cellid|rachroo|tac|earfcnd|earfcnul|cellrange|dlChannelBandwidth$|ulChannelBandwidth$"""

            start_index2 = content.find(start_marker2)
            end_index2 = content.find(end_marker2)
            extracted_data2 = content[start_index2:end_index2]
            # print(extracted_data2) 
            if extracted_data2:
                table_pattern = r"(EUtranCellFDD=\S+)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+\s+\(\w+)\)\s+(\d+\s+\(\w+\)|\s*)\s+(\w+)\s+(?:\[1\] = (SectorCarrier=\d+\-\d+\-\d+))"  #  (\d+\s+\(\w+\)|\s*)
                table_matches = re.findall(table_pattern, extracted_data2, re.MULTILINE)

                columns = [ 'MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']   #,
                table_df = pd.DataFrame(table_matches, columns=columns)
                # print('table_df1,,,,',table_df1)
                table_df[ 'administrativeState'] = table_df['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df[ 'cellBarred'] = table_df[ 'cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df[ 'operationalState'] = table_df[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                # print(table_df1)
                table_df['Site Id'] = globalSiteId
                table_df= table_df[['Site Id','MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']]

                # print(table_df,'table_dftable_dftable_dftable_df')
    file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content3 = file.read()
        if content3:
            start_marker = """hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
            end_marker = """hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""

            start_index = content3.find(start_marker)
            end_index = content3.find(end_marker)
            extracted_data = content3[start_index:end_index]   
            # print( "lkkhh",extracted_data)

            if extracted_data:
                table_pattern1 = r"(EUtranCellFDD=\S+)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+\s+\(\w+)\)\s+(\d+\s+\(\w+\)|\s*)\s+(\w+)\s+(?:\[1\] = (SectorCarrier=\d+))"  #  (\d+\s+\(\w+\)|\s*)
                table_matches1 = re.findall(table_pattern1, extracted_data, re.MULTILINE)

                columns = [ 'MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']   #,
                table_df1 = pd.DataFrame(table_matches1, columns=columns)
                # print('table_df1,,,,',table_df1)
                table_df1[ 'administrativeState'] = table_df1['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df1[ 'cellBarred'] = table_df1[ 'cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df1[ 'operationalState'] = table_df1[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                # print(table_df1)
                table_df1['Site Id'] = globalSiteId_3
                table_df1 = table_df1[['Site Id','MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']]
                
                combined_table_df = pd.concat([table_df,table_df1], ignore_index=True)

                final_col_for_data=[]
                def apply_colorNew(val):
                    for i in val:
                        if(type(i)==type("str")):
                            if("background-color: rgb(250, 9, 9); color:white;" in i) or ("background-color: orange;" in i) or ("background-color: rgb(250, 9, 9);" in i)  :
                                if(val["Site Id"]+" "+val["MO"] not in final_col_for_data_pc):
                                    final_col_for_data_pc.append(val["Site Id"]+" "+val["MO"])
                                else:
                                    print('lkjhgfdsa')


                def apply_color(val):
                    if val.strip() == 'BARRED' or val.strip() == 'true':
                        return 'background-color: rgb(250, 9, 9); color:white;'
                    else:
                        return ''
                # table_df1['cellBarred','primaryPlmnReserved'] = table_df1['cellBarred','primaryPlmnReserved'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')
                columns_to_apply = ['cellBarred', 'primaryPlmnReserved']

                combined_table_df[columns_to_apply] = combined_table_df[columns_to_apply].applymap(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')

                def apply_color(row):
                    if row['administrativeState'].strip() == 'LOCKED' and row['operationalState'].strip() == 'DISABLED':
                        return 'background-color: orange;'
                    if not row['administrativeState'].strip() == 'LOCKED' and row['operationalState'].strip() == 'DISABLED':
                        return 'background-color: rgb(250, 9, 9);'
                    # if row['cellBarred'].strip() == 'BARRED':
                    #     return 'background-color: red;'
                    
                    else:
                        return ''

                combined_table_df['operationalState'] = combined_table_df.apply(lambda row: f'<span class="shobhit" style="{apply_color(row)}">{row["operationalState"]}</span>', axis=1)

                combined_table_df2 = combined_table_df.apply(apply_colorNew,axis=1)
                # print(combined_table_df,'Cell Status')

                # print(final_col_for_data,'Cell Status')
                
                

                html_table = combined_table_df.to_html(escape=False, index=False,
                                                    table_id='styled_table',
                                                    classes='table table-striped table-bordered')

                write_html_table(f"<h2>-----:LTE CELL STATUS-----:-----:<h2>\n \n"+html_table)
   

third_file1(file_path)

################################################################################################################################################################################

#####################  IOT CELL STATUS #######################################################################################################################################################
# if len(final_col_for_data_pc)>0:
#     final_col_for_data_pc.append('<br>')
file_path2="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
def third_file2(file_path2):
    with open(file_path2, 'r') as file:
        content3 = file.read()
        # print("lllll12",content3)
        if content3:
            start_marker = """hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
            end_marker = """hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""

            start_index = content3.find(start_marker)
            end_index = content3.find(end_marker)
            extracted_data = content3[start_index:end_index]   

            if extracted_data:
                # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                table_pattern1 = r"(NbIotCell=\S+)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+\s+\(\w+)\)\s+(\d+\s+\(\w+\)|\s*)\s+(?:\[1\] = (SectorCarrier=\d+))"  # (\d+\s+\(\w+\)|\s*)
                table_matches1 = re.findall(table_pattern1, extracted_data, re.MULTILINE)

                columns = [ 'MO','administrativeState','cellBarred','operationalState','sectorCarrierRef']   #,
                table_df11 = pd.DataFrame(table_matches1, columns=columns)
                table_df11[ 'administrativeState'] = table_df11['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df11['cellBarred'] = table_df11['cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df11[ 'operationalState'] = table_df11[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                # print(table_df11)
                table_df11['Site Id'] = globalSiteId_3
                table_df11 = table_df11[['Site Id','MO','administrativeState','cellBarred','operationalState','sectorCarrierRef']]
                # print('table_df11',table_df11)

                final_col_for_data=[]
                def apply_colorNew(val):
                    for i in val:
                        if(type(i)==type("str")):
                            if("background-color: rgb(250, 9, 9);color:white;" in i) or ("background-color: orange;color:white;" in i):
                                if(val["Site Id"]+" "+val["MO"] not in final_col_for_data_pc):
                                    final_col_for_data_pc.append(val["Site Id"]+" "+val["MO"])

                def apply_color(val):
                    if val.strip() == 'BARRED':
                        return 'background-color: rgb(250, 9, 9);color:white; '
                    else:
                        return ''
                table_df11['cellBarred'] = table_df11['cellBarred'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')

                def apply_color(row):
                    if row['administrativeState'].strip() == 'LOCKED' and row['operationalState'].strip() == 'DISABLED':
                        return 'background-color: orange;color:white;'
                    if not row['administrativeState'].strip() == 'LOCKED' and row['operationalState'].strip() == 'DISABLED':
                        return 'background-color: rgb(250, 9, 9);color:white;'
                    # if row['cellBarred'].strip() == 'BARRED':
                    #     return 'background-color: red;'
                    
                    else:
                        return ''

                # Apply the function to the DataFrame
                table_df11['operationalState'] = table_df11.apply(lambda row: f'<span class="shobhit" style="{apply_color(row)}">{row["operationalState"]}</span>', axis=1)

                combined_table_df2 = table_df11.apply(apply_colorNew,axis=1)
                # print(table_df['substring_found'])

                print(final_col_for_data,'Cell StatusCell Status')
                
                # addDataintoglobalDf("Cell Status", final_col_for_data)


                # global_style = '<style>/* Your global CSS styles here */</style>'

                html_table = global_style +table_df11.to_html(escape=False, index=False,
                                                    table_id='styled_table',
                                                    classes='table table-striped table-bordered')

                write_html_table(f"<h2>-----:IOT CELL STATUS-----:-----:</h2>\n \n"+html_table)
   
third_file2(file_path2)

# addDataintoglobalDf('Cell Status',final_col_for_data_pc )

####################################################################################################################################################################

#####  fourth file(CELL SYSTEM INFORMATION BCCH DATA)   amit sir se pucchna hai ################################################################################################
# if len(final_col_for_data_pc)>0:
#     final_col_for_data_pc.append('<br>')
file_path4="C:/Users/LENOVO/Desktop/dataframework/find_data/fourth_data.txt"
def fourth_file1(file_path4):
    with open(file_path4, 'r') as file:
        content3 = file.read()
        # print("lllll12",content3)

        if content3:
            start_marker1 = """<RLLOP:CELL=CLA411A&CLA411B&CLA411C&CLA411D;"""
            end_marker1 = """<RXTCP:MO=RXOTG-825;"""

            start_index1 = content3.find(start_marker1)
            end_index1 = content3.find(end_marker1)
            extracted_data = content3[start_index1:end_index1]   
            # print( "lkj",extracted_data)

            if extracted_data:
                start_marker2 = """NOT ACCEPTED
Not authorised to execute <!Power per Cell!
<RLCPP:CELL=CLA411A&CLA411B&CLA411C&CLA411D;
CELL CONFIGURATION POWER DATA"""
                end_marker2 = """FAULT INTERRUPT
FAULT CODE 3
CELL NOT DEFINED
(0)CELL=CLA411D
END

<RLSBP:CELL=CLA411A&CLA411B&CLA411C&CLA411D;
CELL SYSTEM INFORMATION BCCH DATA"""

                start_index2 = extracted_data.find(start_marker2)
                end_index2 = extracted_data.find(end_marker2)
                extracted_data2 = extracted_data[start_index2:end_index2]   
                # print( "lkj2",extracted_data2)

                if extracted_data2:
                        # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                        # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                        # table_pattern1 = r"^(\S+)\s*+(\w+)\s*+(\d+)\s*+(\d+)\s*+(\d+)\s*+()\s*"  #
                        table_pattern2=r'(\w+)\s+(\w+)\s+(\d+)\s+(\d+)\s+(\d+)\s+()'
                        table_matches2 = re.findall(table_pattern2, extracted_data2, re.MULTILINE)

                        columns = ['CELL','TYPE','BSPWRB','BSPWRT','MSTXPWR','SCTYPE']   #,
                        table_df2 = pd.DataFrame(table_matches2, columns=columns)
                        a=table_df2['BSPWRB']
                        # print('a',a)
                        b=table_df2['BSPWRT']
                        # print('b',b)
                        c=table_df2['MSTXPWR']
                        # print('c',c)
                        # print('l;l;l;',table_df2)


        if content3:
            start_marker2 = """<RLSTP:CELL=CLA411A&CLA411B&CLA411C&CLA411D;
CELL STATUS"""
            end_marker2 = """<RLCRP:CELL=CLA411A&CLA411B&CLA411C&CLA411D;
CELL RESOURCES"""

            start_index2 = content3.find(start_marker2)
            end_index2 = content3.find(end_marker2)
            extracted_data2 = content3[start_index2:end_index2]   
            # print( "lkkhh",extracted_data2)

            

            if extracted_data2:
                start_marker3 = """CELL      STATE"""
                end_marker3 = """FAULT INTERRUPT"""
                start_index3 = content3.find(start_marker3)
                end_index3 = content3.find(end_marker3)
                extracted_data3 = content3[start_index3:end_index3]   
                # print( "lkkhh",extracted_data3)
                if extracted_data3:
                    # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    table_pattern3 = r"(\S+)\s+(\w+)\s"  #
                    table_matches3 = re.findall(table_pattern3, extracted_data3, re.MULTILINE)

                    columns = ['CELL ','STATE']   #,
                    table_df3 = pd.DataFrame(table_matches3,columns=columns)
                    table_df3 = table_df3.iloc[1:]
                    table_df3 = table_df3.reset_index(drop=True)
                    a1=table_df3['CELL ']
                    b1=table_df3['STATE']
                
                    # table_df3['Site Id'] = 'RLSTP'
                    # table_df3 = table_df3[['Site Id','CELL ','STATE']]
                    # print('l;l;l;\n',table_df3)

        if content3:
            start_marker = """<RLSBP:CELL=CLA411A&CLA411B&CLA411C&CLA411D;"""
            end_marker = """<RLLOP:CELL=CLA411A&CLA411B&CLA411C&CLA411D;"""

            start_index = content3.find(start_marker)
            end_index = content3.find(end_marker)
            extracted_data = content3[start_index:end_index]   
            # print( "lkkhh",extracted_data)

            

            # if extracted_data:
                # start_marker5 = """CELL      STATE"""
                # end_marker5 = """FAULT INTERRUPT"""
                # start_index5
            if extracted_data:
                start_marker3 = """CELL
CLA411A

CB   MAXRET  TX  ATT  T3212  CBQ   CRO  TO  PT  ECSC"""
                end_marker3 = """ACC
CLEAR

CELL
CLA411B

CB   MAXRET  TX  ATT  T3212  CBQ   CRO  TO  PT  ECSC"""
                start_index3 = content3.find(start_marker3)
                end_index3 = content3.find(end_marker3)
                extracted_data3 = content3[start_index3:end_index3] 
                # print( "lk",extracted_data3)
                if extracted_data3:
                    # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    table_pattern3 = r'\bNO\b'  #
                    table_matches3 = re.findall(table_pattern3, extracted_data3, re.MULTILINE)

                    columns = ['CB']   #,
                    f1 = pd.DataFrame(table_matches3,columns=columns)
                    # a2=f1.iloc['0']
                    if not f1.empty:
                        a2 = f1['CB'].iloc[0]
                        # print('CB Value:', a2)
                    else:
                        print("No 'NO' values found in the data.")
                # By removing the space in columns, you should be able to access the 'CB' column correctly. Additionally, I added a check to handle the case when there are no 'NO' values in the data to avoid potential errors.






                    # f1=f1.replace("CB","")
                    # f1 = f1.reset_index(drop=True)  # Reset the index and drop the existing one
                    
                    # d=table_df3['CB '] 
                    # print(table_df3) 
        

            if extracted_data:
                start_marker3 = """CELL
CLA411B

CB   MAXRET  TX  ATT  T3212  CBQ   CRO  TO  PT  ECSC"""
                end_marker3 = """CLA411C

CB   MAXRET  TX  ATT  T3212  CBQ   CRO  TO  PT  ECSC"""
                start_index3 = content3.find(start_marker3)
                end_index3 = content3.find(end_marker3)
                extracted_data3 = content3[start_index3:end_index3] 
                # print( "lk",extracted_data3)
                if extracted_data3:
                    # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    table_pattern3 = r'\bNO\b'  #
                    table_matches3 = re.findall(table_pattern3, extracted_data3, re.MULTILINE)

                    columns = ['CB']   #,
                    f2 = pd.DataFrame(table_matches3,columns=columns)
                    if not f1.empty:
                        b2 = f1['CB'].iloc[0]
                        # print('CB Value:', b2)
                    else:
                        print("No 'NO' values found in the data.")
                    # e=table_df3['CB '] 
                    # print(table_df3)

            
            if extracted_data:
                start_marker3 = """CELL
CLA411C

CB   MAXRET  TX  ATT  T3212  CBQ   CRO  TO  PT  ECSC"""
                end_marker3 = """<RLLOP:CELL=CLA411A&CLA411B&CLA411C&CLA411D;
CELL LOCATING DATA

CELL     BSPWR  BSRXMIN  BSRXSUFF  MSRXMIN  MSRXSUFF  SCHO  MISSNM  AW"""
                start_index3 = content3.find(start_marker3)
                end_index3 = content3.find(end_marker3)
                extracted_data3 = content3[start_index3:end_index3] 
                # print( "lk",extracted_data3)
                if extracted_data3:
                    # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    table_pattern3 = r'\bNO\b'  #
                    table_matches3 = re.findall(table_pattern3, extracted_data3, re.MULTILINE)

                    columns = ['CB ']   #,
                    
                    f3 = pd.DataFrame(table_matches3,columns=columns)

                    if not f1.empty:
                        c2 = f1['CB'].iloc[0]
                        # print('CB Value:', b2)
                    else:
                        print("No 'NO' values found in the data.")
                    
                    # f3 = f3.reset_index(drop=True)  # Reset the index and drop the existing one
                    # f3=f3.replace("CB","")
                    # f3['CB'] = f3['CB'].str.replace(r'^[0\s]+', '', regex=True)
                    
                    # f=table_df3['CB '] 
                    # print(f)
                    # print(table_df3)
                    
                        



                    dta={
                        "BSC":last_word,
                        'CELL':a1,
                        'STATE':b1,
                        'BSPWRB':a,
                        'BSPWRT':b,
                        'MSTXPWR':c,
                        'CB':[a2,b2,c2]

                    }
                    table=pd.DataFrame(dta)

                    final_col_for_data=[]
                    def apply_colorNew(val):
                        for i in val:
                            if(type(i)==type("str")):
                                if("background-color: rgb(250, 9, 9);color:white;" in i) or ("background-color: orange;color:white;" in i):
                                    if(val["BSC"]+" "+val['CELL'] not in final_col_for_data_pc):
                                        final_col_for_data_pc.append(val["BSC"]+" "+val["CELL"])

                    # print(table)
                    def apply_color(val):
                        if val.strip() == 'HALTED':
                            return 'background-color: rgb(250, 9, 9);color:white;'
                        else:
                            return ''
                    table['STATE'] = table['STATE'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')

                    combined_table_df2 = table.apply(apply_colorNew,axis=1)
                
                # print(table_df['substring_found'])

                    print(final_col_for_data,'GSMCell StatusCell Status')

                    # table_df1['Site Id'] = 'MIE04225A'
                    # table_df1 = table_df1[['Site Id','MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']]
                    html_table = global_style +table.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')

                    write_html_table("\n<h2>-----:GSM CELL STATUS-----:</h2>\n \n" + html_table)
   


fourth_file1(file_path4)

# addDataintoglobalDf('Cell Status',final_col_for_data_pc )

###############################################################################################################################################################################################################

######################  fourth file(CELL SYSTEM INFORMATION BCCH DATA) ##################################################################################################################

# if len(final_col_for_data_pc)>0:
#     final_col_for_data_pc.append('<br>')

file_path5="C:/Users/LENOVO/Desktop/dataframework/find_data/fifth_data.txt"
def fifth_file1(file_path5):
    with open(file_path5, 'r') as file:
        content5 = file.read()
        # print("lllll12",content3)

        if content5:
            start_marker1 = """lst VA61251A"""
            end_marker1 = """ alt  """

            start_index1 = content5.find(start_marker1)
            end_index1 = content5.find(end_marker1)
            extracted_data = content5[start_index1:end_index1]   
            # print( "lkj",extracted_data)

            if extracted_data:
                table_pattern2=r'(\d+)\s+\s*(\d+\s+\(\w+)\)\s+(\d+\s+\(\w+)\)\s+(RncFunction=\d,UtranCell=\S+)'  ###   (\d+\s+\(\w+)\)
                table_matches2 = re.findall(table_pattern2, extracted_data, re.MULTILINE)
                # if table_pattern2

                columns = ['Proxy','Adm State','Op. State','MO']    #'MO'
                table_df3 = pd.DataFrame(table_matches2, columns=columns)
                table_df3['Adm State'] = table_df3['Adm State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df3['Op. State'] = table_df3['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                d=table_df3['Proxy']
                d1 = d.loc[0]
                d2 = d.loc[6]
                d3 = d.loc[12]
                da=table_df3['Adm State']
                da1 = da.loc[0] 
                # print(da1,'da1')
                da2 = da.loc[6]
                da3 = da.loc[12]
                db=table_df3['Op. State']
                db1 = db.loc[0] 
                db2 = db.loc[6]
                db3 = db.loc[12]

                p=r"(RncFunction=\d,UtranCell=\S+)"
                if p in table_pattern2:
                    pattern=r"(?:UtranCell=(\S+))"
                    table_match = re.findall(pattern, extracted_data, re.MULTILINE)
                    columns=['CELL']
                    table_ = pd.DataFrame(table_match, columns=columns)
                    # print('table_',table_)
                    cell=table_['CELL']
                    cell1=cell.loc[0]
                    # print("cell1",cell1)
                    cell2=cell.loc[6]
                    cell3=cell.loc[12]

                data={
                    "RNC":globalSiteId_5,
                    "SITE_id":globalSiteId_7,
                    "CELL":(cell1,cell2,cell3),
                    'Proxy':(d1,d2,d3),
                    'Adm State':(da1,da2,da3),
                    'Op. State':(db1,db2,db3),
                    
                }
                da=pd.DataFrame(data)
                print(da,'1237654')

                # table=pd.DataFrame(dta)

                final_col_for_data=[]
                def apply_colorNew(val):
                    for i in val:
                        if(type(i)==type("str")):
                            if("background-color: rgb(250, 9, 9);color:white;" in i) or ("background-color: orange;color:white;" in i):
                                if(val["SITE_id"]+" "+val["CELL"] not in final_col_for_data_pc):
                                    final_col_for_data_pc.append(val["SITE_id"]+" "+val["CELL"])
                
                def apply_color(row):
                    if row['Adm State'].strip() == 'LOCKED' and row['Op. State'].strip() == 'DISABLED':
                        return 'background-color: orange;color:white;'
                    if not row['Adm State'].strip() == 'LOCKED' and row['Op. State'].strip() == 'DISABLED':
                        return 'background-color: red;color:white;'
                    # if row['cellBarred'].strip() == 'BARRED':
                    #     return 'background-color: red;'
                    
                    else:
                        return ''

                # Apply the function to the DataFrame
                da['Op. State'] = da.apply(lambda row: f'<span class="shobhit" style="{apply_color(row)}">{row["Op. State"]}</span>', axis=1)

                combined_table_df2 = da.apply(apply_colorNew,axis=1)

                print(final_col_for_data,'UMTSCell StatusCell Status')

                global_style = '<style>/* Your global CSS styles here */</style>'

                html_table = global_style +da.to_html(escape=False, index=False,
                                                    table_id='styled_table',
                                                    classes='table table-striped table-bordered')

                write_html_table("<h2>-----:UMTS Cell Status-----:-----:</h2>\n \n" + html_table)
                    
fifth_file1(file_path5)
addDataintoglobalDf('Cell Status',final_col_for_data_pc )
####################################################################################################################################

################### -----:5GNR RILINK:-----: ############################################################################################

file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
def third_file1(file_path3):
    with open(file_path3, 'r') as file:
        content3 = file.read()
        # print("lllll12",content3)
        if content3:
            start_marker = """hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
            end_marker = """hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""

            start_index = content3.find(start_marker)
            end_index = content3.find(end_marker)
            extracted_data = content3[start_index:end_index]   
            # print( "lkkhh",extracted_data)

            if extracted_data:
                # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                table_pattern1 = r"(EUtranCellFDD=\S+)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+\s+\(\w+\)|\s*)\s+(\w+)\s+(?:\[1\] = (SectorCarrier=\d+))"  #(SectorCarrier=\d+)\s+(\d+)+\s*(\d+\s+\(ENABLED\))+ \s*(?:\[\d+\] = (.+))$  # (^\[\d+\] = NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+)\s*
                table_matches1 = re.findall(table_pattern1, extracted_data, re.MULTILINE)

                columns = [ 'MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']   #,
                table_df1 = pd.DataFrame(table_matches1, columns=columns)
                table_df1['administrativeState'] = table_df1['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df1['cellBarred'] = table_df1['cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df1[ 'operationalState'] = table_df1[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                # print(table_df1)
                table_df1['Site Id'] = 'LVA61251A'
                table_df1 = table_df1[['Site Id','MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']]
                    # print('table_df1',table_df1)

##########################################################################################
    # file_path2="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    # with open(file_path2, 'r') as file:
    #     content2 = file.read()
    #     # print("lllll12",content3)
    #     if content2:
    #         start_marker = """hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
    #         end_marker = """hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""

    #         start_index = content2.find(start_marker)
    #         end_index = content2.find(end_marker)
    #         extracted_data = content3[start_index:end_index]   
    #         # print( "lkkhh",extracted_data)

    #         if extracted_data:
    #             # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
    #             # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
    #             table_pattern1 = r"(EUtranCellFDD=\S+)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+\s+\(\w+\)|\s*)\s+(\d+\s+\(\w+\)|\s*)\s+(\w+)\s+(?:\[1\] = (SectorCarrier=\d+))"  #(SectorCarrier=\d+)\s+(\d+)+\s*(\d+\s+\(ENABLED\))+ \s*(?:\[\d+\] = (.+))$  # (^\[\d+\] = NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+)\s*
    #             table_matches1 = re.findall(table_pattern1, extracted_data, re.MULTILINE)

    #             columns = [ 'MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']   #,
    #             table_df2 = pd.DataFrame(table_matches1, columns=columns)
    #             table_df2['administrativeState'] = table_df2['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
    #             table_df2['cellBarred'] = table_df2['cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
    #             table_df2[ 'operationalState'] = table_df2[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
    #             # print(table_df1)
    #             table_df2['Site Id'] = 'LVA61251A'
    #             table_df2 = table_df2[['Site Id','MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']]
    #                 # print('table_df1',table_df1)
#################################################################################################
                    
################################
    file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
    with open(file_path1, 'r') as file:
        content = file.read()
        # print(content)
        if content:
            start_marker = """ mfitr"""
            end_marker = """ """+globalSiteId+"""> pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'"""

            start_index = content.find(start_marker)
            end_index = content.find(end_marker)
            extracted_data = content[start_index:end_index]
            # print("lkjihih",extracted_data)

            if extracted_data :
#                 start_marker1 = """================================================================================================================================
# CELL            SC      FRU    BOARD          PUSCH  PUCCH       A      B      C      D  DELTA
# ================================================================================================================================"""
#                 end_marker1 = """================================================================================================================================

# MIE04225A> pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'"""

#                 start_index1 = content.find(start_marker1)
#                 end_index1 = content.find(end_marker1)
#                 extracted_data1 = content[start_index1:end_index1]

                # print("jjjj",extracted_data1)

                # if extracted_data1:
                #     pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
                #     table_matche = re.findall(pattern, extracted_data, re.MULTILINE)
                #     if table_matche:
                #         date = table_matche[0]
                #         print('date:::',date)
            # if extracted_data1:
                pattern1 = r'(FDD=\S+)\s+(\d+\-\d+\-\d+)\s+(\d+\-\d+)\s+(\S+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+\s*(\d+\.\d+|\d)\s'
                
                table_matches1= re.findall(pattern1, extracted_data, re.MULTILINE)

                if table_matches1:
                    columns = ['CELL','SC','FRU',' BOARD','PUSCH','PUCCH' ,'A','B','C','D','DELTA'] # 
                    table_df = pd.DataFrame(table_matches1, columns=columns)
                    # global table_df['CELL']
                    _1=table_df['CELL']
                    _2=table_df['A']

                    # print('_2',_2)
                    _3=table_df['B']
                    _4=table_df['C']
                    _5=table_df['D']
                    _6=table_df['DELTA']
                        # table_df.insert(0, 'Date', date)
                        # print('lklklk\n',table_df)
        ##########################################
        if content:
            start_marker = """hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
            end_marker = """hget ^EUtranCellFDD|TDD|NBIOT cellid|rachroo|tac|earfcnd|earfcnul|cellrange|dlChannelBandwidth$|ulChannelBandwidth$"""

            start_index = content.find(start_marker)
            end_index = content.find(end_marker)
            extracted_data = content[start_index:end_index]
            # print("lkjihih",extracted_data)

#             if extracted_data :
#                 start_marker1 = """=================================================================================================================
# MO                        administrativeState cellBarred     operationalState primaryPlmnReserved sectorCarrierRef
# ================================================================================================================="""
#                 end_marker1 = """=================================================================================================================
# Total: 6 MOs

# Added 6 MOs to group: hget_group

# MIE04225A> hget ^EUtranCellFDD|TDD|NBIOT cellid|rachroo|tac|earfcnd|earfcnul|cellrange|dlChannelBandwidth$|ulChannelBandwidth$"""

#                 start_index1 = content.find(start_marker1)
#                 end_index1 = content.find(end_marker1)
#                 extracted_data1 = content[start_index1:end_index1]

                # print("jjjj",extracted_data1)

                # if extracted_data1:
                #     pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
                #     table_matche = re.findall(pattern, extracted_data, re.MULTILINE)
                #     if table_matche:
                #         date = table_matche[0]
                #         print('date:::',date)
            if extracted_data:
                pattern2 = r'(EUtranCellFDD=\S+)\s(\d+\s+\(\w+)\)\s+(\d+\s+\(\w+)\)\s+(\d+\s+\(\w+)\)\s+(\w+)\s+(?:\[1\] = (SectorCarrier=\d+))'#(\d+\s+\(\w+)\)
                
                table_matches2= re.findall(pattern2, extracted_data, re.MULTILINE)
                # print('table_matches2',table_matches2)
                if table_matches2:
                    columns = ['MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef'] # 
                    table_df213= pd.DataFrame(table_matches2, columns=columns)
                    table_df213['administrativeState'] = table_df213['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                    table_df213['cellBarred'] = table_df213['cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                    table_df213[ 'operationalState'] = table_df213[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                    # table_df213['Site Id'] = 'MIE04225A'
                    # table_df213=table_df213[['Site Id','MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']]
                    # print('ttpp',table_df213)
                    s1=table_df213['MO']
                    # print('s1s1s1s1',s1)
                    s2=table_df213['administrativeState']
                    s3=table_df213['cellBarred']
                    s4=table_df213['operationalState']
                    s5=table_df213['primaryPlmnReserved']
                    s6=table_df213['sectorCarrierRef']

    #                 # print('ttt\n',table_df1)
    # ###########################################



                    dtta={
                        'Site Id':globalSiteId,
                        'MO':s1,
                        'administrativeState':s2,
                        'cellBarred':s3,
                        'operationalState':s4,
                        'primaryPlmnReserved':s5,
                        'sectorCarrierRef':s6,
                        # 'MO':_1,
                        'A':_2,
                        'B':_3,
                        'C':_4,
                        'D':_5,
                        'DELTA':_6
                    }
                    ddd=pd.DataFrame(dtta)
                    # ddd['Site Id'] = 'MIE04225A'
                    
                    # print('ddd',ddd)
                    

                    
######################################################################################
                combined_table_df = pd.concat([ddd,table_df1], ignore_index=True)
                # print('combined_table_df\n',combined_table_df)
                # if "NaN" in combined_table_df:
                #     combined_table_df.replace("NaN","")

                combined_table_df = combined_table_df.fillna('')

                def apply_color(val):
                    # if val.strip() == 'BARRED':
                    if val.strip() == 'BARRED' or val.strip() == 'true':
                        return 'background-color: rgb(250, 9, 9);color:white; '
                    else:
                        return ''
                # combined_table_df['cellBarred'] = combined_table_df['cellBarred'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')
                columns_to_apply = ['cellBarred', 'primaryPlmnReserved']

                combined_table_df[columns_to_apply] = combined_table_df[columns_to_apply].applymap(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')


                def apply_color(row):
                    if row['administrativeState'].strip() == 'LOCKED' and row['operationalState'].strip() == 'DISABLED':
                        return 'background-color: orange;color:white;'
                    if not row['administrativeState'].strip() == 'LOCKED' and row['operationalState'].strip() == 'DISABLED':
                        return 'background-color: red;color:white;'
                    # if row['cellBarred'].strip() == 'BARRED':
                    #     return 'background-color: red;'
                    
                    else:
                        return ''

                # Apply the function to the DataFrame
                combined_table_df['operationalState'] = combined_table_df.apply(lambda row: f'<span class="shobhit" style="{apply_color(row)}">{row["operationalState"]}</span>', axis=1)


                # global_style = '<style>/* Your global CSS styles here */</style>' 
                # ###############################################################
                html_table = global_style + combined_table_df.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')

                write_html_table("\n<h2>-----: RILINK STATUS:-----:</h2>\n \n" + html_table)
   
third_file1(file_path3)



################## UVA61251A2> hget ret electricalAntennaTilt|maxTilt|minTilt #############################################################################################

file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/fifth_data.txt" 
def sixth_file3(file_path3):
    with open(file_path3, 'r') as file:
        content3 = file.read()
        # print("lllll12",content3)
        if content3:
            start_marker = """st ret"""
            end_marker = """get . electrical"""

            start_index = content3.find(start_marker)
            end_index = content3.find(end_marker)
            extracted_data = content3[start_index:end_index]   
            # print( "lkkhh",extracted_data)

            if extracted_data:
#                 start_marker1 = """UVA61251A2> st ret

# 220105-08:31:51 11.170.49.196 17.0m RBS_NODE_MODEL_U_2_51 stopfile=/tmp/12453"""
#                 end_marker1 = """UVA61251A2> get . electrical

# 220105-08:31:52 11.170.49.196 17.0m RBS_NODE_MODEL_U_2_51 stopfile=/tmp/12453"""
#                 start_index1 = content3.find(start_marker1)
#                 end_index1 = content3.find(end_marker1)
#                 extracted_data1 = content3[start_index1:end_index1]   
                # print( "lllppp",extracted_data1)

            # if extracted_data1:
                table_pattern1= r"\b(\d+)\s+()\s+(\d+\s+\(\w+)\)\s+(.*)\b"
                # if table_pattern1 in extracted_data1:
                # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                # table_pattern1 = r"\b(\d+)\s+()\s+(\d+\s+\(ENABLED\))\s+(.*)\b"  #^1 \(ENABLED\)$

                # if re.match(table_pattern1, extracted_data1):
                #     print("Pattern matches extracted data1")
                

                table_matches1 = re.findall(table_pattern1, extracted_data, re.MULTILINE)
                # if table_matches1 in extracted_data1:

                columns = ['Proxy','Adm State',' Op. State ',' MO']   #
                table_df1 = pd.DataFrame(table_matches1, columns=columns)
                table_df1[' Op. State '] = table_df1[' Op. State '].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                # print(table_df1)
                a=table_df1[' Op. State ']
                # print(a)
                a1=a[29]
                a2=a[31]
                a3=a[34]
                a4=a[36]
                a5=a[39]
                a6=a[41]

                # print(a1)


            if extracted_data:
                start_marker1 = """hget ret electricalAntennaTilt|maxTilt|minTilt"""
                end_marker1 = """get . fqband"""
                start_index1 = content3.find(start_marker1)
                end_index1 = content3.find(end_marker1)
                extracted_data1 = content3[start_index1:end_index1]   
                # print( "lllppp",extracted_data1)

                if extracted_data1:
                    table_pattern1= r"\b(.*)\s+(\d+)\s+(\d+)\s+(\d+)\b"
                    # if table_pattern1 in extracted_data1:
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    # table_pattern1 = r"\b(\d+)\s+()\s+(\d+\s+\(ENABLED\))\s+(.*)\b"  #^1 \(ENABLED\)$

                    # if re.match(table_pattern1, extracted_data1):
                    #     print("Pattern matches extracted data1")
                    
  
                    table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)
                    # if table_matches1 in extracted_data1:

                    columns = ['MO','electricalAntennaTilt','maxTilt',' minTilt']   #
                    table_df1 = pd.DataFrame(table_matches1, columns=columns)
                    
                    t1=table_df1['MO']
                    t2=table_df1['electricalAntennaTilt']
                    # print(table_df1)

                    data={
                        "SITE_ID":globalSiteId_7,
                        'RET MO':t1,
                        'electricalAntennaTilt':t2,
                        'Op. State':[a1,a2,a3,a4,a5,a6]
                    }
                    dd=pd.DataFrame(data)
                    # print('laks',dd)



                    def apply_color(val):

                        if val.strip() == 'DISABLED':
                            return 'background-color: rgb(250, 9, 9); color:white;'
                        else:
                            return ''

                    dd['Op. State'] = dd['Op. State'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')

                    # Generate the HTML table with the applied styling
                    html_table = dd.to_html(escape=False, index=False, table_id='styled_table', classes='table table-striped table-bordered')


                    write_html_table("\n<h2>-----:UMTS RET STATUS:-----:</h2>\n \n" + html_table)
sixth_file3(file_path3)

################################################################################################################################################################################

################## MIE04225A> sdir #############################################################################################################################################################################################

def extract_data45(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = """sdir"""
        end_marker = """hget . allowedplmnlist"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]   
        # print( "lkkhh",extracted_data)

        if extracted_data:
            start_marker1 = """..........
+--------+                  +----------------+"""
            end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

"""+globalSiteId+""">

"""+globalSiteId+"""> hget . allowedplmnlist"""
            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]
            # print( "lllllmmmmmnnnn\n",extracted_data1)


            html_table = f"<h2>-----:MIE04225A SDIR:-----:</h2>\n{extracted_data1}"

            write_html_table(html_table)


extract_data45(file_path)

##############################################################################################################################

################### NIE04225A2> sdir ######################################################################################################

file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
def NIE04225A2_sdir(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        start_marker = """sdir"""
        end_marker = """cvls"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]   
        # print( "lkkhh",extracted_data)

        if extracted_data:
            start_marker1 = """...........
+--------+               +-------------+"""
            end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

"""+globalSiteId_2+"""> cvls"""
            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]

            html_table = f"<h2>-----:NIE04225A2 SDIR:-----:</h2>\n{extracted_data1}"

            write_html_table(html_table)


NIE04225A2_sdir(file_path)

##############################################################################################################

################### LVA61251A> sdir ########################################################################################

file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
def third_file2(file_path3):
    with open(file_path3, 'r') as file:
        content = file.read()

        start_marker = """sdir"""
        end_marker = """pst"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]   
        # print( "lkkhh",extracted_data)

        if extracted_data:
            start_marker1 = """.............................
+--------+                         +----------+"""
            end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

"""+globalSiteId_3+"""> pst"""
            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]
            # print( "lllllmmmmmnnnn\n",extracted_data1)


            html_table = f"<h2>-----:LVA61251A SDIR:-----:</h2>\n{extracted_data1}"
 
            write_html_table(html_table)

third_file2(file_path3)
###############################################################################################################################################################################

#####################  UVA61251A2> invxrc ##############################################################################################################################################
file_path5="C:/Users/LENOVO/Desktop/dataframework/find_data/fifth_data.txt"
def invxrc(file_path5):
    with open(file_path5, 'r') as file:
        content = file.read()

        start_marker = """invxrc"""
        end_marker = """get . digital"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]   
        # print( "lkkhh",extracted_data)

        if extracted_data:
            start_marker1 = """Node: RBS6131W                  CXP9023291/3_R4FA25 W15.0.2.5 (C15.0-EP19)"""
            end_marker1 = """get . dis"""
            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]
            # print( "lllllmmmmmnnnn\n",extracted_data1)


            html_table = f"<h2>-----:UVA61251A2 INVXRC:-----:</h2>\n{extracted_data1}"
 
            write_html_table(html_table)

invxrc(file_path5)






# column1 = []

# def Summary():
    # global column1
    # print(column21,'lkjhgfvvbnmm')
    # def color_Summary():
    #     if column21 == None:
    #     return  "f{html_table = html_table.replace}('<tr>', '<tr style="color: red;">', 1)"
    # summary = {
    #     "Item": ['RSSI', 'VSWR', 'VSWR Delta', 'Alarms', 'RET', 'RET Labels', 'TMA', 'SFP', 'Fiber Loss', 'SDIR', 'RRU Status', 'Cell Status', 'Other'],
    #     # "Status": [color_Summary() + ['NOK'] * 12,],  #'NOK', 'NOK', 'NOK', 'NOK', 'NOK', 'OK', 'NA', 'OK', 'NOK', 'OK', 'OK', 'NOK', 'OK'
    #     'Content':  [column21] + [None].len(row)    #column21 if len(column21) else [None] * 13  
    # }

    # summ_df = pd.DataFrame(summary)

    # def apply_color(val):
    #     if val.strip() == 'HALTED':
    #         return 'background-color: rgb(250, 9, 9);color:white; '
    #     else:
    #         return ''
    #     table['STATE'] = table['STATE'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')

    # html_table = global_style + summ_df.to_html(escape=False, index=False,
    #                                             table_id='styled_table',
    #                                             classes='table table-striped table-bordered')

    # write_html_table("\n<h2>-----:Summary:-----:</h2>\n" + html_table)
    
# Summary()




print(global_summ_df)

def apply_color(val):
    if val.strip() == 'NOK':
        return 'background-color: rgb(250, 9, 9);color:white; '
    else:
        return 'background-color: green;color:white;'
global_summ_df["Status"] = global_summ_df["Status"].apply(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')

html_table =  global_summ_df.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')
write_html_table_front("\n<h2>-----:SUMMARY:-----:</h2>\n "+html_table )

