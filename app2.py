import re
import pandas as pd
import os


def highlight_red(val):
    if val < '-116:00':
        return 'background-color: red;'
    else:
        return ''

##############################################################################

# extracted_path = os.path.join(os.getcwd(), "all_data", "final_data")
# f = open(extracted_path, "a+")
global_style = """
<style>
th {
    background-color: blue;
    color: white;
    text-align: left;

}

.condition {
        color: red; /* Define the styles for the 'condition' class */
        background-color: yellow;
    }


</style>
"""

open('out.html', 'w').close()

def write_html_table(html_table):
    # Write the HTML table to a file
    with open('outnnn.html', 'a') as html_file:
        html_file.write(html_table)

##############################################################################

extracted_path=os.path.join(os.getcwd(),"all_data","final_data")
f=open( extracted_path,"a+")
def write_data(data):   
    # f.write(data)
    f.write(data + "\n")
write_data("""\n\t--------------------------------------------------------------------------------------------\n
           ----------------------------------------PARSED DATA----------------------------------------\n
           ---------------------------------------------------------------------------------------------\n""" )

#######################################################################################################################
# @apply_blue_color_to_columns(patterns=['SiteID'])
def table_data():
    data = {'SiteID': ('MIE04225A',"NIE04225A2",'LVA61251A'),
            'RNC': ('N/A',"N/A","N/A"),
            'Node': ('RadioNode LN',"RadioNode N",'RadioNode L'),
            'Software Version': ('CXP9024418/15_R74C54 (23.Q2)',"CXP2010174/1_R71C54 (23.Q2)",'CXP9024418/15_R37C36 (21.Q3)'),
            'ONM IP': ('11.244.16.43',"11.244.16.42",'11.170.49.212'),
        }

    df = pd.DataFrame(data)
    global_style = "<style>td { text-align: left; }</style>"
    html_table = global_style + df.to_html(escape=False, index=False,
                                                              table_id='styled_table',
                                                              classes='table table-striped table-bordered')

    write_html_table("-----:NODE INFO:-----:"+html_table)

    # print(df)
    table=df.to_string(index=False)
    write_data('\n-----:NODE INFO:-----:\n '+table)
    # return df
table_data()
# write_data_to_file(result1, 'result1.html')

##########################################################################################################################

##################################
##############################################

file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"

def extract_data11(file_path):
    

    with open(file_path, 'r') as file:
        content = file.read()
        print('ccccccccccc', content)

##############################

        start_marker = "MIE04225A> hget (^FieldReplaceableUnit=|^AuxPlugInUnit=|^PlugInUnit=) administrativeState|operationalstate|product|isshared"
        end_marker = "MIE04225A> hget rilink RiLinkId|linkRate|operationalState|riPortRef1|riPortRef2"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]

        if extracted_data:
            table_pattern = r"^(FieldReplaceableUnit=\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\S+)\s+(\d+\s+\(ENABLED\))\s+(.+?)\s+(.+?)\s+(.+?)\s+(\S+)\s+(\S+)$"
            # table_pattern = r"^(FieldReplaceableUnit=\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\S+)\s+(\d+\s+\(ENABLED\))\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)$"
            table_matches = re.findall(table_pattern, extracted_data, re.MULTILINE)

            if table_matches:
                columns = ['MO', 'administrativeState', 'isSharedWithExternalMe', 'operationalState', 'productName', 'productNumber', 'productRevision', 'productionDate', 'serialNumber']
                table_df = pd.DataFrame(table_matches, columns=columns)
                # print("8th log::\n", table_df)

                serial= table_df["serialNumber"]
                # print('llaaa\n',serial)
                sn1=serial[0]
                sn2=serial[1]
                sn3=serial[3]

                print('llaaa\n',sn1,sn2,sn3)

                stat= table_df["operationalState"]
                # state1 = stat.replace('(', '').replace(')', '')
                # print(state1,'1qa')
                # state2 = stat.replace('1', '')
                # print(state2,'2qa')
                state=stat.replace("1","")
                # print('llaaa\n',state)
                op1=state[0]
                op1= op1.replace('(', '').replace(')', '').replace('1', '')
                # state2 = op1.replace('1', '')
                # print(state1,'2qa')
                op2=state[1]
                op2= op2.replace('(', '').replace(')', '').replace('1', '')
                op3=state[3]
                op3= op3.replace('(', '').replace(')', '').replace('1', '')

                # print('--------:VSWR:--------:\n',sn1,sn2,sn3)

                # secondLog=table_df.to_string()
                # write_data("fiifififiif:\n"+secondLog)
        #     else:
        #         print("No matching table data found.")
        # else:
        #     print("No extracted data found.")


#################################




        start_marker = """MIE04225A> sdir"""
        end_marker = """MIE04225A> hget . allowedplmnlist"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print( "lkkhh",extracted_data)



        if extracted_data :
            start_marker12="""MIE04225A> sdir"""
            end_marker12= """........................
...Checking available boards on node..."""
            start_index12 = content.find(start_marker12)
            end_index12 = content.find(end_marker12)
            extracted_data12= content[start_index12:end_index12]
            # print("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",extracted_data12)

            if extracted_data12:
                # pattern1=r"^(\d+:\d+:\d+)\s"

                # table_matches1 = re.findall(pattern1, extracted_data, re.MULTILINE)#, re.MULTILINE

                pattern1 = r'\b\d{2}:\d{2}:\d{2}-\d{4}\b'
                table_matches1 = re.findall(pattern1, extracted_data, re.MULTILINE)

                if table_matches1:
                    for time_string in table_matches1:
                        print("VSWR:Extracted time string:", time_string)
                else:
                    print("Time string not found in the data.")



        if extracted_data :
            # print("oi")
            start_marker12= """=====================================================================================================================================
FRU   ;LNH    ;BOARD          ;RF  ;BP  ;TX (W/dBm)  ;VSWR (RL)   ;RX (dBm) ;UEs/gUEs  ;Sector/AntennaGroup/Cells (State:CellIds:PCIs)
====================================================================================================================================="""
            end_marker12= """-------------------------------------------------------------------------------------------------------------------------------------

MIE04225A>

MIE04225A> hget . allowedplmnlist"""

            start_index12 = content.find(start_marker12)
            end_index12 = content.find(end_marker12)
            extracted_data12= content[start_index12:end_index12]
            # print("nnn",extracted_data12)
            

            if extracted_data12:
                # table_pattern12 = r'^(\d+-\d+)\s*;(\S+)\s*;(\S+)\s*;([^;]+);([^;]+);([^;]+);(\d+\.\d+\s+\(\d+\.\d+\))\s*;([^;]+);([^;]+);([^;]+)$'
                # table_pattern12 = r'^(\d+-\d+)\s*;(\S+)\s*;(\S+)\s*;([^;]+);([^;]+);([^;]+);(\d+\.\d+\s+\(\d+\.\d+\))\s*;([^;]+);([^;]+);([^;]+)$'
                # table_pattern12 = r'^(\d+-\d+)\s*;(\S+)\s*;(\S+)\s*;([^;]+);([^;]+);([^;]+);(\d+\.\d+\s+\(\d+\.\d+\))\s*;([^;]+);([^;]+);([^;]+)$'
                # table_pattern12 = r'^\s*(\d+-\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+-\s+(\S+)\s+(\d+\.\d+\s+\(\d+\.\d+\))\s+(\d+/-)\s*;([^;]+);([^;]+)$'
                # table_pattern12 = r'^\s*(\d+-\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+-\s+(\S+)\s+(\d+\.\d+\s+\(\d+\.\d+\))\s+(\d+/-)\s*;([^;]+);([^;]+)$'
                # table_pattern12 = r'^(\d+-\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\S+)\s+(\d+\.\d+\s+\(\d+\.\d+\))\s+(\d+/-)\s*;([^;]+);([^;]+)$'
                #SE=\d+-\d+\s+AG=\d+-\d+\s+FDD=\w+\s+FDD=\w+\s+NRC=\w+\s+\(\d+:\d+:\d+,\s+\d+:\d+:\d+,\s+\d+:\d+:\d+\)
                table_pattern12 = r'^(\d+-\d+)\s*;(\S+)\s*;(\S+)\s*;([^;]+);([^;]+);([^;]+);(\d+\.\d+\s+\(\d+\.\d+\))\s*;([^;]+);([^;]+);([^;]+)$(?!\s*[-]+)'
                # table_pattern12 = r'^\d+-\d+\s*;BXP_2\s*;([^\n]+)\s*;\s*[A-Z]\s*;\s*\d+\s*;[^;]*\s*;\s*[^;]*\s*;\s*[^;]*\s*;\s*[^;]*\s*;[^;]*$'

                # table_pattern12 = r'(\d+-\d+)\s*;BXP_2\s*;([^;]+)\s*;(\w)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(.+)'
                
                # table_pattern12 = r'^([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);(.+)$'

                # table_pattern12 = r'^(\S+)\s*;(\S+)\s*;(\S+)\s*;(\S+)\s*;(\S+)\s*;([\d\.\-]+)\s*;([\d\.\(\)]+)\s*;(\S*)\s*;(\S+)\s*;(.+)$'
                # table_pattern12 = r'^(\S+)\s*;(\S+)\s*;(\S+)\s*;(\S+)\s*;(\S+)\s*;([^;]+)\s*;([^;]+)\s*;(\S+)\s*;(\S+)\s*;(.+)$'
                # table_pattern12 = r'^([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);(.+)$'

                # table_pattern12 = r'^([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);(.+)$'

                table_matches12 = re.findall(table_pattern12, extracted_data12, re.MULTILINE)#, re.MULTILINE

                if table_matches12:

                    columns = ['FRU' , 'LNH', 'BOARD', 'RF', 'BP', 'TX (W/dBm)','VSWR (RL)','RX (dBm)','UEs/gUEs','Sector/AntennaGroup/Cells (State:CellIds:PCIs)']  ##,'RX (dBm)'  

                
                    table_df12 = pd.DataFrame(table_matches12, columns=columns,)#,
                    # table_df12 = table_df12[~table_df12['Sector/AntennaGroup/Cells (State:CellIds:PCIs)'].str.contains(r'-+MIE04225A>')]
                    # print(";;;;;;;:\n", table_df12)

            if extracted_data12:
                pattern = r'(FDD=\S+ FDD=\S+ NRC=\S+)\s'

                table_matches = re.findall(pattern, extracted_data12, re.MULTILINE)
                if table_matches:

                    columns1 = ['Sector/AntennaGroup/Cells (State:CellIds:PCIs)']  ##,'RX (dBm)'  

                
                    table = pd.DataFrame(table_matches, columns=columns1,)#,
                    # print("colllllllllllllllll:\n", table)
                    # table_df12 = table_df12[~table_df12['Sector/AntennaGroup/Cells (State:CellIds:PCIs)'].str.contains(r'-+MIE04225A>')]
                    global c1,c2,c3
                    
                    c1 = table.iloc[0]
                    c1=c1.to_string(index=False)
                    c2 = table.iloc[4] #
                    c2=c2.to_string(index=False)
                    c3 = table.iloc[8] 
                    c3=c3.to_string(index=False)

                    # print("Column 1:", c1)
                    # print("Column 2:", c2)
                    # print("Column 3:", c3)
                    

            #     else:
            #         print('not matches table')
            # else:
            #         print('not found data')





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
                    # print('b',B)

                    # delta1= a11-b11
                    # print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",delta1)

                    C=VSWR_column[2]
                    C1 = float(C.split()[0])
                    # print('c',C)

                    delta1= A1-C1
                    # print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",delta1)

                    D=VSWR_column[3]
                    D1= float(D.split()[0])
                    # print('d',D)
                    delta2= B1-D1
                    # print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",delta2)

                    E=VSWR_column[4]
                    # print(e)
                    E11= float(E.split()[0]) 
                    # print('e',E11)

                    F=VSWR_column[5]
                    # print(f)
                    F11= float(F.split()[0]) 
                    # print('f',F)

                    # delta12= e11-f11
                    # print("jklkllllllllllllllllllllllllllllll",delta12)

                    G=VSWR_column[6]
                    G11= float(G.split()[0])
                    # print('g',G)
                    delta3= E11-G11
                    # print("jklkllllllllllllllllllllllllllllll",delta3)

                    H=VSWR_column[7]
                    H11= float(H.split()[0])
                    # print('h',H)
                    delta4= F11-H11
                    # print("jklkllllllllllllllllllllllllllllll",delta4)

                    K=VSWR_column[8]
                    K13= float(K.split()[0]) 
                    # print('k',K13)

                    L=VSWR_column[9]
                    L13= float(L.split()[0]) 
                    # print('l',L13)
                    # delta13= k13-l13
                    # print("jklkllllllllllllllllllllllllllllll",delta13)

                    M=VSWR_column[10]
                    M13= float(M.split()[0])
                    # print('m',M13)

                    delta5= K13-M13
                    # print("j@@@@@@@@@@@@@@@@@@@@@@@@@@",delta5)


                    N=VSWR_column[11]
                    N13= float(N.split()[0])
                    # print('n',N)

                    delta6= L13-N13
                    # print("jklkllllllllllllllllllllllllllllll",delta6)


                    

                   

                    # rf_column = table_df12['RF']
                    # print("RF Column:\n", rf_column)


                    cell_column = table_df12['Sector/AntennaGroup/Cells (State:CellIds:PCIs)']
                    # print("Rcell Column:\n", cell_column)


                    table_df12 = table_df12['VSWR (RL)'].transpose()

                    # print("VSWR (RL) as Row:\n", table_df12)

                    # fourtysevenLog=table_df12.to_string(index=False)
                    # write_data("\n"+fourtysevenLog)

                    # table=df.to_string(index=False)
                    # write_data('\n-----:NODE INFO:-----:\n'+table)
########################################

    file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
# def extract_data1112(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # print('1qa',content)
        if content :
            # print('1qa',content)
            start_marker21= """NIE04225A2> sdir"""
            end_marker21= """-------------------------------------------------------------------------------------------------------------------------------------

NIE04225A2> cvls"""

            start_index21 = content.find(start_marker21)
            end_index21 = content.find(end_marker21)
            extracted_data21= content[start_index21:end_index21]
            # print("nnn",extracted_data21)

            if extracted_data21:
                # pattern1=r"^(\d+:\d+:\d+)\s"

                # table_matches1 = re.findall(pattern1, extracted_data, re.MULTILINE)#, re.MULTILINE

                pattern1 = r'\b\d{2}:\d{2}:\d{2}-\d{4}\b'
                table_matches1 = re.findall(pattern1, extracted_data21, re.MULTILINE)

                if table_matches1:
                    for time_string1 in table_matches1:
                        print("VSWR:Extracted time string:", time_string1)
                else:
                    print("Time string not found in the data.")
            

            if extracted_data21:
                start_marker22= """=====================================================================================================================================
FRU   ;LNH      ;BOARD       ;RF  ;BP  ;TX (W/dBm)  ;VSWR (RL)   ;RX (dBm) ;UEs/gUEs  ;Sector/AntennaGroup/Cells (State:CellIds:PCIs)
====================================================================================================================================="""
                end_marker22= """-------------------------------------------------------------------------------------------------------------------------------------

    NIE04225A2> cvls"""

                start_index22 = extracted_data21.find(start_marker22)
                end_index22 =extracted_data21.find(end_marker22)
                extracted_data22= extracted_data21[start_index22:end_index22]
                # print("nnn",extracted_data22)

                if extracted_data22:
                    
                    table_pattern22 = r'^(\d+-\d+)\s*;(\S+)\s*;(\S+)\s*;([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+)$(?!\s*[-]+)'   ######;(\d+\.\d+\s+\(\d+\.\d+\))\s*;([^;]+);([^;]+);([^;]+)$(?!\s*[-]+)
              

                    table_matches22 = re.findall(table_pattern22, extracted_data22, re.MULTILINE)#, re.MULTILINE
                    # print(';;;',table_matches22)
                    if table_matches22:

                        columns = ['FRU', 'LNH' , 'BOARD','RF', 'BP', 'TX (W/dBm)','VSWR (RL)','RX (dBm)','UEs/gUEs','Sector/AntennaGroup/Cells (State:CellIds:PCIs)']  ## '  

                    
                        table_df22 = pd.DataFrame(table_matches22, columns=columns,)#,

                        # table_df12 = table_df12[~table_df12['Sector/AntennaGroup/Cells (State:CellIds:PCIs)'].str.contains(r'-+MIE04225A>')]
                        # print("45th-12th:\n", table_df22)

                if extracted_data22:
                    # pattern23 = r'([^;]+)$'
                    pat=( r'(NRC=\S+)')
                    # if pat in pattern23:
                    table_matches23 = re.findall(pat, extracted_data22, re.MULTILINE)
                    # print(',,,,,',table_matches23)
                    if table_matches23:

                        # columns = ['Sector/AntennaGroup/Cells (State:CellIds:PCIs)']  ##,'RX (dBm)'  

                    
                        table23= pd.DataFrame(table_matches23)#,, columns=columns
                        # print('rrrrrrrrrr',table23)
                        # table_df23 = table_df23[~table_df23['Sector/AntennaGroup/Cells (State:CellIds:PCIs)'].str.contains(r'-+NIE04225A2>')]
                        # print("col:\n", table23)
                        # a=table23.iloc[0:2]
                        # print("Column a:", a)
                        # b=table23.iloc[2:4]
                        # print("Column b:", b)
                        # c=table23.iloc[4:6]
                        # print("Column c:", c)

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
                        # c11 = table23.iloc[0, 0] if not table23.empty else None
                        # c22 = table23.iloc[0, 0] if table23.shape[0] > 1 else None
                        # c33 = table23.iloc[0, 0] if table23.shape[0] > 2 else None

                        # print("Column 11:", c11)
                        # print("Column 22:", c22)
                        # print("Column 33:", c33)


                #     else:
                #         print('not matches table')
                # else:
                #         print('not found data')





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
                    site_Id1="MIE04225A"
                    

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
                    # print('asd',df)

                    site_Id2="NIE04225A2"
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

                    df1 = pd.DataFrame(data3, )
                    # print('3wa',df1)
                    # print("col:\n", df1.to_string(index=False))



                    
                    

                    

###########################


####################################

                    combined_table_df = pd.concat([df, df1], ignore_index=True)
                    # print('combined_table_df.columns',combined_table_df.columns)


                    def apply_color(val):

                        # print(len(val),"ENABLED",val.strip()=="ENABLED",)

                        # dskjhksajdlksa
                        if val.strip() == 'ENABLED':
                            return 'background-color: red; '
                        else:
                            return ''
                    combined_table_df['Op.State'] = combined_table_df['Op.State'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')
                    # combined_table_df['Op. State'] = combined_table_df['Op. State'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')


                    # combined_table_df = combined_table_df.reset_index(drop=True)
                    html_table = combined_table_df.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')
                    # with open('styled_table.html', 'w') as file:
                    #     file.write(html_table)

                    # Save or display the HTML table as needed
                    write_html_table("-----:VSWR:-----:\n" + html_table)



                    # def highlight_red(val):
                    #     if val == 'ENABLED':
                    #         return f'<span style="background-color: red; display: inline-block; padding: 2px;">{val}</span>'
                    #     else:
                    #         return val

                    # # Apply the highlight_red function to the specified columns
                    # columns_to_style = ["Op.State"]
                    # for column in columns_to_style:
                    #     combined_table_df[column] = combined_table_df[column].apply(highlight_red)

                    # # Reset the index
                    # combined_table_df = combined_table_df.reset_index(drop=True)

                    # html_table =combined_table_df.to_html(escape=False, index=False,
                    #                                           table_id='styled_table',
                    #                                           classes='table table-striped table-bordered')

                    # write_html_table("-----:VSWR:-----:\n"+html_table)

                    # print('3333333333333333333333333333333333333333333333333333333333333333333333333333oijinnhu\n',df)
                    # fourtysevenLog=df.to_string(index=False)
                    # write_data("\n"+fourtysevenLog)

                else:
                    print("No matching table data found.")  
            else:
                print("No extracted data found.")

                extract_data456(c1,c2,c3)
    # if file_path== None:
    #     return c1,c2,c3
extract_data11(file_path)


######################################
####################################################

#####################################################################################################################

#################################################################################################################

# def highlight_red(val):
#     color = 'red' if float(val) < -116 else 'black'
#     return f'color: {color};'
# def highlight_red(val):
#     if float(val) < -116:
#         return 'background-color: red;'
#     else:
#         return ''
file_path_copy='C:/Users/LENOVO/Desktop/dataframework/find_data/find_data copy.txt'
def RSSI(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # print(content)

        start_marker = """MIE04225A> pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'"""
        end_marker = """MIE04225A> pmr -m 3 -r 206 | egrep -i 'Acc_InitialERabEstabSuccRate|Acc_InitialErabSetupSuccRate|Acc_InitialUEContextEstabSuccRate|Acc_RrcConnSetupSuccRate|Acc_S1SigEstabSuccRate|Ret_ERabRetainabilityRate|Ret_ErabRelAbnormal'"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print("lkjihih",extracted_data)

        if extracted_data :
            start_marker1 = """206) LTE EUtranCell Traffic Performance, ROP by ROP
Report from \d{4}-\d{2}-\d{2}\s\d{2}:\d{2} UTC to \d{4}-\d{2}-\d{2}\s\d{2}:\d{2} UTC (12 ropfiles)
Node SW: CXP9024418/15_R74C54 (23.Q2)"""
            end_marker1 = """MIE04225A> pmr -m 3 -r 206 | egrep -i 'Acc_InitialERabEstabSuccRate|Acc_InitialErabSetupSuccRate|Acc_InitialUEContextEstabSuccRate|Acc_RrcConnSetupSuccRate|Acc_S1SigEstabSuccRate|Ret_ERabRetainabilityRate|Ret_ErabRelAbnormal'"""

            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]

            print("jjjj",extracted_data1)

            if extracted_data1:
                pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
                table_matche = re.findall(pattern, extracted_data, re.MULTILINE)
                if table_matche:
                    date = table_matche[0]
                    # print('date:::',date)
            if extracted_data1:
                pattern = r'\b(\d{2}:\d{2})\s+(\w+_\w+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s'
                
                table_matches1= re.findall(pattern, extracted_data1, re.MULTILINE)

                if table_matches1:
                    columns = ['Time','Counter ','DIE04225A11','DIE04225A21','DIE04225A31','EIE04225A11','EIE04225A21','EIE04225A31'] #  
                    table_df = pd.DataFrame(table_matches1, columns=columns)
                    a=table_df['DIE04225A11']
                    # print('aaaaaaa',a)
                    table_df.insert(0, 'Date', date)
                    # table_df['DIE04225A11'] = table_df.apply(lambda row: f'background-color: red;' if float(row['DIE04225A11']) < -116 else '', axis=1)
                    # table_df['DIE04225A11'] = table_df['DIE04225A11'].apply(lambda x: f'color: red; {x}' if float(x) < -116 else x)
                    # table_df = table_df.apply(highlight_red, subset=['DIE04225A11'])
                    # table_df.reset_index(drop=True, inplace=True)
                    # table_df.data = table_df.data.reset_index(drop=True)
                    
                    
                    # table_df = table_df.style.applymap(highlight_red, subset=['DIE04225A11'])
                    # # table_df = table_df.data
                    # # table_df = table_df.reset_index(drop=True)
                    # table_df = table_df.data.reset_index(drop=True)
                   
                    # html_tableFinal = table_df.to_html(escape=False, index=False,table_id='styled_table', classes='table table-striped table-bordered')  ###.replace('<table', '<table border="1" class="table table-striped table-bordered"')
                    # html_tableFinal = html_tableFinal.replace('<table', '<table border="1" class="table table-striped table-bordered"')



                    def highlight_red(val):
                        try:
                            val = float(val)
                            if val > -110 or val < -121 :
                                return f'<span style="background-color: red;">{val}</span>'
                            else:
                                return val
                        except ValueError:
                            return val

                    
                    columns_to_style = ['DIE04225A11', 'DIE04225A21', 'DIE04225A31', 'EIE04225A11', 'EIE04225A21', 'EIE04225A31']

                    # Apply styling to the specified columns
                    for column in columns_to_style:
                        table_df[column] = table_df[column].apply(highlight_red)
                    
                    # Reset the index to remove the index column
                    table_df = table_df.reset_index(drop=True)
                    
                    # Generate an HTML table with inline cell styling
                    html_tableFinal = table_df.to_html(escape=False, index=False, table_id='styled_table', classes='table table-striped table-bordered')
                    
                    # Replace the '<td>' tags to include 'style' attribute
                    # html_tableFinal = html_table.replace('<td>', '<td style="text-align: center;">')
                    
                    write_html_table("--------:RSSI--------:"+html_tableFinal)
# 
                else:
                    print("No matching table data found.")
            else:
                print("No extracted data found.")

RSSI(file_path)

##############################################################################################################################
file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
def alt(file_path3):
        # file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content = file.read()
        # print(content)

        start_marker = """LVA61251A> pmr -m .5 -r 206 | egrep '(Int_RadioRecInterference)'"""
        end_marker = """LVA61251A> pmxe -m 2 NRCellDU= Int_AvgRadioRecInterferencePwr$"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print("lkjihih",extracted_data)

        if extracted_data :
            start_marker1 = """206) LTE EUtranCell Traffic Performance, ROP by ROP
Report from 2022-01-05 13:00 UTC to 2022-01-05 13:29 UTC (2 ropfiles)
Node SW: CXP9024418/15_R37C36 ()
Error evaluating formula Oth_PathLossNbDistr at /opt/ericsson/amos/moshell/pmXtab line 453, <> line 9596."""
            end_marker1 = """LVA61251A> pmxe -m 2 NRCellDU= Int_AvgRadioRecInterferencePwr$"""

            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]

            # print("jjjj",extracted_data1)

            if extracted_data1:
                pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
                table_matche = re.findall(pattern, extracted_data, re.MULTILINE)
                if table_matche:
                    date = table_matche[0]
                    # print('date:::',date)
            if extracted_data1:
                pattern1 = r'\b(\d{2}:\d{2})\s+(\w+_\w+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s'
                
                table_matches1= re.findall(pattern1, extracted_data1, re.MULTILINE)

                if table_matches1:
                    columns = ['Time','Counter ','DVA61251A11','DVA61251A21','DVA61251A31','LVA61251A11','LVA61251A21','LVA61251A31'] # 

                    table_df = pd.DataFrame(table_matches1, columns=columns)
                    # table_df['DVA61251A11']
                    # print( list(table_df['DVA61251A11']),'++++++++++++++++++Shobhit++++++++++++++++')
                    table_df.insert(0, 'Date', date)
                    # print('lklklk',table_df)

                    html_table = global_style + table_df.to_html(escape=False, index=False,
                                                              table_id='styled_table',
                                                              classes='table table-striped table-bordered')

                    write_html_table("--------:RSSI--------(LVA61251A):"+html_table)

                    # print("RSSI:\n", table_df)
                    fourtysevenLog= table_df.to_string(index=False)
                    write_data("\n--------:RSSI:--------:\n"+fourtysevenLog)

alt(file_path3)  

#########################################################################################################################




################################################################################################################################


def extract_data111(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "MIE04225A> hget ^TermPointToGNodeB= ip|administrativeState|operationalState"
        end_marker = "MIE04225A> lst AntennaNearUnit"

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

                data= {"SiteID":["MIE04225A"],
                    "Total No. of X2 Links":[num_rows],
                    "Total No.of Disabled X2 Link":[DISABLED_count2],
                    "DISABLED_count2":[ENABLED_count1]

                }

                df = pd.DataFrame(data)
                # print('ppp',df)

##################################
    file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path1, 'r') as file:
        content = file.read()

        start_marker1 = "NIE04225A2> hget ^TermPointToGNodeB= ip|administrativeState|operationalState"
        end_marker1 = "NIE04225A2> stst"

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
                
                # print("ooooooooooooooo:\n", table_df1)

                num_rows1 = len(table_df1)
                # print(f"Number of rows: {num_rows1}")


                ENABLED_count3 = 0
                DISABLED_count4 = 0

                for i in table_df1['upIpAddress']:
                    if i == '(ENABLED)':
                        ENABLED_count3 += 1
                    elif i == '(DISABLED)':
                        DISABLED_count4 += 1
                    else:
                        print("Data not available")

                # print('Count of (ENABLED)NIE04225A2>:',ENABLED_count3)
                # print('Count of (DISABLED)NIE04225A2>:', DISABLED_count4)

                data1= {"SiteID":["NIE04225A2"],
                    "Total No. of X2 Links":[num_rows1],
                    "Total No.of Disabled X2 Link":[DISABLED_count4],
                    "DISABLED_count2":[ENABLED_count3]

                }

                df1 = pd.DataFrame(data1)
                # print('pppppppppppppppp',df1)
######################################
                combined_table_df = pd.concat([df, df1], ignore_index=True)
                html_table = global_style +combined_table_df.to_html(escape=False, index=False,
                                                              table_id='styled_table',
                                                              classes='table table-striped table-bordered')

                write_html_table("\n-----:X2 Link Status Start:----':\n"+html_table)

                # print(df)

                secondLog=df.to_string(index=False)
                write_data("\n-----:X2 Link Status Start:----':\n"+secondLog)

            else:
                print("No matching table data found.")
        else:
            print("No extracted data found.")

extract_data111(file_path)

################################################################################################################################

# def extract_data1(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()

#         start_marker = "hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"
#         end_marker = "MIE04225A> hget ^EUtranCellFDD|TDD|NBIOT cellid|rachroo|tac|earfcnd|earfcnul|cellrange|dlChannelBandwidth$|ulChannelBandwidth$"


#         start_index = content.find(start_marker)
#         end_index = content.find(end_marker)
#         extracted_data = content[start_index:end_index]
#         data_lines = []
#         lines = extracted_data.strip().split('\n')


#         for line in lines:
#             if not line.startswith('#'):
#                 data_lines.append(line)
#             # print("djwifhuhkjdjhbhbjf",line)
#         data_text = '\n'.join(data_lines)
#         # print( data_text)
# # extract_data(file_path)        

#         for i,li in enumerate(data_lines):
            
#             if(li=="================================================================================================================="):
#                 # print(f"Line index: {i}")
#                 # print(li, "data_lines")

#                 if i == 4 :
#                     table_pattern = r"(NRCellCU=\S+)\s+(\d+)\s*$"
#                     table_matches = re.findall(table_pattern, content, re.MULTILINE)
#                     if table_matches:
#                         columns = ['MO', 'nRTAC']
#                         table_df = pd.DataFrame(table_matches, columns=columns)
#                         # print("5th log::\n", table_df)
#                         # secondLog=table_df.to_string()
#                         # write_data("fifth-first log:\n'MIE04225A> hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$'::"+secondLog)
#                         # twentyfourLog=table_df.to_string()
#                         # write_data("twentyfourLog\n"+twentyfourLog)

#                     else:
#                         print("No matching data found.")

#                 if i==15: 

#                 # table_pattern = r"(NRCellDU=\S+)\s+(\S+)\s+(i\[\d+\]\s*=\s*\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\[.*\])\s+(\S+)\s+(\S+)\s+(\S+)"
#                     table_pattern1 = r"(\S+)\s+(\d+\s+\(UNLOCKED\))\s+i\[1\]\s*=\s*(\d+)\s+(\d+\s+\(NOT_BARRED\))\s+(\d+\s+\(NOT_RESERVED\))\s+(\d+)\s+\[1\]\s*=\s*(\S+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\d+)"
#                     # table_pattern1 = r"NRCellDU=(\S+)\s+(\d+)\s+\(UNLOCKED\)\s+i\[1\] = (\d+)\s+1 \(NOT_BARRED\)\s+1 \(NOT_RESERVED\)\s+(\d+)\s+\[1\] = NRSectorCarrier=(\S+)\s+(\d+)\s+1 \(ENABLED\)\s+(\d+)"
#                     # table_pattern1 = r"(NRCellDU=\S+)\s+(\d+)\s+\((\S+)\)\s+\S+\s+\((\S+)\)\s+\S+\s+\((\S+)\)\s+(\d+)\s+\[.*\]\s+(\d+)\s+\((\S+)\)\s+\d+"
#                     table_matches1 = re.findall(table_pattern1, content, re.MULTILINE)
#                     # if table_pattern1 in data_text: 

#                     if table_matches1:
#                         columns = ['MO', 'administrativeState', 'bandList', 'cellBarred', 'cellReservedForOperator','nRPCI','nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']
#                         table_df1 = pd.DataFrame(table_matches1, columns=columns)

#                         table_df1['Site Id'] = 'MIE04225A'
#                         table_df1['cellRange'] = ''

#                         table_df1 = table_df1[['Site Id','MO', 'administrativeState', 'bandList', 'cellBarred','cellRange', 'cellReservedForOperator','nRPCI','nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']]

#                         # combined_table_df = pd.concat([table_df1, table_df2], ignore_index=True)
#                         html_table = global_style +table_df.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                         write_html_table("\n-----:5GNR CELL STATUS:-----:\n"+html_table)

#                         print("5th-second log :\'hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$'::\n", table_df1)
#                         secondLog=table_df1.to_string(index=False)
#                         write_data("\n-----:5GNR CELL STATUS:-----:\n"+secondLog)
                        
#                     else:
#                         print("No matching data found.")

# extract_data1(file_path)
file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
def extract_data1112(file_path):
    # file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "MIE04225A> hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"
        end_marker = "MIE04225A> hget ^EUtranCellFDD|TDD|NBIOT cellid|rachroo|tac|earfcnd|earfcnul|cellrange|dlChannelBandwidth$|ulChannelBandwidth$"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print('table_matches',extracted_data)
        if extracted_data:
            table_pattern= r"(NRCellDU=\S+)\s+(\d+\s+\(UNLOCKED\))\s+(?:i\[1\] = (\d+))\s+(\d+\s+\(NOT_BARRED)\)\s+(\d+\s+\(NOT_RESERVED\))\s+(\d+)\s+(?:\[1\] = (NRSectorCarrier=\S+))\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\d+)"

            # Define regex pattern to extract data
            # table_pattern2= r"(\S+)\s+(\d+\s+\(UNLOCKED\))\s+i\[1\]\s*=\s*(\d+)\s+(\d+\s+\(NOT_BARRED\))\s+(\d+\s+\(NOT_RESERVED\))\s+(\d+)\s+\[1\]\s*=\s*(\S+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\d+)"
            # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))?\s+(\d+\s+\(\w+\))?\s+(.*)$'
            # table_pattern= r'NRCellDU=(.*?) (\d+)\s+\((.*?)\)\s+i\[2\] = (\d+)\s+\d+\s+(\d+)\s+\((.*?)\)\s+(\d+)\s+\[1\] = NRSectorCarrier=(.*?)\s+(\d+)\s+(\d+)\s+\((.*?)\)\s+(\d+)'
            # table_pattern= r"(NRCellDU=\S+)\s+(\d+\s+\(UNLOCKED\))\s+(i\[2\] = \d+\s+\d+\s+)\s+(\d+\s+\(\w+)\)\s+(\d+\s+\(NOT_RESERVED\))\s+(\d+)\s+(\[1\] = NRSectorCarrier=\S+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\d+)"
            # Find matches using the regex pattern
            table_matches = re.findall(table_pattern, extracted_data, re.MULTILINE)
            # print("table_matches",table_matches)
            if table_matches:
                columns = ['MO', 'administrativeState', 'bandList', 'cellBarred', 'cellReservedForOperator','nRPCI' ,'nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']  ### 
                table_df = pd.DataFrame(table_matches, columns=columns)
                table_df['operationalState'] = table_df['operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df['administrativeState'] = table_df['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df['cellBarred'] = table_df['cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df['cellReservedForOperator'] = table_df['cellReservedForOperator'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                # print(' table_df[operationalState]', table_df['operationalState'])
                # table_df=table_df.columns['operationalState']
                # table_df= table_df.replace('(', '').replace(')', '').replace('1', '')
                table_df['Site Id'] = 'MIE04225A'
                table_df['cellRange'] = ''
                table_df = table_df[['Site Id','MO', 'administrativeState', 'bandList', 'cellBarred','cellRange', 'cellReservedForOperator','nRPCI','nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']]
                # print('(((((())))))',table_df)

    file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path1, 'r') as file:
        content = file.read()

        start_marker1 = "NIE04225A2> hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"
        end_marker1 = "NIE04225A2> hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"

        start_index1 = content.find(start_marker1)
        end_index1 = content.find(end_marker1)
        extracted_data1 = content[start_index1:end_index1]
        # print(extracted_data1)
        if extracted_data1:
            # Define regex pattern to extract data
            # table_pattern2= r"(\S+)\s+(\d+\s+\(UNLOCKED\))\s+i\[1\]\s*=\s*(\d+)\s+(\d+\s+\(NOT_BARRED\))\s+(\d+\s+\(NOT_RESERVED\))\s+(\d+)\s+\[1\]\s*=\s*(\S+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\d+)"
            # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))?\s+(\d+\s+\(\w+\))?\s+(.*)$'
            # table_pattern= r'NRCellDU=(.*?) (\d+)\s+\((.*?)\)\s+i\[2\] = (\d+)\s+\d+\s+(\d+)\s+\((.*?)\)\s+(\d+)\s+\[1\] = NRSectorCarrier=(.*?)\s+(\d+)\s+(\d+)\s+\((.*?)\)\s+(\d+)'

            table_pattern1= r"(NRCellDU=\S+)\s+(\d+\s+\(UNLOCKED\))\s+\s*(?:i\[2\] = (\d+\s+\d+\s+))\s*+(\d+\s+\(\w+)\)\s+(\d+\s+\(NOT_RESERVED\))\s+(\d+)\s+(?:\[1\] = (NRSectorCarrier=\S+))\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\d+)"

            # table_pattern1 = r"(NRCellDU=\S+)\s+(\d+\s+\(UNLOCKED\))\s+\s*(?:i\[2\] = (\d+\s+\d+\s+))\s*+(\d+\s+\(\w+)\)\s+(\d+\s+\(NOT_RESERVED\))\s+(\d+)\s+(\[1\] = NRSectorCarrier=\S+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\d+)"

            # Find matches using the regex pattern
            table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)
            # print("table_matches",table_matches1)
            if table_matches1:
                columns = ['MO', 'administrativeState', 'bandList', 'cellBarred', 'cellReservedForOperator','nRPCI' ,'nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']  ### 
                table_df1 = pd.DataFrame(table_matches1, columns=columns)
                table_df1['operationalState'] = table_df1['operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df1['administrativeState'] = table_df1['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df1['cellBarred'] = table_df1['cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df1['cellReservedForOperator'] = table_df1['cellReservedForOperator'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '') 
                table_df1['Site Id'] = 'NIE04225A2'
                table_df1['cellRange'] = ''
                

                table_df1 = table_df1[['Site Id','MO', 'administrativeState', 'bandList', 'cellBarred','cellRange', 'cellReservedForOperator','nRPCI','nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']]
               
                combined_table_df = pd.concat([table_df, table_df1], ignore_index=True)
                print('combined_table_df',combined_table_df)

                # def apply_color(row):
                #     admin_state = row['administrativeState'].strip()
                #     operational_state = row['operationalState'].strip()
                    
                #     print(len(row), "ENABLED", operational_state == "ENABLED")
                    
                #     if admin_state == 'UNLOCKED' and operational_state == 'ENABLED':
                #         return 'background-color: red; color: white'
                #     if val.strip() == 'ENABLED':
                #             return 'background-color: red; '
                #         else:
                #             return ''

                #     dd['Op. State'] = dd['Op. State'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')
                #     else:
                #         return ''

                    # print(len(row),"ENABLED",row.strip()=="ENABLED",)
                    # if row['administrativeState'] == 'UNLOCKED' and row['operationalState'] == 'ENABLED':
                    #     return 'background-color: red; color: white'
                    # else:
                    #     return ''
                # combined_table_df['operationalState'] = combined_table_df.apply(apply_color, axis=1)
                # combined_table_df['operationalState'] = combined_table_df['operati/onalState'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')
                # combined_table_df['Op. State'] = combined_table_df['Op. State'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')


                # combined_table_df = combined_table_df.reset_index(drop=True)
                html_table = combined_table_df.to_html(escape=False, index=False,
                                                    table_id='styled_table',
                                                    classes='table table-striped table-bordered')

                # def apply_color(row):
                #     if row['administrativeState'] == 'UNLOCKED' and row['operationalState'] == 'ENABLED':
                #         return 'background-color: red; color: white'
                #     else:
                #         return ''

                # # Apply the CSS class to the entire DataFrame
                # styled_df = combined_table_df.style.applymap(apply_color, subset=['administrativeState', 'operationalState'])

                # # Generate the HTML table with the applied styling
                # html_table = styled_df.to_html(escape=False, index=False, classes='table table-striped table-bordered')

                # # Print the HTML table or write it to a file
                # print(html_table)
                with open('styled_table.html', 'w') as file:
                    file.write(html_table)

                html_table = combined_table_df.to_html(escape=False, index=False,
                                              table_id='styled_table',
                                              classes='table table-striped table-bordered')
                write_html_table("\n-----:5GNR CELL STATUS:-----:\n" + html_table)
                secondLog = table_df.to_string(index=False)
                write_data("\n-----:5GNR GPS AND SYNC:-----:\n" + secondLog)
            else:
                print("No matching table data found.")
        else:
            print("No extracted data found.")

# # Call the function with the file path
# # file_path = "path_to_your_log_file.txt"
extract_data1112(file_path)


#########################################################################################################################

# start_log_pattern = r'MIE04225A> alt'
# end_log_pattern = r'>>> Total: \d+ Alarms \(\d Critical, \d Major\)'
# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'

# def extract_between_logs(file_path, start_log_pattern, end_log_pattern):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         start_indices = [match.start() for match in re.finditer(start_log_pattern, content)]
#         end_indices = [match.start() for match in re.finditer(end_log_pattern, content)]

#         for start_idx, end_idx in zip(start_indices, end_indices):
#             section = content[start_idx:end_idx]
#             # print("Found relevant section:")
#             # print(section)
            
#             log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
#             matches = re.findall(log_pattern, section)
            
#             if matches:
#                 columns = ['Date & Time (UTC)', 'S Specific Problem', 'MO (Cause/AdditionalInfo)']
#                 table_df = pd.DataFrame(matches, columns=columns)
#                 # print("3rd log::\n",table_df)

#                 # table_df['Site Id'] = 'MIE04225A'

#                 # print("addition :log::\n", table_df)

#                 table_df['Site Id'] = 'MIE04225A'

#                 # Reorder columns
#                 table_df = table_df[[ 'Site Id','Date & Time (UTC)', 'S Specific Problem', 'MO (Cause/AdditionalInfo)']]
#                 print('999999999',table_df)
# ###################################
    
#     file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
#     with open(file_path1, 'r') as file:
#         content1 = file.read()
#         # print('4321',content1)

#         start_log_pattern =" NIE04225A2> alt"
#         end_log_pattern = r'>>> Total: \d+ Alarms \(\d Critical, \d Major\)'

#         start_indices1 = [match.start() for match in re.finditer(start_log_pattern, content1)]
#         end_indices1 = [match.start() for match in re.finditer(end_log_pattern, content1)]

#         for start_idx1, end_idx1 in zip(start_indices1, end_indices1):
#             section = content1[start_idx1:end_idx1]
            
#             print('1234',section)
            
#             log_pattern1 = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
#             matches = re.findall(log_pattern1, section)
            
#             if matches:
#                 columns = ['Date & Time (UTC)', 'S Specific Problem', 'MO (Cause/AdditionalInfo)']
#                 table_df1 = pd.DataFrame(matches, columns=columns)
#                 print("888888888888888888888",table_df1)

#                 table_df1['Site Id'] = 'NIE04225A2'

#                 # Reorder columns
#                 table_df1 = table_df1[[ 'Site Id','Date & Time (UTC)', 'S Specific Problem', 'MO (Cause/AdditionalInfo)']]
# ####################################################
#                 combined_table_df = pd.concat([table_df, table_df1], ignore_index=True)

#                 html_table = global_style + combined_table_df.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                 write_html_table("\n-----:5GNR ALARMS:-----:\n"+html_table)

#                 # print("additional column ::\n", table_df)

#                 secondLog=table_df.to_string(index=False)
#                 write_data("\n-----:5GNR ALARMS:-----:\n"+secondLog)
#             else:
#                 print("No matches found in the section.")
#             # print("=" * 100)



# extract_between_logs(file_path, start_log_pattern, end_log_pattern)


file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
def extract_data18(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "MIE04225A> alt"
        end_marker = "MIE04225A> get (^ENodeBFunction=1$|^GNBDUFunction=) ^gNBId$|^gNBIdLength$|^eNBId$"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print(extracted_data)
        if extracted_data:
            table_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(m)\s+(.+)\s+\(([^)]+)\)"
            # table_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'

            table_matches = re.findall(table_pattern, extracted_data, re.MULTILINE)

            if table_matches:
                columns = ['Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']  ### 
                table_df = pd.DataFrame(table_matches, columns=columns)

                table_df['Site Id'] = 'MIE04225A'
                table_df = table_df[['Site Id','Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']]  ### 
                
                
                # print("]]]]]]]]]]]]]]]]]]]]]\n",table_df)

    file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker1 = "NIE04225A2> alt"
        end_marker1 = "NIE04225A2> get (^ENodeBFunction=1$|^GNBDUFunction=) ^gNBId$|^gNBIdLength$|^eNBId$"

        start_index1 = content.find(start_marker1)
        end_index1 = content.find(end_marker1)
        extracted_data1 = content[start_index1:end_index1]
        # print(extracted_data1)
        if extracted_data1:
            # Define regex pattern to extract data
            table_pattern1 = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+m\s+(\S+)\s+(.+)\s+\(([^)]+)\)"

            # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))?\s+(\d+\s+\(\w+\))?\s+(.*)$'

            # table_pattern1 = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s;(\w+)\s; (\w+ \w+ \w+)\s;(.+)'

            # Find matches using the regex pattern
            table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

            if table_matches1:
                columns = ['Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']  ### 
                table_df1 = pd.DataFrame(table_matches1, columns=columns)

                table_df1['Site Id'] = 'NIE04225A2'
                table_df1 = table_df1[['Site Id','Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']]  ### 
                

                
                
                # print("]]]]]]]]]]]]]]]]]]]]]\n",table_df1)
    file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content = file.read()
        if content:
            start_marker2= "LVA61251A> alt"
            end_marker2 = "NIE04225A2> get (^ENodeBFunction=1$|^GNBDUFunction=) ^gNBId$|^gNBIdLength$|^eNBId$"

            start_index2 = content.find(start_marker2)
            end_index2 = content.find(end_marker2)
            extracted_data2 = content[start_index2:end_index2]
            # print(extracted_data1)
            if extracted_data2:
                # Define regex pattern to extract data
                table_pattern2 = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(m)\s+(.+)\s+\(([^)]+)\)"

                # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))?\s+(\d+\s+\(\w+\))?\s+(.*)$'

                # table_pattern1 = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s;(\w+)\s; (\w+ \w+ \w+)\s;(.+)'

                # Find matches using the regex pattern
                table_matches2 = re.findall(table_pattern2, extracted_data2, re.MULTILINE)

                if table_matches2:
                    columns = ['Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']  ### 
                    table_df2 = pd.DataFrame(table_matches2, columns=columns)

                    table_df2['Site Id'] = 'LVA61251A'
                    table_df2 = table_df2[['Site Id','Date & Time (UTC)', 'S','Specific Problem', 'MO (Cause/AdditionalInfo)']]  ### 
                    
                    combined_table_df = pd.concat([table_df, table_df1,table_df2], ignore_index=True)
                    # combined_table_df = pd.concat([table_df, table_df1], ignore_index=True)
                    
                    # print("]]]]]]]]]]]]]]]]]]]]]\n",table_df2)

                html_table = combined_table_df.to_html(escape=False, index=False,
                                              table_id='styled_table',
                                              classes='table table-striped table-bordered')
                write_html_table("\n-----:-----:5GNR ALARMS:-----::-----:\n" + html_table)
                secondLog = table_df.to_string(index=False)
                write_data("\n-----:-----:5GNR ALARMS:-----::-----:\n" + secondLog)

            else:
                print("No matching table data found.")
        else:
            print("No extracted data found.")


extract_data18(file_path)



################################################################################################################

# def extract_data18(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()

#         start_marker = "MIE04225A> st sync"
#         end_marker = "MIE04225A> get . noofsat"

#         start_index = content.find(start_marker)
#         end_index = content.find(end_marker)
#         extracted_data = content[start_index:end_index]
#         # print( extracted_data)

#         if extracted_data:
#             # table_pattern = r"(\d+)\s+-\s+\d\s+\(ENABLED\)\s+Equipment=(\d+),FieldReplaceableUnit=([A-Z0-9-]+),SyncPort=(\d+)"

#             # table_pattern =r'^(\d+)\s+(\d\s+\(\w+\))\s+(\w+\s*=\s*\d+\S*)\s*,\s*(\w+\s*=\s*\w+[-\d]+)\s*,\s*(\w+\s*=\s*\d+)'
#             # table_pattern = r"(\d+)\s+(\d\s+\(UNLOCKED\))\s+(\d+\s+\(ENABLED\))\s+(.*?)$"

#             table_pattern = r"(\d+)\s+(\d\s+\(UNLOCKED\))\s+(.*?)$" 

#             # table_pattern = r"(\d+)\s+([\d\s\(\)A-Z=]+)\s+(\d+\s?\(.*?\))?\s+(.*?)$"
#             # table_pattern = r"(\d+)\s+([\d\s\(\)A-Z=]+)\s+(\d+\s?\(.*?\))?\s+(.*)$"
#             # table_pattern = r"(\d+)\s+([\d\s\(\)A-Z=]+)\s+(\d+\s?\(.*?\))?\s+(.*)$"
#             # table_pattern = r"(\d+)\s+([\d\s\(\)A-Z=]+)\s+(\d+\s?\(.*?\))?\s+(.*)$"
#             # table_pattern = r"(NRNetwork=\d+,\w+=\w+,\w+=\w+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
#             table_matches = re.findall(table_pattern, extracted_data, re.MULTILINE)

#             if table_matches:
#                 columns = ['Proxy', 'Adm State',  'MO'] ### 'Op. State',
#                 # columns = ['MO', 'administrativeState', 'ipsecEpAddress', 'ipv4Address', 'ipv6Address', 'operationalState', 'upIpAddress', 'usedIpAddress']
#                 table_df = pd.DataFrame(table_matches, columns=columns)
#                 table_df['Site Id'] = 'MIE04225A'
#                 print('ttttttttttttttttt',table_df)
# #######################################
#             table_pattern = r"(\d+)\s+(\d\s+\(ENABLED\))\s+(.*?)$" 

#             # table_pattern = r"(\d+)\s+([\d\s\(\)A-Z=]+)\s+(\d+\s?\(.*?\))?\s+(.*?)$"
#             # table_pattern = r"(\d+)\s+([\d\s\(\)A-Z=]+)\s+(\d+\s?\(.*?\))?\s+(.*)$"
#             # table_pattern = r"(\d+)\s+([\d\s\(\)A-Z=]+)\s+(\d+\s?\(.*?\))?\s+(.*)$"
#             # table_pattern = r"(\d+)\s+([\d\s\(\)A-Z=]+)\s+(\d+\s?\(.*?\))?\s+(.*)$"
#             # table_pattern = r"(NRNetwork=\d+,\w+=\w+,\w+=\w+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"
#             table_matches = re.findall(table_pattern, extracted_data, re.MULTILINE)

#             if table_matches:
#                 columns = ['Proxy', 'Op. State',  'MO'] ### 'Op. State',
#                 # columns = ['MO', 'administrativeState', 'ipsecEpAddress', 'ipv4Address', 'ipv6Address', 'operationalState', 'upIpAddress', 'usedIpAddress']
#                 table_df2 = pd.DataFrame(table_matches, columns=columns)
#                 table_df2['Site Id'] = 'MIE04225A'
#                 print('ttttttttttttttttt',table_df2)

# ###############################################

# #########
#     # file_path = "C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
#     # with open(file_path, 'r') as file:
#     #     content = file.read()

#     #     start_marker1 = "NIE04225A2> st TermPoint"
#     #     end_marker1 = "NIE04225A2> lpr ,.*Relation="

#     #     start_index1 = content.find(start_marker1)
#     #     end_index1 = content.find(end_marker1)
#     #     extracted_data1 = content[start_index1:end_index1]
#     #     print('sssssssssssssssssssssss', extracted_data1)

#     #     if extracted_data1:
#     #         # table_pattern1 = r"(\d+)\s+(\d+\s+\(UNLOCKED\))\s+(\d+\s+\(ENABLED\))\s+(.*)$"
#     #         # table_pattern1 = r"(\d+)\s+(\d\s+\(UNLOCKED\))\s+(\d\s+\(ENABLED\))\s+(.*?)$"
#     #         # table_pattern1 = r"(\d+)\s+(\d\s+\(UNLOCKED\))\s+(\d\s+\(ENABLED\))\s+(.*?)$"
#     #         # table_pattern1 = r"(\d+)\s+(\d\s+\(UNLOCKED\))\s+(\d+\w+)\s+(.*?)$" 

#     #         table_pattern1 = r"(\d+)\s+([\d\s\(\)A-Z=]+)\s+(\d+\s?\(.*?\))?\s+(.*)$"
            
#     #         table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

#     #         if table_matches:
#     #             # columns = ['Proxy', 'Adm State', 'Op. State', 'MO']
#     #             # columns = ['MO', 'administrativeState', 'ipsecEpAddress', 'ipv4Address', 'ipv6Address', 'operationalState', 'upIpAddress', 'usedIpAddress']
#     #             table_df1 = pd.DataFrame(table_matches1, columns=columns)
#     #             table_df1['Site Id'] = 'NIE04225A2'
#     #             print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh',table_df)
#                 combined_table_df = pd.concat([table_df, table_df2], ignore_index=True)
# #################

#                 # Reorder columns

#                 table_df = table_df[[ 'Site Id','Proxy', 'Adm State','Op. State',  'MO']]   ## 
#                 html_table = global_style +combined_table_df.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                 write_html_table("\n-----:5GNR GPS AND SYNC:-----:\n" +html_table)

#                 # print("additional column ::\n", table_df)
#                 print(combined_table_df )
#                 print("18th log:\n", table_df)
#                 secondLog=table_df.to_string(index=False)
#                 write_data("\n-----:5GNR GPS AND SYNC:-----:\n" +secondLog)
#             else:
#                 print("No matching table data found.")
#         else:
#             print("No extracted data found.")

# extract_data18(file_path)




##############GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGOGGGGGGGGGGGPPPPPPPPPP###################


def extract_data18(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "MIE04225A> st sync"
        end_marker = "MIE04225A> get . noofsat"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]

        if extracted_data:
            table_pattern = r'(\d+)\s+(\S+\s+\(.*\)|\s*)\s+(\S+\s+\(.*\)|\s*)\s+(.*)$'
            # table_pattern = r'^(\d+)\s+(\d+\s+\(UNLOCKED\)|\d+\s+\(ENABLED\)|"-")\s+(\d+\s+\(UNLOCKED\)|\d+\s+\(ENABLED\)|"-")\s+(.*)$'

            # Define regex pattern to extract data
            # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))\s+(\d+\s+\(\w+\))?\s+(.*)$'
            # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))?\s+(\d+\s+\(\w+\))?\s+(.*)$'

            
            table_matches = re.findall(table_pattern, extracted_data, re.MULTILINE)

            if table_matches:
                columns = ['Proxy', 'Adm State', 'Op. State', 'MO']

                table_df = pd.DataFrame(table_matches, columns=columns)
                table_df['Adm State'] = table_df['Adm State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df['Op. State'] = table_df['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                table_df['Site Id'] = 'MIE04225A'
                table_df = table_df[['Site Id','Proxy', 'Adm State', 'Op. State', 'MO']]
                # table_df['Adm State'] = table_df.apply(lambda row: row['Adm State'] if 'UNLOCKED' in row['Op. State'] else '', axis=1)
                # table_df['Op. State'] = table_df.apply(lambda row: row['Op. State'] if 'ENABLED' in row['Adm State'] else '', axis=1)
                # print("18th log:")
                # print("]]]]]]]]]]]]]]]]]]]]]\n",table_df)


############
    file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path1, 'r') as file:
        content = file.read()

        start_marker1 = "NIE04225A2> st sync"
        end_marker1 = "NIE04225A2> get . noofsat"

        start_index1 = content.find(start_marker1)
        end_index1 = content.find(end_marker1)
        extracted_data1 = content[start_index1:end_index1]
        # print('aaaaaaaaaa',extracted_data1)
        if extracted_data1:
            # Define regex pattern to extract data
            
            # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))?\s+(\d+\s+\(\w+\))?\s+(.*)$'
            # table_pattern1 = r'(\d+)\s+(\d+\s+\(\w+\))\s+(\d+\s+\(\w+\))\s+(.*)$'

            table_pattern1 = r'(\d+)\s+(\S+\s+\(.*\)|\s*)\s+(\S+\s+\(.*\)|\s*)\s+(.*)$'

            # Find matches using the regex pattern
            table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

            if table_matches1:
                columns = ['Proxy', 'Adm State', 'Op. State', 'MO']   ### 
                table_df1 = pd.DataFrame(table_matches1, columns=columns)  ##
                table_df1['Adm State'] = table_df1['Adm State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df1['Op. State'] = table_df1['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df1['Site Id'] = 'NIE04225A2'
                table_df1 = table_df1[['Site Id','Proxy', 'Adm State', 'Op. State', 'MO']]  ### 
                
                # print("18th log:")
                # print("]]]]]]]]]]]]]]]]]]]]]\n",table_df1)

##########################################################
    file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content = file.read()
        # print('content',content)
        start_marker2 = "LVA61251A> st sync"
        end_marker2 = "LVA61251A> get ^RadioEquipmentClock= ^radioClockState$"

        start_index2 = content.find(start_marker2)
        end_index2 = content.find(end_marker2)
        extracted_data2 = content[start_index2:end_index2]
        # print('aaaaaaaaaa',extracted_data2)
        if extracted_data2:
            # Define regex pattern to extract data
            
            # table_pattern = r'^(\d+)\s+(\d+\s+\(\w+\))?\s+(\d+\s+\(\w+\))?\s+(.*)$'
            # table_pattern1 = r'(\d+)\s+(\d+\s+\(\w+\))\s+(\d+\s+\(\w+\))\s+(.*)$'

            table_pattern2 = r'(\d+)\s+()\s+(\d+\s+\(ENABLED\))\s(.*)'

            # Find matches using the regex pattern
            table_matches2 = re.findall(table_pattern2, extracted_data2, re.MULTILINE)

            if table_matches2:
                columns = ['Proxy', 'Adm State', 'Op. State', 'MO']   ### 
                table_df2 = pd.DataFrame(table_matches2, columns=columns)  ##
                table_df2['Adm State'] = table_df2['Adm State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df2['Op. State'] = table_df2['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                table_df2['Site Id'] = 'LVA61251A'
                table_df2 = table_df2[['Site Id','Proxy', 'Adm State', 'Op. State', 'MO']]  ### 
                
                # print("18th log:")
                # print("]]]]]]]]]]]]]]]]]]]]]\n",table_df2)

                

                combined_table_df = pd.concat([table_df, table_df1,table_df2], ignore_index=True)

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
                write_html_table("\n\n-----:5GNR GPS AND SYNC:-----: \n" + html_table)
                # secondLog = table_df.to_string(index=False)
                # write_data("\n-----:5GNR GPS AND SYNC:-----:\n" + secondLog)
            else:
                print("No matching table data found.")
        else:
            print("No extracted data found.")

# Call the function with the file path
# file_path = "path_to_your_log_file.txt"
extract_data18(file_path)




##############################GGGGGGGGGGGGGG**************G#*((#################))



##################################################################################################################

def ANTENNANEARUNIT(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = """MIE04225A> hget ^AntennaNearUnit= ^rfPortRef$|^onUnitUniqueId$|^uniqueId$"""
        end_marker = """MIE04225A> hget ^RetSubUnit= ^electricalAntennaTilt$|^iuantAntennaModelNumber$|^iuantBaseStationId$|^maxTilt$|^minTilt$|^operationalState$|^tiltChangeStatus$|^userLabel$"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print(extracted_data)

        if extracted_data :
            start_marker1 = """=================================================================================================================
MO                                      onUnitUniqueId      rfPortRef                          uniqueId
================================================================================================================="""
            end_marker1 = """=================================================================================================================
Total: 3 MOs

Added 3 MOs to group: hget_group

MIE04225A> hget ^RetSubUnit= ^electricalAntennaTilt$|^iuantAntennaModelNumber$|^iuantBaseStationId$|^maxTilt$|^minTilt$|^operationalState$|^tiltChangeStatus$|^userLabel$"""

            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]

            # print("jjjj",extracted_data1)

            if extracted_data1:
                # table_pattern1 = r"AntennaUnitGroup=(\d+-\d+),AntennaNearUnit=(\d+)\s+(RF\d+-\w+)\s+FieldReplaceableUnit=(\d+-\d+),RfPort=\w+\s+(RF\d+-\w+)"
                # table_pattern1 = r"AntennaUnitGroup=(\d+-\d+),AntennaNearUnit=(\d+)\s+(RF\d+-\w+)\s+FieldReplaceableUnit=(\d+-\d+),RfPort=\w+\s+(RF\d+-\w+)"
                # table_pattern1 = r"AntennaUnitGroup=(\d+-\d+),AntennaNearUnit=(\d+)\s+(RF\d+-\w+)\s+FieldReplaceableUnit=(\d+-\d+),RfPort=\w+\s+(RF\d+-\w+)"
                # table_pattern1 = r"^(AntennaUnitGroup=\d+-\d+,AntennaNearUnit=\d+)\s+(RF\d+-\w+)\s+FieldReplaceableUnit=(\d-\d)\s+RfPort=\w+\s+(RF\d+-\w+)$"
                table_pattern1 = r"^(AntennaUnitGroup=\d+-\d+,AntennaNearUnit=\d+).*(RF\d+-\w+).*(FieldReplaceableUnit=\d-\d).*(RfPort=\w+\s+RF\d+-\w+)$"
                # table_pattern1=r"^(AntennaUnitGroup=\d-\d+,AntennaNearUnit=\d+)\s*;(RF\d+-\w+)"  #;(\S+)\s*;(\S+)\s*;(\S+)\s*
                # table_pattern  =  r'^\s*(\d+)\s+(\d\s+\(\w+\))\s+(\d\s+\(\w+\))\s+(.+)$'
                # table_pattern = re.compile(r'\s+(\d+)\s+(\d \([A-Z]+\))\s+(\d \([A-Z]+\))\s+(.+)')
                # table_pattern= r"(\d+)\s+(PmJob=\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\d+)\s*$"
                # table_pattern = r"(NRCellCU=\S+)\s+(caStatusActive)\s+(\S+)"
                
                table_matches1= re.findall(table_pattern1, extracted_data1, re.MULTILINE)

                if table_matches1:
                    columns = ['MO ','onUnitUniqueId','rfPortRef','uniqueId'] #,'rfPortRef','uniqueId'
                    # columns = [ 'Proxy ', 'Adm State','Op. State','MO']
                    # columns = [ 'Proxy', 'Job','ReqState','CurrState','Granul','nrRdrs/Evts']
                    # columns = [ 'Time', 'Object','pmCaConfigAtt','pmCaConfigDlSamp','pmCaConfigDlSumSaDistr','pmCaConfigSucc','pmEndcCaConfigAtt','pmEndcCaConfigSucc']
                    table_df = pd.DataFrame(table_matches1, columns=columns)


                    table_df['Site Id'] = 'MIE04225A'

                # Reorder columns
                    table_df = table_df[[ 'Site Id','MO ','onUnitUniqueId','rfPortRef','uniqueId']]

                    html_table = global_style + table_df.to_html(escape=False, index=False,
                                                              table_id='styled_table',
                                                              classes='table table-striped table-bordered')

                    write_html_table("-----:5GNR ANTENNANEARUNIT:-----:"+html_table)

                    # print("ANTENNANEARUNIT:\n", table_df)
                    fourtysevenLog= table_df.to_string(index=False)
                    write_data("-----:5GNR ANTENNANEARUNIT:-----:"+fourtysevenLog)
                else:
                    print("No matching table data found.")
            else:
                print("No extracted data found.")


ANTENNANEARUNIT(file_path)


####################################################################################################################
def ret(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = """MIE04225A> hget ^RetSubUnit= ^electricalAntennaTilt$|^iuantAntennaModelNumber$|^iuantBaseStationId$|^maxTilt$|^minTilt$|^operationalState$|^tiltChangeStatus$|^userLabel$"""
        end_marker = """MIE04225A> hget ^TmaSubUnit= ^tmaType$|^iuantAntennaModelNumber$|^iuantBaseStationId$|^dlAttenuation$|^dlTrafficDelay$|^operationalState$|^ulGain$|^userLabel$|^ulTrafficDelay$"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]
        # print(extracted_data)

        if extracted_data :
            start_marker1 = """=================================================================================================================
MO                                                   electricalAntennaTilt iuantAntennaModelNumber iuantBaseStationId maxTilt minTilt operationalState tiltChangeStatus userLabel
================================================================================================================="""
            end_marker1 = """=================================================================================================================
Total: 3 MOs

Added 3 MOs to group: hget_group

MIE04225A> hget ^TmaSubUnit= ^tmaType$|^iuantAntennaModelNumber$|^iuantBaseStationId$|^dlAttenuation$|^dlTrafficDelay$|^operationalState$|^ulGain$|^userLabel$|^ulTrafficDelay$"""

            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]

            # print("jjjj",extracted_data1)

            if extracted_data1:
                table_pattern1 = r'(AntennaUnitGroup=\d+-\d+,AntennaNearUnit=\d+,RetSubUnit=\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d\s+\(ENABLED\))\s+(\d\s+\(IDLE\))\s+(\S+)'
                # table_pattern1 = r"AntennaUnitGroup=(\d+-\d+),AntennaNearUnit=(\d+)\s+(RF\d+-\w+)\s+FieldReplaceableUnit=(\d+-\d+),RfPort=\w+\s+(RF\d+-\w+)"
                # table_pattern1 = r"AntennaUnitGroup=(\d+-\d+),AntennaNearUnit=(\d+)\s+(RF\d+-\w+)\s+FieldReplaceableUnit=(\d+-\d+),RfPort=\w+\s+(RF\d+-\w+)"
                # table_pattern1 = r"AntennaUnitGroup=(\d+-\d+),AntennaNearUnit=(\d+)\s+(RF\d+-\w+)\s+FieldReplaceableUnit=(\d+-\d+),RfPort=\w+\s+(RF\d+-\w+)"
                # table_pattern1 = r"^(AntennaUnitGroup=\d+-\d+,AntennaNearUnit=\d+)\s+(RF\d+-\w+)\s+FieldReplaceableUnit=(\d-\d)\s+RfPort=\w+\s+(RF\d+-\w+)$"
                # table_pattern1 = r"^(AntennaUnitGroup=\d+-\d+,AntennaNearUnit=\d+).*(RF\d+-\w+).*(FieldReplaceableUnit=\d-\d).*(RfPort=\w+\s+RF\d+-\w+)$"
                
                table_matches1= re.findall(table_pattern1, extracted_data1, re.MULTILINE)

                if table_matches1:
                    columns = ['MO ','electricalAntennaTilt','iuantAntennaModelNumber','iuantBaseStationId','maxTilt','minTilt','operationalState','tiltChangeStatus',' userLabel'] #,'rfPortRef','uniqueId'
                    # columns = [ 'Proxy ', 'Adm State','Op. State','MO']
                    # columns = [ 'Proxy', 'Job','ReqState','CurrState','Granul','nrRdrs/Evts']
                    # columns = [ 'Time', 'Object','pmCaConfigAtt','pmCaConfigDlSamp','pmCaConfigDlSumSaDistr','pmCaConfigSucc','pmEndcCaConfigAtt','pmEndcCaConfigSucc']
                    table_df = pd.DataFrame(table_matches1, columns=columns)
                    table_df['operationalState'] = table_df['operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    table_df['tiltChangeStatus'] = table_df['tiltChangeStatus'].str.replace(r'(', '').str.replace(')', '').str.replace('3', '')

                    table_df['Site Id'] = 'MIE04225A'

                # Reorder columns
                    table_df = table_df[[ 'Site Id','MO ','electricalAntennaTilt','iuantAntennaModelNumber','iuantBaseStationId','maxTilt','minTilt','operationalState','tiltChangeStatus',' userLabel']]
                    html_table = global_style + table_df.to_html(escape=False, index=False,
                                                              table_id='styled_table',
                                                              classes='table table-striped table-bordered')

                    write_html_table("-----:5GNR RET Status:-----:\n"+html_table)

                    # print("RetSubUnit:\n", table_df)
                    fourtysevenLog= table_df.to_string(index=False)
                    write_data("-----:5GNR RET Status:-----:\n"+fourtysevenLog)
                else:
                    print("No matching table data found.")
            else:
                print("No extracted data found.")



ret(file_path)
############################################################################################################################################################################


#####################################################################################################


def extract_data2(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "MIE04225A> hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"
        end_marker = "MIE04225A> hget ^SectorEquipmentFunction= administrativeState|operationalState|availableHwOutputPower|reservedBy"

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
                    table_pattern = r"(\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(?:\[1\]\s*=\s*( ))"
                    table_matches = re.findall(table_pattern, content, re.MULTILINE)
                    if table_matches:
                        columns = ['MO', 'administrativeState', 'arfcnDL', 'arfcnUL', 'bSChannelBwDL', 'bSChannelBwUL', 'configuredMaxTxPower', 'operationalState', 'reservedBy']
                        table_df = pd.DataFrame(table_matches, columns=columns)
                        table_df['administrativeState'] = table_df['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                        table_df[ 'operationalState'] = table_df[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                        table_df['Site Id'] = 'MIE04225A'

                # Reorder columns
                        table_df = table_df[[ 'Site Id','MO', 'administrativeState', 'arfcnDL', 'arfcnUL', 'bSChannelBwDL', 'bSChannelBwUL', 'configuredMaxTxPower', 'operationalState', 'reservedBy']]
    file_path = "C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker1 = "NIE04225A2> hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"
        end_marker1 = "NIE04225A2> hget ^SectorEquipmentFunction= administrativeState|operationalState|availableHwOutputPower|reservedBy"

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
                    table_pattern1 = r"(\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(?:\[1\]\s*=\s*(NRCellDU=\S+))"
                    table_matches1 = re.findall(table_pattern1, content, re.MULTILINE)
                    if table_matches1:
                        columns = ['MO', 'administrativeState', 'arfcnDL', 'arfcnUL', 'bSChannelBwDL', 'bSChannelBwUL', 'configuredMaxTxPower', 'operationalState', 'reservedBy']
                        table_df1 = pd.DataFrame(table_matches1, columns=columns)
                        table_df1['administrativeState'] = table_df1['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                        table_df1[ 'operationalState'] = table_df1[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                # table_df1['Op. State'] = table_df1['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                        table_df1['Site Id'] = 'NIE04225A2'
                        # print('12222222222222222222@@@@@@@@@@',table_df1)
                        combined_table_df = pd.concat([table_df, table_df1], ignore_index=True)



                        html_table = global_style + combined_table_df.to_html(escape=False, index=False,
                                                              table_id='styled_table',
                                                              classes='table table-striped table-bordered')

                        write_html_table("\n-----:5GNR SECTOR STATUS:-----:\n"+html_table)
                        # print("6th log::\n", combined_table_df)
                        twentyfourLog=table_df.to_string(index=False)
                        write_data("\n-----:5GNR SECTOR STATUS:-----:\n"+twentyfourLog)

                    else:
                        print("No matching data found.")


extract_data2(file_path)



# def extract_data2(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()

#         start_marker = "MIE04225A> hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"
#         end_marker = """=================================================================================================================
# MO                    configuredMaxTxPower operationalState reservedBy
# ================================================================================================================="""
#         start_index = content.find(start_marker)
#         end_index = content.find(end_marker)
#         extracted_data = content[start_index:end_index]
#         print( '1111111111111111111111111111111',extracted_data)
#         if extracted_data:
#             start_marker1 = """=================================================================================================================
# MO                      administrativeState arfcnDL arfcnUL bSChannelBwDL bSChannelBwUL configuredMaxTxPower operationalState reservedBy
# ================================================================================================================="""
#             end_marker1 = """=================================================================================================================
# MO                    configuredMaxTxPower operationalState reservedBy
# ================================================================================================================="""
#             start_index1 = content.find(start_marker1)
#             end_index1 = content.find(end_marker1)
#             extracted_data1 = content[start_index1:end_index1]
#             print("22222222222222222222",extracted_data1)




 #################################################################################################################

# def extract_data5(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()

#         start_marker = "MIE04225A> hget rilink RiLinkId|linkRate|operationalState|riPortRef1|riPortRef2"
#         end_marker = "IE04225A> hget sfp prod"

#         start_index = content.find(start_marker)
#         end_index = content.find(end_marker)
#         extracted_data1 = content[start_index:end_index]
#         # print( extracted_data)

#     file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
#     with open(file_path, 'r') as file:
#         content = file.read()

#         start_marker = "NIE04225A2> hget rilink RiLinkId|linkRate|operationalState|riPortRef1|riPortRef2"
#         end_marker = "NIE04225A2> hget sfp prod"

#         start_index = content.find(start_marker)
#         end_index = content.find(end_marker)
#         extracted_data2 = content[start_index:end_index]
#         print('lllllll', extracted_data2)

#         if extracted_data1:
#             table_pattern1 = r"(.+?)\s+(\d+)\s+(\d\s+\(ENABLED\))\s+(.+?)\s+(.+?)\s+(.+)$"
#             table_matches1 = re.findall(table_pattern1, extracted_data1 , re.MULTILINE)
        
#         if extracted_data2:
#             table_pattern2 = r"(.+?)\s+(\d+)\s+(\d\s+\(ENABLED\))\s+(.+?)\s+(.+?)\s+(.+)$"
#             table_matches2 = re.findall(table_pattern2, extracted_data2 , re.MULTILINE)

#             if table_matches1:
#                 columns= ['MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']
#                 # columns = ['MO', 'administrativeState', 'isSharedWithExternalMe', 'operationalState', 'productName', 'productNumber', 'productRevision', 'productionDate', 'serialNumber']
#                 table_df1 = pd.DataFrame(table_matches1, columns=columns)

#                 table_df1['Site Id'] = 'MIE04225A'

#             if table_matches2:
#             # columns= ['MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']
#             # columns = ['MO', 'administrativeState', 'isSharedWithExternalMe', 'operationalState', 'productName', 'productNumber', 'productRevision', 'productionDate', 'serialNumber']
#                 table_df2 = pd.DataFrame(table_matches2)
#                 print('klllllllkklklk',table_df2)
#                 table_df2['Site Id'] = 'NIE04225A2'

#                 combined_table_df = pd.concat([table_df1, table_df2], ignore_index=True)

#                 combined_table_df = combined_table_df[['Site Id', 'MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']]
#                 print('combined_table_df,combined_table_df',combined_table_df)
#                 # Reorder columns
#                 # table_df = table_df1 and table_df2[[ 'Site Id','MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']]

#                 html_table = global_style +combined_table_df.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                 write_html_table("\n-----:5GNR RILINK:-----:\n"+html_table)

#                 print("9th log:\n", combined_table_df)
#                 secondLog=combined_table_df.to_string(index=False)
#                 write_data("\n-----:5GNR RILINK:-----:\n"+secondLog)
#             else:
#                 print("No matching table data found.")
#         else:
#             print("No extracted data found.")

# extract_data5(file_path)





# import pandas as pd
# import re

def extract_data5(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "MIE04225A> hget rilink RiLinkId|linkRate|operationalState|riPortRef1|riPortRef2"
        end_marker = "IE04225A> hget sfp prod"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data1 = content[start_index:end_index]

    file_path = "C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "NIE04225A2> hget rilink RiLinkId|linkRate|operationalState|riPortRef1|riPortRef2"
        end_marker = "NIE04225A2> hget sfp prod"

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data2 = content[start_index:end_index]
        # print('lllllll', extracted_data2)

    if extracted_data1:
        table_pattern1 = r"(.+?)\s+(\d+)\s+(\d\s+\(ENABLED\))\s+(.+?)\s+(.+?)\s+(.+)$"
        table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

        columns = [ 'MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']
        table_df1 = pd.DataFrame(table_matches1, columns=columns)
        table_df1[ 'operationalState'] = table_df1[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
        table_df1['Site Id'] = 'MIE04225A'
        table_df1 = table_df1[['Site Id','MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']]

    if extracted_data2:
        table_pattern2 = r"(.+?)\s+(\d+)\s+(\d\s+\(ENABLED\))\s+(.+?)\s+(.+?)\s+(.+)$"
        table_matches2 = re.findall(table_pattern2, extracted_data2, re.MULTILINE)

        if table_matches2:
            table_df2 = pd.DataFrame(table_matches2, columns=columns)  # Use the same columns as table_df1
            table_df2[ 'operationalState'] = table_df2[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
            # print('klllllllkklklk', table_df2)
            table_df2['Site Id'] = 'NIE04225A2'

            combined_table_df = pd.concat([table_df1, table_df2], ignore_index=True)

            html_table = combined_table_df.to_html(escape=False, index=False, table_id='styled_table',
                                                    classes='table table-striped table-bordered')

            write_html_table("\n-----:5GNR RILINK:-----:\n" + html_table)

            # print("9th log:\n", combined_table_df)
            secondLog = combined_table_df.to_string(index=False)
            write_data("\n-----:5GNR RILINK:-----:\n" + secondLog)
        else:
            print("No matching table data found.")
    else:
        print("No extracted data found.")

extract_data5(file_path)


##################################################################################################
##################################################################################################

def extract_data455(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = """MIE04225A> sdir"""
        end_marker = """MIE04225A> hget . allowedplmnlist"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]   
        # print( "lkkhh",extracted_data)

        if extracted_data:
            start_marker1 = """..........
+--------+                  +----------------+"""
            end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

MIE04225A>

MIE04225A> hget . allowedplmnlist"""
            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]
            # print( "lllllmmmmmnnnn\n",extracted_data1)

            if extracted_data1:
                start_marker21 = """=====================================================================================================================================
ID ;LINK ;RiL                ;WL1     ;TEMP1 ;TXbs1 ;TXdBm1 ;RXdBm1 ;BER1   ;WL2     ;TEMP2 ;TXbs2 ;TXdBm2 ;RXdBm2 ;BER2   ;DlLoss ;UlLoss ;LENGTH ;TT
====================================================================================================================================="""
                end_marker21 = """-------------------------------------------------------------------------------------------------------------------------------------

=====================================================================================================================================
ID ;RiL                ;BOARD          ;SFPLNH  ;PORT ;VENDOR       ;VENDORPROD       ;REV  ;SERIAL          ;DATE     ;ERICSSONPROD   ;WL      ;TEMP  ;TXbs  ;TXdBm  ;RXdBm  ; BER
====================================================================================================================================="""
                start_index21 = content.find(start_marker21)
                end_index21 = content.find(end_marker21)
                extracted_data21 = content[start_index21:end_index21]
                # print( "lllllmmmmmnnnn\n",extracted_data2)

                if extracted_data21:
                    table_pattern21="^(\d+)\s*;(\w+)\s*;([A-Za-z0-9-]+)\s*;([\d.]+)\s*;(\d+C)\s*;(\d+%)\s* ;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([\d.]+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([^;]+)\s*;\s*(\d+\.\d+)\s*;\s*(\d+m)\s*;\s*(\d+)"   ### ;\s*([A-Za-z0-9-]+)\s*;\s*;\s*([\d.]+)\s*;\s*([\d.%-]+)\s*;\s*([\d.-]+)\s*;\s*([\d.-]+)\s*;\s*(\d+)\s*;\s*([\d.]+)\s*;\s*([\d.]+)\s*;\s*([\d.%-]+)\s*;\s*([\d.-]+)\s*;\s*([\d.-]+)\s*;\s*(\d+)\s*;\s*(-?\d+(\.\d+)?)\s*;\s*(\d+m)\s*;\s*(\d+)$

                    table_matches21 = re.findall(table_pattern21, extracted_data21, re.MULTILINE)

                    # print(table_matches2)

                    if table_matches21:
                        global c1,c2,c3
                        columns = [ 'ID', 'LINK', 'RiL', 'WL1', 'TEMP1', 'TXbs1','TXdBm1','RXdBm1' ,'BER1','WL2','TEMP2','TXbs2','TXdBm2','RXdBm2','BER2','DlLoss','UlLoss','LENGTH','TT']   ## 
                        table_df21 = pd.DataFrame(table_matches21, columns=columns)
                        table_df21['Site Id'] = 'MIE04225A'
                        table_df21['Cell'] = (c1,c2,c3)
                        # table_df2['Cell'] = (c1,c2,c3,c1,c2,c3)
                        table_df21 = table_df21[['Site Id' ,'Cell','ID', 'LINK', 'RiL', 'WL1', 'TEMP1', 'TXbs1','TXdBm1','RXdBm1','BER1','WL2','TEMP2','TXbs2','TXdBm2','RXdBm2','BER2','DlLoss','UlLoss','LENGTH','TT']]

                        # table_df2 = pd.DataFrame(table_matches2, columns=columns)  # Use the same columns as table_df1
                        # print('klllllllkklklk', table_df2)
                        # table_df2['Site Id'] = 'NIE04225A2'
                        # print('klllllllkklklk\n', table_df2)

                        # html_table = f"-----:=====================:-----:\n{table_df2}"
                        # write_html_table(html_table)

                        # df = pd.DataFrame(extracted_data1)

                        html_table = global_style +table_df21.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')

            write_html_table(f"-----:_+_+_+_+_+_+_+_+_+_+:-----:\n{html_table}")

extract_data455(file_path)

#####################################################################################################################

def extract_data456(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = """MIE04225A> sdir"""
        end_marker = """MIE04225A> hget . allowedplmnlist"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]   
        # print( "lkkhh",extracted_data)

        if extracted_data:
            start_marker1 = """..........
+--------+                  +----------------+"""
            end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

MIE04225A>

MIE04225A> hget . allowedplmnlist"""
            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]
            # print( "lllllmmmmmnnnn\n",extracted_data1)

            if extracted_data1:
                start_marker2 = """=====================================================================================================================================
ID ;RiL                ;BOARD          ;SFPLNH  ;PORT ;VENDOR       ;VENDORPROD       ;REV  ;SERIAL          ;DATE     ;ERICSSONPROD   ;WL      ;TEMP  ;TXbs  ;TXdBm  ;RXdBm  ; BER
====================================================================================================================================="""
                end_marker2 = """-------------------------------------------------------------------------------------------------------------------------------------
TN ;                   ;BB6630         ;000100   ;  A ;FINISARCORP. ;FTLX1370W4BTL    ;A    ;N4LBJ59         ;20201122 ;NON-ERICSSON   ;NA      ;NA    ;NA    ;NA     ;NA     ;NZ/0
-------------------------------------------------------------------------------------------------------------------------------------"""
                start_index2 = content.find(start_marker2)
                end_index2 = content.find(end_marker2)
                extracted_data2 = content[start_index2:end_index2]
                # print( "lllllmmmmmnnnn\n",extracted_data2)

                if extracted_data2:
                    table_pattern2="^(\d+)\s*;([A-Za-z0-9-]+)\s*;(\S+)\s*;(\S+)\s*;\s*(\d+)\s*;(\S+)\s*;(\S+)\s*;(\w+)\s*;(\S+)\s*;(\d+)\s*;(\w+/\d+ R1A)\s*;(\d+\.\d+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*"   ###   ;(\w+)\s*;([\d.]+)\s*;(\d+C)\s*;(\d+%)\s* ;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([\d.]+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*;\s*([^;]+)\s*;\s*(\d+\.\d+)\s*;\s*(\d+m)\s*;\s*(\d+)

                    table_matches2 = re.findall(table_pattern2, extracted_data2, re.MULTILINE)

                    # print(table_matches2)

                    if table_matches2:
                        
                        global c1,c2,c3
                        columns = [ 'ID', 'RiL','BOARD','SFPLNH','PORT','VENDOR','VENDORPROD ','REV','SERIAL','DATE','ERICSSONPROD','WL','TEMP','TXbs','TXdBm','RXdBm',' BER']   ##  , 'LINK', 'RiL', 'WL1', 'TEMP1', 'TXbs1','TXdBm1','RXdBm1' ,'BER1','WL2','TEMP2','TXbs2','TXdBm2','RXdBm2','BER2','DlLoss','UlLoss','LENGTH','TT'
                        table_df2 = pd.DataFrame(table_matches2, columns=columns)
                        table_df2['Site Id'] = 'MIE04225A'
                        table_df2['Cell'] = (c1,c2,c3,c1,c2,c3)
                        table_df2 = table_df2[['Site Id','Cell','ID', 'RiL','BOARD','SFPLNH','PORT','VENDOR','VENDORPROD ','REV','SERIAL','DATE','ERICSSONPROD','WL','TEMP','TXbs','TXdBm','RXdBm',' BER']]
                        # extract_data11(file_path)  
                        
                        
                        # table_df2 = pd.DataFrame(table_matches2, columns=columns)  # Use the same columns as table_df1
                        # print('klllllllkklklk\n', table_df2)
                        # table_df2['Site Id'] = 'NIE04225A2'
                        # print('klllllllkklklk\n', table_df2)

                        # html_table = f"-----:=====================:-----:\n{table_df2}"
                        # write_html_table(html_table)

                        # df = pd.DataFrame(extracted_data1)

                        html_table = global_style +table_df2.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')

                        write_html_table(f"-----:_+_+_+_+_+_+_+_+_+_+_-_-_-----_-----:-----:\n{html_table}")
                      
extract_data456(file_path)

###################################################################################################################################

##################################################################################################
##################################################################################################
file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
def third_file1(file_path3):
    with open(file_path3, 'r') as file:
        content3 = file.read()
        # print("lllll12",content3)
        if content3:
            start_marker = """LVA61251A> hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
            end_marker = """LVA61251A> hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""

            start_index = content3.find(start_marker)
            end_index = content3.find(end_marker)
            extracted_data = content3[start_index:end_index]   
            # print( "lkkhh",extracted_data)

            if extracted_data:
                start_marker1 = """=================================================================================================================
MO                        administrativeState cellBarred     operationalState primaryPlmnReserved sectorCarrierRef     
================================================================================================================="""
                end_marker1 = """=================================================================================================================
Total: 6 MOs

Added 6 MOs to group: hget_group
..
=================================================================================================================
MO                    administrativeState cellBarred     operationalState sectorCarrierRef     
================================================================================================================="""
                start_index1 = content3.find(start_marker1)
                end_index1 = content3.find(end_marker1)
                extracted_data1 = content3[start_index1:end_index1]   
                # print( "lkkhh",extracted_data1)

                if extracted_data1:
                    # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    table_pattern1 = r"(EUtranCellFDD=\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\d+\s+\(NOT_BARRED\))\s+(\d+\s+\(ENABLED\))\s+(\w+)\s+(?:\[1\] = (SectorCarrier=\d+))"  #(SectorCarrier=\d+)\s+(\d+)+\s*(\d+\s+\(ENABLED\))+ \s*(?:\[\d+\] = (.+))$  # (^\[\d+\] = NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+)\s*
                    table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

                    columns = [ 'MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']   #,
                    table_df1 = pd.DataFrame(table_matches1, columns=columns)
                    table_df1[ 'administrativeState'] = table_df1['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    table_df1[ 'cellBarred'] = table_df1[ 'cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    table_df1[ 'operationalState'] = table_df1[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    # print(table_df1)
                    table_df1['Site Id'] = 'LVA61251A'
                    table_df1 = table_df1[['Site Id','MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']]

                    html_table = global_style +table_df1.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')

                    write_html_table(f"-----:LTE CELL STATUS-----:-----:\n{html_table}")
   

third_file1(file_path3)

##################################################################################################################



##################################################################################################
##################################################################################################
file_path2="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
def third_file2(file_path2):
    with open(file_path2, 'r') as file:
        content3 = file.read()
        # print("lllll12",content3)
        if content3:
            start_marker = """LVA61251A> hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
            end_marker = """LVA61251A> hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""

            start_index = content3.find(start_marker)
            end_index = content3.find(end_marker)
            extracted_data = content3[start_index:end_index]   
            # print( "lkkhh",extracted_data)

            if extracted_data:
                start_marker1 = """=================================================================================================================
MO                    administrativeState cellBarred     operationalState sectorCarrierRef     
================================================================================================================="""
                end_marker1 = """=================================================================================================================
Total: 3 MOs

Added 3 MOs to group: hget_group

LVA61251A> hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""
                start_index1 = content3.find(start_marker1)
                end_index1 = content3.find(end_marker1)
                extracted_data1 = content3[start_index1:end_index1]   
                # print( "lkkhh",extracted_data1)

                if extracted_data1:
                    # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    table_pattern1 = r"(NbIotCell=\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\d+\s+\(NOT_BARRED\))\s+(\d+\s+\(ENABLED\))\s+(?:\[1\] = (SectorCarrier=\d+))"  #
                    table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

                    columns = [ 'MO','administrativeState','cellBarred','operationalState','sectorCarrierRef']   #,
                    table_df11 = pd.DataFrame(table_matches1, columns=columns)
                    table_df11[ 'administrativeState'] = table_df11['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    table_df11['cellBarred'] = table_df11['cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    table_df11[ 'operationalState'] = table_df11[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    # print(table_df1)
                    table_df11['Site Id'] = 'LVA61251A'
                    table_df11 = table_df11[['Site Id','MO','administrativeState','cellBarred','operationalState','sectorCarrierRef']]
                    # print('table_df11',table_df11)

                    html_table = global_style +table_df11.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')

                    write_html_table(f"-----:IOT CELL STATUS-----:-----:\n{html_table}")
   

third_file2(file_path2)

####################################################################################################################
#############################################################################################################################



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

                        columns = ['CELL ','TYPE','BSPWRB','BSPWRT','MSTXPWR','SCTYPE']   #,
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

                    columns = ['CB ']   #,
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
                        'CELL ':a1,
                        'STATE':b1,
                        'BSPWRB':a,
                        'BSPWRT':b,
                        'MSTXPWR':c,
                        'CB':[a2,b2,c2]

                    }
                    table=pd.DataFrame(dta)
                    # print(table)

                    # table_df1['Site Id'] = 'MIE04225A'
                    # table_df1 = table_df1[['Site Id','MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']]
                    html_table = global_style +table.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')

                    write_html_table(f"-----:fourth file(CELL SYSTEM INFORMATION BCCH DATA)-----:-----:\n{html_table}")
   

fourth_file1(file_path4)




##########################################################################################################################################

def extract_data45(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = """MIE04225A> sdir"""
        end_marker = """MIE04225A> hget . allowedplmnlist"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]   
        # print( "lkkhh",extracted_data)

        if extracted_data:
            start_marker1 = """..........
+--------+                  +----------------+"""
            end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

MIE04225A>

MIE04225A> hget . allowedplmnlist"""
            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]
            # print( "lllllmmmmmnnnn\n",extracted_data1)


            html_table = f"-----:5GNR SDIR Status(MIE04225A> sdir):-----:\n{extracted_data1}"

            # Call the write_html_table function to save the HTML table
            write_html_table(html_table)

            # df = pd.DataFrame(extracted_data1)

            # html_table = global_style + df.to_html(escape=False, index=False,
                                                        # table_id='styled_table',
                                                        # classes='table table-striped table-bordered')

            # write_html_table(f"-----:5GNR SDIR Status:-----:\n{extracted_data1}")

extract_data45(file_path)

#         if extracted_data:
#             start_marker1=""" ..........
# +--------+                  +----------------+"""
#             end_marker1="""-------------------------------------------------------------------------------------------------------------------------------------

# MIE04225A>

# MIE04225A> hget . allowedplmnlist"""

#             start_index1 = content.find(start_marker1)
#             end_index1= content.find(end_marker1)
#             extracted_data1 = content[start_index1:end_index1]
#             print( "lkkhh",extracted_data1)
            

#             with open("final_data", 'w') as final_data:
#                 final_data.write(extracted_data1)



# extract_data45(file_path)

##########1st@@@@@@@@@@@@@
#         if extracted_data :
#             start_marker1 = """..........
# +--------+                  +----------------+"""
#             end_marker1 = """=====================================================================================================================================
# ID RiL                Type Res MO1-MO2           BOARD1-BOARD2         AlmIDs Cells (States)                                          Issue (Failed checks)
# ====================================================================================================================================="""

#             start_index1 = content.find(start_marker1)
#             end_index1 = content.find(end_marker1)
#             extracted_data1 = content[start_index1:end_index1]
#             # print("45th-first:\n",extracted_data1)
            
#             if extracted_data1:
#                 start_marker = re.escape(start_marker1)
#                 end_marker = re.escape(end_marker1)

#                 match = re.search(f"{start_marker}(.*?){end_marker}", content, re.DOTALL)
#                 if match:
#                     data_between_markers = match.group(1).strip()

#                     # Split the data into lines and create a list
#                     data_list = data_between_markers.split("\n")

#                     # Create a pandas DataFrame from the list
#                     df = pd.DataFrame(data_list, columns=["Data"])

#                     html_table = global_style + df.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                     write_html_table("\n-----:5GNR SDIR Status:-----:\n"+html_table)
                    
#                     # Display the DataFrame
#                     print("45th-first:::\n",df)
#                     fourtysevenLog=df.to_string(index=False)
#                     write_data("\n-----:5GNR SDIR Status:-----:\n"+fourtysevenLog)
#                 else:
#                     print("No match found between markers.")
#             else:
#                 print("Log not found in the content.")


#        ###############2nd #####     
#         if extracted_data :
#             start_marker2 = """=====================================================================================================================================
# ID RiL                Type Res MO1-MO2           BOARD1-BOARD2         AlmIDs Cells (States)                                          Issue (Failed checks)
# ====================================================================================================================================="""
#             end_marker2 = """-------------------------------------------------------------------------------------------------------------------------------------

# Node: RadioNode LN   CXP9024418/15_R74C54 (23.Q2)   LTE-FDD NR-LB-FDD-SA-NSA"""

#             start_index2 = content.find(start_marker2)
#             end_index2 = content.find(end_marker2)
#             extracted_data2 = content[start_index2:end_index2]
#             # print("kdjhj",extracted_data2)

#             if extracted_data2:
#                 table_pattern2 = r'^(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+\s+\S+)\s+(.+)$'
#                 # table_pattern2 = r'\s*(\d+)\s+([A-Z0-9-]+)\s+([A-Z0-9]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([\w\s=()]+)\s+(Passed)$'
#                 # table_pattern2 = r'\s*(\d+)\s+([A-Z0-9-]+)\s+([A-Z0-9]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([\w\s=()]+)\s+(Passed)$'

#                 # table_pattern2 = r"\s*(\d+)\s+([\w-]+)\s+([A-Z0-9]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s$"
#                 # table_pattern = r'(\d+)\s+(BB-\d+-[A-Z]-\d+-[A-Z]+\d+)\s+(\w+)\s+(\w+)\s+(\w+-\w+)\s+(\w+-\w+)\s+(\w+\s?\-\s?\w+)\s+(.+)$'
#                 # table_pattern = r'(\d+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+\-\w+)\s+(\w+\-\w+)\s+(\w+\s?\-\s?\w+)\s+(.+)'
#                 # table_pattern = r'^(\d+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+\s+\w+)\s+(\w+\s+\w+)\s+(\w+\s+\w+)\s+(.+)$'
#                 # table_pattern = r"\s*(\d+)\s+([\w-]+)\s+([A-Z0-9]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s"
                
#                 table_matches = re.findall(table_pattern2, extracted_data2, re.MULTILINE)

#                 if table_matches:
#                     columns = ['ID', 'RiL', 'Type', 'Res', 'MO1-MO2', 'BOARD1-BOARD2', 'AlmIDs', 'Cells (States)', 'Issue (Failed checks)']
#                     table_df = pd.DataFrame(table_matches, columns=columns)

#                     html_table = global_style + table_df.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                     write_html_table("\n"+html_table)
#                     print("45th-second:\n", table_df)
#                     fourtysevenLog=table_df.to_string(index=False)
#                     write_data("\n"+fourtysevenLog)
#                 else:
#                     print("No matching table data found.")  
#             else:
#                 print("No extracted data found.")

# ########$$$$$$@@@@@@@#########$$$$$$$$@@@@@@@@@

#         if extracted_data :
#             start_marker21 = """=====================================================================================================================================
# ID RiL                Type Res MO1-MO2           BOARD1-BOARD2         AlmIDs Cells (States)                                          Issue (Failed checks)
# =====================================================================================================================================
# 1 BB-01-A-6-01-Data2 O101 OK  BB-01(A) 6-01(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A11 FDD=EIE04225A11 NRC=KIE04225A11 (1,1,1) Passed
# 2 BB-01-B-6-02-Data2 O101 OK  BB-01(B) 6-02(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A21 FDD=EIE04225A21 NRC=KIE04225A21 (1,1,1) Passed
# 3 BB-01-C-6-03-Data2 O101 OK  BB-01(C) 6-03(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A31 FDD=EIE04225A31 NRC=KIE04225A31 (1,1,1) Passed
# -------------------------------------------------------------------------------------------------------------------------------------

# """
#             end_marker21 = """=====================================================================================================================================
# AntennaNearUnit                          ;ST  ;TYPE   ;PRODUCTNR  ;REV   ;UNIQUEID             ;RfPort
# ====================================================================================================================================="""

#             start_index21 = content.find(start_marker21)
#             end_index21 = content.find(end_marker21)
#             extracted_data21 = content[start_index21:end_index21]
#             print("kdjhj",extracted_data21)

#             if extracted_data21 :
#                 start_marker22 = """=====================================================================================================================================
# 1 BB-01-A-6-01-Data2 O101 OK  BB-01(A) 6-01(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A11 FDD=EIE04225A11 NRC=KIE04225A11 (1,1,1) Passed
# 2 BB-01-B-6-02-Data2 O101 OK  BB-01(B) 6-02(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A21 FDD=EIE04225A21 NRC=KIE04225A21 (1,1,1) Passed
# 3 BB-01-C-6-03-Data2 O101 OK  BB-01(C) 6-03(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A31 FDD=EIE04225A31 NRC=KIE04225A31 (1,1,1) Passed
# -------------------------------------------------------------------------------------------------------------------------------------
# """
#                 end_marker22 = """=====================================================================================================================================
# FRU   ;LNH    ;BOARD          ;ST ;FAULT ;OPER ;MAINT ;STAT ;PRODUCTNUMBER   ;REV     ;SERIAL        ;DATE     ;PMTEMP ; TEMP ; UPT ;SW                  ;
# ====================================================================================================================================="""

#                 start_index22 = content.find(start_marker22)
#                 end_index22 = content.find(end_marker22)
#                 extracted_data22 = content[start_index22:end_index22]
#                 print("khjjjjj",extracted_data22)



#                 if extracted_data22:
#                     table_pattern22= r'Node:\s+(.*?)\s+(\S+)\s+\((.*?)\)\s+(\S+)\s+(\S+)'
#                     # table_pattern21=r'Node:\s+(.*?)\s+(\S+)\s+\((.*?)\)\s+(\S+)\s+(\S+)'
#                     # table_pattern21= r'Node:\s+(.*?)\s+(\S+)\s+\((.*?)\)\s+(\S+)\s+(\S+)'
#                     # table_pattern2 = r'\s*(\d+)\s+([A-Z0-9-]+)\s+([A-Z0-9]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([\w\s=()]+)\s+(Passed)$'
#                     # table_pattern2 = r'\s*(\d+)\s+([A-Z0-9-]+)\s+([A-Z0-9]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([A-Z0-9-]+)\s+([\w\s=()]+)\s+(Passed)$'

#                     # table_pattern2 = r"\s*(\d+)\s+([\w-]+)\s+([A-Z0-9]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s$"
#                     # table_pattern = r'(\d+)\s+(BB-\d+-[A-Z]-\d+-[A-Z]+\d+)\s+(\w+)\s+(\w+)\s+(\w+-\w+)\s+(\w+-\w+)\s+(\w+\s?\-\s?\w+)\s+(.+)$'
#                     # table_pattern = r'(\d+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+\-\w+)\s+(\w+\-\w+)\s+(\w+\s?\-\s?\w+)\s+(.+)'
#                     # table_pattern = r'^(\d+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+\s+\w+)\s+(\w+\s+\w+)\s+(\w+\s+\w+)\s+(.+)$'
#                     # table_pattern = r"\s*(\d+)\s+([\w-]+)\s+([A-Z0-9]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s"
                    
#                     table_matches22 = re.findall(table_pattern22, extracted_data22,re.MULTILINE)  ###, re.MULTILINE

#                     if table_matches22:
#                         columns = ['node_name', 'node_id', 'version', 'network_type', 'mode']
#                         table_df22 = pd.DataFrame(table_matches22, columns=columns)
#                         html_table = global_style + table_df22.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                         write_html_table("\n"+html_table)
#                         print("45th-after second:\n", table_df22)
#                         fourtysevenLog=table_df22.to_string(index=False)
#                         write_data("\n"+fourtysevenLog)
#                     else:
#                         print("No matching table data found.")    
#                 else:
#                     print("No extracted data found.")






# ######################## 3rd  $$$$$$$$$$$$$$$$$$$$$$$abhi nahi hua###################

#         if extracted_data :
#             print("oi")
#             start_marker3= """=====================================================================================================================================
# FRU   ;LNH    ;BOARD          ;ST ;FAULT ;OPER ;MAINT ;STAT ;PRODUCTNUMBER   ;REV     ;SERIAL        ;DATE     ;PMTEMP ; TEMP ; UPT ;SW                  ;
# ====================================================================================================================================="""
#             end_marker3 = """=====================================================================================================================================
# AntennaNearUnit                          ;ST  ;TYPE   ;PRODUCTNR  ;REV   ;UNIQUEID             ;RfPort
# ====================================================================================================================================="""

#             start_index3 = extracted_data.find(start_marker3)
#             end_index3 = extracted_data.find(end_marker3)
#             extracted_data3 = extracted_data[start_index3:end_index3]
#             # print("kdjhj",extracted_data3)

#             if extracted_data3:
#                 # table_pattern3=r"^\s*(\S+)\s+;(\S+)\s+;(\S+)\s+;(\S+)\s+;(\S+)\s+;(\S+)\s+;(\S+)\s+;(\S+)\s+;(\S+/\d+)\s+;(\S+)\s+;(\S+)\s+;(\d+)\s+;(\S+)\s+;(\S+)\s+;(\S+)\s+;(\S+)\s+;(\S+)\s+\(([^)]+)\)"

#                 table_pattern3=r"^\s*(\S+)\s+;(\S+)\s+;(\S+)\s+;(.*?);\s*([\w\s]+)\s*;\s*([\w\s]+)\s*;\s*([\w\s]+)\s*;\s*([\w/w]+)\s*;\s*([\w/d]+)\s*;\s*([\w\s]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;(.*)$"#\s*([^;]+)\s*;    ;(.*)$    #\s*([\w\d\s%_]+)?\s*;      \s*\(([^)]+)\)
#                 # table_pattern3=r"^(\S+)\s+(\S+)\s" #+(\S+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+/\d+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s*(.*)$

#                 # table_pattern3=r"^([\W-]+)\s*;\s*([\w\s_]+)\s*;\s*([\w\s]+)\s*;\s*(\d+)\s*;\s*([\w\s]+)\s*;\s*([\w\s]+)\s*;\s*([\w\s]+)\s*;\s*([\w\s]+)\s*;\s*([\w\d\/]+)\s*;\s*([\w\d]+)\s*;\s*([\w\d]+)\s*;\s*(\d+)\s*;\s*(\d+(\.\d+)?)\s*;\s*(\d+(\.\d+)?)\s*;\s*(\d+(\.\d+)?)\s*;\s*([\w\d\s%_]+)?\s*;$"

#                 # table_pattern3=r"^(\S)\s+(\d)\s+(\S)\s+(\d)\s+(\W)\s+(\W)\s+(\W)\s+(\W)\s+(\S/d)\s+(\S)\s+(\S)\s+(\d)\s+(\S)\s+(\S)\s"
#                 # table_pattern3= r'^([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*(\d+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*(.*?)\s*;$'
#                 # table_pattern3= r'^([^;]+);([^;]+);([^;]+);(\d+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);$'
#                 # table_pattern3 =r"^(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);$"

#                 # table_pattern3 = r'^([^;]+);([^;]+);([^;]+);(\d+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);$'
#                 # table_pattern3 = r'^([\w\s-]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;(\d+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s/-]+)\s*;([\w\s/-]+)\s*;([\w\s/-]+)\s*;(\d+)\s*;([\w\s.()]+)\s*;([\w\s.()]+)\s*;([\w\s.()]+)\s*;([\w\s.()]+)\s*;(.*)\s*;$'

#                 # table_pattern3= r'^([\w\s-]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;(\d+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s/-]+)\s*;([\w\s/-]+)\s*;([\w\s/-]+)\s*;(\d+)\s*;([\w\s.()]+)\s*;([\w\s.()]+)\s*;([\w\s.()]+)\s*;([\w\s.()]+)\s*;(.*)\s*;$'
#                 # table_pattern3 = r'^=+\s*(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+\.\.\.\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+\.\.\.\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s*$'


#                 # table_pattern3 = r'^([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;$'

#                 # table_pattern3 = r'^([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;$'
#                 # table_pattern3 = r'^([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;$'

                
#                 table_matches3 = re.findall(table_pattern3, extracted_data3,re.MULTILINE)#, re.MULTILINE

#                 if table_matches3:
                                                              
#                     table_df3 = pd.DataFrame(table_matches3)
#                     html_table_unstyled = global_style + table_df3.to_html(escape=False, index=False, header=False,
#                                                           table_id='styled_table',
#                                                           classes='table table-striped table-bordered')
    
#     # Define a CSS class to style the first row (you can customize the style)
#                     first_row_style = 'background-color: blue; color: white;'
                    
#                     # Apply the styling to the entire HTML table
#                     # Replace the first row with the styled first row
#                     html_table_styled = html_table_unstyled.replace('<tr>', f'<tr style="{first_row_style}">', 1)


#                     # columns = ['FRU', ';LNH', ';BOARD', ';ST', ';FAULT', ';OPER', ';MAINT', ';STAT', ';PRODUCTNUMBER', ';REV', ';SERIAL', ';DATE', ';PMTEMP', '; TEMP', '; UPT', ';SW' ,';']

#                     # columns = ['FRU', 'LNH', 'BOARD', 'ST', 'FAULT', 'OPER', 'MAINT', 'STAT', 'PRODUCTNUMBER', 'REV', 'SERIAL', 'DATE', 'PMTEMP', 'TEMP', 'UPT', 'SW',';']
#                     # columns = ['FRU', 'LNH']
#                     # columns = ['ID', 'RiL', 'Type', 'Res', 'MO1-MO2', 'BOARD1-BOARD2', 'AlmIDs', 'Cells (States)', 'Issue (Failed checks)']
                
#                     # table_df3 = pd.DataFrame(table_matches3)#   ,columns=columns
#                     # html_table = global_style + table_df3.to_html(escape=False, index=False,
#                                                             #   table_id='styled_table',
#                                                             #   classes='table table-striped table-bordered')

#                     write_html_table("\n"+html_table_styled)
#                     # print("45th-third:\n", table_df3)
#                     # secondLog=table_df3.to_string(index=False,header=False)
#                     # write_data("\n"+secondLog)
#                 else:
#                     print("No matching table data found.")  
#             else:
#                 print("No extracted data found.")






            



# #################### 4th $$$$$$$$$$$$$$$$$$$abhi nahi hua#####################################

#         if extracted_data :
#             print("oi")
#             start_marker4= """=====================================================================================================================================
# XPBOARD   ;ST ;FAULT ;OPER ;PRODUCTNUMBER ;REV ;SERIAL/NAME ;DATE     ; TEMP ;MO
# ====================================================================================================================================="""
#             end_marker4 = """=====================================================================================================================================
# ID ;T ;RiL                ;BPBP ;BOARD1         ;LNH1 ;PORT ;R ;LINK ;RATE  ; BER ;BOARD2         ;LNH2 ;PORT ;R ;LINK ;RATE  ; BER ;LENGTH ;MO1 - MO2
# ====================================================================================================================================="""

#             start_index4 = extracted_data.find(start_marker4)
#             end_index4 = extracted_data.find(end_marker4)
#             extracted_data4 = extracted_data[start_index4:end_index4].strip()
#             # print("kdjhj",extracted_data4)

#             if extracted_data4:
#                 # table_pattern4 = r"^(?!=+)(?<=\s)(\S+)\s*+(\S+)\s*+(\S+)\s*+(\S+)\s*+(\S+)\s*+(\S+)\s*+(\S+)\s*+(\S+)\s*+(\S+)\s*+(\S+)\s*+(\S+)$"

#                 # table_pattern4 = r'^([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;$'


#                 table_pattern4 = r"^(?!=+)(?<=\s)(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)"



#                 # table_pattern4 =  r"^([^;]+);\s*(\d*)\s*;\s*([^;]*)\s*;\s*([^;]*)\s*;\s*([^;]*)\s*;\s*([^;]*)\s*;\s*([^;]*)\s*;\s*([^;]*)\s*;\s*([^;]*)\s*;\s*(.*)$"

#                 # table_pattern4 =  r'^(\S+)\s*;([^;]+)\s*;([^;]+)'  #;([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);(.*)$


#                 # table_pattern4 = r"^([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;\s*([^;]+)\s*"


#                 # table_pattern4 = r'^(\w+)\s* '#;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;$'

#                 # table_pattern4 = r'^([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;$'


#                 # table_pattern4 = r'^([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;$'


#                 # table_pattern4 = r'^([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;$'

#                 # table_pattern4 = r'^([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;$'
#                 # table_pattern4 = r'^(\S+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)$'

#                 # table_pattern4 = r'^([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)$'
#                 # table_pattern4 = r'([\w\s]+)\s*;([\w\s]*)\s*'
#                 # table_pattern4 = r'([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*)$'
#                 # table_pattern4 = r'([\w\s]+)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;$'
#                 # table_pattern4 = r'^([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;$'
#                 # table_pattern4 = r"\s*(\d+)\s+([\w-]+)\s+([A-Z0-9]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s"
#                 # table_matches4 = re.split(table_pattern4, extracted_data4.strip())

#                 table_matches4 = re.findall(table_pattern4, extracted_data4, re.MULTILINE)#, re.MULTILINE

#                 if table_matches4:

#                     # columns=['XPBOARD', 'ST', 'FAULT']
#                     # columns = ['XPBOARD', 'ST', 'FAULT', 'OPER', 'PRODUCTNUMBER', 'REV', 'SERIAL/NAME', 'DATE', 'TEMP', 'MO'] # 'ST', 'FAULT', 'OPER', 'PRODUCTNUMBER', 'REV', 'SERIAL/NAME', 'DATE', 'TEMP', 'MO'
#                     # columns = ['FRU', ';LNH', ';BOARD', ';ST', ';FAULT', ';OPER', ';MAINT', ';STAT', ';PRODUCTNUMBER', ';REV', ';SERIAL', ';DATE', ';PMTEMP', '; TEMP', '; UPT', ';SW' ,';']

#                     # columns = ['XPBOARD','ST','FAULT','OPER','PRODUCTNUMBER','REV ','SERIAL/NAME','DATE','TEMP','MO']
#                     # columns = ['ID', 'RiL', 'Type', 'Res', 'MO1-MO2', 'BOARD1-BOARD2', 'AlmIDs', 'Cells (States)', 'Issue (Failed checks)']
#                     table_df4 = pd.DataFrame(table_matches4) 
#                     html_table_unstyled = global_style + table_df4.to_html(escape=False, index=False, header=False,
#                                                           table_id='styled_table',
#                                                           classes='table table-striped table-bordered')
    
#     # Define a CSS class to style the first row (you can customize the style)
#                     first_row_style = 'background-color: blue; color: white;'
                    
#                     # Apply the styling to the entire HTML table
#                     # Replace the first row with the styled first row
#                     html_table_styled = html_table_unstyled.replace('<tr>', f'<tr style="{first_row_style}">', 1)
                
#                     # table_df4 = pd.DataFrame(table_matches4) 

#                     # # html_table = global_style + table_df4.to_html(escape=False, index=False,header=False,
#                     #                                           table_id='styled_table',
#                     #                                           classes='table table-striped table-bordered')

#                     write_html_table("\n"+html_table_styled)
#                     print("45th-fourth:\n", table_df4)
#                     secondLog=table_df4.to_string(index=False,header=False)
#                     write_data("\n"+secondLog)
#                 else:
#                     print("No matching table data found.")  
#             else:
#                 print("No extracted data found.")








# ####################5th $$$$$$$$$$$$$$$$$$$$$$$$$$abhi nahi hua ################

#         if extracted_data :
#             print("oi")
#             start_marker5= """=====================================================================================================================================
# ID ;T ;RiL                ;BPBP ;BOARD1         ;LNH1 ;PORT ;R ;LINK ;RATE  ; BER ;BOARD2         ;LNH2 ;PORT ;R ;LINK ;RATE  ; BER ;LENGTH ;MO1 - MO2
# ====================================================================================================================================="""
#             end_marker5 = """=====================================================================================================================================
# ID ;LINK ;RiL                ;VENDOR1      ;VENDORPROD1      ;REV1 ;SERIAL1         ;DATE1    ;ERICSSONPROD1  ;VENDOR2      ;VENDORPROD2      ;REV2 ;SERIAL2         ;DATE2    ;ERICSSONPROD2  ;TT ;WL1     ;WL2
# ====================================================================================================================================="""

#             start_index5 = content.find(start_marker5)
#             end_index5 = content.find(end_marker5)
#             extracted_data5 = content[start_index5:end_index5].strip()
#             # print("kdjhj",extracted_data5)

#             if extracted_data5:
                
#                 # table_pattern5=r"^(\d+)\s*;([^;]+);(\S+)\s*;(\d+)\s*;(\S+)\s*;(\d+)\s*;([^;]+);(\w)\s*;(\w+)\s*;(\d+\.\d+[A-Z])\s*;([^;]+)\s*;(\S+)\s*;([^;]+)\s*;([^;]+)\s*;(\w+)\s*;(\w+)\s*;(\d+\.\d+[A-Z])\s*;([^;]+)\s*;([^;]+)\s*;\(([^)]+)\)$"

#                 table_pattern5=r"^(\d+)\s*;([^;]+);(\S+)\s*;(\d+)\s*;(\S+)\s*;(\d+)\s*;([^;]+);(\w)\s*;(\w+)\s*;(\d+\.\d+[A-Z])\s*;([^;]+)\s*;(\S+)\s*;([^;]+)\s*;([^;]+)\s*;(\w+)\s*;(\w+)\s*;(\d+\.\d+[A-Z])\s*;([^;]+)\s*;([^;]+)\s*;(.*)$"  #(Fru=[A-Za-z0-9-]+\([^)]*\))\s*
#                 # table_pattern3=r"^\s*(\S+)\s+;(\S+)\s+;(\S+)\s+;(.*?);\s*([\w\s]+)\s*;\s*([\w\s]+)\s*;\s*([\w\s]+)\s*;\s*([\w/w]+)\s*;\s*([\w/d]+)\s*;\s*([\w\s]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;(.*)$"
#                 # table_pattern5 = r'^(\d+)\s*;(\w+)\s*;([^;]+)\s*;(\d+\.\d+)\s*;([^\s]+)\s*;(\d+%)\s*;([-\d.]+)\s*;([-\d.]+)\s*;(\d+)\s*;(\d+\.\d+)\s*;([^\s]+)\s*;(\d+%)\s*;([-\d.]+)\s*;([-\d.]+)\s*;(\d+)\s*;(\d+\.\d+)\s*;([-\d.]+)\s*;([-\d.]+)\s*;(\d+m)\s*;(\d+)'
#                 # table_pattern5 = r'^(\d+)\s*;(\w+)\s*;([^;]+)\s*;(\w+)\s*;([^;]+)\s*;(\w+)\s*;(\d+)\s*;(\w)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;(\w+)\s*;(\w+)\s*;(\d+)\s*;(\w+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)$'
#                 # table_pattern5 = r'^([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+)(.+)$'
#                 # table_pattern5= r'^(\d+)\s*,(\d+)\s*;(\w)\s*;(\d+)\s*;(\w+)\s*;(\d+)\s*;(\d+)\s*;(\w+)\s*;(\w+)\s*;([^;]+)\s*;(\d+)\s*;(\w+)\s*;(\w+)\s*;(\d+)\s*;(\w+)\s*;(\w+)\s*;([^;]+)\s*;(\d+)\s*;([\d\s]+)\s*;([^;]+)$'
#                 # table_pattern5 = r'^(\d+)\s*;(\w+)\s*;([^;]+)\s*;(\w+)\s*;([^;]+)\s*;(\w+)\s*;(\w+)\s*;(\w+)\s*;(\w+)\s*;([^;]+)\s*;(\w+)\s*;(\w+)\s*;(\w+)\s*;(\w+)\s*;(\w+)\s*;(\w+)\s*;([^;]+)\s*;(\w+)\s*;(\w+)\s*;([^;]+)$'

#                 # table_pattern5 = r'^(\d+)\s*;(\d+)\s*;(\w+)\s*;(\d+)\s*;(\w+)\s*;(\d+)\s*;(\d+)\s*;(\w+)\s*;(\w+)\s*;(\w+)\s*;(\d+)\s*;(\w+)\s*;(\w+)\s*;(\d+)\s*;(\w+)\s*;(\w+)\s*;(\w+)\s*;([^;]+)\s*;(\d+)\s*;(\w+)\s*;([^;]+)$'

#                 # table_pattern5 = r'^(\d+)\s*;(\w+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;(\w+)\s*;(\d+)\s*;(\w+)\s*;(\w+)\s*;([^;]+)\s*;(\w+)\s*;(\w+)\s*;(\d+)\s*;(\w+)\s*;(\d+)\s*;(\w+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)$'

#                 # table_pattern5 = r'^(\d+)\s*;(\w+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;(\d+)\s*;(\d+)\s*;(\w)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;(\d+)\s*;(\d+)\s*;(\w)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)$'
#                 # table_pattern4 = r'^(\d+)\s*;(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;$'
#                 # table_pattern4 = r'^(\d+)\s*;(\w+)\s*;([\w\s-]+)\s*;(\d+)\s*;([\w\s-]+)\s*;([\w\s\d-]+)\s*;(\d+)\s*;(\w)\s*;([\w\s]+)\s*;([\d.G]+)\s*;([\d\s]+)\s*;([\w\s-]+)\s*;([\w\s-]+)\s*;(\d+)\s*;(\w)\s*;([\w\s]+)\s*;([\d.G]+)\s*;([\d\s]+)\s*;([\w\s\d]+)\s*;$'
#                 # table_pattern4 = r"(\d+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*"
#                 # table_pattern4 = r'([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*);([\w\s]*)$'
#                 # table_pattern4 = r'([\w\s]+)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;([\w\s]*)\s*;$'
#                 # table_pattern4 = r'^([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;([\w\s]+)\s*;$'
#                 # table_pattern4 = r"\s*(\d+)\s+([\w-]+)\s+([A-Z0-9]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s"
                
#                 table_matches5 = re.findall(table_pattern5, extracted_data5,re.MULTILINE)#, re.MULTILINE

#                 if table_matches5:
#                     columns = ['ID', 'T', 'RiL', 'BPBP', 'BOARD1', 'LNH1', 'PORT', 'R', 'LINK', 'RATE', 'BER', 'BOARD2', 'LNH2', 'PORT', 'R', 'LINK', 'RATE', 'BER', 'LENGTH', 'MO1 - MO2']  # , 'LENGTH'
                
#                     table_df5 = pd.DataFrame(table_matches5, columns=columns)

#                     html_table = global_style + table_df5.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                     write_html_table("\n"+html_table)
#                     print("45th-5th ::\n", table_df5)
#                     secondLog=table_df5.to_string(index=False)
#                     write_data("\n"+secondLog)
#                 else:
#                     print("No matching table data found.")  
#             else:
#                 print("No extracted data found.")



# ################ 6th ###################################

#         if extracted_data :
#             print("oi")
#             start_marker5= """=====================================================================================================================================
# ID ;LINK ;RiL                ;VENDOR1      ;VENDORPROD1      ;REV1 ;SERIAL1         ;DATE1    ;ERICSSONPROD1  ;VENDOR2      ;VENDORPROD2      ;REV2 ;SERIAL2         ;DATE2    ;ERICSSONPROD2  ;TT ;WL1     ;WL2
# ====================================================================================================================================="""
#             end_marker5= """=====================================================================================================================================
# ID ;LINK ;RiL                ;WL1     ;TEMP1 ;TXbs1 ;TXdBm1 ;RXdBm1 ;BER1   ;WL2     ;TEMP2 ;TXbs2 ;TXdBm2 ;RXdBm2 ;BER2   ;DlLoss ;UlLoss ;LENGTH ;TT
# ====================================================================================================================================="""

#             start_index5 = content.find(start_marker5)
#             end_index5 = content.find(end_marker5)
#             extracted_data5= content[start_index5:end_index5].strip()
#             # print("kdjhj",extracted_data5)

#             if extracted_data5:
#                 # table_pattern5 = r"^(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(?!.*\n-------------------------------------).*$"
# # ^(?!Total:)\s*
#                 table_pattern5 = r'^(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]\S*)$'
#                 # table_pattern5 = r'(\d+)\s*;\s*(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+\.\d+[KM]?)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;(\d+\.\d+[KM]?)\s*;(\d+\.\d+[KM]?)$'
#                 # table_pattern5 = r'^(\d+)\s*;(\w+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;$'
#                 # table_pattern5= r'^(\d+)\s*;(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;$'
                
#                 table_matches4 = re.findall(table_pattern5, extracted_data5,re.MULTILINE)#, re.MULTILINE

#                 if table_matches4:
#                     columns = [
#                 'ID', 'LINK', 'RiL', 'VENDOR1', 'VENDORPROD1', 'REV1', 'SERIAL1', 'DATE1', 'ERICSSONPROD1',
#                 'VENDOR2', 'VENDORPROD2', 'REV2', 'SERIAL2', 'DATE2', 'ERICSSONPROD2', 'TT', 'WL1', 'WL2'
#             ]
#                     # columns = ['ID', 'T', 'RiL', 'BPBP', 'BOARD1', 'LNH1', 'PORT', 'R', 'LINK', 'RATE', 'BER', 'BOARD2', 'LNH2', 'PORT', 'R', 'LINK', 'RATE', 'BER', 'LENGTH', 'MO1 - MO2']
                
#                     table_df4 = pd.DataFrame(table_matches4, columns=columns)#### 
#                     html_table = global_style + table_df4.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                     write_html_table("\n"+html_table)   
#                     print("45th-6th:\n", table_df4)
#                     fourtysevenLog=table_df4.to_string(index=False)
#                     write_data("\n"+fourtysevenLog)
#                 else:
#                     print("No matching table data found.")  
#             else:
#                 print("No extracted data found.")

# ###################7th########################################################

#         if extracted_data :
#             print("oi")
#             start_marker5= """=====================================================================================================================================
# ID ;LINK ;RiL                ;WL1     ;TEMP1 ;TXbs1 ;TXdBm1 ;RXdBm1 ;BER1   ;WL2     ;TEMP2 ;TXbs2 ;TXdBm2 ;RXdBm2 ;BER2   ;DlLoss ;UlLoss ;LENGTH ;TT
# ====================================================================================================================================="""
#             end_marker5= """=====================================================================================================================================
# ID ;RiL                ;BOARD          ;SFPLNH  ;PORT ;VENDOR       ;VENDORPROD       ;REV  ;SERIAL          ;DATE     ;ERICSSONPROD   ;WL      ;TEMP  ;TXbs  ;TXdBm  ;RXdBm  ; BER
# ====================================================================================================================================="""

#             start_index5 = content.find(start_marker5)
#             end_index5 = content.find(end_marker5)
#             extracted_data5= content[start_index5:end_index5]
# #           print("nnn",extracted_data5)
#             # extracted_data5 = extracted_data5.replace("0\n------------------------------------------..", "")

#             if extracted_data5:
#                 # table_pattern5 = r"^(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(0)\s*$"


#                 # table_pattern5 = r"^(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s"

#                 # table_pattern5 = r'^(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;];)'

#                 # table_pattern5 = r'^(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)$'
#                 # table_pattern5 = r'^(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)$'
#                 # table_pattern5 = r'^(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)$'     ([^;]\S*)$

#                 table_pattern5 = r'^(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]*0)\s*'

#                 # table_pattern5 = r'^(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)'
#                 # table_pattern5 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)'
#                 # table_pattern5 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)'
#                 # table_pattern5 = r'(\d+)\s*;\s*(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+\.\d+[KM]?)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;(\d+\.\d+[KM]?)\s*;(\d+\.\d+[KM]?)$'
#                 # table_pattern5 = r'^(\d+)\s*;(\w+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;$'
#                 # table_pattern5= r'^(\d+)\s*;(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;$'
                
#                 # table_matches4 = re.findall(table_pattern5, extracted_data5, re.MULTILINE)#, re.MULTILINE
#                 # table_matches= [match for match in table_matches if match[-1] != "0\n------------------------------------------.."]
#                 table_matches4 = re.findall(table_pattern5, extracted_data5, re.MULTILINE)#, re.MULTILINE

#                 if table_matches4:
#                     column = [
#                     'ID', 'LINK', 'RiL', 'WL1', 'TEMP1', 'TXbs1', 'TXdBm1', 'RXdBm1', 'BER1', 'WL2', 'TEMP2', 'TXbs2','TXdBm2', 'RXdBm2', 'BER2', 'DlLoss', 'UlLoss', 'LENGTH', 'TT']
#                 #     columns = [
#                 # 'ID', 'LINK', 'RiL', 'VENDOR1', 'VENDORPROD1', 'REV1', 'SERIAL1', 'DATE1', 'ERICSSONPROD1',
#                 # 'VENDOR2', 'VENDORPROD2', 'REV2', 'SERIAL2', 'DATE2', 'ERICSSONPROD2', 'TT', 'WL1', 'WL2']
#                     # columns = ['ID', 'T', 'RiL', 'BPBP', 'BOARD1', 'LNH1', 'PORT', 'R', 'LINK', 'RATE', 'BER', 'BOARD2', 'LNH2', 'PORT', 'R', 'LINK', 'RATE', 'BER', 'LENGTH', 'MO1 - MO2']
                
#                     table_df4 = pd.DataFrame(table_matches4, columns=column)
#                     html_table = global_style + table_df4.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                     write_html_table("\n"+html_table)
#                     print("45th-7th:\n", table_df4)
#                     fourtysevenLog=table_df4.to_string(index=False)
#                     write_data("\n"+fourtysevenLog)
#                 else:
#                     print("No matching table data found.")  
#             else:
#                 print("No extracted data found.")


# #################################### 8th ########################################

#             if extracted_data :
#                 print("oi")
#                 start_marker8= """=====================================================================================================================================
# ID ;RiL                ;BOARD          ;SFPLNH  ;PORT ;VENDOR       ;VENDORPROD       ;REV  ;SERIAL          ;DATE     ;ERICSSONPROD   ;WL      ;TEMP  ;TXbs  ;TXdBm  ;RXdBm  ; BER
# ====================================================================================================================================="""
#                 end_marker8= """-------------------------------------------------------------------------------------------------------------------------------------
# TN ;                   ;BB6630         ;000100   ;  A ;FINISARCORP. ;FTLX1370W4BTL    ;A    ;N4LBJ59         ;20201122 ;NON-ERICSSON   ;NA      ;NA    ;NA    ;NA     ;NA     ;NZ/0
# -------------------------------------------------------------------------------------------------------------------------------------"""

#                 start_index8 = content.find(start_marker8)
#                 end_index8 = content.find(end_marker8)
#                 extracted_data8= content[start_index8:end_index8]
#                 # print("nnn",extracted_data8)

#                 if extracted_data8:
#                     # table_pattern8 = r"(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*"
#                     # table_pattern8 = r"(\d+)\s;([^;]+)\s;([^;]+)\s;([^;]+)\s;(\d+)\s;([^;]+)\s;([^;]+)\s;(\w)\s;([^;]+)\s;(\d+)\s;([^;]+)\s;([^;]+)\s;([^;]+)\s;([^;]+)\s;([^;]+)\s;([^;]+)\s;([^;]+)\s;([^;]+)\s*$"


#                     # table_pattern8 = r"^(?![=]+\s*$)(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*$"
#                     # table_pattern8= r"^(?!0  ==============================================..|1  ==============================================)(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*$"
                    


#                     table_pattern8= r"^(\d+)\s*+(\S+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\w)\s*;([^;]+)\s*;(\d+)\s*;([A-Z\d/]+\s+[A-Z\d]+)\s*;(\d+\.\d+)\s*;(\d+[A-Z]+)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;([^;]*0)\s*"

#                     # table_pattern8= r'\s*(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;\s*'
#                     # table_pattern8= r'^(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;$'
#                     # table_pattern8 = r'\s*(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;\s*'
#                     # Define the regular expression pattern
#                     # table_pattern8 = r'(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;'

#                     # table_pattern8 = r'(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)'
#                     # table_pattern8 = r'\s*(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;\s*'
#                     # table_pattern8= r'\s*(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;\s*'
#                     # table_pattern8= r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([\d.]+ [KM]?)\s*;([^\n]+)\s*;(\d+[A-Z]?)\s*;([\d.%-]+)\s*;([-+]?\d*\.\d+)\s*;([-+]?\d*\.\d+)\s*;(\d+)'

#                     # table_pattern8 = r'^([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+)(.+)$'

#                     # table_pattern8= r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([\d.]+ [KM]?)\s*;([^\n]+)\s*;(\d+[A-Z]?)\s*;([\d.%-]+)\s*;([-+]?\d*\.\d+)\s*;([-+]?\d*\.\d+)\s*;(\d+)'
#                     # table_pattern8 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([\d.]+ [KM]?)\s*;([^\n]+)\s*;(\d+[A-Z]?)\s*;([\d.%-]+)\s*;([-+]?\d*\.\d+)\s*;([-+]?\d*\.\d+)\s*;(\d+)'
#                     # table_pattern8 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;(\d+\.\d+[KM]?)\s*;([^\n]+)\s*;(\d+[A-Z]?)\s*;(\d+%?)\s*;([-+]?\d*\.\d+)\s*;([-+]?\d*\.\d+)\s*;(\d+)'
#                     # table_pattern5 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)'
#                     # table_pattern5 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)'
#                     # table_pattern5 = r'(\d+)\s*;\s*(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+\.\d+[KM]?)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;(\d+\.\d+[KM]?)\s*;(\d+\.\d+[KM]?)$'
#                     # table_pattern5 = r'^(\d+)\s*;(\w+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;$'
#                     # table_pattern5= r'^(\d+)\s*;(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;$'
                    
#                     table_matches8 = re.findall(table_pattern8, extracted_data8, re.MULTILINE)#, re.MULTILINE

#                     if table_matches8:
#                         columns = ['ID', 'RiL', 'BOARD', 'SFPLNH', 'PORT', 'VENDOR', 'VENDORPROD', 'REV', 'SERIAL', 'DATE', 'ERICSSONPROD' , 'WL','TEMP', 'TXbs', 'TXdBm', 'RXdBm', 'BER']  #, 'RXdBm'
                    
#                         table_df8 = pd.DataFrame(table_matches8,columns =columns )
#                         html_table = global_style + table_df8.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                         write_html_table("\n"+html_table)
#                         print("45th-8th:\n", table_df8)
#                         fourtysevenLog=table_df8.to_string(index=False)
#                         write_data("\n"+fourtysevenLog)
#                     else:
#                         print("No matching table data found.")  
#                 else:
#                     print("No extracted data found.")

# ########################### 10 ################################

#             if extracted_data :
#                 print("oi")
#                 start_marker10 = """=====================================================================================================================================
# BOARD  ;LNH    ;PORT   ;T ;S ;OpMode   ;AutoNeg ;MacAddress        ;VlanIds       ;LOS ;BER
# ====================================================================================================================================="""
#                 end_marker10= """-------------------------------------------------------------------------------------
# Prio  ;ST  ;syncRefType    ;refStatus  ;opQualLevel   ;SyncReference
# -------------------------------------------------------------------------------------"""

#                 start_index10 = content.find(start_marker10)
#                 end_index10= content.find(end_marker10)
#                 extracted_data10= content[start_index10:end_index10]
#                 # print("nnn",extracted_data10)
                

#                 if extracted_data10:
#                     table_pattern10 = r'(\w+)\s*;(\w+)\s*;(\w+)\s*;(\w)\s*;(\w)\s*;(\w+)\s*;(\w+)\s*;([\w:]+)\s*;([\d,]+)\s*;(\d+)\s*;(\w+\/\d+)'
#                     # table_pattern5 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;(\d+\.\d+[KM]?)\s*;([^\n]+)\s*;(\d+[A-Z]?)\s*;(\d+%?)\s*;([-+]?\d*\.\d+)\s*;([-+]?\d*\.\d+)\s*;(\d+)'
#                     # table_pattern5 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)'
#                     # table_pattern5 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)'
#                     # table_pattern5 = r'(\d+)\s*;\s*(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+\.\d+[KM]?)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;(\d+\.\d+[KM]?)\s*;(\d+\.\d+[KM]?)$'
#                     # table_pattern5 = r'^(\d+)\s*;(\w+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;$'
#                     # table_pattern5= r'^(\d+)\s*;(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;$'
                    
#                     table_matches10 = re.findall(table_pattern10, extracted_data10, re.MULTILINE)#, re.MULTILINE

#                     if table_matches10:
#                         columns = [
#     'BOARD', 'LNH', 'PORT', 'T', 'S', 'OpMode', 'AutoNeg', 'MacAddress', 'VlanIds', 'LOS', 'BER'
# ]
                    
#                         table_df10 = pd.DataFrame(table_matches10, columns=columns)
#                         html_table = global_style + table_df10.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                         write_html_table("\n"+html_table)
#                         print("45th-10th:\n", table_df10)
#                         fourtysevenLog=table_df10.to_string(index=False)
#                         write_data("\n"+fourtysevenLog)
#                     else:
#                         print("No matching table data found.")  
#                 else:
#                     print("No extracted data found.")

#                 if extracted_data10:
#                     pattern = r'radioClockState\s*:\s*(\w+)'
#                     # pattern=r"(\w+)\s*"
#                     matches = re.search(pattern, extracted_data10)
#                     if matches:
#                         # Extract the value
#                         extracted_value = matches.group(1)
#                         # col=['radioClockState']
                        
#                         # Create a DataFrame
#                         df = pd.DataFrame({'radioClockState:': [extracted_value]})
#                         html_table = global_style + df.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                         write_html_table("\n"+html_table)
                        
#                         # Print the DataFrame
#                         print(df)
#                         fourtysevenLog=df.to_string(index=False)
#                         write_data("\n"+fourtysevenLog)


# ################# 11th ####################
#             if extracted_data :
#                 print("oi")
#                 start_marker11= """-------------------------------------------------------------------------------------
# Prio  ;ST  ;syncRefType    ;refStatus  ;opQualLevel   ;SyncReference
# -------------------------------------------------------------------------------------"""
#                 end_marker11= """=====================================================================================================================================
# FRU   ;LNH    ;BOARD          ;RF  ;BP  ;TX (W/dBm)  ;VSWR (RL)   ;RX (dBm) ;UEs/gUEs  ;Sector/AntennaGroup/Cells (State:CellIds:PCIs)
# ====================================================================================================================================="""

#                 start_index11 = content.find(start_marker11)
#                 end_index11 = content.find(end_marker11)
#                 extracted_data11= content[start_index11:end_index11]
#                 # print("nnn",extracted_data11)
                

#                 if extracted_data11:
#                     table_pattern11 = r'^(?!\s*[-]+)(\d+\s*\*?\d*)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)'


#                     # table_pattern11 = r'(\d+\s*\*?\d*)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)'
#                     # table_pattern11 = r'(\d+\s*\*?\d*)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)'

#                     # table_pattern11 = r'(\d+\s*\*?\d*)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)'

#                     # table_pattern11 = r'(?<=\n)(\d+\s*\*?\d*)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;\s*([^\n;]+)\s*;([^\n;]+)'
#                     # table_pattern11 = r'(?<=\n)(\d+\s+|\*\d+\s+)([^;]+)\s+;([^;]+)\s+;([^;]+)\s+;([^;]+)\s+;(.+?)(?=\n|$)'

#                     # table_pattern11 =r'(?<=\n)(\d+\s+|\*\d+\s+)([^;]+)\s+;([^;]+)\s+;([^;]+)\s+;([^;]+)\s+;(.+?)(?=\n|$)'
#                     # table_pattern11 = r'^(\d+)\s*;\s*(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(\d+)\s*;([^;]+)$'

#                     # table_pattern11 =r"^\s*([^;]+)\s*"
#                     # table_pattern11 =r'^\s*(\d+)\s*;\s*(\S+)\s*;(\S+)\s*;(\S+)\s*;(\S+)\s*;(.+)$'
#                     # table_pattern5 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;(\d+\.\d+[KM]?)\s*;([^\n]+)\s*;(\d+[A-Z]?)\s*;(\d+%?)\s*;([-+]?\d*\.\d+)\s*;([-+]?\d*\.\d+)\s*;(\d+)'
#                     # table_pattern5 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)'
#                     # table_pattern5 = r'(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)'
#                     # table_pattern5 = r'(\d+)\s*;\s*(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+\.\d+[KM]?)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;(\d+\.\d+[KM]?)\s*;(\d+\.\d+[KM]?)$'
#                     # table_pattern5 = r'^(\d+)\s*;(\w+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\w)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;$'
#                     # table_pattern5= r'^(\d+)\s*;(\w+)\s*;([^\n]+)\s*;(\d+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;(\d+)\s*;(\w)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;([^\n]+)\s*;$'
                    
#                     table_matches11 = re.findall(table_pattern11, extracted_data11, re.MULTILINE)#, re.MULTILINE

#                     if table_matches11:
#                         columns = ['Prio' , 'ST' , 'syncRefType', 'refStatus', 'opQualLevel', 'SyncReference']  ##
                    
#                         table_df11 = pd.DataFrame(table_matches11, columns=columns)
#                         html_table = global_style + table_df11.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                         write_html_table("\n"+html_table)
#                         print("45th-11th:\n", table_df11)
#                         fourtysevenLog=table_df11.to_string(index=False)
#                         write_data("\n"+fourtysevenLog)
#                     else:
#                         print("No matching table data found.")  
#                 else:
#                     print("No extracted data found.")

# ##################### 12th ##################################
#             if extracted_data :
#                 start_marker12="""MIE04225A> sdir"""
#                 end_marker12= """........................
# ...Checking available boards on node..."""
#                 start_index12 = content.find(start_marker12)
#                 end_index12 = content.find(end_marker12)
#                 extracted_data12= content[start_index12:end_index12]
#                 print("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",extracted_data12)

#                 if extracted_data12:
#                     # pattern1=r"^(\d+:\d+:\d+)\s"

#                     # table_matches1 = re.findall(pattern1, extracted_data, re.MULTILINE)#, re.MULTILINE

#                     pattern1 = r'\b\d{2}:\d{2}:\d{2}-\d{4}\b'
#                     table_matches1 = re.findall(pattern1, extracted_data, re.MULTILINE)

#                     if table_matches1:
#                         for time_string in table_matches1:
#                             print("VSWR:Extracted time string:", time_string)
#                     else:
#                         print("Time string not found in the data.")



#             if extracted_data :
#                 # print("oi")
#                 start_marker12= """=====================================================================================================================================
# FRU   ;LNH    ;BOARD          ;RF  ;BP  ;TX (W/dBm)  ;VSWR (RL)   ;RX (dBm) ;UEs/gUEs  ;Sector/AntennaGroup/Cells (State:CellIds:PCIs)
# ====================================================================================================================================="""
#                 end_marker12= """-------------------------------------------------------------------------------------------------------------------------------------

# MIE04225A>

# MIE04225A> hget . allowedplmnlist"""

#                 start_index12 = content.find(start_marker12)
#                 end_index12 = content.find(end_marker12)
#                 extracted_data12= content[start_index12:end_index12]
#                 # print("nnn",extracted_data12)
             

#                 if extracted_data12:
#                     # table_pattern12 = r'^(\d+-\d+)\s*;(\S+)\s*;(\S+)\s*;([^;]+);([^;]+);([^;]+);(\d+\.\d+\s+\(\d+\.\d+\))\s*;([^;]+);([^;]+);([^;]+)$'
#                     # table_pattern12 = r'^(\d+-\d+)\s*;(\S+)\s*;(\S+)\s*;([^;]+);([^;]+);([^;]+);(\d+\.\d+\s+\(\d+\.\d+\))\s*;([^;]+);([^;]+);([^;]+)$'
#                     # table_pattern12 = r'^(\d+-\d+)\s*;(\S+)\s*;(\S+)\s*;([^;]+);([^;]+);([^;]+);(\d+\.\d+\s+\(\d+\.\d+\))\s*;([^;]+);([^;]+);([^;]+)$'
#                     # table_pattern12 = r'^\s*(\d+-\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+-\s+(\S+)\s+(\d+\.\d+\s+\(\d+\.\d+\))\s+(\d+/-)\s*;([^;]+);([^;]+)$'
#                     # table_pattern12 = r'^\s*(\d+-\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+-\s+(\S+)\s+(\d+\.\d+\s+\(\d+\.\d+\))\s+(\d+/-)\s*;([^;]+);([^;]+)$'
#                     # table_pattern12 = r'^(\d+-\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\S+)\s+(\d+\.\d+\s+\(\d+\.\d+\))\s+(\d+/-)\s*;([^;]+);([^;]+)$'
#                     #SE=\d+-\d+\s+AG=\d+-\d+\s+FDD=\w+\s+FDD=\w+\s+NRC=\w+\s+\(\d+:\d+:\d+,\s+\d+:\d+:\d+,\s+\d+:\d+:\d+\)
#                     table_pattern12 = r'^(\d+-\d+)\s*;(\S+)\s*;(\S+)\s*;([^;]+);([^;]+);([^;]+);(\d+\.\d+\s+\(\d+\.\d+\))\s*;([^;]+);([^;]+);([^;]+)$(?!\s*[-]+)'
#                     # table_pattern12 = r'^\d+-\d+\s*;BXP_2\s*;([^\n]+)\s*;\s*[A-Z]\s*;\s*\d+\s*;[^;]*\s*;\s*[^;]*\s*;\s*[^;]*\s*;\s*[^;]*\s*;[^;]*$'

#                     # table_pattern12 = r'(\d+-\d+)\s*;BXP_2\s*;([^;]+)\s*;(\w)\s*;(\d+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;(.+)'
                    
#                     # table_pattern12 = r'^([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);(.+)$'

#                     # table_pattern12 = r'^(\S+)\s*;(\S+)\s*;(\S+)\s*;(\S+)\s*;(\S+)\s*;([\d\.\-]+)\s*;([\d\.\(\)]+)\s*;(\S*)\s*;(\S+)\s*;(.+)$'
#                     # table_pattern12 = r'^(\S+)\s*;(\S+)\s*;(\S+)\s*;(\S+)\s*;(\S+)\s*;([^;]+)\s*;([^;]+)\s*;(\S+)\s*;(\S+)\s*;(.+)$'
#                     # table_pattern12 = r'^([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);(.+)$'

#                     # table_pattern12 = r'^([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);([^;]+);(.+)$'
   
#                     table_matches12 = re.findall(table_pattern12, extracted_data12, re.MULTILINE)#, re.MULTILINE

#                     if table_matches12:

#                         columns = ['FRU' , 'LNH', 'BOARD', 'RF', 'BP', 'TX (W/dBm)','VSWR (RL)','RX (dBm)','UEs/gUEs','Sector/AntennaGroup/Cells (State:CellIds:PCIs)']  ##,'RX (dBm)'  

                    
#                         table_df12 = pd.DataFrame(table_matches12, columns=columns,)#,
#                         html_table = global_style + table_df12.to_html(escape=False, index=False,
#                                                               table_id='styled_table',
#                                                               classes='table table-striped table-bordered')

#                         write_html_table("\n"+html_table)
#                         # table_df12 = table_df12[~table_df12['Sector/AntennaGroup/Cells (State:CellIds:PCIs)'].str.contains(r'-+MIE04225A>')]
#                         print("45th-12th:\n", table_df12)
#                         fourtysevenLog=table_df12.to_string(index=False)
#                         write_data("\n"+fourtysevenLog)

#                         # fru_column = table_df12['FRU'].drop_duplicates()
#                         # print("FRU Column:\n", fru_column)

#                         # BOARD_column = table_df12['BOARD'].drop_duplicates()
#                         # print("BOARD Column:\n", BOARD_column)

#                         # VSWR_column = table_df12['VSWR (RL)']
#                         # print("VSWR (RL) Column:\n",VSWR_column)

#                         # rf_column = table_df12['RF']
#                         # print("RF Column:\n", rf_column)


#                         # cell_column = table_df12['Sector/AntennaGroup/Cells (State:CellIds:PCIs)']
#                         # print("Rcell Column:\n", cell_column)


#                         # # table_df12 = table_df12['VSWR (RL)'].transpose()

#                         # # print("VSWR (RL) as Row:\n", table_df12)

#                         # fourtysevenLog=table_df12.to_string(index=False)
#                         # write_data("\n"+fourtysevenLog)


                        

#                         # table=df.to_string(index=False)
#                         # write_data('\n-----:NODE INFO:-----:\n'+table)

#                         # site_Id="MIE04225A"

#                         # data2 = {
#                         #     "Site_Id":site_Id,
#                         #     'DATETIME': time_string,
#                         #     "CELL":cell_column,
#                         #     'BOARD': BOARD_column,
#                         #     "RF":rf_column,
#                         #     'FRU': fru_column
#                         # }

#                         # df = pd.DataFrame(data2)

#                         # print('oijinnhu\n',df)
#                         # fourtysevenLog=df.to_string(index=False)
#                         # write_data("ttttttttttt\n"+fourtysevenLog)


#                     else:
#                         print("No matching table data found.")  
#                 else:
#                     print("No extracted data found.")

# extract_data45(file_path)

   

###############################################################################################################################



#########################################################################################################################################



# log_pattern="NIE04225A2> get ^ManagedElement= ^managedElementType$ > $MEId"
# file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
# def log_data(file_path,log_pattern):

#       with open(file_path, 'r') as file:
#         log_data = file.read()
#         # if log_pattern in file_path:
#         if log_pattern in log_data:

#             pattern = r'^ManagedElement=(\w+)\s+managedElementType\s+(\w+)'

#             matches = re.findall(pattern, log_data, re.MULTILINE)

#             extracted_df = pd.DataFrame(matches, columns=['ManagedElement', 'managedElementType'])
#             global_style = "<style>td { text-align: left; }</style>"
#             html_table = global_style +extracted_df.to_html(escape=False, index=False,
#                                                                     table_id='styled_table',
#                                                                     classes='table table-striped table-bordered')

#             write_html_table("\n-----::-----:\n"+html_table)
#             print("1st log:\'MIE04225A> get ^ManagedElement= ^managedElementType$ > $MEId':::\n",extracted_df)
#             # first_log_data =extracted_df.to_string()
#         # write_data("1st log:\n'MIE04225A> get ^ManagedElement= ^managedElementType$ > $MEId':::\n"+first_log_data)
# log_data(file_path,log_pattern)



################################################################################################################

###############################################################################################################@|

file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
def extract_data45(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = """NIE04225A2> sdir"""
        end_marker = """NIE04225A2> cvls"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]   
        # print( "lkkhh",extracted_data)

        if extracted_data:
            start_marker1 = """...........
+--------+               +-------------+"""
            end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

NIE04225A2> cvls"""
            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]
            # print( "lllllmmmmmnnnn\n",extracted_data1)


            html_table = f"-----:5GNR SDIR Status(NIE04225A2> sdir):-----:\n{extracted_data1}"
 
            # Call the write_html_table function to save the HTML table
            write_html_table(html_table)
 
            # df = pd.DataFrame(extracted_data1)

            # html_table = global_style + df.to_html(escape=False, index=False,
                                                        # table_id='styled_table',
                                                        # classes='table table-striped table-bordered')

            # write_html_table(f"-----:5GNR SDIR Status:-----:\n{extracted_data1}")

extract_data45(file_path)



#######################################################################################################


file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
def third_file2(file_path3):
    with open(file_path3, 'r') as file:
        content = file.read()

        start_marker = """LVA61251A> sdir"""
        end_marker = """LVA61251A> pst"""

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        extracted_data = content[start_index:end_index]   
        # print( "lkkhh",extracted_data)

        if extracted_data:
            start_marker1 = """.............................
+--------+                         +----------+"""
            end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

LVA61251A> pst"""
            start_index1 = content.find(start_marker1)
            end_index1 = content.find(end_marker1)
            extracted_data1 = content[start_index1:end_index1]
            # print( "lllllmmmmmnnnn\n",extracted_data1)


            html_table = f"-----:5GNR SDIR Status(LVA61251A> sdir):-----:\n{extracted_data1}"
 
            # Call the write_html_table function to save the HTML table
            write_html_table(html_table)
 
            # df = pd.DataFrame(extracted_data1)

            # html_table = global_style + df.to_html(escape=False, index=False,
                                                        # table_id='styled_table',
                                                        # classes='table table-striped table-bordered')

            # write_html_table(f"-----:5GNR SDIR Status:-----:\n{extracted_data1}")

third_file2(file_path3)


#################################################################################################################

file_path="C:/Users/LENOVO/Desktop/dataframework/upload1/UVA61251A2_UMTS_Pre_Check (1).txt"
def extract_data11(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # print(content)

        output_file_path="C:/Users/LENOVO/Desktop/dataframework/find_data/fifth_data.txt"
        with open(output_file_path, "w") as output_file:
            # for line in phrase_data:
            output_file.write(content)

extract_data11(file_path)

file_path5="C:/Users/LENOVO/Desktop/dataframework/find_data/fifth_data.txt"
def fifth_file1(file_path5):
    with open(file_path5, 'r') as file:
        content5 = file.read()
        # print("lllll12",content3)

        if content5:
            start_marker1 = """VARNC004> lst VA61251A"""
            end_marker1 = """VARNC004> alt"""

            start_index1 = content5.find(start_marker1)
            end_index1 = content5.find(end_marker1)
            extracted_data = content5[start_index1:end_index1]   
            # print( "lkj",extracted_data)

            if extracted_data:
                start_marker2 = """===================================================================================
Proxy  Adm State     Op. State     MO
==================================================================================="""
                end_marker2 = """===================================================================================
Total: 20 MOs

VARNC004> alt"""

                start_index2 = extracted_data.find(start_marker2)
                end_index2 = extracted_data.find(end_marker2)
                extracted_data2 = extracted_data[start_index2:end_index2]   
                # print( "lkj2",extracted_data2)

                if extracted_data2:
                    # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    # table_pattern1 = r"^(\S+)\s*+(\w+)\s*+(\d+)\s*+(\d+)\s*+(\d+)\s*+()\s*"  #
                    table_pattern2=r'(\d+)\s+\s*(\d+\s+\(UNLOCKED\))\s+(\d+\s+\(ENABLED\))\s+(RncFunction=\d,UtranCell=\S+)'
                    table_matches2 = re.findall(table_pattern2, extracted_data2, re.MULTILINE)
                    # if table_pattern2

                    columns = ['Proxy','Adm State','Op. State','MO']    #'MO'
                    table_df3 = pd.DataFrame(table_matches2, columns=columns)
                    table_df3['Adm State'] = table_df3['Adm State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    table_df3['Op. State'] = table_df3['Op. State'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    d=table_df3['Proxy']
                    d1 = d.loc[0]
                    d2 = d.loc[6]
                    d3 = d.loc[12]
                    da=table_df3['Adm State']
                    da1 = da.loc[0] 
                    da2 = da.loc[6]
                    da3 = da.loc[12]
                    db=table_df3['Op. State']
                    db1 = db.loc[0] 
                    db2 = db.loc[6]
                    db3 = db.loc[12]
                    # print(d1,d2,d3)
                    # print('l;l;l;\n',table_df3)

                    p=r"(RncFunction=\d,UtranCell=\S+)"
                    if p in table_pattern2:
                        pattern=r"(?:UtranCell=(\S+))"
                        table_match = re.findall(pattern, extracted_data2, re.MULTILINE)
                        columns=['CELL']
                        table_ = pd.DataFrame(table_match, columns=columns)
                        # print('table_',table_)
                        cell=table_['CELL']
                        cell1=cell.loc[0]
                        # print("cell1",cell1)
                        cell2=cell.loc[6]
                        cell3=cell.loc[12]

                    data={
                        "CELL":(cell1,cell2,cell3),
                        'Proxy':(d1,d2,d3),
                        'Adm State':(da1,da2,da3),
                        'Op. State':(db1,db2,db3),
                        
                    }
                    da=pd.DataFrame(data)
                    # print(da)
                    html_table = global_style +da.to_html(escape=False, index=False,
                                                        table_id='styled_table',
                                                        classes='table table-striped table-bordered')

                    write_html_table(f"-----:fourth file(CELL SYSTEM INFORMATION BCCH DATA)-----:-----:\n{html_table}")
                    

fifth_file1(file_path5)


# file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
# def mfitr(file_path1):
#         # file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
#     with open(file_path1, 'r') as file:
#         content = file.read()
#         # print(content)
#         if content:
#             start_marker = """MIE04225A> mfitr"""
#             end_marker = """MIE04225A> pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'"""

#             start_index = content.find(start_marker)
#             end_index = content.find(end_marker)
#             extracted_data = content[start_index:end_index]
#             print("lkjihih",extracted_data)

#             if extracted_data :
#                 start_marker1 = """================================================================================================================================
# CELL            SC      FRU    BOARD          PUSCH  PUCCH       A      B      C      D  DELTA
# ================================================================================================================================"""
#                 end_marker1 = """================================================================================================================================

# MIE04225A> pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'"""

#                 start_index1 = content.find(start_marker1)
#                 end_index1 = content.find(end_marker1)
#                 extracted_data1 = content[start_index1:end_index1]

#                 print("jjjj",extracted_data1)

#                 # if extracted_data1:
#                 #     pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
#                 #     table_matche = re.findall(pattern, extracted_data, re.MULTILINE)
#                 #     if table_matche:
#                 #         date = table_matche[0]
#                 #         print('date:::',date)
#                 if extracted_data1:
#                     pattern1 = r'(FDD=\S+)\s+(\d+\-\d+\-\d+)\s+(\d+\-\d+)\s+(\S+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+\s*(\d+\.\d+|\d)\s'
                    
#                     table_matches1= re.findall(pattern1, extracted_data1, re.MULTILINE)

#                     if table_matches1:
#                         columns = ['CELL','SC','FRU',' BOARD','PUSCH','PUCCH' ,'A','B','C','D','DELTA'] # 
#                         table_df = pd.DataFrame(table_matches1, columns=columns)
#                         # global table_df['CELL']
#                         _1=table_df['CELL']
#                         _2=table_df['A']

#                         print('_2',_2)
#                         _3=table_df['B']
#                         _4=table_df['C']
#                         _5=table_df['D']
#                         _6=table_df['DELTA']
#                         # table_df.insert(0, 'Date', date)
#                         # print('lklklk\n',table_df)
#         ##########################################
#         if content:
#             start_marker = """MIE04225A> hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
#             end_marker = """MIE04225A> hget ^EUtranCellFDD|TDD|NBIOT cellid|rachroo|tac|earfcnd|earfcnul|cellrange|dlChannelBandwidth$|ulChannelBandwidth$"""

#             start_index = content.find(start_marker)
#             end_index = content.find(end_marker)
#             extracted_data = content[start_index:end_index]
#             print("lkjihih",extracted_data)

#             if extracted_data :
#                 start_marker1 = """=================================================================================================================
# MO                        administrativeState cellBarred     operationalState primaryPlmnReserved sectorCarrierRef
# ================================================================================================================="""
#                 end_marker1 = """MIE04225A> hget ^EUtranCellFDD|TDD|NBIOT cellid|rachroo|tac|earfcnd|earfcnul|cellrange|dlChannelBandwidth$|ulChannelBandwidth$"""

#                 start_index1 = content.find(start_marker1)
#                 end_index1 = content.find(end_marker1)
#                 extracted_data1 = content[start_index1:end_index1]

#                 print("jjjj",extracted_data1)

#                 # if extracted_data1:
#                 #     pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
#                 #     table_matche = re.findall(pattern, extracted_data, re.MULTILINE)
#                 #     if table_matche:
#                 #         date = table_matche[0]
#                 #         print('date:::',date)
#                 if extracted_data1:
#                     pattern1 = r'(EUtranCellFDD=\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\d+\s+\(NOT_BARRED\))\s+(\d+\s+\(ENABLED\))\s+(\w+)\s+(?:\[1\] = (SectorCarrier=\d+))'
                    
#                     table_matches1= re.findall(pattern1, extracted_data1, re.MULTILINE)
#                     if table_matches1:
#                         columns = ['MO ','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef'] # 
#                         table_df1 = pd.DataFrame(table_matches1, columns=columns)
#                         s1=table_df1['MO ']
#                         s2=table_df1['administrativeState']
#                         s3=table_df1['cellBarred']
#                         s4=table_df1['operationalState']
#                         s5=table_df1['primaryPlmnReserved']
#                         s6=table_df1['sectorCarrierRef']

#                         # print('ttt\n',table_df1)
#         ###########################################



#                         dtta={
#                             'Site Id':'MIE04225A',
#                             'MO ':s1,
#                             'administrativeState':s2,
#                             'cellBarred':s3,
#                             'operationalState':s4,
#                             'primaryPlmnReserved':s5,
#                             'sectorCarrierRef':s6,
#                             # 'CELL':_1,
#                             'A':_2,
#                             'B':_3,
#                             'C':_4,
#                             'D':_5,
#                             'DELTA':_6
#                         }
#                         ddd=pd.DataFrame(dtta)
#                         # ddd['Site Id'] = 'MIE04225A'
                        
#                         print('ddd',ddd)

#                         html_table = global_style + ddd.to_html(escape=False, index=False,
#                                                                 table_id='styled_table',
#                                                                 classes='table table-striped table-bordered')

#                         write_html_table("--------:mfitr--------:"+html_table)

#                         # print("RSSI:\n", table_df)
#                         fourtysevenLog= table_df.to_string(index=False)
#                         write_data("\n--------:RSSI:--------:\n"+fourtysevenLog)

# mfitr(file_path1) 

# file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
# def third_file1(file_path3):
#     with open(file_path3, 'r') as file:
#         content3 = file.read()
#         # print("lllll12",content3)
#         if content3:
#             start_marker = """LVA61251A> hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
#             end_marker = """LVA61251A> hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""

#             start_index = content3.find(start_marker)
#             end_index = content3.find(end_marker)
#             extracted_data = content3[start_index:end_index]   
#             # print( "lkkhh",extracted_data)

#             if extracted_data:
#                 start_marker1 = """=================================================================================================================
# MO                        administrativeState cellBarred     operationalState primaryPlmnReserved sectorCarrierRef     
# ================================================================================================================="""
#                 end_marker1 = """=================================================================================================================
# Total: 6 MOs

# Added 6 MOs to group: hget_group
# ..
# =================================================================================================================
# MO                    administrativeState cellBarred     operationalState sectorCarrierRef     
# ================================================================================================================="""
#                 start_index1 = content3.find(start_marker1)
#                 end_index1 = content3.find(end_marker1)
#                 extracted_data1 = content3[start_index1:end_index1]   
#                 # print( "lkkhh",extracted_data1)

#                 if extracted_data1:
#                     # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
#                     # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
#                     table_pattern1 = r"(EUtranCellFDD=\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\d+\s+\(NOT_BARRED\))\s+(\d+\s+\(ENABLED\))\s+(\w+)\s+(?:\[1\] = (SectorCarrier=\d+))"  #(SectorCarrier=\d+)\s+(\d+)+\s*(\d+\s+\(ENABLED\))+ \s*(?:\[\d+\] = (.+))$  # (^\[\d+\] = NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+)\s*
#                     table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

#                     columns = [ 'MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']   #,
#                     table_df1 = pd.DataFrame(table_matches1, columns=columns)
#                     print(table_df1)
#                     p1=table_df1['MO']
#                     p2=table_df1['administrativeState']
#                     p3=table_df1['cellBarred']
#                     p4=table_df1['operationalState']
#                     p5=table_df1['primaryPlmnReserved']
#                     p6=table_df1['sectorCarrierRef']
                    # table_df1.table_df['A']
                    # table_df1.table_df['B']
                    # table_df1.table_df['C']
                    # table_df1.table_df['D']
                    # table_df1.table_df['DELTA']
                    # table_df1['Site Id'] = 'LVA61251A'
                    # table_df1 = table_df1[['Site Id','MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']]

                    ########################################
#     file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
#     with open(file_path1, 'r') as file:
#         content = file.read()
#         # print(content)

#         start_marker = """MIE04225A> mfitr"""
#         end_marker = """MIE04225A> pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'"""

#         start_index = content.find(start_marker)
#         end_index = content.find(end_marker)
#         extracted_data = content[start_index:end_index]
#         print("lkjihih",extracted_data)

#         if extracted_data :
#             start_marker1 = """================================================================================================================================
# CELL            SC      FRU    BOARD          PUSCH  PUCCH       A      B      C      D  DELTA
# ================================================================================================================================"""
#             end_marker1 = """
# MIE04225A> pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'"""

#             start_index1 = content.find(start_marker1)
#             end_index1 = content.find(end_marker1)
#             extracted_data1 = content[start_index1:end_index1]

#             print("jjjj",extracted_data1)


#             if extracted_data1:
#                 pattern1 = r'(FDD=\S+)\s+(\d+\-\d+\-\d+)\s+(\d+\-\d+)\s+(\S+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+\s*(\d+\.\d+|\d)\s'
                
#                 table_matches1= re.findall(pattern1, extracted_data1, re.MULTILINE)

#                 if table_matches1:
#                     columns = ['CELL','SC','FRU',' BOARD','PUSCH','PUCCH' ,'A','B','C','D','DELTA'] # 
#                     table_df = pd.DataFrame(table_matches1, columns=columns)
#                     # global table_df['CELL']
#                     _1=table_df['CELL']
#                     _2=table_df['A']
#                     _3=table_df['B']
#                     _4=table_df['C']
#                     _5=table_df['D']
#                     _6=table_df['DELTA']
#                     # table_df.insert(0, 'Date', date)
#                     # print('lklklk\n',table_df)
#                     global ddd
#                     dtta={
#                         'A':_2,
#                         'B':_3,
#                         'C':_4,
#                         'D':_5,
#                         'DELTA':_6
#                     }
#                     ddd=pd.DataFrame(dtta)

#                     print("table_df1+ddd",ddd)

#                     # table_df1['Site Id'] = 'MIE04225A'
#                     # table_df1 = table_df1[['Site Id','MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']]
#                     html_table = global_style +ddd.to_html(escape=False, index=False,
#                                                         table_id='styled_table',
#                                                         classes='table table-striped table-bordered')

#                     write_html_table(f"-----:LTE CELL STATUS-----:-----:\n{html_table}")
   

# third_file1(file_path3)


# def mfirt(file_path1):
#     file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
#     with open(file_path1, 'r') as file:
#         content = file.read()
#         print(content)


#         if extracted_data1:
#             pattern1 = r'(FDD=\S+)\s+(\d+\-\d+\-\d+)\s+(\d+\-\d+)\s+(\S+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+\s*(\d+\.\d+|\d)\s'
            
#             table_matches1= re.findall(pattern1, extracted_data1, re.MULTILINE)

#             if table_matches1:
#                 columns = ['CELL','SC','FRU',' BOARD','PUSCH','PUCCH' ,'A','B','C','D','DELTA'] # 
#                 table_df = pd.DataFrame(table_matches1, columns=columns)
#                 # global table_df['CELL']
#                 _1=table_df['CELL']
#                 _2=table_df['A']
#                 _3=table_df['B']
#                 _4=table_df['C']
#                 _5=table_df['D']
#                 _6=table_df['DELTA']
#                 # table_df.insert(0, 'Date', date)
#                 # print('lklklk\n',table_df)
#                 global ddd
#                 dtta={
#                     'A':_2,
#                     'B':_3,
#                     'C':_4,
#                     'D':_5,
#                     'DELTA':_6
#                 }
#                 ddd=pd.DataFrame(dtta)

#                 print("table_df1+ddd",ddd)

# mfirt()



file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
def third_file1(file_path3):
    with open(file_path3, 'r') as file:
        content3 = file.read()
        # print("lllll12",content3)
        if content3:
            start_marker = """LVA61251A> hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
            end_marker = """LVA61251A> hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""

            start_index = content3.find(start_marker)
            end_index = content3.find(end_marker)
            extracted_data = content3[start_index:end_index]   
            # print( "lkkhh",extracted_data)

            if extracted_data:
                start_marker1 = """=================================================================================================================
MO                        administrativeState cellBarred     operationalState primaryPlmnReserved sectorCarrierRef     
================================================================================================================="""
                end_marker1 = """=================================================================================================================
Total: 6 MOs

Added 6 MOs to group: hget_group
..
=================================================================================================================
MO                    administrativeState cellBarred     operationalState sectorCarrierRef     
================================================================================================================="""
                start_index1 = content3.find(start_marker1)
                end_index1 = content3.find(end_marker1)
                extracted_data1 = content3[start_index1:end_index1]   
                # print( "lkkhh",extracted_data1)

                if extracted_data1:
                    # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    table_pattern1 = r"(EUtranCellFDD=\S+)\s+(\d+\s+\(UNLOCKED\))\s+(\d+\s+\(NOT_BARRED\))\s+(\d+\s+\(ENABLED\))\s+(\w+)\s+(?:\[1\] = (SectorCarrier=\d+))"  #(SectorCarrier=\d+)\s+(\d+)+\s*(\d+\s+\(ENABLED\))+ \s*(?:\[\d+\] = (.+))$  # (^\[\d+\] = NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+)\s*
                    table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

                    columns = [ 'MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']   #,
                    table_df1 = pd.DataFrame(table_matches1, columns=columns)
                    table_df1['administrativeState'] = table_df1['administrativeState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    table_df1['cellBarred'] = table_df1['cellBarred'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    table_df1[ 'operationalState'] = table_df1[ 'operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    # print(table_df1)
                    table_df1['Site Id'] = 'LVA61251A'
                    table_df1 = table_df1[['Site Id','MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']]
                    # print('table_df1',table_df1)
                    
################################
    file_path1="C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
    with open(file_path1, 'r') as file:
        content = file.read()
        # print(content)
        if content:
            start_marker = """MIE04225A> mfitr"""
            end_marker = """MIE04225A> pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'"""

            start_index = content.find(start_marker)
            end_index = content.find(end_marker)
            extracted_data = content[start_index:end_index]
            # print("lkjihih",extracted_data)

            if extracted_data :
                start_marker1 = """================================================================================================================================
CELL            SC      FRU    BOARD          PUSCH  PUCCH       A      B      C      D  DELTA
================================================================================================================================"""
                end_marker1 = """================================================================================================================================

MIE04225A> pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'"""

                start_index1 = content.find(start_marker1)
                end_index1 = content.find(end_marker1)
                extracted_data1 = content[start_index1:end_index1]

                # print("jjjj",extracted_data1)

                # if extracted_data1:
                #     pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
                #     table_matche = re.findall(pattern, extracted_data, re.MULTILINE)
                #     if table_matche:
                #         date = table_matche[0]
                #         print('date:::',date)
                if extracted_data1:
                    pattern1 = r'(FDD=\S+)\s+(\d+\-\d+\-\d+)\s+(\d+\-\d+)\s+(\S+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+\s*(\d+\.\d+|\d)\s'
                    
                    table_matches1= re.findall(pattern1, extracted_data1, re.MULTILINE)

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
            start_marker = """MIE04225A> hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
            end_marker = """MIE04225A> hget ^EUtranCellFDD|TDD|NBIOT cellid|rachroo|tac|earfcnd|earfcnul|cellrange|dlChannelBandwidth$|ulChannelBandwidth$"""

            start_index = content.find(start_marker)
            end_index = content.find(end_marker)
            extracted_data = content[start_index:end_index]
            # print("lkjihih",extracted_data)

            if extracted_data :
                start_marker1 = """=================================================================================================================
MO                        administrativeState cellBarred     operationalState primaryPlmnReserved sectorCarrierRef
================================================================================================================="""
                end_marker1 = """=================================================================================================================
Total: 6 MOs

Added 6 MOs to group: hget_group

MIE04225A> hget ^EUtranCellFDD|TDD|NBIOT cellid|rachroo|tac|earfcnd|earfcnul|cellrange|dlChannelBandwidth$|ulChannelBandwidth$"""

                start_index1 = content.find(start_marker1)
                end_index1 = content.find(end_marker1)
                extracted_data1 = content[start_index1:end_index1]

                # print("jjjj",extracted_data1)

                # if extracted_data1:
                #     pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
                #     table_matche = re.findall(pattern, extracted_data, re.MULTILINE)
                #     if table_matche:
                #         date = table_matche[0]
                #         print('date:::',date)
                if extracted_data1:
                    pattern2 = r'(EUtranCellFDD=\S+)\s(\d+\s+\(UNLOCKED\))\s+(\d+\s+\(NOT_BARRED\))\s+(\d+\s+\(ENABLED\))\s+(\w+)\s+(?:\[1\] = (SectorCarrier=\d+))'#
                    
                    table_matches2= re.findall(pattern2, extracted_data1, re.MULTILINE)
                    # print('table_matches2',table_matches2)
                    if table_matches2:
                        columns = ['MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef'] # 
                        table_df213= pd.DataFrame(table_matches2, columns=columns)
                        table_df213['Site Id'] = 'MIE04225A'
                        table_df213=table_df213[['Site Id','MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']]
                        # print('ttpp',table_df213)
                        s1=table_df1['MO']
                        s2=table_df1['administrativeState']
                        s3=table_df1['cellBarred']
                        s4=table_df1['operationalState']
                        s5=table_df1['primaryPlmnReserved']
                        s6=table_df1['sectorCarrierRef']

        #                 # print('ttt\n',table_df1)
        # ###########################################



                        dtta={
                            'Site Id':'MIE04225A',
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
                        
        #                 print('ddd',ddd)
                        

                        
######################################################################################
                    combined_table_df = pd.concat([ddd,table_df1], ignore_index=True)
                    # print('combined_table_df\n',combined_table_df)
                    # if "NaN" in combined_table_df:
                    #     combined_table_df.replace("NaN","")

                    combined_table_df = combined_table_df.fillna('') 
                    # ###############################################################
                    html_table = global_style + combined_table_df.to_html(escape=False, index=False,
                                                            table_id='styled_table',
                                                            classes='table table-striped table-bordered')

                    write_html_table("\n-----:5GNR RILINK:-----:\n" + html_table)
   

third_file1(file_path3)
#########################################################################################################

file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/fifth_data.txt" 
def fifth_file3(file_path3):
    with open(file_path3, 'r') as file:
        content3 = file.read()
        # print("lllll12",content3)
        if content3:
            start_marker = """UVA61251A2> invrxb"""
            end_marker = """UVA61251A2> get . dis"""

            start_index = content3.find(start_marker)
            end_index = content3.find(end_marker)
            extracted_data = content3[start_index:end_index]   
            # print( "lkkhh",extracted_data)

            if extracted_data:
                start_marker1 = """=====================================================================================================================================
ID LINK WL1  TEMP1 TXbs1 TXdBm1 RXdBm1 BER1   WL2  TEMP2 TXbs2 TXdBm2 RXdBm2 BER2   DlLoss UlLoss
====================================================================================================================================="""
                end_marker1 = """-------------------------------------------------------------------------------------------------------------------------------------

=====================================================================================================================================
ID BOARD       SFPLNH             PORT VENDOR  VENDORPROD       REV  SERIAL         DATE     ERICSSONPROD   WL   TEMP  TXbs  TXdBm  RXdBm   BER
====================================================================================================================================="""
                start_index1 = content3.find(start_marker1)
                end_index1 = content3.find(end_marker1)
                extracted_data1 = content3[start_index1:end_index1]   
                # print( "lkkhh",extracted_data1)

                if extracted_data1:
                    # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    table_pattern1 = r"(\d+)\s+(Up)\s+(\d+)\s+(\d+C)\s+(\d+%)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(\d+)\s+(\d+)\s+(\d+C)\s+(\d+%)\s+(-\d+\.\d+)\s+(-\d+\.\d+)\s+(\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s"  #(\d+)\s+

                    # if re.match(table_pattern1, extracted_data1):
                    #     print("Pattern matches extracted data1")
                    

                    table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)

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
                start_marker2 = """=====================================================================================================================================
AuxPiu    LNH                  BOARD       RF  TX (W/dBm)  VSWR (RL)    Sector/Cells (localCellIds/CellIds,PCIs)
====================================================================================================================================="""
                end_marker2 = """-------------------------------------------------------------------------------------------------------------------------------------
Tip: use option "g" to print graphical view of CPRI connections and RF connections.

UVA61251A2> get . dis"""
                start_index2 = content3.find(start_marker2)
                end_index2 = content3.find(end_marker2)
                extracted_data2 = content3[start_index2:end_index2]   
                # print( "ppppp",extracted_data2)

                if extracted_data2:
                    # table_pattern1= r"EUtranCellFDD=(\S+) (\d+) \(UNLOCKED\) (\d+) \(NOT_BARRED\) (\d+) \(ENABLED\) false \[(\d+)\] = SectorCarrier=(\d+)"
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    table_pattern2 = r'(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+([0-9.]+ \(\d+\.\d+\))\s+(\S+)\s+((?:SR=\d+ \S+ \(\d+\))|(?:N/A))\s'

                    # if re.match(table_pattern1, extracted_data1):
                    #     print("Pattern matches extracted data1")
                    

                    table_matches2 = re.findall(table_pattern2, extracted_data2, re.MULTILINE)

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
                    table_pattern3 = r'\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.*)'
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
                    # b1=table_df2['VSWR (RL)']
                    # b2=table_df2['Sector/Cells (localCellIds/CellIds,PCIs)']
                    # print(table_df3)

###########################
#######################
    file_path6="C:/Users/LENOVO/Desktop/dataframework/find_data/seventh_data.txt"
    with open(file_path6, 'r') as file:
        content = file.read()
        if content:
            start_marker1 = "VARNC004> get UtranCell=.*(VA61251A).* ^cellreserved$|^accessClassNBarred$|^accessClassesBarredCs$|^accessClassesBarredPs$|^cId"
            # print(start_marker1)
            end_marker1 = "VARNC004> alt"

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
                    t1= table_df4['MO']  #table_df4['MO']+table_df4['value'].apply(lambda x: f'({x})')
                    t2=table_df4['Attribute']
                    # t3=table_df4['value']
                    # add=[f'({t1}+\n({t3}))']
                    
            #         table_df1['Site Id'] = 'NIE04225A2'
            #         table_df1 = table_df1[['Site Id','Proxy', 'Adm State', 'Op. State', 'MO']]  ### 
                    
                    # print(" log:\n",table_df1)

#############################

                    data={
                        'Site_Id':'UVA61251A2',
                        'Cells':t1,                       
                        'BER1':a2,
                        'BER2':a3,
                        'DlLoss':a4,
                        'UlLoss':a5,
                        'VSWR (RL)':c,
                       
                        # 'value':t3

                    }
                    # import pandas as pd
                    table_df=pd.DataFrame(data)
                    # print(table_df)

                    html_table = global_style + table_df.to_html(escape=False, index=False,
                                                              table_id='styled_table',
                                                              classes='table table-striped table-bordered')

                    write_html_table("\n-----:UVA61251A2_UMTS_Pre_Check (2):-----:\n" + html_table)
                    

                    # print('qws',a)
                    # else:
                    #     print("Pattern does not match extracted data1")
                    # # table_df1['Site Id'] = 'UVA61251A2'
                    # # table_df1 = table_df1[['Site Id','MO','administrativeState','cellBarred','operationalState','primaryPlmnReserved','sectorCarrierRef']]
                    # print('table_df1',table_df1)
fifth_file3(file_path3)
#####################################################################################

file_path3="C:/Users/LENOVO/Desktop/dataframework/find_data/fifth_data.txt" 
def sixth_file3(file_path3):
    with open(file_path3, 'r') as file:
        content3 = file.read()
        # print("lllll12",content3)
        if content3:
            start_marker = """UVA61251A2> st ret"""
            end_marker = """UVA61251A2> get . electrical"""

            start_index = content3.find(start_marker)
            end_index = content3.find(end_marker)
            extracted_data = content3[start_index:end_index]   
            # print( "lkkhh",extracted_data)

            if extracted_data:
                start_marker1 = """UVA61251A2> st ret

220105-08:31:51 11.170.49.196 17.0m RBS_NODE_MODEL_U_2_51 stopfile=/tmp/12453"""
                end_marker1 = """UVA61251A2> get . electrical

220105-08:31:52 11.170.49.196 17.0m RBS_NODE_MODEL_U_2_51 stopfile=/tmp/12453"""
                start_index1 = content3.find(start_marker1)
                end_index1 = content3.find(end_marker1)
                extracted_data1 = content3[start_index1:end_index1]   
                # print( "lllppp",extracted_data1)

                if extracted_data1:
                    table_pattern1= r"\b(\d+)\s+()\s+(\d+\s+\(ENABLED\))\s+(.*)\b"
                    # if table_pattern1 in extracted_data1:
                    # table_pattern1 = r"\d+\s+(SectorCarrier=\d+)\s+(\d+)\s+(\d+\s+\(ENABLED\))\s+(\[\d+\] = (?:NbIotCell=\S+ EUtranCellFDD=\S+ UlCompGroup=\d+|\S+ EUtranCellFDD=\S+ NbIotCell=\S+ UlCompGroup=\d+))"
                    # table_pattern1 = r"\b(\d+)\s+()\s+(\d+\s+\(ENABLED\))\s+(.*)\b"  #^1 \(ENABLED\)$

                    # if re.match(table_pattern1, extracted_data1):
                    #     print("Pattern matches extracted data1")
                    
  
                    table_matches1 = re.findall(table_pattern1, extracted_data1, re.MULTILINE)
                    # if table_matches1 in extracted_data1:

                    columns = ['Proxy','Adm State',' Op. State ',' MO']   #
                    table_df1 = pd.DataFrame(table_matches1, columns=columns)
                    table_df1[' Op. State '] = table_df1[' Op. State '].str.replace(r'(', '').str.replace(')', '').str.replace('1', '')
                    # print(table_df1)
                    a=table_df1[' Op. State ']
                    a1=a[0]
                    a2=a[4]
                    a3=a[7]
                    a4=a[9]
                    a5=a[12]
                    a6=a[14]

                    # print(a1)


            if extracted_data:
                start_marker1 = """UVA61251A2> hget ret electricalAntennaTilt|maxTilt|minTilt"""
                end_marker1 = """=================================================================================================================
MO             maxTilt minTilt
================================================================================================================="""
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
                        'RET MO':t1,
                        'electricalAntennaTilt':t2,
                        'Op. State':[a1,a2,a3,a4,a5,a6]
                    }
                    dd=pd.DataFrame(data)
                    # print('laks',dd)



                    def apply_color(val):

                        # print(len(val),"ENABLED",val.strip()=="ENABLED",)

                        # dskjhksajdlksa
                        if val.strip() == 'ENABLED':
                            return 'background-color: red; '
                        else:
                            return ''

                    dd['Op. State'] = dd['Op. State'].apply(lambda x: f'<span style="{apply_color(x)}">{x}</span>')

                    # Generate the HTML table with the applied styling
                    html_table = dd.to_html(escape=False, index=False, table_id='styled_table', classes='table table-striped table-bordered')

                    # Print the HTML table or write it to a file
                    # print('laks', dd)
                    # with open('styled_table.html', 'w') as file:
                    #     file.write(html_table)

                    
                    # def highlight_red(val):


                    #     # print(len(val.strip()),"ENABLED")
                        
                    #     if val == 'ENABLED':
                    #         return f'<span style="color: red; padding: 2px;">{val}</span>'
                    #     else:
                    #         return val
                        
                    
                    # dd['Op. State'] = dd['Op. State'].apply(highlight_red)  # Note the spaces in the column name

                    # # dd = dd.reset_index(drop=True)

                    # # Generate the HTML table
                    # html_table = dd.to_html(escape=False, index=False, table_id='styled_table', classes='table table-striped table-bordered')



                    write_html_table("\n-----:UVA61251A2> hget ret electricalAntennaTilt|maxTilt|minTilt:-----:\n" + html_table)
sixth_file3(file_path3)
















