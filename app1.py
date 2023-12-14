from flask import Flask,request,jsonify
from werkzeug.utils import secure_filename
import os
import re
# import magic
import pandas as pd

app = Flask(__name__)

# @app.route("/", methods=["POST","GET"])
# def hello_world():
#     if request.method == "POST":
#         file= request.files["filename"]

#         if file:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join('C:/Users/LENOVO/Desktop/dataframework/uploads', filename))
#             return jsonify({'message': 'File uploaded successfully'})
#         return jsonify({'error': 'Error uploading the file'})

#     return file

# file_path= "C:/Users/LENOVO/Desktop/dataframework/uploads/MIE04225A_PreCheck_MMBBscriptrun.log" 
# log="hpget . pmendcsetupueatt|pmEndcSetupUeSucc|^pmmacvoldl$|^pmmacvolul$|PMMACVOLDLDRB$"
# def count_line(file_path):
#     df = pd.read_table(file_path)
#     if log in df:

#     print(df)



# import pandas as pd

# file_path = "C:/Users/LENOVO/Desktop/dataframework/uploads/MIE04225A_PreCheck_MMBBscriptrun.log"
# log = "hpget . pmendcsetupueatt|pmEndcSetupUeSucc|^pmmacvoldl$|^pmmacvolul$|PMMACVOLDLDRB$"

# def extract_matching_rows(file_path, log_pattern):
#     df = pd.read_table(file_path, header=None, names=['log'])

#     matching_rows = df[df['log'].str.contains(log_pattern, na=False)]

#     return matching_rows

# try:
#     matching_data = extract_matching_rows(file_path, log)
#     print("Matching Data:")
#     print(matching_data)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")





# import pandas as pd

# file_path = "C:/Users/LENOVO/Desktop/dataframework/uploads/MIE04225A_PreCheck_MMBBscriptrun.log"
# log = "hpget . pmendcsetupueatt|pmEndcSetupUeSucc|^pmmacvoldl$|^pmmacvolul$|PMMACVOLDLDRB$"

# output_file_path = "C:/Users/LENOVO/Desktop/dataframework/find_data/lg_data.txt"

# def extract_matching_rows(file_path, log_pattern):
#     df = pd.read_table(file_path, header=None, names=['log'])

#     matching_rows = df[df['log'].str.contains(log_pattern, na=False)]

#     return matching_rows

# try:
#     matching_data = extract_matching_rows(file_path, log)
#     print("Matching Data:")
#     print(matching_data)

#     # Save the matching data to the output file
#     matching_data.to_csv(output_file_path, index=False)

#     print(f"Matching data saved to: {output_file_path}")
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")




# import pandas as pd

# file_path = "C:/Users/LENOVO/Desktop/dataframework/uploads/MIE04225A_PreCheck_MMBBscriptrun.log"
# # log = "hpget . pmendcsetupueatt|pmEndcSetupUeSucc|^pmmacvoldl$|^pmmacvolul$|PMMACVOLDLDRB$"
# log="MIE04225A> hpget . pmendcsetupueatt|pmEndcSetupUeSucc|^pmmacvoldl$|^pmmacvolul$|PMMACVOLDLDRB$"

# output_file_path = "C:/Users/LENOVO/Desktop/dataframework/extracted_data.txt"

# def extract_matching_data(file_path, log_pattern):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()

#     matching_data = []
#     is_matching = False

#     for line in lines:
#         if log_pattern in line:
#             if is_matching:
#                 break
#             else:
#                 is_matching = True
#                 matching_data.append(line)
#         elif is_matching:
#             matching_data.append(line)

#     return matching_data

# try:
#     matching_data = extract_matching_data(file_path, log)
#     print("Matching Data:")
#     for line in matching_data:
#         print(line, end='')

#     # Save the matching data to the output file
#     with open(output_file_path, 'w') as output_file:
#         for line in matching_data:
#             output_file.write(line)

#     print(f"Matching data saved to: {output_file_path}")
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")






# import re
# import pandas as pd
# # from app import *

# log_data=r"hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"
# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# col="""=================================================================================================================
# MO                   nRTAC
# ================================================================================================================="""
# def extract1( file_path,log_data):#log_data
#     with open(file_path, 'r') as file:
#         read = file.read()
#         if log_data in read and col in read:
#             print("yrrr")
#             # log_pattern = r'^NRCellCU=(\w+)\s+(\d+)'
#             log_pattern = r'^NRCellCU=(\w+)\s+(\d{7})'
#             matches = re.findall(log_pattern, read, re.MULTILINE)
#             if matches:
#                 print(matches)
#                 columns=['MO', 'nRTAC']
#                 table_data = [list(match) for match in matches]
#                 table_df = pd.DataFrame(table_data, columns=columns)
#                 print(table_df)

# extract1(file_path, log_data)
import re


# col="""====================================================================================================================
# Date & Time (UTC)   S Specific Problem                    MO (Cause/AdditionalInfo)
# ===================================================================================================================="""

# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# lg_d = "alt"

# def extract_data1(lg_d, file_path):
#     with open(file_path, 'r') as file:
#         # Read the whole file as a string
#         read = file.read()

#     if lg_d in read and col in read:
#         # Use regular expression to find the table data
#         table_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(.+?)\s+(.+)"

#         table_matches = re.findall(table_pattern, read)

#         # If table data is found
#         if table_matches:
#             # Create a DataFrame with the desired columns
#             columns_to_keep = ['Date & Time (UTC)', 'S Specific Problem', 'MO (Cause/AdditionalInfo)']
#             table_data = [list(match) for match in table_matches]
#             table_df = pd.DataFrame(table_data, columns=columns_to_keep)

#             print("table_df==\n", table_df)
#             # thirdLog=table_df.to_string()
#             # write_data("thirdLog\n"+thirdLog)
            

#         else:
#             raise ValueError("Unable to find the table data in the file.")

# # Call the function to extract and parse data.
# try:
#     extract_data1(lg_d, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print(f"An error occurred: {e}")



# import re
# import pandas as pd

# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'

# def extract_between_logs(file_path, start_log_pattern, end_log_pattern):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         start_indices = [match.start() for match in re.finditer(start_log_pattern, content)]
#         end_indices = [match.start() for match in re.finditer(end_log_pattern, content)]

#         for start_idx, end_idx in zip(start_indices, end_indices):
#             section = content[start_idx:end_idx]
#             print("Found relevant section:")
#             # print(section)
            
#             log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
#             matches = re.findall(log_pattern, section)
            
#             if matches:
#                 columns = ['Date & Time (UTC)', 'S Specific Problem', 'MO (Cause/AdditionalInfo)']
#                 table_df = pd.DataFrame(matches, columns=columns)
#                 print(table_df)
#             else:
#                 print("No matches found in the section.")
#             # print("=" * 100)

# start_log_pattern = r'MIE04225A> alt'
# end_log_pattern = r'>>> Total: \d+ Alarms \(\d Critical, \d Major\)'

# extract_between_logs(file_path, start_log_pattern, end_log_pattern)



# log_data=r"hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"
# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# col1="""=================================================================================================================
# MO                   administrativeState bandList   cellBarred     cellReservedForOperator nRPCI nRSectorCarrierRef            nRTAC   operationalState ssbFrequency
# ================================================================================================================="""
# def extract1( file_path,log_data):#log_data
#     with open(file_path, 'r') as file:
#         read = file.read()
#         if log_data in read and col1 in read:
#             print("yrrr")
#             # log_pattern = r'(NRCellDU=\S+)\s+(\S+)\s+(i[1] =\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+'
#             log_pattern = r'(NRCellDU=\S+)\s+(\S+)\s+(i\[\d+\]\s*=\s*\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\[.*\])\s+(\S+)\s+(\S+)\s+(\S+)\s+'
#             matches = re.findall(log_pattern, read, re.MULTILINE)
#             if matches:
#                 print(matches)
#                 columns=['MO', 'administrativeState','bandList','cellBarred ','cellReservedForOperator','nRPCI','nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']
#                 table_data = [list(match) for match in matches]
#                 table_df = pd.DataFrame(table_data, columns=columns)
#                 print("5thlog1",table_df)
#                 # fifthLog=table_df.to_string()
#                 # write_data("fifthLog\n"+fifthLog)

# extract1(file_path, log_data)



# log41 = "hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"
# start_log = """=================================================================================================================
# MO                   nRTAC
# ================================================================================================================="""
# end_log = """NRCellDU=KIE04225A31 1 (UNLOCKED)        i[1] = 71  1 (NOT_BARRED) 1 (NOT_RESERVED)        92    [1] = NRSectorCarrier=6-03-01 3630080 1 (ENABLED)      0
# ================================================================================================================="""
# log_second="""=================================================================================================================
# MO                        administrativeState cellBarred     operationalState primaryPlmnReserved sectorCarrierRef
# ================================================================================================================="""
# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log2="""Added 3 MOs to group: hget_group"""
# def extract_data41(file_path,log41,log2):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         # print(content)

#         if log41 in content:
#             print("iguyg")
#             start_marker = re.escape(start_log)
#             end_marker = re.escape(end_log)

#             match = re.search(f"{start_marker}(.*?){end_marker}", content, re.DOTALL)
#             if match:
#                 data_between_markers = match.group(1).strip()

#                 # Split the data into lines and create a list
#                 data_list = data_between_markers.split("\n")

#                 # Create a pandas DataFrame from the list
#                 df = pd.DataFrame(data_list, columns=["Data"])
#                 print("log41:::\n",df)
                
                
#                 if log2 in df:
#                     print('jhg')
#                     log_pattern = r'(NRCellDU=\S+)\s+(\S+)\s+(i\[\d+\]\s*=\s*\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\[.*\])\s+(\S+)\s+(\S+)\s+(\S+)\s+'
#                     matches = re.findall(log_pattern, df, re.MULTILINE)
#                     if matches:
#                         column_names = ['MO', 'administrativeState', 'bandList', 'cellBarred', 'cellReservedForOperator',
#                                         'nRPCI', 'nRSectorCarrierRef', 'nRTAC', 'operationalState', 'ssbFrequency']
#                         table_data = [list(match) for match in matches]
#                         table_df = pd.DataFrame(table_data, columns=column_names)
#                         print("5thlog",table_df)
#                 # Display the DataFrame
#                 # print("log41:::\n",df)
#                 # fourtysevenLog=df.to_string()
#                 # write_data("fourtysevenLog\n"+fourtysevenLog)
#             else:
#                 print("No match found between markers.")
#         else:
#             print("Log not found in the content.")

# extract_data41(file_path,log41,log2)



# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'

# def extract_between_logs(file_path, start_log_pattern, end_log_pattern):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         start_indices = [match.start() for match in re.finditer(start_log_pattern, content)]
#         end_indices = [match.start() for match in re.finditer(end_log_pattern, content)]

#         for start_idx, end_idx in zip(start_indices, end_indices):
#             section = content[start_idx:end_idx]
#             print("Found relevant section:")
#             # print(section)
#             log_pattern = r'(NRCellDU=\S+)\s+(\S+)\s+(i\[\d+\]\s*=\s*\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\[.*\])\s+(\S+)\s+(\S+)\s+(\S+)'
#             # log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
#             matches = re.findall(log_pattern, section)
            
#             if matches:
#                 columns = ['MO', 'administrativeState', 'bandList','cellBarred','cellReservedForOperator','nRPCI','nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']
#                 table_df = pd.DataFrame(matches, columns=columns)
#                 print(table_df)
#             else:
#                 print("No matches found in the section.")
#             # print("=" * 100)

# start_log_pattern = r"""=================================================================================================================
# MO                   administrativeState bandList   cellBarred     cellReservedForOperator nRPCI nRSectorCarrierRef            nRTAC   operationalState ssbFrequency
# ================================================================================================================="""
# end_log_pattern = r""""Added 3 MOs to group: hget_group"""

# extract_between_logs(file_path, start_log_pattern, end_log_pattern)



# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log2 = """hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"""
# log="""=================================================================================================================
# MO                   administrativeState bandList   cellBarred     cellReservedForOperator nRPCI nRSectorCarrierRef            nRTAC   operationalState ssbFrequency
# =================================================================================================================
# NRCellDU=KIE04225A11 1 (UNLOCKED)        i[1] = 71  1 (NOT_BARRED) 1 (NOT_RESERVED)        243   [1] = NRSectorCarrier=6-01-01 3630080 1 (ENABLED)      0
# NRCellDU=KIE04225A21 1 (UNLOCKED)        i[1] = 71  1 (NOT_BARRED) 1 (NOT_RESERVED)        817   [1] = NRSectorCarrier=6-02-01 3630080 1 (ENABLED)      0
# NRCellDU=KIE04225A31 1 (UNLOCKED)        i[1] = 71  1 (NOT_BARRED) 1 (NOT_RESERVED)        92    [1] = NRSectorCarrier=6-03-01 3630080 1 (ENABLED)      0
# ================================================================================================================="""
# def extract_data3(log2, file_path):
#     with open(file_path, 'r') as file:
#         # Read the whole file as a string
#         read = file.read()

#     if log2 in read and log in read:
#         # Use regular expression to find the table data
#         # table_pattern = r"(?m)^SectorEquipmentFunction=(.*?)\s+(\d+ \(.*?)\s+(\d+)\s+(\d+ \(.*?)\s*=\s+(NRSectorCarrier=.*?)$"
#         table_pattern = r"(NRCellDU=\S+)\s+(\S+)\s+(i\[\d+\]\s*=\s*\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\[.*\])\s+(\S+)\s+(\S+)\s+(\S+)"
         
#         table_matches = re.findall(table_pattern, read)

#         # If table data is found
#         if table_matches:
#             # Create a DataFrame with the desired columns
#             columns_to_keep = ['MO', 'administrativeState', 'bandList', 'cellBarred', 'cellReservedForOperator','nRPCI','nRSectorCarrierRef','nRTAC','operationalState','ssbFrequency']
#             table_data = [list(match) for match in table_matches]
#             table_df = pd.DataFrame(table_data, columns=columns_to_keep)

#             print("log2==::\n", table_df)
#             # nineLog=table_df.to_string()
#             # write_data("nineLog\n"+nineLog)

#         else:
#             raise ValueError("Unable to find the table data in the file.")

# # Call the function to extract and parse data.
# try:
#     extract_data3(log2, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print(f"An error occurred: {e}")




if __name__ == ("__main__"):
    app.run(debug=True,port=2020)


#############################5th log

# log_data=r"hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell)"

# def extract1( log_pattern):#log_data
#     matches = re.findall(log_pattern, log_data, re.MULTILINE)
#     return matches
# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log_pattern = r'^NRCellCU=(\w+)\s+(\d+)'

# with open(file_path, 'r') as file:
#     log_data = file.read()
# matches = extract1( log_pattern)#log_data,
# if not matches:
#     print("No matches found for the given log pattern.")
# else:
#     data_list = [{'MO': match[0], 'nRTAC': match[1]} for match in matches]
#     extracted_df = pd.DataFrame(data_list)
#     print("Extracted Data:")
#     print(extracted_df)
#     fifthLog=extracted_df.to_string()
#     write_data("fifthlog\n"+fifthLog)


import re
import pandas as pd

# Sample data
data = """
=====================================================================================================================================
FRU   ;LNH    ;BOARD          ;ST ;FAULT ;OPER ;MAINT ;STAT ;PRODUCTNUMBER   ;REV     ;SERIAL        ;DATE     ;PMTEMP ; TEMP ; UPT ;SW                  ;
=====================================================================================================================================
BB-01 ;000100 ;BB6630         ; 1 ;  OFF ;  ON ;  OFF ;  ON ;KDU137848/11    ;R3B     ;B070261927    ;20200502 ;3 (OK) ;      ;16.5 ;                    ;
6-01  ;BXP_2  ;RRU4449B71B85A ; 1 ;  OFF ;  ON ;  OFF ; N/A ;KRC161756/1     ;R1F     ;CF88567144    ;20210128 ;4 (OK) ; 56.0 ;16.5 ;CXP9013268%15_R94JK ; (Radio4449B71B85A)
6-02  ;BXP_3  ;RRU4449B71B85A ; 1 ;  OFF ;  ON ;  OFF ; N/A ;KRC161756/1     ;R1F     ;CF87909749    ;20200620 ;4 (OK) ; 51.0 ;16.5 ;CXP9013268%15_R94JK ; (Radio4449B71B85A)
6-03  ;BXP_4  ;RRU4449B71B85A ; 1 ;  OFF ;  ON ;  OFF ; N/A ;KRC161756/1     ;R1F     ;CF87910986    ;20200620 ;4 (OK) ; 51.0 ;16.5 ;CXP9013268%15_R94JK ; (Radio4449B71B85A)
"""

# Define the regular expression pattern to extract rows of data
table_pattern = r'^([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;([^;]+)\s*;$'

# Find all matching lines in the data
table_matches = re.findall(table_pattern, data, re.MULTILINE)

if table_matches:
    # Create a list of column names
    columns = [
        'FRU', 'LNH', 'BOARD', 'ST', 'FAULT', 'OPER', 'MAINT', 'STAT', 'PRODUCTNUMBER', 'REV',
        'SERIAL', 'DATE', 'PMTEMP', 'TEMP', 'UPT', 'SW'
    ]

    # Create a DataFrame for the table
    table_df = pd.DataFrame(table_matches, columns=columns)

    # Display the DataFrame for the table
    print(table_df)
else:
    print("No matching table data found.")
