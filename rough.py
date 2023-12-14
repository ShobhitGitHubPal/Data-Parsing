




# Import necessary libraries
import pandas as pd
import re
import os

filepath2="C:/Users/LENOVO/Desktop/dataframework/find_data/second_data.txt"
def extract_data455(filepath2):
    
    with open(filepath2, 'r') as file:
            content2 = file.read()

            start_marker2= """sdir"""
            end_marker2 = """cvls"""

            start_index2 = content2.find(start_marker2)
            end_index2 = content2.find(end_marker2)
            extracted_data2 = content2[start_index2:end_index2]   
            # print( "lkkhh",extracted_data2)

            if extracted_data2:
                start_marker3 = """...........
+--------+               +-------------+"""
                end_marker3 = """ NIE04225A2> cvls"""
                start_index3 = content2.find(start_marker3)
                end_index3 = content2.find(end_marker3)
                extracted_data3 = content2[start_index3:end_index3]
                print( "lllllmmmmmnnnn\n",extracted_data3)

                if extracted_data3:
                    table_pattern3="(\d+)\s;([A-Za-z0-9-]+)\s*;(\S+)\s*;(\S+)\s*;\s*(\d+)\s*;(\S+)\s*;(\S+)\s*;(\w+)\s*;(\S+)\s*;(\d+)\s*;(\w+/\d+ R1A)\s*;(\d+\.\d+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*"   ###   ;([A-Za-z0-9-]+)\s*;(\S+)\s*;(\S+)\s*;\s*(\d+)\s*;(\S+)\s*;(\S+)\s*;(\w+)\s*;(\S+)\s*;(\d+)\s*;(\w+/\d+ R1A)\s*;(\d+\.\d+)\s*;(\d+C)\s*;(\d+%)\s*;(-\d+\.\d+)\s*;(-\d+\.\d+)\s*;\s*(\d+)\s*

                    table_matches3 = re.findall(table_pattern3, extracted_data3, re.MULTILINE)

                    print(table_matches3)

                    if table_matches3:
                        
                        # global c1,c2,c3
                        columns = [ 'ID', 'RiL','BOARD','SFPLNH','PORT','VENDOR','VENDORPROD ','REV','SERIAL','DATE','ERICSSONPROD','WL','TEMP','TXbs','TXdBm','RXdBm',' BER']   ##   , 'RiL','BOARD','SFPLNH','PORT','VENDOR','VENDORPROD ','REV','SERIAL','DATE','ERICSSONPROD','WL','TEMP','TXbs','TXdBm','RXdBm',' BER'
                        table_df3 = pd.DataFrame(table_matches3, columns=columns)
                        print(table_df3,'table_df3table_df3table_df3table_df3table_df3')

extract_data455(filepath2)