from flask import Flask,request,jsonify
from werkzeug.utils import secure_filename
import os
import re
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def hello_world():
    if request.method == "POST":
        file= request.files["filename"]

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('C:/Users/LENOVO/Desktop/dataframework/uploads', filename))
            return jsonify({'message': 'File uploaded successfully'})
        return jsonify({'error': 'Error uploading the file'})

    return file


file_path= "C:/Users/LENOVO/Desktop/dataframework/uploads/MIE04225A_PreCheck_MMBBscriptrun.log" 
# folder_name = "find_data"
def count_line(file_path):
    df = pd.read_table(file_path)
    # output_file_path = os.path.join(folder_name, "data.txt")
    # df.append(output_file_path)
    print(df)


count_line(file_path)

def parse_data(file_path, phrase):
    index_numbers = []
    total_occurrences = 0

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if phrase in line:
                total_occurrences += 1
                index_numbers.append(line_number)

    data = {
        'Index Number': index_numbers
    }
    df = pd.DataFrame(data)

    # print("Total occurrences of '{}': {}".format(phrase, total_occurrences))
    # print("Index numbers where '{}' is present:".format(phrase))

    print(f"Total occurrences of {phrase} : {total_occurrences}")
    print(f"Index numbers where {phrase} is present:")
    print(df)


phrase="MIE04225A>"
parse_data(file_path, phrase)

###############################################################################################
def extract_data_between_phrases(file_path, phrase):
    index_numbers = []
    data_between_phrases = []

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if phrase in line:
                index_numbers.append(line_number)

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for start, end in zip(index_numbers, index_numbers[1:] + [len(lines) + 1]):
            data_between_phrases.extend(lines[start - 1:end - 1])

    return data_between_phrases


phrase = "MIE04225A>"


phrase_data = extract_data_between_phrases(file_path, phrase)
# print(phrase_data)
folder_name = "find_data"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
output_file_path = os.path.join(folder_name, "find_data.txt")
with open(output_file_path, "w") as output_file:
    for line in phrase_data:
        output_file.write(line.strip() + "\n")

print("Data has been saved to 'find_data/find_data.txt'",line)
#############################################################################################

extracted_path=os.path.join(os.getcwd(),"all_data","test.log")
f=open( extracted_path,"a+")
def write_data(data):
    

    # f.write(data)
    f.write(data + "\n")
write_data("data")
    # f.close()
# for i in range(10):
#     write_data("")



#################===== 1 #####################

log_pattern = 'get ^ManagedElement= ^managedElementType$ > $MEId'
def log_data(file_path,log_pattern):

    with open(file_path, 'r') as file:
        log_data = file.read()
        # if log_pattern in file_path:

        pattern = r'^ManagedElement=(\w+)\s+managedElementType\s+(\w+)'

        matches = re.findall(pattern, log_data, re.MULTILINE)

        extracted_df = pd.DataFrame(matches, columns=['ManagedElement', 'managedElementType'])
        first_log_data =extracted_df.to_string()
        print(first_log_data)
        write_data("first_log\n"+first_log_data)
log_data(file_path, log_pattern)



#######=====2222

log_pattern1 = 'get DateAndTime='
def log_data1(file_path, log_pattern):
    with open(file_path, 'r') as file:
        log_data = file.read()
    escaped_pattern = re.escape(log_pattern)
    pattern = rf'{escaped_pattern}.*?localDateTime\s+(\d{{4}}-\d{{2}}-\d{{2}}T\d{{2}}:\d{{2}}:\d{{2}})'
    matches = re.findall(pattern, log_data, re.DOTALL)
    extracted_df = pd.DataFrame(matches, columns=['localDateTime'])
    print(extracted_df)
    secondLog=extracted_df.to_string()
    write_data("secondLog\n"+secondLog)
log_data1(file_path, log_pattern1)

####

####################### log3   correct code ######################################


# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# lg_d = "alt"

# def extract_data1(lg_d, file_path):
#     with open(file_path, 'r') as file:
#         # Read the whole file as a string
#         read = file.read()

#     if lg_d in read:
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
#             thirdLog=table_df.to_string()
#             write_data("thirdLog\n"+thirdLog)
            

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



file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'

def extract_between_logs(file_path, start_log_pattern, end_log_pattern):
    with open(file_path, 'r') as file:
        content = file.read()
        start_indices = [match.start() for match in re.finditer(start_log_pattern, content)]
        end_indices = [match.start() for match in re.finditer(end_log_pattern, content)]

        for start_idx, end_idx in zip(start_indices, end_indices):
            section = content[start_idx:end_idx]
            print("Found relevant section:")
            # print(section)
            
            log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
            matches = re.findall(log_pattern, section)
            
            if matches:
                columns = ['Date & Time (UTC)', 'S Specific Problem', 'MO (Cause/AdditionalInfo)']
                table_df = pd.DataFrame(matches, columns=columns)
                print(table_df)
            else:
                print("No matches found in the section.")
            # print("=" * 100)

start_log_pattern = r'MIE04225A> alt'
end_log_pattern = r'>>> Total: \d+ Alarms \(\d Critical, \d Major\)'

extract_between_logs(file_path, start_log_pattern, end_log_pattern)

####################################################################################


################=====4444444
log_pattern4 = 'get (^ENodeBFunction=1$|^GNBDUFunction=) ^gNBId$|^gNBIdLength$|^eNBId$'

def log_data3(file_path, log_pattern4):
    with open(file_path, 'r') as file:
        log_data = file.read()

    escaped_pattern = re.escape(log_pattern4)

    pattern = r'{}.*?gNBId\s+(\d+).*?gNBIdLength\s+(\d+)'.format(escaped_pattern)

    matches = re.findall(pattern, log_data, re.DOTALL)

    extracted_df = pd.DataFrame(matches, columns=['gNBId', 'gNBIdLength'])

    print("4log",extracted_df)
    fourthLog=extracted_df.to_string()
    write_data("fourthLog\n"+fourthLog)

log_data3(file_path, log_pattern4)



  
#############################5th log ####################################################



log_data=r"hget (^EUtranCellTDD=|^EUtranCellFDD=|^NbIotCell=|^NRcell) ^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
col="""=================================================================================================================
MO                   nRTAC
================================================================================================================="""
def extract1( file_path,log_data):#log_data
    with open(file_path, 'r') as file:
        read = file.read()
        if log_data in read and col in read:
            print("yrrr")
            # log_pattern = r'^NRCellCU=(\w+)\s+(\d+)'
            log_pattern = r'^NRCellCU=(\w+)\s+(\d{7})'
            matches = re.findall(log_pattern, read, re.MULTILINE)
            if matches:
                # print(matches)
                columns=['MO', 'nRTAC']
                table_data = [list(match) for match in matches]
                table_df = pd.DataFrame(table_data, columns=columns)
                print("5thlog",table_df)
                fifthLog=table_df.to_string()
                write_data("fifthLog\n"+fifthLog)

extract1(file_path, log_data)
# # ##############################################



# # ######## 6th log
# log_data=r"^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef"
# def extract_data( log_pattern):#log_data
#     matches = re.findall(log_pattern, log_data, re.MULTILINE)
#     return matches
# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log_pattern =  r'NRCellDU=(\w+)\s+(\d+)\s+i\[2\]\s+=\s+(\d+)\s+(\d+)\s+(\d+)\s+\(NOT_BARRED\)\s+(\d+)\s+\(NOT_RESERVED\)\s+(\d+)\s+\[\d+\]\s+=\s+NRSectorCarrier=(\S+)\s+(\d+)\s+\d+\s+\(ENABLED\)\s+(\d+)'

# with open(file_path, 'r') as file:
#     log_data = file.read()
# matches = extract_data( log_pattern)#log_data,
# if not matches:
#     print("No matches found for the given log pattern.")
# else:
#     for match in matches:
#         print(match)
#     extracted_df = pd.DataFrame(data_list)
#     print("Extracted Data:")
#     print(extracted_df)





def extract(log_data, column_names):
    lines = log_data.strip().split('\n')
    data_list = []
    is_data_started = False

    for line in lines:
        if line.startswith("MO "):
            is_data_started = True
            continue

        if is_data_started:
            row_data = re.findall(r'\S+', line)
            if len(row_data) == len(column_names):
                data_list.append(dict(zip(column_names, row_data)))

    return data_list

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log_data= "^administrativeState$|^operationalState$|^cellBarred$|^primaryPlmnReserved$|sectorCarrierRef"

with open(file_path, 'r') as file:
    log_data = file.read()

column_names = ['MO', 'administrativeState', 'bandList', 'cellBarred', 'cellReservedForOperator',
                'nRPCI', 'nRSectorCarrierRef', 'nRTAC', 'operationalState', 'ssbFrequency']

extracted_data = extract(log_data, column_names)

if not extracted_data:
    print("No matches found for the given log pattern.")
else:
    extracted_df = pd.DataFrame(extracted_data)
    print("Extracted Data:")
    print("6thlog",extracted_df)
    sixthLog=extracted_df.to_string()
    write_data("sixthlog1\n"+sixthLog)

    # output_file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/extracted_data.xml'
    # extracted_df.to_csv(output_file_path, index=False)
    # print(f"Extracted data saved to {output_file_path}")
    # fifthLog=extracted_df.to_string()
    # write_data("fifthlog\n"+fifthLog)

################################################################


# import re

# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log_pattern = r'\$\|cellReservedForOperator\|nCGI\|nRPCI\|nRTAC\|ssbfrequency\$\|\^bandList\$\s*'
# column_names_to_check = ['MO', 'administrativeState', 'cellBarred', 'operationalState', 'primaryPlmnReserved', 'sectorCarrierRef']

# with open(file_path, 'r') as file:
#     log_data = file.read()

# # Search for the log pattern in the file
# matches = re.search(log_pattern, log_data)

# if matches:
#     print("Log pattern found in the file.")
    
#     # Check if all the columns are present in the file
#     for column_name in column_names_to_check:
#         if column_name not in log_data:
#             print(f"Column '{column_name}' is missing in the file.")
# else:
#     print("Log pattern not found in the file.")

############################################  7th Log #############

def extract_data(log_data, column_names):

    # print(log_data, column_names)
    lines = log_data.strip().split('\n')
    data_list = []
    is_data_started = False

    for line in lines:
        if line.startswith("MO "):
            is_data_started = True
            continue

        if is_data_started:
            row_data = re.findall(r'\S+', line)
            if len(row_data) == len(column_names):
                data_list.append(dict(zip(column_names, row_data)))

    return data_list

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log_data_A = "$|cellReservedForOperator|nCGI|nRPCI|nRTAC|ssbfrequency$|^bandList$"

with open(file_path, 'r') as file:
    log_data_var = file.read()


if log_data_A in log_data_var:

    column_names = ['MO', 'administrativeState', 'cellBarred', 'operationalState',
                    'primaryPlmnReserved', 'sectorCarrierRef']

    extracted_data = extract_data(log_data_var, column_names)

    if not extracted_data:
        print("No matches found for the given log pattern.")
    else:
        extracted_df = pd.DataFrame(extracted_data)
        print("Extracted Data:")
        print(extracted_df)
        seventhLog=extracted_df.to_string()
    write_data("seventhLog\n"+seventhLog)
else:
    print("Log pattern not found in the file.")


 
######################===== 888888===========#######################

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log1 = "administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"

def extract_data2(log1, file_path):
    with open(file_path, 'r') as file:
        # Read the whole file as a string
        read = file.read()

        # Use regex to find the table header
        header_pattern = r"MO\s+administrativeState\s+arfcn\s*DL\s+arfcn\s*UL\s+bSChannelBw\s*DL\s+bSChannelBw\s*UL\s+configuredMaxTxPower\s+operationalState\s+reservedBy"
        header_match = re.search(header_pattern, read)

        if header_match:
            header_start = header_match.start()
            header_end = header_match.end()

            # Use regex to find the table data
            data_pattern = r"NRSectorCarrier=\S+\s+([^\n]+)"
            data_matches = re.findall(data_pattern, read[header_end:])

            if data_matches:
                # Extracted table data as a list of strings
                table_data_str = data_matches

                # Create a DataFrame with the desired columns
                columns_to_keep = ['MO', 'administrativeState', 'arfcnDL', 'arfcnUL', 'bSChannelBwDL', 'bSChannelBwUL', 'configuredMaxTxPower', 'operationalState', 'reservedBy']
                table_data = [re.split(r'\s{2,}', row.strip(), maxsplit=len(columns_to_keep)-1) for row in table_data_str]

                # Check if the number of columns in the data matches the expected number of columns
                num_columns_in_data = len(table_data[0])
                if num_columns_in_data < len(columns_to_keep):
                    # Append None values for the missing columns
                    num_missing_columns = len(columns_to_keep) - num_columns_in_data
                    for i in range(num_missing_columns):
                        for row in table_data:
                            row.append(None)

                table_df = pd.DataFrame(table_data, columns=columns_to_keep)

                # Clean up the DataFrame columns
                table_df['administrativeState'] = table_df['administrativeState'].str.extract(r'(\d+)')
                table_df['arfcnDL'] = table_df['arfcnDL'].str.extract(r'(\d+)')
                table_df['arfcnUL'] = table_df['arfcnUL'].str.extract(r'(\d+)')
                table_df['bSChannelBwDL'] = table_df['bSChannelBwDL'].str.extract(r'(\d+)')
                table_df['bSChannelBwUL'] = table_df['bSChannelBwUL'].str.extract(r'(\d+)')
                table_df['configuredMaxTxPower'] = table_df['configuredMaxTxPower'].str.extract(r'(\d+)')
                table_df['operationalState'] = table_df['operationalState'].str.extract(r'(\d+)')

                print("log1::\n", table_df)
                eightLog=table_df.to_string()
                write_data("eightLog\n"+eightLog)
            else:
                raise ValueError("Unable to find the table data in the file.")
        else:
            raise ValueError("Unable to find the table header in the file.")

# Call the function to extract and parse data.
try:
    extract_data2(log1, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An error occurred: {e}")




#############====9999999999999###############################

# log2= "administrativeState|operationalState|availableHwOutputPower|reservedBy"
# file_path= 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# def extract_data3(log2, file_path):
#     with open(file_path, 'r') as file:
#         # Read the whole file as a string
#         read = file.read()
#         if log2 in log2:
#             columns=["MO", "administrativeState", "availableHwOutputPower", "operationalState", "reservedBy " ]
#             if all(column in read for column in columns):
#                 print("The log and all columns are present in the file.")
        

# extract_data3(log2, file_path)


import re
import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log2 = "administrativeState|operationalState|availableHwOutputPower|reservedBy"

def extract_data3(log2, file_path):
    with open(file_path, 'r') as file:
        # Read the whole file as a string
        read = file.read()

    if log2 in read:
        # Use regular expression to find the table data
        # table_pattern = r"(?m)^SectorEquipmentFunction=(.*?)\s+(\d+ \(.*?)\s+(\d+)\s+(\d+ \(.*?)\s*=\s+(NRSectorCarrier=.*?)$"
        table_pattern = r"(?m)^SectorEquipmentFunction=(.*?)\s+(\d+ \(.*?)\s+(\d+)\s+(\d+ \(.*?)\s*=\s+(NRSectorCarrier=.*?)$"
         
        table_matches = re.findall(table_pattern, read)

        # If table data is found
        if table_matches:
            # Create a DataFrame with the desired columns
            columns_to_keep = ['MO', 'administrativeState', 'availableHwOutputPower', 'operationalState', 'reservedBy']
            table_data = [list(match) for match in table_matches]
            table_df = pd.DataFrame(table_data, columns=columns_to_keep)

            print("log2==::\n", table_df)
            nineLog=table_df.to_string()
            write_data("nineLog\n"+nineLog)

        else:
            raise ValueError("Unable to find the table data in the file.")

# Call the function to extract and parse data.
try:
    extract_data3(log2, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An error occurred: {e}")




# import re
# import pandas as pd

# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# lg_d = "administrativeState|operationalState|availableHwOutputPower|reservedBy"

# def extract_data1(lg_d, file_path):
#     with open(file_path, 'r') as file:
#         # Read the whole file as a string
#         read = file.read()

#     if lg_d in read:
#         # Use regular expression to find the table data
#         table_pattern = r"(?m)^SectorEquipmentFunction=(.*?)\s+(\d+ \(.*?)\s+(\d+)\s+(\d+ \(.*?)\s*=\s+(NRSectorCarrier=.*?)$"

#         table_matches = re.findall(table_pattern, read)

#         # If table data is found
#         if table_matches:
#             # Create lists to store data for each column
#             mo_list = []
#             administrativeState_list = []
#             availableHwOutputPower_list = []
#             operationalState_list = []
#             reservedBy_list = []

#             for match in table_matches:
#                 mo_list.append(match[0].strip())
#                 administrativeState_list.append(match[1].strip())
#                 availableHwOutputPower_list.append(match[2].strip())
#                 operationalState_list.append(match[3].strip())
#                 reservedBy_list.append(match[4].strip())

#             # Create a DataFrame with the extracted data
#             table_data = {
#                 'MO': mo_list,
#                 'administrativeState': administrativeState_list,
#                 'availableHwOutputPower': availableHwOutputPower_list,
#                 'operationalState': operationalState_list,
#                 'reservedBy': reservedBy_list
#             }

#             table_df = pd.DataFrame(table_data)

#             print("table_df==\n", table_df)

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



##################### ====10101010############################


# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log3 = "hget (^FieldReplaceableUnit=|^AuxPlugInUnit=|^PlugInUnit=) administrativeState|operationalstate|product|isshared"

# def extract_data4(log3, file_path):
#     with open(file_path, 'r') as file:
#         # Read the whole file as a string
#         read = file.read()

#     if log3 in read:
#         print("yes")
#         table_pattern = r"(?m)^FieldReplaceableUnit=(.*?)\s+(\d+ \([^)]*\))\s+(\w+)\s+(\w+)\s+(.*)\s+(\d+)\s+(\w+)$"
#         # table_pattern = r"^FieldReplaceableUnit=(.*?)\s+(\d+ \(.*?)\s+(\w*)\s+(\w+)\s+(.*)\s+(\d+)\s+(\w+)$"
#         # table_pattern = r"^FieldReplaceableUnit=(.*?)\s+(\d+ \(.*?)\s+(\w*)\s+(\w+)\s+(.*)\s+(\d+)\s+(\w+)$"
#         # table_pattern = r"(?m)^FieldReplaceableUnit=(.*?)\s+(\d+ \(.*?)\s+(\w*)\s+(\d+ \(.*?)\s+(\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+)\s+(\w+)?\s*(\w*)?\s+(\d+)?$"
#         # table_pattern = r"(?m)^FieldReplaceableUnit=(.*?)\s+(\d+ \(.*?)\s+(\w*)\s+(\d+ \(.*?)\s+(\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+)\s+(\w+)?\s*(\w*)?\s+(\d+)?$"
#         table_matches = re.findall(table_pattern, read)
#         # table_matches = re.search(table_pattern, read)
#         print("lkjj",table_matches)

#         # If table data is found
#         if table_matches:
#             print("yes22")
#             # Create a DataFrame with the desired columns
#             columns_to_keep = ['MO', 'administrativeState', 'isSharedWithExternalMe', 'operationalState', 'productName', 'productNumber', 'productRevision', 'productionDate', 'serialNumber']
#             table_data = [list(match) for match in table_matches]
#             table_df = pd.DataFrame(table_data, columns=columns_to_keep)

#             print("log3==::\n", table_df)

#         else:
#             raise ValueError("Unable to find the table data in the file.")

# # Call the function to extract and parse data.
# try:
#     extract_data4(log3, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print(f"An error occurred: {e}")





# import re
# import pandas as pd

# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log3 = "hget (^FieldReplaceableUnit=|^AuxPlugInUnit=|^PlugInUnit=) administrativeState|operationalstate|product|isshared"

# def extract_data4(log3, file_path):
#     with open(file_path, 'r') as file:
#         # Read the whole file as a string
#         read = file.read()

#     if log3 in read:
#         # table_pattern = r"(?m)^FieldReplaceableUnit=(.*?)\s+(\d+ \([^)]*\))\s+(\w+)\s+(\w+)\s+(.*?)\s+(\d+)\s+(\w+)\s+(\w+)\s+(\w+)$"
#         table_pattern = r"(?m)^FieldReplaceableUnit=(.*?)\s+(\d+ \([^)]*\))\s+(\w+)\s+(\w+)\s+(.*)\s+(\d+)\s+(\w+)$"
#         table_matches = re.findall(table_pattern, read)
#         print("ldkjekej/n",table_matches)

#         # If table data is found
#         if table_matches:
#             # Create a DataFrame with the desired columns
#             columns_to_keep = ['MO', 'administrativeState', 'isSharedWithExternalMe', 'operationalState', 'productName', 'productNumber', 'productRevision', 'productionDate', 'serialNumber']
#             table_data = [list(match) for match in table_matches]
#             print("jiuidq",table_data)
#             table_df = pd.DataFrame(table_data, columns=columns_to_keep)
#             print("Extracted data:\n", table_df)

#         else:
#             raise ValueError("Unable to find the table data in the file.")

# # Call the function to extract and parse data.
# try:
#     extract_data4(log3, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print(f"An error occurred: {e}")





# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log3 = "hget (^FieldReplaceableUnit=|^AuxPlugInUnit=|^PlugInUnit=) administrativeState|operationalstate|product|isshared"

# def extract_data4(log3, file_path):
#     with open(file_path, 'r') as file:
#         # Read the whole file as a string
#         read = file.read()

#     if log3 in read:
#         print("yes")
#         table_pattern = r"(FieldReplaceableUnit=[\w-]+)\s+(\d\s+\(\w+\))\s+(\w+)\s+(\d\s+\(\w+\))\s+(.*?)\s+(\d+)\s+(\w+)"
#         table_matches = re.findall(table_pattern, read)
#         print("matches", table_matches)

#         # If table data is found
#         if table_matches:
#             print("yes22")
#             # Create a DataFrame with the desired columns
#             columns_to_keep = ['MO', 'administrativeState', 'isSharedWithExternalMe', 'operationalState', 'productName', 'productNumber', 'productRevision']
#             table_data = [list(match) for match in table_matches]
#             table_df = pd.DataFrame(table_data, columns=columns_to_keep)

#             # Additional columns present in the file but not required based on the given query
#             # Remove them from the DataFrame
#             table_df.drop(columns=['productName', 'productNumber', 'productRevision'], inplace=True)

#             # Rename the remaining columns to match the desired output
#             table_df.rename(columns={
#                 'MO': 'FieldReplaceableUnit',
#                 'administrativeState': 'administrativeState (UNLOCKED/LOCKED)',
#                 'isSharedWithExternalMe': 'isShared',
#                 'operationalState': 'operationalState (ENABLED/DISABLED)'
#             }, inplace=True)

#             print("log3==::\n", table_df)

#         else:
#             raise ValueError("Unable to find the table data in the file.")

# # Call the function to extract and parse data.
# try:
#     extract_data4(log3, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print(f"An error occurred: {e}")



# import re
# import pandas as pd

# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log3 = "hget (^FieldReplaceableUnit=|^AuxPlugInUnit=|^PlugInUnit=) administrativeState|operationalstate|product|isshared"

# def extract_data4(log3, file_path):
#     with open(file_path, 'r') as file:
#         # Read the whole file as a string
#         read = file.read()

#     if log3 in read:
#         print("yes")
#         table_pattern = r"(FieldReplaceableUnit=[\w-]+)\s+(\d\s+\(\w+\))\s+(false|true)\s+(\d\s+\(\w+\))\s+(.*)\s+(\d+)\s+(\w+)"
#         table_matches = re.findall(table_pattern, read)

#         # If table data is found
#         if table_matches:
#             print("yes22")
#             # Create a DataFrame with the desired columns
#             columns_to_keep = ['FieldReplaceableUnit', 'administrativeState', 'isShared', 'operationalState', 'productName', 'productNumber', 'productRevision', 'productionDate', 'serialNumber']
#             table_data = [list(match) for match in table_matches]
#             table_df = pd.DataFrame(table_data, columns=columns_to_keep)

#             # Convert data types for specific columns
#             table_df['administrativeState'] = table_df['administrativeState'].str.extract(r'(\w+)').astype(int)
#             table_df['isShared'] = table_df['isShared'].map({'false': False, 'true': True})
#             table_df['operationalState'] = table_df['operationalState'].str.extract(r'(\w+)').astype(int)
#             table_df['productNumber'] = table_df['productNumber'].str.extract(r'(\w+)').astype(str)
#             table_df['productionDate'] = pd.to_datetime(table_df['productionDate'], format='%Y%m%d')

#             print("log3==::\n", table_df)

#         else:
#             raise ValueError("Unable to find the table data in the file.")

# # Call the function to extract and parse data.
# try:
#     extract_data4(log3, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print(f"An error occurred: {e}")


import re
import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log3 = "hget (^FieldReplaceableUnit=|^AuxPlugInUnit=|^PlugInUnit=) administrativeState|operationalstate|product|isshared"

def extract_data4(log3, file_path):
    with open(file_path, 'r') as file:
        
        read = file.read()

    if log3 in read:
        print("yes")
        table_pattern = r"(FieldReplaceableUnit=[\w-]+)\s+(\d\s+\(\w+\))\s+(false|true)\s+(\d\s+\(\w+\))\s+(.*)"
        table_matches = re.findall(table_pattern, read)

       
        if table_matches:
            print("yes22")
            # Create a DataFrame with the desired columns
            columns_to_keep = ['FieldReplaceableUnit', 'administrativeState', 'isShared', 'operationalState', 'productName']
            table_data = [list(match) for match in table_matches]
            table_df = pd.DataFrame(table_data, columns=columns_to_keep)

            # Convert data types for specific columns
            table_df['administrativeState'] = table_df['administrativeState'].str.extract(r'(\w+)').astype(int)
            table_df['isShared'] = table_df['isShared'].map({'false': False, 'true': True})
            table_df['operationalState'] = table_df['operationalState'].str.extract(r'(\w+)').astype(int)

            # Split productName into productNumber, productRevision, productionDate, and serialNumber
            product_details = table_df['productName'].str.extract(r'(.*)\s+(\w+\s+\w+)\s+(\d+)\s+(\w+)$')
            table_df['productName'] = product_details[0]
            table_df['productNumber'] = product_details[1]
            table_df['productRevision'] = product_details[2]
            table_df['productionDate'] = product_details[3]
            table_df.drop(columns=['productName'], inplace=True)

            # Convert productionDate to datetime
            table_df['productionDate'] = pd.to_datetime(table_df['productionDate'], format='%Y%m%d')

            print("log3==::\n", table_df)
            tenthLog=table_df.to_string()
            write_data("tenthLog\n"+tenthLog)

        else:
            raise ValueError("Unable to find the table data in the file.")

# Call the function to extract and parse data.
try:
    extract_data4(log3, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An error occurred: {e}")
##################################################################################


########====11111111   correct ######################################




import re
import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log4 = "hget rilink RiLinkId|linkRate|operationalState|riPortRef1|riPortRef2"

def extract_data5(log4, file_path):
    with open(file_path, 'r') as file:
        # Read the whole file as a string
        read = file.read()

    if log4 in read:
        # Use regular expression to find the table data
        table_pattern = r"RiLink=(.*?)\s+(\d+)\s+(\d \(.*?)\)\s+(.*?)\s+FieldReplaceableUnit=(.*?)\s+FieldReplaceableUnit=(.*?)$"

        table_matches = re.findall(table_pattern, read, re.MULTILINE)

        # If table data is found
        if table_matches:
            # Create a DataFrame with the desired columns
            columns_to_keep = ['MO', 'linkRate', 'operationalState', 'riLinkId', 'riPortRef1', 'riPortRef2']
            table_df = pd.DataFrame(table_matches, columns=columns_to_keep)

            print("log4==::\n", table_df)
            eleventhLog=table_df.to_string()
            write_data("eleventhLog\n"+eleventhLog)

        else:
            raise ValueError("Unable to find the table data in the file.")

# Call the function to extract and parse data.
try:
    extract_data5(log4, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An error occurred: {e}")

####################################################################################

###########=====121212   may be correct#######################################

# import re
# import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log5="hget sfp prod"
def extract_sfp_data(file_path):
    with open(file_path, 'r') as file:
        # Read the whole file as a string
        read = file.read()

        if log5 in read:
            print("kjjh")
        # Use regular expression to find the table data

            table_pattern = r"(FieldReplaceableUnit=.*?)\s+FTLX1370W4BTL(-E7)?\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)$"

            table_matches = re.findall(table_pattern, read, re.MULTILINE)

    # If table data is found
        if table_matches:
            # Create a DataFrame with the desired columns
            columns_to_keep = ['MO', 'manufacturerDesignation', 'manufacturerId', 'manufacturerRevision',
                            'negotiatedBitRate', 'productNumber', 'productRevision', 'productionDate', 'serialNumber']
            table_df = pd.DataFrame(table_matches, columns=columns_to_keep)

            print("SFP Data:\n", table_df)
            twelveLog=table_df.to_string()
            write_data("twelveLog\n"+twelveLog)

        else:
            raise ValueError("Unable to find the table data in the file.")

# Call the function to extract and parse data.
try:
    extract_sfp_data(file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An error occurred: {e}")




# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log6 = "hget sfp prod"

# def extract_data6(log6, file_path):
#     with open(file_path, 'r') as file:
#         # Read the whole file as a string
#         read = file.read()

#     if log6 in read:
#         print("ndwjwwi")
#         # Use regular expression to find the table data
#         table_pattern = r"(FieldReplaceableUnit=(.*?)\s*,\s*SfpModule=(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s*?$)"

#         table_matches = re.findall(table_pattern, read, re.MULTILINE)

#         # If table data is found
#         if table_matches:
#             # Create a DataFrame with the desired columns
#             columns_to_keep = ['MO', 'manufacturerDesignation', 'manufacturerId', 'manufacturerRevision',
#                                'negotiatedBitRate', 'productNumber', 'productRevision', 'productionDate', 'serialNumber']

#             table_data = []
#             for match in table_matches:
#                 row_data = list(match[1:])
#                 table_data.append(row_data)

#             table_df = pd.DataFrame(table_data, columns=columns_to_keep)

#             print("log6:::\n", table_df)
#             # twelthLog=table_df.to_string()
#             # write_data("twelthLog\n"+twelthLog)
#             # output_file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/log5.txt'
#             # table_df.to_xml(output_file_path, index=False)

#         else:
#             raise ValueError("Unable to find the table data in the file.")
        

# # Call the function to extract and parse data.
# try:
#     extract_data(log6, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print(f"An error occurred: {e}")



############ ==========131313131 correct ##########################################

import re
import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log7 = "hget (^TermPointToMme=|^TermPointToAmf=) ^ipAddress1$|^ipAddress2$|^ipv4Address1$|^ipv4Address2$|^administrativeState$|^operationalState$"

def extract_data7(log7, file_path):
    with open(file_path, 'r') as file:
        # Read the whole file as a string
        read = file.read()

    if log7 in read:
        # Use regular expression to find the table data
        table_pattern = r"(TermPointToAmf=.*?)\s+(\d+ \(.*?)\s+([\d.]+)\s+([\d.]+)\s+(\d+ \(.*?)$"

        table_matches = re.findall(table_pattern, read, re.MULTILINE)

        # If table data is found
        if table_matches:
            # Create a DataFrame with the desired columns
            columns_to_keep = ['MO', 'administrativeState', 'ipv4Address1', 'ipv4Address2', 'operationalState']
            table_data = [list(match) for match in table_matches]
            table_df = pd.DataFrame(table_data, columns=columns_to_keep)

            print("log7:\n", table_df)
            thirteenLog=table_df.to_string()
            write_data("thirteenLog\n"+thirteenLog)

        else:
            raise ValueError("Unable to find the table data in the file.")

# Call the function to extract and parse data.
try:
    extract_data7(log7, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An error occurred: {e}")
###################################################################################################################

######################=========== 14141414########################################

import re
import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log8 = "hget ^VlanPort= vlanId|encapsulation|reservedBy"

def extract_data8(log8, file_path):
    with open(file_path, 'r') as file:
        # Read the whole file as a string
        read = file.read()

    if log8 in read:
        # Use regular expression to find the table data
        table_pattern = r"(VlanPort=\w+)\s+(.*?)\s+(.*?)\s+(\d+)\s*$"

        table_matches = re.findall(table_pattern, read, re.MULTILINE)

        # If table data is found
        if table_matches:
            # Create a DataFrame with the desired columns
            columns_to_keep = ['MO', 'encapsulation', 'reservedBy', 'vlanId']
            table_data = [list(match) for match in table_matches]
            table_df = pd.DataFrame(table_data, columns=columns_to_keep)

            print("log8:\n", table_df)
            fourteenLog=table_df.to_string()
            write_data("fourteenLog\n"+fourteenLog)

        else:
            raise ValueError("Unable to find the table data in the file.")

# Call the function to extract and parse data.
try:
    extract_data8(log8, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An error occurred: {e}")

# ############=======15151515151  all code is correct teeno logic sahi hai useful hai###############################################

# import re
# import pandas as pd

# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log9 = "hget ^AddressIPv ^usedAddress$|^address$"

# def extract_data9(log9, file_path):
#     with open(file_path, 'r') as file:
#         read = file.read()
#         # print(read)


#     if log9 in read:
#         # print('mckhv')
#         table_pattern = r"(Router=\w+,[^,]+)\s+([\d./]+)\s+([\d./]+)"
#         # table_pattern = r"(Router=\w+,[^,]+),AddressIPv4=([\d.]+/\d+)\s+([\d.]+/\d+)"
#         # table_matches = re.findall(table_pattern, read, re.MULTILINE)
#         # table_matches = re.findall(table_pattern, read, re.MULTILINE | re.DOTALL)
#         table_matches = re.findall(table_pattern, read, re.MULTILINE | re.IGNORECASE)
        

#         if table_matches:
#             columns_to_keep = ['MO', 'address', 'usedAddress']
#             table_data = [list(match) for match in table_matches]
#             table_df = pd.DataFrame(table_data, columns=columns_to_keep)

#             print("log9::::\n", table_df)
#         else:
#             raise ValueError("Unable to find the table data in the file.")
#     else:
#         print("Log not found in the file.")

# try:
#     extract_data9(log9, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print(f"An error occurred: {e}")


##### ye bhi 15 log ka code correct hai

# import re
# import pandas as pd

# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log9 = "hget ^AddressIPv ^usedAddress$|^address$"

# def extract_data9(log9, file_path):
#     with open(file_path, 'r') as file:
#         read = file.read()

#     if log9 in read:
#         table_pattern = r"(Router=\w+,[^,]+)\s+([\d./]+)\s+([\d./]+)"
#         table_matches = re.findall(table_pattern, read)

#         if table_matches:
#             columns_to_keep = ['MO', 'address', 'usedAddress']
#             table_df = pd.DataFrame(table_matches, columns=columns_to_keep)

#             print("Parsed Data:\n", table_df)
#         else:
#             print("No matching data found.")
#     else:
#         print("Log not found in the file.")

# try:
#     extract_data9(log9, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")

##### ye bhi 15 log ka code correct hai
import re
import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log9 = "hget ^AddressIPv ^usedAddress$|^address$"

def extract_data9(log9, file_path):
    with open(file_path, 'r') as file:
        read = file.read()

    if log9 in read:
        table_pattern = r"MO\s+address\s+usedAddress\n={100,}\n([\s\S]+?)(?:\n{2,}|\Z)"
        match = re.search(table_pattern, read)
        
        if match:
            data_section = match.group(1)
            rows = data_section.strip().split('\n')
            
            columns = ['MO', 'address', 'usedAddress']
            data = [line.split() for line in rows]
            
            table_df = pd.DataFrame(data, columns=columns)
            print("log9:::\n", table_df)
            fifteenLog=table_df.to_string()
            write_data("fifteenLog\n"+fifteenLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data9(log9, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

###########  stop 15 log9 #########################################################################################


###############-======1616161616 log10 correct#####################################################



import re
import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log10 = "lpr router"

def extract_data10(log10, file_path):
    with open(file_path, 'r') as file:
        read = file.read()

    if log10 in read:
        # table_pattern = r"Proxy\s+MO\n={100,}\n([\s\S]+?)(?:\n\n|\Z)"
        table_pattern = r"Proxy\s+MO\n=+\n([\s\S]+?)(?:\n{2,}|\Z)"
        match = re.search(table_pattern, read)
        
        if match:
            data_section = match.group(1)
            rows = data_section.strip().split('\n')
            
            columns = ['Proxy', 'MO']
            data = [line.split(None, 1) for line in rows if line.strip()]
            
            table_df = pd.DataFrame(data, columns=columns)
            print("log10::::\n", table_df)
            sixteenLog=table_df.to_string()
            write_data("thirdLog\n"+sixteenLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data10(log10, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

##################### stop ##16log completed##############################################

#################=======1717171 log11 ###############################################

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log11 = "hget ^TermPointToGNB= ip|administrativeState|operationalState"

def extract_data11(log11, file_path):
    with open(file_path, 'r') as file:
        read = file.read()

    if log11 in read:
        proxy_mo_pattern = r"MO\s+administrativeState\s+ipsecEpAddress\s+ipv4Address\s+ipv6Address\s+operationalState\s+upIpAddress\s+usedIpAddress\n={100,}\n([\s\S]+?)(?:\n{2,}|\Z)"
        proxy_mo_match = re.search(proxy_mo_pattern, read)
        
        if proxy_mo_match:
            proxy_mo_section = proxy_mo_match.group(1)
            lines = proxy_mo_section.strip().split('\n')
            
            data = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 8:
                    data.append(parts)
            
            columns = ['MO', 'administrativeState', 'ipsecEpAddress', 'ipv4Address', 'ipv6Address', 'operationalState', 'upIpAddress', 'usedIpAddress']
            table_df = pd.DataFrame(data, columns=columns)
            
            print("log11::::\n", table_df)
            seventeenLog=table_df.to_string()
            write_data("seventeenLog\n"+seventeenLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data11(log11, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
# ############ stop ############################################################################################

# #######========181818181 log12 ###########################################################################################################

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log12 = "hget ^TermPointToGNodeB= ip|administrativeState|operationalState"

def extract_data12(log12, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    start_index = -1
    end_index = -1
    for idx, line in enumerate(lines):
        if log12 in line:
            start_index = idx + 2
            break
    
    if start_index == -1:
        print("Log not found in the file.")
        return

    for idx in range(start_index, len(lines)):
        if lines[idx].strip() == "":
            end_index = idx
            break

    if end_index == -1:
        end_index = len(lines)

    data = []
    for idx in range(start_index, end_index):
        parts = lines[idx].strip().split()
        if len(parts) == 8:
            data.append(parts)

    columns = ['MO', 'administrativeState', 'ipsecEpAddress', 'ipv4Address', 'ipv6Address', 'operationalState', 'upIpAddress', 'usedIpAddress']
    table_df = pd.DataFrame(data, columns=columns)

    if not table_df.empty:
        print("log12:\n", table_df)
        eighteenLog=table_df.to_string()
        write_data("eighteenLog\n"+eighteenLog)
    else:
        print("No matching data found.")

try:
    extract_data12(log12, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

####################  stop  #######################################


############# =============19191918 log13 #############################################



file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log13 = "sts"

def extract_data13(log13, file_path):
    with open(file_path, 'r') as file:
        # Read the whole file as a string
        read = file.read()

    if log13 in read:
        print('uhuubuh')
        # Extract radioClockState information
        clock_state_pattern = r"radioClockState\s+:\s+(.*?)\n"
        clock_state_match = re.search(clock_state_pattern, read)
        radio_clock_state = clock_state_match.group(1) if clock_state_match else "N/A"

        # Use regular expression to find the table data
        table_pattern = r"\*?(\d+)\s+(\d+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(.*?)\s+\((.*?)\)"
        table_matches = re.findall(table_pattern, read, re.MULTILINE)

        # If table data is found
        if table_matches:
            # Create a DataFrame with the desired columns
            columns_to_keep = ['Prio', 'ST', 'syncRefType', 'refStatus', 'opQualLevel', 'SyncReference', 'Details']
            table_df = pd.DataFrame(table_matches, columns=columns_to_keep)

            # Add radioClockState information to the DataFrame
            table_df['radioClockState'] = radio_clock_state

            print("log13::::\n", table_df)
            ninteenLog=table_df.to_string()
            write_data("ninteenLog\n"+ninteenLog)

        else:
            raise ValueError("Unable to find the table data in the file.")
    else:
        raise ValueError("Log not found in the file.")

# Call the function to extract and parse data.
try:
    extract_data13(log13, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An error occurred: {e}")


########### stop ################################################################################


############### ========== 20202020202 log14 ###################################################

import re
import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log14 = "st sync"

def extract_data14(log14, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log14 in content:
        # Use regex pattern to find the table data
        table_pattern = r"(\d+)\s+([\d\s\(\)A-Z=]+)\s+(\d+\s?\(.*?\))?\s+(.*)$"

        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = ['Proxy', 'Adm State', 'Op. State', 'MO']
            table_df = pd.DataFrame(table_matches, columns=columns)

            print("log14:\n", table_df)
            twentyLog=table_df.to_string()
            write_data("twentyLog\n"+twentyLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

# Call the function to extract and parse data.
try:
    extract_data14(log14, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

################# stop ###############################################################

######################## 212121 log15 all logic is correct ##############################################

# import re
# import pandas as pd

# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log15 = "get . noofsat"

# def extract_data15(log15, file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()

#     if log15 in content:
#         # Use regex pattern to find the table data
#         table_pattern = r"(Synchronization=.*\d)\s+(\w+)\s+(\d+)\s*$"

#         table_matches = re.findall(table_pattern, content, re.MULTILINE)

#         if table_matches:
#             columns = ['MO', 'Attribute', 'Value']
#             table_df = pd.DataFrame(table_matches, columns=columns)

#             # Reformat "MO" column to remove '='
#             table_df['MO'] = table_df['MO'].apply(lambda x: x.split('=')[0].strip())

#             print("log15::::\n", table_df)
#         else:
#             print("No matching data found.")
#     else:
#         print("Log not found in the file.")

# # Call the function to extract and parse data.
# try:
#     extract_data15(log15, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")




# import re
# import pandas as pd

# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log = "get . noofsat"

# def extract_data(log, file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()

#     if log in content:
#         # Use regex pattern to find the table data
#         table_pattern = r"(Synchronization=.*\d)\s+(\w+)\s+(\d+)\s*$"

#         table_matches = re.findall(table_pattern, content, re.MULTILINE)

#         if table_matches:
#             columns = ['MO', 'Attribute', 'Value']
#             table_df = pd.DataFrame(table_matches, columns=columns)

#             # Reformat "MO" column to remove '=' and append 'Synchronization'
#             table_df['MO'] = 'Synchronization ' + table_df['MO'].apply(lambda x: x.split('=')[1].strip())

#             print("Parsed data:\n", table_df)
#         else:
#             print("No matching data found.")
#     else:
#         print("Log not found in the file.")

# # Call the function to extract and parse data.
# try:
#     extract_data(log, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")



# import re
# import pandas as pd

# file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log = "get . noofsat"

# def extract_data(log, file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()

#     if log in content:
#         # Use regex pattern to find the table data
#         table_pattern = r"((?:Synchronization=.*\d)\s+\w+\s+\d+)\s*$"

#         table_matches = re.findall(table_pattern, content, re.MULTILINE)

#         if table_matches:
#             columns = ['MO']
#             table_df = pd.DataFrame(table_matches, columns=columns)

#             print("Parsed data:\n", table_df)
#         else:
#             print("No matching data found.")
#     else:
#         print("Log not found in the file.")

# # Call the function to extract and parse data.
# try:
#     extract_data(log, file_path)
# except FileNotFoundError:
#     print(f"File not found at the specified path: {file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")


######  this is very correct code
import re
import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log15= "get . noofsat"

def extract_data15(log15, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log15 in content:
        
        table_pattern = r"((?:Synchronization=.*\d)\s+\w+\s+\d+)\s*$"

        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = ['MO', 'Attribute', 'Value']
            table_data = [(match.split()[0], match.split()[1], match.split()[2]) for match in table_matches]
            table_df = pd.DataFrame(table_data, columns=columns)

            print("log15:::\n", table_df)
            twentyoneLog=table_df.to_string()
            write_data("twentyoneLog\n"+twentyoneLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data15(log15, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

############################ stop #################################################################################


############ =============22222222 log 16 ###################################

import re
import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log16 = "hget ^RadioEquipmentClockReference= ^administrativeState$|^operationalState$"

def extract_data16(log, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log16 in content:
        # Use regex pattern to find the table data
        table_pattern = r"((Synchronization=.*?ClockReference=\S+)\s+(\d+\s+\(.*?\))\s+(\d+\s+\(.*?\)))\s*$"

        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = ['MO', 'administrativeState', 'operationalState']
            table_data = [(match[1], match[2], match[3]) for match in table_matches]
            table_df = pd.DataFrame(table_data, columns=columns)

            print("log16:::::\n", table_df)
            twentytwoLog=table_df.to_string()
            write_data("twentytwoLog\n"+twentytwoLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

# Call the function to extract and parse data.
try:
    extract_data16(log16, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

############# stop ########################################################################

#############=========232323 log17 #############################################################3
import re
import pandas as pd

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log17 = "get ^RadioEquipmentClock= ^radioClockState$"

def extract_data17(log17, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        

    if log17 in content:
        # Use regex pattern to find the table data
        table_pattern = r"(Synchronization=.*?Clock=\S+)\s+(radioClockState)\s+(\d+\s+\(.*?\))\s*$"

        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = ['MO', 'Attribute', 'Value']
            table_data = [(match[0], match[1], match[2]) for match in table_matches]
            table_df = pd.DataFrame(table_data, columns=columns)

            print("log17:::::\n", table_df)
            twentythreeLog=table_df.to_string()
            write_data("twentythreeLog\n"+twentythreeLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

# Call the function to extract and parse data.
try:
    extract_data17(log17, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
########## stop ###################################################################################

#############=========== 242424242424 log 18 #############################################333


def extract_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        start_marker = "MIE04225A> hpget . pmendcsetupueatt|pmEndcSetupUeSucc|^pmmacvoldl$|^pmmacvolul$|PMMACVOLDLDRB$"
        end_marker = "MIE04225A> st interme|bblink|eran"


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
        print( data_text)
        

        for i,li in enumerate(data_lines):
            
            if(li=="================================================================================================================="):
                print(f"Line index: {i}")
                print(li, "data_lines")

                # if i == 5 :
                table_pattern = r"(NRCellCU=\S+)\s+(\d+)\s+(\d+)\s*$"
                table_matches = re.findall(table_pattern, content, re.MULTILINE)
                if table_matches:
                    columns = ['MO', 'pmEndcSetupUeAtt', 'pmEndcSetupUeSucc']
                    table_df = pd.DataFrame(table_matches, columns=columns)
                    print("log18::::::\n", table_df)
                    twentyfourLog=table_df.to_string()
                    write_data("twentyfourLog\n"+twentyfourLog)

                else:
                    print("No matching data found.") 
                # else:
                #     print("Log not found in the file.")

                # if i == 7 :
                    # table_pattern1 = r"(?m)^MO\s+(\S+)\s+(\S+)\s+(\S+)\s*$"
                    # table_pattern =    r"(?m)^MO\s+(\S+)\s+(\S+)\s+(\S+)\s*$"
                table_pattern = r"(GNBDUFunction=\S+)\s+(\d+)\s+(\d+)\s*$"
                table_matches1 = re.findall(table_pattern, content, re.MULTILINE)

                if table_matches1:
                    columns = ['MO', 'pmMacVolDl', 'pmMacVolUl']
                    table_df1 = pd.DataFrame(table_matches1, columns=columns)
                    print("second:\n", table_df1)
                    twentyfour1Log=table_df1.to_string()
                    write_data("twentyfour1Log\n"+twentyfour1Log)
                else:
                    print("No matching data found.")

                # else:
                #     print("Log not found in the file.")

                # if i == 11 :
                    # print("yes")
                    
                    # table_pattern = r"(NRCellDU=\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s*$"
                    # table_pattern = r"NRCellDU=\S+\s+(\d+)\s+(\d+)\s+(\d+)\s*$"
                    # table_pattern = r"^(NRCellDU=\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s*$"
                table_pattern = r"^(NRCellDU=\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s*$"
                
                table_matches2 = re.findall(table_pattern, content, re.MULTILINE)

                if table_matches2:
                    columns = ['MO', 'pmMacVolDl', 'pmMacVolDlDrb','pmMacVolUl']

                    # print(table_matches1)
                    table_df2 = pd.DataFrame(table_matches2, columns=columns)
                    print("third:\n", table_df2)
                    twentyfour2Log=table_df2.to_string()
                    write_data("twentyfour2Log\n"+twentyfour2Log)
                else:
                    print("No matching data found.")

                # else:
                #     print("Log not found in the file.")
                # if i == 16 :
                    # print("yes")
                    
                    # table_pattern = r"(NRCellDU=\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s*$"
                    # table_pattern = r"NRCellDU=\S+\s+(\d+)\s+(\d+)\s+(\d+)\s*$"
                    # table_pattern = r"^(EUtranCellFDD=\S+\s+\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*$"
                table_pattern = r"^(EUtranCellFDD=\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*$"
                
                table_matches3 = re.findall(table_pattern, content, re.MULTILINE)

                if table_matches3:
                    columns = ['MO', 'pmEndcSetupUeAtt', 'pmEndcSetupUeAttNrRestricted','pmEndcSetupUeSucc','pmEndcSetupUeSuccNrRestricted','pmMacVolUl']

                    # print(table_matches1)
                    table_df3 = pd.DataFrame(table_matches3, columns=columns)
                    print("fourth:\n", table_df3)
                    twentyfour3Log=table_df3.to_string()
                    write_data("twentyfour3Log\n"+twentyfour3Log)
                else:
                    print("No matching data found.")

                # if i == 20 :
                    # print("yes")
                    
                    
                    # table_pattern=r"[A-Z\d]+,GUtranFreqRelation=\d+,GUtranCellRelation=[A-Z\d-]+ (\d+)\s+(\d+)"
                table_pattern = r"^(EUtranCellFDD=\S+\s+\S+)\s+(\d+)\s+(\d+)*$"
                table_matches4 = re.findall(table_pattern, content, re.MULTILINE)

                if table_matches4:
                    columns = ['MO', 'pmEndcSetupUeAtt','pmEndcSetupUeSucc']

                    # print(table_matches1)
                    table_df4 = pd.DataFrame(table_matches4, columns=columns)
                    print("last::::\n", table_df4)
                    twentyfour4Log=table_df4.to_string()
                    write_data("twentyfour4Log\n"+twentyfour4Log)
                else:
                    print("No matching data found.")

                            
try:
    extract_data(file_path)
   
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

####### stop ################################################################33

########### 252525 log19##############################################################3

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log19 = "st interme|bblink|eran"

def extract_data19(log19, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log19 in content:
        # Use regex pattern to find the table data
        table_pattern = r"^\s*(\d+)\s+(\S+(?:\s+\(\S+\))?)\s+(\S+(?:\s+\(\S+\))?)\s+(.+)$"

        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = ['Proxy', 'Adm State', 'Op. State', 'MO']
            table_df = pd.DataFrame(table_matches, columns=columns)

            print("log19:\n", table_df)
            twentyfiveLog=table_df.to_string()
            write_data("twentyfiveLog\n"+twentyfiveLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

# Call the function to extract and parse data.
try:
    extract_data19(log19, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

######################## stop ##############################################

############======262626 log 20 ####################################################

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log20 = "st interme|bblink|eran"
def extract_data_table(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        if log20 in content and "Configured IML links:" in content:
            
            # Extract the data using regex pattern
            table_pattern = r"\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([\w:]+)\s*\|\s*([\w:]+)\s*\|\s*([\w-]+)\s*\|\s*(\d+)\s*\|\s*([\w\s]+)\s*\|\s*([\w\s]*)\s*\|"
            table_matches = re.findall(table_pattern, content)

            if table_matches:
                columns = ['clientRef', 'linkRef', 'sessId', 'mpId', 'nearEndCpmMac', 'farEndCpmMac', 'imlPortName', 'vlanId', 'state', 'reason']
                table_df = pd.DataFrame(table_matches, columns=columns)
                print("first:\n", table_df)
                twentysixLog=table_df.to_string()
                write_data("twentysixLog\n"+twentysixLog)
            else:
                print("No matching table data found.")
        else:
            print('no log')
        #


        ######## this code is incorrect i need help ##########
        # if log20 in content and "IML link measurement data " in content:
        #     print('yes')
        #     # Extract the data using regex pattern
        #     # table_pattern = r"\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([\w:]+)\s*\|\s*([\w:]+)\s*\|\s*([\w-]+)\s*\|\s*(\d+)\s*\|\s*([\w\s]+)\s*\|\s*([\w\s]*)\s*\|"
        #     table_pattern2 = r"\| +(\d+) +\| +(\d+) +\| +(\d+) +\| +(\d+) +\| +(\w+\s*\w*) +\| +(\w+\s*\w*) +\| +(\d+) +\| +(\d+) +\| +([\w\s]+) +\| +([\w\s]+) +\| +([\w\s]+) +\| +([\w\s]+) +\| +([\w\s]+) +\| +([\w\s]+) +\| +([\w\s]+) +\|"
        #     # table_pattern2 = r"\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([\w\s]+)\s*\|\s*([\w\s]+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+\.\d+)\s*\|\s*(\d+\.\d+)\s*\|\s*(\d+\.\d+)\s*\|\s*(\d+\.\d+)\s*\|\s*(\d+\.\d+)\s*\|\s*(\d+\.\d+)\s*\|\s*(\d+\.\d+)\s*\|"
        #     table_matches2 = re.findall(table_pattern2, content)
        #     print(table_matches2)

        #     if table_matches2:
        #         print('match')
        #         columns = ['linkRef', 'frame', 'measure', 'batch', 'Admin RTT', 'Oper RTT', 'requests', 'lost', 'RTT last 24h (Min)', 'RTT last 24h (Max)', 'RTT last 15 min (Min)', 'RTT last 15 min (Max)', 'RTT last min (Min)', 'RTT last min (Avg)', 'RTT last min (Max)']
        #         # columns = ['linkRef', 'frame size', 'measure frequency', 'batch size', 'Admin RTT state ', 'Oper RTT state', 'requests', 'lost', 'RTT last 24h ','RTT last 15 min ','RTT last min ']
        #         # columns = ['linkRef', 'frame', 'measure', 'batch', 'Admin RTT', 'Oper RTT', 'requests', 'lost', 'RTT last 24h (Min)', 'RTT last 24h (Max)', 'RTT last 15 min (Min)', 'RTT last 15 min (Max)', 'RTT last min (Min)', 'RTT last min (Avg)', 'RTT last min (Max)']
        #         table_df2 = pd.DataFrame(table_matches2, columns=columns)
        #         print("second:\n", table_df2)
        #     else:
        #         print("No matching table data found.")
        


        if log20 in content and "IML Application links:" in content:
            print('yes')
            # Extract the data using regex pattern
            table_pattern3 = r"\|\s*(\d+)\s*\|\s*([\w:]+)\s*\|\s*([\w:]+)\s*\|"
            table_matches3 = re.findall(table_pattern3, content)

            if table_matches3:
                columns = ['linkRef', ' nearEndAppMac ', 'farEndAppMac ']
                table_df = pd.DataFrame(table_matches3, columns=columns)
                print("third:\n", table_df)
                twentysix1Log=table_df.to_string()
                write_data("twentysix1Log\n"+twentysix1Log)
            else:
                print("No matching table data found.")
        else:
            print('no log')



        
    except FileNotFoundError:
        print(f"File not found at the specified path: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to extract and parse data.
extract_data_table(file_path)

################### stop ########################################################################

#############=========== 2727 log21 ###########################################################

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log21 = "st interme|bblink|eran"

def extract_data21(log21, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log21 in content:
        # Use regex pattern to find the table data
        # table_pattern = r"^\s*(\d+)\s+(\S+(?:\s+\(\S+\))?)\s+(\S+(?:\s+\(\S+\))?)\s+(.+)$"
        # table_pattern = r"([\w=]+)\s+([\w\s]+)\s+([\w\s]+)"
        table_pattern =r"^(NRCellDU=\S+)\s+([\w\s]+)\s+(\d+)\s*$"
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = ['MO ', 'Attribute', 'Value']
            table_df = pd.DataFrame(table_matches, columns=columns)

            print("log21:\n", table_df)
            twentysevenLog=table_df.to_string()
            write_data("twentysevenLog\n"+twentysevenLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data21(log21, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
##################################### stop #############################################

#####========2828282828 log 22 ######################################################

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log22 = "pmxh . pmmacvoldlscell"

def extract_data22(log22, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log22 in content:
        pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
        table_matche = re.findall(pattern, content, re.MULTILINE)
        if table_matche:
            date = table_matche[0]
            # print("Date:", date)
        
        table_pattern = r"(\d{2}:\d{2})\s+([\w=]+)\s+(\d+)\s+(\d+)"
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            
            columns = [ 'Time', 'Object','pmMacVolDlSCell','pmMacVolDlSCellExt']
            table_df = pd.DataFrame(table_matches, columns=columns)
            table_df.insert(0, 'Date', date) 
            print("log22:\n", table_df)
            twentyeightLog=table_df.to_string()
            write_data("twentyeightLog\n"+twentyeightLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data22(log22, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

###############stop ############################################

#########====2929292  log23 ########################################################

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log23 = "hpget . pmendccaconfigatt|pmendccaconfigsucc$|pmCaConfigDlSumSaDistr"

def extract_data23(log23, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log23 in content:
        print('yeeeef')
        
        table_pattern =r"(NRCellCU=\S+)\s+l\[\d+\]\s*=\s*((?:\d+\s*)+)\s+(\d+)\s+(\d+)"

        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            
            columns = [ 'MO', 'pmCaConfigDlSumSaDistr','pmEndcCaConfigAtt','pmEndcCaConfigSucc']
            table_df = pd.DataFrame(table_matches, columns=columns)
             
            print("log23:\n", table_df)
            twentynineLog=table_df.to_string()
            write_data("twentynineLog\n"+twentynineLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data23(log23, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
 
############## stop #######################################################################################

############### 3030303 log 24 ###############################################

log24=  "pmxh . pmcaconfigatt|pmcaconfigsucc|pmcaconfigdlsamp|pmendccaconfigatt|pmendccaconfigsucc$|PMCACONFIGDLSUMSADISTR$"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'

def extract_data24(log24, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log24 in content:
        pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
        table_matche = re.findall(pattern, content, re.MULTILINE)
        if table_matche:
            date = table_matche[0]
            # print("Date:", date)
        
        # table_pattern = r"(\d{2}:\d{2})\s+([\w=]+)\s+(\d+)\s+(\d+)"
        table_pattern = r"(\d{2}:\d{2})\s+([\w=]+)\s+(\d+)\s+(\d+)\s+([\d,]+)\s+(\d+)\s+(\d+)\s+(\d+)"
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            
            columns = [ 'Time', 'Object','pmCaConfigAtt','pmCaConfigDlSamp','pmCaConfigDlSumSaDistr','pmCaConfigSucc','pmEndcCaConfigAtt','pmEndcCaConfigSucc']
            table_df = pd.DataFrame(table_matches, columns=columns)
            table_df.insert(0, 'Date', date) 
            print("log24:\n", table_df)
            thirtyLog=table_df.to_string()
            write_data("thirtyLog\n"+thirtyLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data24(log24, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
#############stop #######################################

#############=====31313131 log25#####################################################


file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log25 = "get . caStatusActive    true"

def extract_data25(log25, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log25 in content:
        
        # table_pattern =r"(NRCellCU=\S+)\s+l\[\d+\]\s*=\s*((?:\d+\s*)+)\s+(\d+)\s+(\d+)"
        table_pattern = r"(NRCellCU=\S+)\s+(caStatusActive)\s+(\S+)"

        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            
            columns = [ 'MO', 'Attribute','Value']
            table_df = pd.DataFrame(table_matches, columns=columns)
             
            print("log25:\n", table_df)
            thirtyoneLog=table_df.to_string()
            write_data("thirtyoneLog\n"+thirtyoneLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data25(log25, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

############ stop###############################################################

######### =====  32 log26 #########################################

log26=  "pmxe NRcellDu int_AvgradiorecinterferencePwr$ -m 2"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'

def extract_data26(log26, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log26 in content:
        pattern=r"Date:\s+(\d{4}-\d{2}-\d{2})"
        table_matche = re.findall(pattern, content, re.MULTILINE)
        if table_matche:
            date = table_matche[0]
            # print("Date:", date)
        
        # table_pattern = r"(\d{2}:\d{2})\s+([\w=]+)\s+(\d+)\s+(\d+)"
        # table_pattern = r"(\d{2}:\d{2})\s+([\w=]+)\s+(\d+)\s+(\d+)\s+([\d,]+)\s+(\d+)\s+(\d+)\s+(\d+)"
        table_pattern = r"(\S+)\s+(\S+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)"
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            
            columns = [ 'Object ', 'Counter','19:30','19:45','20:00','20:15','20:30','20:45','21:00','21:15']
            table_df = pd.DataFrame(table_matches, columns=columns)
            table_df.insert(0, 'Date', date) 
            print("log26:\n", table_df)
            thirtytwoLog=table_df.to_string()
            write_data("thirtytwoLog\n"+thirtytwoLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data26(log26, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
############# stop ############################################################

############====33333333 log27###########################################################

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log27 = "get . caStatusActive    true"

def extract_data27(log27, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log27 in content:
        
        # table_pattern =r"(NRCellCU=\S+)\s+l\[\d+\]\s*=\s*((?:\d+\s*)+)\s+(\d+)\s+(\d+)"
        # table_pattern = r"(NRCellCU=\S+)\s+(caStatusActive)\s+(\S+)"
        table_pattern= r"(\d+)\s+(PmJob=\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\d+)\s*$"
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            
            columns = [ 'Proxy', 'Job','ReqState','CurrState','Granul','nrRdrs/Evts']
            table_df = pd.DataFrame(table_matches, columns=columns)
             
            print("log27:\n", table_df)
            thirtythreeLog=table_df.to_string()
            write_data("thirtythreeLog\n"+thirtythreeLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data27(log27, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

############# stop #####################################################

###########=====34343434343434 log28 ########################################################

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
# log28 = "get ^KeyFileInformation= ^sequenceNumber$"
log="""
MIE04225A> get ^KeyFileInformation= ^sequenceNumber$

230727-14:35:36-0700 11.244.16.43 23.0d MSRBS_NODE_MODEL_23.Q2_608.28193.115_333c stopfile=/tmp/144981
=================================================================================================================
MO                                                      Attribute         Value
=================================================================================================================
"""
def extract_data28(log, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        if log in content:
            print("jndwjhw")

            table_pattern = r"(Lm=1\S+)\s+(\S+)\s+(\S+)\s*$"
    #         # table_pattern = r"(NRCellCU=\S+KeyFileManagement=\S+KeyFileInformation=\S+ )\s+(\S+)\s+(\S+)"
            table_matches = re.findall(table_pattern, content, re.MULTILINE)

            if table_matches :
                
                columns = [ 'MO ', 'Attribute ','Value']
                table_df = pd.DataFrame(table_matches, columns=columns)
                
                print("log28:\n", table_df)
                thirtyfourLog=table_df.to_string()
                write_data("thirtyfourLog\n"+thirtyfourLog)
            else:
                print("No matching data found.")
        # else:
        #     print("Log not found in the file.")

try:
    extract_data28(log, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")


####################################################################################

############=== 353535353 log29 not come correct output##################################################################################

file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log29 = "hget CXC4011018|CXC4011056|CXC4011427|CXC4011667|CXC4012015|CXC4012600|CXC4011714"

def extract_data29(log, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        if log29 in content:
            print('iudbdgh1kbdnbdby3y4y1iebh')
            
            # table_pattern =r"(NRCellCU=\S+)\s+l\[\d+\]\s*=\s*((?:\d+\s*)+)\s+(\d+)\s+(\d+)"
            # table_pattern = r"(NRCellCU=\S+)\s+(caStatusActive)\s+(\S+)"
            table_pattern = r'^(Lm=1,\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+\S+\s+(\S+)\s+(\S+)$'
            table_matches = re.findall(table_pattern, content, re.MULTILINE)

            if table_matches:
                
                columns = [ 'MO', 'expiration','featureKeyId','keyId ','name','productType','shared','state ','validFrom']
                table_df = pd.DataFrame(table_matches, columns=columns)
                    
                print("log29:\n", table_df)
                thirtyfifthLog=table_df.to_string()
                write_data("thirtyfifthLog\n"+thirtyfifthLog)
            else:
                print("No matching data found.")
        else:
            print("Log not found in the file.")

        log = """Added 7 MOs to group: hget_group
......
=================================================================================================================
MO                           description                             featureKey                          featureState  featureStateId keyId      licenseState serviceState
================================================================================================================="""
        if log29 in content and log in content:#log29 in content and
            print('i12w325536')
            
            # table_pattern2= r'^(\S+)\s+(.*?)\s+(\[1\] = .+?)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$'
            table_pattern2 = r'^(\S+)\s+(.*?)\s+(\[1\] = .+?)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$'
            table_matches2 = re.findall(table_pattern2, content, re.MULTILINE)

            if table_matches2:
                
                columns = [ 'MO', 'description','featureKey','featureState','featureStateId','keyId','licenseState','serviceState ','extracolumn']
                table_df2 = pd.DataFrame(table_matches2, columns=columns)
                    
                print("second:\n", table_df2)
                thirtyfifth2Log=table_df2.to_string()
                write_data("thirtyfifthLog\n"+thirtyfifth2Log)

            else:
                print("No matching data found.")
        else:
            print("Log not found in the file.")


try:
    extract_data29(log, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

###########################################################################

#########=====36363636 log30  incorrect come output######################################################################

log30=  "invl CXC4010912|CXC4010723|CXC4010961|CXC4012240|CXC4010990"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'

def extract_data30(log30, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log30 in content:
        print('krhvug4y')
        table_pattern  = r'^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.*?)\s*$'
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = [ 'FeatureName ', 'FeatureKey ','FAJ','LicenseState','FeatureState','ServiceState ','ValidFrom','ValidUntil','Description']
            table_df = pd.DataFrame(table_matches, columns=columns)
            
            print("log30:\n", table_df)
            thirtysixthLog=table_df.to_string()
            write_data("thirtysixthLog\n"+thirtysixthLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data30(log30, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
###############stop #############################################

####======37373737 log31 #############################################

log31=  "hget UtranFreqRelation= cellReselectionPriority|connectedModeMobilityPrio|mobilityAction|voicePrio|csFallbackPrio|qrxlevmin"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'

def extract_data31(log31, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log31 in content:
        print('krhvug4y')
        table_pattern = r'^(NRCellCU=\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$'
        # table_pattern  = r'^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)*$'
        # table_pattern = r"(NRCellCU=\S+)\s+(EUtranFreqRelation=\S+)\s+(\S+)\s+(-\S+)\s+(\S+)*$"
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = [ 'MO ', 'cellReselectionPriority ','connectedModeMobilityPrio','qRxLevMin','voicePrio']
            table_df = pd.DataFrame(table_matches, columns=columns)
            
            print("log31:\n", table_df)
            thirtyseventhLog=table_df.to_string()
            write_data("thirtyseventhLog\n"+thirtyseventhLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data31(log31, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

##################stop#############################################
############======= 383383838383 log 32 #############################

log32=  "hget ^EUtranCellRelation= sCellCandidate|amoAllowed|isHoAllowed|isRemoveAllowed"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log1="""=================================================================================================================
MO                                                  isHoAllowed isRemoveAllowed
================================================================================================================="""

def extract_data32(log32, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        if log32 in content and log1 in content:
            # table_pattern = r'^(NRCellCU=\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$'
            # table_pattern  = r'^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)*$'
            # table_pattern =  r'^(\S+)\s+(\S+)\s+(\S+)\s*$'
            table_pattern = r'^(NRCellCU=\S+,EUtranCellRelation=\S+)\s+(\S+)\s+(\S+)\s*$'
            table_matches = re.findall(table_pattern, content, re.MULTILINE)

            if table_matches:
                columns = [ 'MO ', 'isHoAllowed','isRemoveAllowed']
                table_df = pd.DataFrame(table_matches, columns=columns)
                
                print("log32:\n", table_df)
                thirtyeighthLog=table_df.to_string()
                write_data("thirtyeighthLog\n"+thirtyeighthLog)
            else:
                print("No matching data found.")
        else:
            print("Log not found in the file.")

        log2=""".............................................................................................................................................................................................................................
=================================================================================================================
MO                                                                                      amoAllowed isHoAllowed isHoAllowedBr isRemoveAllowed sCellCandidate
================================================================================================================="""

        if log32  in content and log2 in content :
            print('khju')
            
            table_pattern1 = r'^(EUtranCellFDD=\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$'
            # table_pattern1 = r'^EUtranCellFDD=(\S+),EUtranFreqRelation=(\S+),EUtranCellRelation=(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$'
            table_matches1 = re.findall(table_pattern1, content, re.MULTILINE)

            if table_matches1:
                columns = [ 'MO ', 'amoAllowed','isHoAllowed','isHoAllowedBr','isRemoveAllowed','sCellCandidate']
                table_df1 = pd.DataFrame(table_matches1, columns=columns)
                
                print("swcond:\n", table_df1)
                thirtyeighth2Log=table_df1.to_string()
                write_data("thirtyeighth2Log\n"+thirtyeighth2Log)
                
            else:
                print("No matching data found.")
        else:
            print("Log not found in the file.")

try:
    extract_data32(log32, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
##################### stop #######################################################
#############========3939 log33  nc #########################################################


log33=  "get . sCellCandidate 1"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'

def extract_data33(log33, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log33 in content:
        print('krhvug4y')
        table_pattern = r'^(EUtranCellFDD=\S+)\s+(\S+)\s+(\S+)\s*$'
        # table_pattern  =  r'^EUtranCellFDD=(\S+),EUtranFreqRelation=(\S+),EUtranCellRelation=(\S+)\s+sCellCandidate\s+(\S+)\s*$'
        
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = [ 'MO ', 'Attribute ','Value']
            table_df = pd.DataFrame(table_matches, columns=columns)
            
            print("log33:\n", table_df)
            thirtynineLog=table_df.to_string()
            write_data("thirtynineLog\n"+thirtynineLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data33(log33, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
############stop ######################################################

##########40 log34###############################################

log34=  "st TermPoint"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'

def extract_data34(log34, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log34 in content:
        print('krhvug4y')
        # table_pattern = r'^(EUtranCellFDD=\S+)\s+(\S+)\s+(\S+)\s*$'
        table_pattern  =  r'^\s*(\d+)\s+(\S+)\s+(\S+)\s+(ENodeBFunction=\S+,\S+)\s*$'
        
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = [ 'Proxy ', 'Adm State','Op. State','MO']
            table_df = pd.DataFrame(table_matches, columns=columns)
            
            print("log34:\n", table_df)
            fourtyLog=table_df.to_string()
            write_data("fourtyLog\n"+fourtyLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data34(log34, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

##################### stop ######################

####### ====414141 log 35 #####################################################

log35=  "lpr ,.*Relation="
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'

def extract_data35(log35, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log35 in content:
        
        # table_pattern = r'^(EUtranCellFDD=\S+)\s+(\S+)\s+(\S+)\s*$'
        # table_pattern  =  r'^\s*(\d+)\s+(\S+)\s+(\S+)\s+(ENodeBFunction=\S+,\S+)\s*$'
        table_pattern=r'^\s*(\d+)\s+(ENodeBFunction=\S+,\S+)\s*$'
        
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = [ 'Proxy ','MO']
            table_df = pd.DataFrame(table_matches, columns=columns)
            
            print("log35:\n", table_df)
            fourtyoneLog=table_df.to_string()
            write_data("fourtyoneLog\n"+fourtyoneLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data35(log35, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
######################### stop#############################################################

#################### 424242 log 36####################################

log36=  "lga"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
log="""======================================================================================================
Timestamp           Type Sev    Description
======================================================================================================"""
def extract_data36(log36, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log36 in content and log in content:
        print("kwu")
        
        # table_pattern = r'^(EUtranCellFDD=\S+)\s+(\S+)\s+(\S+)\s*$'
        # table_pattern  =  r'^\s*(\d+)\s+(\S+)\s+(\S+)\s+(ENodeBFunction=\S+,\S+)\s*$'
        # table_pattern=r'^\s*(\d+)\s+(ENodeBFunction=\S+,\S+)\s*$'
        table_pattern = r'^(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+(\w+)\s+(.+)$'
        
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = [ 'Timestamp','Type','Sev ','Description']
            table_df = pd.DataFrame(table_matches, columns=columns)
            
            print("log36:\n", table_df)
            fourtytwoLog=table_df.to_string()
            write_data("fourtytwoLog\n"+fourtytwoLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data36(log36, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
########################################## stop #########################################

#############43 log37 ##########################################################


log37=  "lgg"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
def extract_data37(log37, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if log37 in content:
        # print("kwu")
        table_pattern = r'^(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+(\w+)\s+(\w+:\s+\d+\.)\s+(.+)$'
        # table_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\d+) (\w+)      No:\s+(\d+)\. Board restart\. Reason: (\w+) restart\. Rank: (\w+)\. Extra: '([^']*)'"
        # table_pattern = r'^(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+(\w+)\s+(\w+:\s+\d+\.)\s+(.+)$'  
        # table_pattern = r'^(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+(\w+)\s+(\w+:\s+\d+\.)\s+(.+)$'
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = ['Timestamp (UTC) ', 'Board', 'Restart Number', 'Restart Reason', 'Extra Info']
            
            # columns = [ 'Timestamp','(UTC) ','Board',' Restart']
            table_df = pd.DataFrame(table_matches, columns=columns)
            
            print("log37:\n", table_df)
            fourtythreeLog=table_df.to_string()
            write_data("fourtythreeLog\n"+fourtythreeLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data37(log37, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

############# stop ##############################################

################44 log 38 ######################################################

log38="st all disabled"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
def extract_data38(log38, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # print(content)

    if log38 in content:
        print("khuy")
        # table_pattern = r'^(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+(\w+)\s+(\w+:\s+\d+\.)\s+(.+)$'
        # table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+ENodeBFunction=(\d+),EUtraNetwork=(\d+),ExternalENodeBFunction=([-\d]+),TermPointToENB=([-\d]+)"
        # table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+ENodeBFunction=(\d+),EUtraNetwork=(\d+),ExternalENodeBFunction=([-\d]+),TermPointToENB=([-\d]+)"
        table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+(.+)"
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            # columns = ['Proxy', 'Adm State', 'Op. State', 'ENodeBFunction', 'EUtraNetwork', 'ExternalENodeBFunction', 'TermPointToENB']
            columns = ['Proxy', 'Adm State', 'Op. State', 'MO']
            # columns = ['Proxy', 'Adm', 'State', ' Op. State', 'MO']
            # columns = [ 'Timestamp','(UTC) ','Board',' Restart']
            table_df = pd.DataFrame(table_matches, columns=columns)
            
            print("log38:\n", table_df)
            fourtyfourLog=table_df.to_string()
            write_data("fourtyfourLog\n"+fourtyfourLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data38(log38, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

########### stop #########################
#########== 45 log 39 #################@###################

log39="st all enabled"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
def extract_data39(log39, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # print(content)

    if log39 in content:
        print("lwdiuwi")

        # table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+(.+)"
        # table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+ENodeBFunction=\S+,EUtraNetwork=\S+,ExternalENodeBFunction=\S+,TermPointToENB=\S+"
        table_pattern= r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+(ENodeBFunction=\S+,EUtraNetwork=\S+,ExternalENodeBFunction=\S+,TermPointToENB=\S+)\s"
        # table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+(.+)"
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = ['Proxy', 'Adm State', 'Op. State', 'MO']
            table_df = pd.DataFrame(table_matches, columns=columns)
            
            print("log39:\n", table_df)
            fourtyfiveLog=table_df.to_string()
            write_data("fourtyfiveLog\n"+fourtyfiveLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data39(log39, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
########################### stop#################################

############## 46 log40 #####################################################
log40="pr UpgradePackage"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
def extract_data40(log40, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # print(content)

    if log40 in content:
        
        # table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+(.+)"
        # table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+ENodeBFunction=\S+,EUtraNetwork=\S+,ExternalENodeBFunction=\S+,TermPointToENB=\S+"
        table_pattern= r"(\d+)\s+(SystemFunctions=\S+,SwM=\S+,UpgradePackage=\S+)\s"
        # table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+(.+)"
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = ['Proxy','MO']
            table_df = pd.DataFrame(table_matches, columns=columns)
            
            print("log40:\n", table_df)
            fourtysixLog=table_df.to_string()
            write_data("fourtysixLog\n"+fourtysixLog)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data40(log40, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

############ stop ########################################################
#########=====47 log41 ####################################################


log41 = "sdir"
start_log = "+--------+                  +----------------+"
end_log = "+--------+"
log_second="""=====================================================================================================================================
ID RiL                Type Res MO1-MO2           BOARD1-BOARD2         AlmIDs Cells (States)                                          Issue (Failed checks)
=====================================================================================================================================
1 BB-01-A-6-01-Data2 O101 OK  BB-01(A) 6-01(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A11 FDD=EIE04225A11 NRC=KIE04225A11 (1,1,1) Passed
2 BB-01-B-6-02-Data2 O101 OK  BB-01(B) 6-02(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A21 FDD=EIE04225A21 NRC=KIE04225A21 (1,1,1) Passed
3 BB-01-C-6-03-Data2 O101 OK  BB-01(C) 6-03(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A31 FDD=EIE04225A31 NRC=KIE04225A31 (1,1,1) Passed
-------------------------------------------------------------------------------------------------------------------------------------"""
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
def extract_data41(file_path,log41):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

    if log41 in content:
        start_marker = re.escape(start_log)
        end_marker = re.escape(end_log)

        match = re.search(f"{start_marker}(.*?){end_marker}", content, re.DOTALL)
        if match:
            data_between_markers = match.group(1).strip()

            # Split the data into lines and create a list
            data_list = data_between_markers.split("\n")

            # Create a pandas DataFrame from the list
            df = pd.DataFrame(data_list, columns=["Data"])
            
            # Display the DataFrame
            print("log41:::\n",df)
            fourtysevenLog=df.to_string()
            write_data("fourtysevenLog\n"+fourtysevenLog)
        else:
            print("No match found between markers.")
    else:
        print("Log not found in the content.")
 ########## not correct out put ##################   
    log_second="""=====================================================================================================================================
ID RiL                Type Res MO1-MO2           BOARD1-BOARD2         AlmIDs Cells (States)                                          Issue (Failed checks)
=====================================================================================================================================
1 BB-01-A-6-01-Data2 O101 OK  BB-01(A) 6-01(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A11 FDD=EIE04225A11 NRC=KIE04225A11 (1,1,1) Passed
2 BB-01-B-6-02-Data2 O101 OK  BB-01(B) 6-02(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A21 FDD=EIE04225A21 NRC=KIE04225A21 (1,1,1) Passed
3 BB-01-C-6-03-Data2 O101 OK  BB-01(C) 6-03(D2) BB6630 RRU4449B71B85A        FDD=DIE04225A31 FDD=EIE04225A31 NRC=KIE04225A31 (1,1,1) Passed
-------------------------------------------------------------------------------------------------------------------------------------"""

    if log41 in content and log_second in content :###and log_second in content
        # print("liehvcdbn")
        # table_pattern = r"ID\s+RiL\s+Type\s+Res\s+MO1-MO2\s+BOARD1-BOARD2\s+AlmIDs\s+Cells \(States\)\s+Issue \(Failed checks\)"
        
        # table_pattern = r"(\d+)\s+([\w-]+)\s+([A-Z0-9]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w\s]+)\s+\(([\d,]+)\)\s+([\w\s]+)"
        table_pattern = r"\s*(\d+)\s+([\w-]+)\s+([A-Z0-9]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s$"
        # table_pattern= r'(\d+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+.+?)'
        table_matches = re.findall(table_pattern, content, re.MULTILINE)
        
       
        if table_matches:
            # print(table_matches)
            columns = ['ID','RiL','Type','Res','MO1-MO2','BOARD1-BOARD2 ','AlmIDs','Cells (States)','Issue (Failed checks)']
            table_df = pd.DataFrame(table_matches, columns=columns)

            print("secondlog::\n",table_df)
            fourtyseven2Log=table_df.to_string()
            write_data("fourtyseven2Log\n"+fourtyseven2Log)

        else:
            print("data not found")

    else:
        print("Log not found in the file.")
# ############# this data is not find #################
    fourth_log="""=====================================================================================================================================
FRU   ;LNH    ;BOARD          ;ST ;FAULT ;OPER ;MAINT ;STAT ;PRODUCTNUMBER   ;REV     ;SERIAL        ;DATE     ;PMTEMP ; TEMP ; UPT ;SW                  ;
====================================================================================================================================="""
    if log41 in content and fourth_log in content:
        print("978856")
        # table_pattern= r"([\w-]+)\s*;([\w/]+)\s*;([\w/ ]+)\s*;(\d+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;"
        # table_pattern = r"\s*([\w-]+)\s*;([\w/]+)\s*;([\w/ ]+)\s*;(\d+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;([\w/ ]+)\s*;"
        # table_pattern = r"^(\w+)\s*;(\w+)\s*;(\w+)\s*;\s*\d+\s*;(\s*OFF\s*|\s*ON\s*)\s*;(\s*OFF\s*|\s*ON\s*)\s*;(\s*OFF\s*|\s*ON\s*)\s*;(\s*OFF\s*|\s*ON\s*)\s*;(\w+)\s*;(\w+)\s*;(\w+)\s*;(\d+)\s*;\s*\d+\s*;\s*\d+(\.\d+)?\s*;\s*\d+(\.\d+)?\s*;([^;]+)\s*;"
        table_pattern =r"^(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);$"
        table_matches = re.findall(table_pattern, content)
        if table_matches:
            # columns = [
#     "FRU", "LNH", "BOARD", "ST", "FAULT", "OPER", "MAINT",
#     "STAT", "PRODUCTNUMBER", "REV", "SERIAL", "DATE", "PMTEMP",
#     "TEMP", "UPT", "SW", "UNUSED1", "UNUSED2", "SW_DESCRIPTION"
# ]
            columns = ['FRU', 'LNH', 'BOARD', 'ST', 'FAULT', 'OPER', 'MAINT', 'STAT', 'PRODUCTNUMBER', 'REV', 'SERIAL', 'DATE', 'PMTEMP', 'TEMP', 'UPT', 'SW']
            table_data = [list(row) for row in table_matches]
            table_df = pd.DataFrame(table_data, columns=columns)
            print("Extracted Table:\n", table_df)
        else:
            print("Data not found")
    else:
        print("Log not found in the file.")

    log_fifth= """=====================================================================================================================================
XPBOARD   ;ST ;FAULT ;OPER ;PRODUCTNUMBER ;REV ;SERIAL/NAME ;DATE     ; TEMP ;MO
====================================================================================================================================="""
    if log41 in content and log_fifth in content :###and log_second in content
        # print("liehvcdbn")
        # table_pattern ="^([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*(.*)"
        table_pattern = r"\s*(\d+)\s+([\w-]+)\s+([A-Z0-9]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s+([\w-]+)\s"
        # table_pattern= r'(\d+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+.+?)'
        table_matches = re.findall(table_pattern, content, re.MULTILINE)
        
       
        if table_matches:
            # print(table_matches)
            columns = ['XPBOARD','ST','FAULT','OPER','PRODUCTNUMBER','REV ','SERIAL/NAME','DATE','TEMP','MO']
            table_df = pd.DataFrame(table_matches, columns=columns)
            print("fiffth::\n",table_df)
            # print("fifthlog::\n",table_df)
            fourtyseven5Log=table_df.to_string()
            write_data("fourtyseven5Log\n"+fourtyseven5Log)

        else:
            print("data not found")



#     log_sixth= """=====================================================================================================================================
# ID ;T ;RiL                ;BPBP ;BOARD1         ;LNH1 ;PORT ;R ;LINK ;RATE  ; BER ;BOARD2         ;LNH2 ;PORT ;R ;LINK ;RATE  ; BER ;LENGTH ;MO1 - MO2
# ====================================================================================================================================="""
#     if log41 in content and log_sixth in content:
#         print("yyyyyyyyyy")
#         # table_pattern = r"(\d+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*"
#         # table_pattern = r"(\d+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*" 
#         table_pattern = r"(\d+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([A-Z])\s*;\s*([^;]+)\s*"##;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*
    
#         table_matches = re.findall(table_pattern, content, re.MULTILINE)       
#         if table_matches:
#             print("tttbbb")
#             columns = ['ID', 'T', 'RiL', 'BPBP', 'BOARD1', 'LNH1', 'PORT', 'R', 'LINK', 'RATE', 'BER', 'BOARD2', 'LNH2', 'PORT', 'R', 'LINK', 'RATE', 'BER', 'LENGTH', 'MO1 - MO2']
#             # columns = ['ID','T','RiL','BPBP','BOARD1','LNH1','PORT','R','LINK','RATE','BER','BOARD2','LNH2','PORT','PORT','LINK','RATE','BER','LENGTH','MO1 - MO2']
#             table_df = pd.DataFrame(table_matches, columns=columns)

#             print("sixthlog::\n",table_df)

#         else:
#             print("Data not found")
#     else:
#         print("Log patterns not found")




    

extract_data41(file_path,log41)
################################# stop ############################################
########## 48 log42 ##################################################################
log42="cvls"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
def extract_data42(log42, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # print(content)
    log1="""=================================================================================================================
230727-14:45            BackupName                                                           SwVersion
=================================================================================================================
LastCreatedBackup:      Post_ServSpecMobility_Act_230726-1831                                CXP9024418/15_R74C54
LastRestoredBackup:     NTAC_26032023111110
-----------------------------------------------------------------------------------------------------------------"""

    if log42 in content and log1 in content:

        table_pattern = r"LastCreatedBackup:\s+(.+)\s+([A-Z0-9/]+)"
        last_restored_pattern = r"LastRestoredBackup:\s+(.+)"

        table_matches = re.findall(table_pattern, content, re.MULTILINE)
        last_restored_match = re.search(last_restored_pattern, content, re.MULTILINE)

        if table_matches and last_restored_match:
            data = []
            for match in table_matches:
                backup_name = match[0]
                sw_version = match[1]
                data.append((backup_name, sw_version))

            last_restored_backup = last_restored_match.group(1)
            data.append(('LastRestoredBackup', last_restored_backup))

            columns = ['BackupName', 'SwVersion']
            table_df = pd.DataFrame(data, columns=columns)

            
            print("log42:\n", table_df)
            fourtyeight1Log=table_df.to_string()
            write_data("fourtyeight1Log\n"+fourtyeight1Log)
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

    log2="""-----------------------------------------------------------------------------------------------------------------
Current SwVersion:      CXP9024418/15_R74C54 (23.Q2)
BrmHouseKeeping:        ENABLED (max: 20 backups)
BrmFailSafe:            IDLE
RestoreEscalationList:  s[2] = Final_backup_for_BASEBAND_CXP9024418/15_R74C54_20230711T081137+0000 Rollback_backup_BASEBAND_CXP9024418/15_R69C42_20230711T080002+0000
=============================================================================================================================================="""

    if log42 in content and log2 in content:
        # print("csjjscghj")

        # pattern = r"Current SwVersion:\s+([^(\n]+)\nBrmHouseKeeping:\s+([^(\n]+)\nBrmFailSafe:\s+([^(\n]+)\nRestoreEscalationList:\s+([^(\n]+)"
        pattern=r"Current SwVersion:\s+(.*?)\nBrmHouseKeeping:\s+(.*?)\nBrmFailSafe:\s+(.*?)\nRestoreEscalationList:\s+(.*?)\n"


        matches = re.search(pattern, content,re.MULTILINE)
        # print(matches)
        if matches:
            try:
                current_sw_version = matches.group(1).strip()
                brm_house_keeping = matches.group(2).strip()
                brm_fail_safe = matches.group(3).strip()
                restore_escalation_list = matches.group(4).strip()

                data = {
                    'Current SwVersion': [current_sw_version],
                    'BrmHouseKeeping': [brm_house_keeping],
                    'BrmFailSafe': [brm_fail_safe],
                    'RestoreEscalationList': [restore_escalation_list]
                }

                df = pd.DataFrame(data)
                print("log2:\n", df)
                fourtyeight2Log=df.to_string()
                write_data("fourtyeight2Log\n"+fourtyeight2Log)
            except Exception as e:
                print(e)
    else:
        print("No matching data found.")

    log3="""==============================================================================================================================================
SwVersion             ProductData           ProdDate  Rel        LMs  InstallationDate     ActivationDate       DeactivationDate
==============================================================================================================================================
CXP9024418/15-R74C54  CXP9024418/15_R74C54  20230616  23.Q2       74  2023-07-11 08:05:50  2023-07-11 08:05:50
=============================================================================================================================================="""

    if log42 in content and log3 in content:
        print("yyguy")
        pattern = r"\s*(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$"

        # pattern = r"\s*(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$"
        matches = re.findall(pattern, content, re.MULTILINE)
        print("lklklklllkl")

        if matches:
            columns = ['SwVersion', 'ProductData', 'ProdDate', 'Rel', 'LMs', 'InstallationDate', 'ActivationDate', 'DeactivationDate']
            table_df = pd.DataFrame(matches, columns=columns)

            print("log3:\n", table_df)
            fourtyeight3Log=table_df.to_string()
            write_data("fourtyeight3Log\n"+fourtyeight3Log)
        else:
            print("No matching data found.")


    log4="""==============================================================================================================================================
UpgradePackage        ProductData           ProdDate  Rel        CreationDate         State
==============================================================================================================================================
CXP9024418/15-R64C56  CXP9024418/15_R64C56  20221207  22.Q4.0-3  2023-01-06 08:20:37  PREPARE_COMPLETED
CXP9024418/15-R69C42  CXP9024418/15_R69C42  20230316  23.Q1.0-3  2023-04-07 07:49:56  PREPARE_COMPLETED
CXP9024418/15-R74C54  CXP9024418/15_R74C54  20230616  23.Q2      2023-07-11 08:06:46  COMMIT_COMPLETED
=============================================================================================================================================="""    
    if log42 in content and log4 in content:
        print("yyguy")
        # pattern = r"\s*([\w/-]+)\s+([\w/]+)\s+(\d+)\s+([\d\w.-]+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$"
        pattern = r"\s*([\w/-]+)\s+([\w/]+)\s+(\d+)\s+([\d\w.-]+)\s+(\S+)\s+(\S+)\s*$"
        matches = re.findall(pattern, content, re.MULTILINE)
        print("lklklklllkl")

        if matches:
            columns = ['UpgradePackage', 'ProductData', 'ProdDate', 'Rel', 'CreationDate', ' State']
            table_df = pd.DataFrame(matches, columns=columns)

            print("log4:\n", table_df)
            fourtyeight4Log=table_df.to_string()
            write_data("fourtyeight4Log\n"+fourtyeight4Log)
        else:
            print("No matching data found.")

    log5="""==============================================================================================================================================
Id  BackupName                                                           CreationTime         SwVersion            Rel        Type   Stat  MO
=============================================================================================================================================="""
    if log42 in content and log5 in content:
        pattern = r"(\d+)\s+([\w/]+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+BrmBackup=(\d+)"
        matches = re.findall(pattern, content, re.MULTILINE)
        if matches:
            columns = ['Id', 'BackupName', 'CreationTime', 'SwVersion', 'Rel', 'Type', 'Stat', 'MO', 'BrmBackup']
            # columns = ['Id', ' BackupName', 'CreationTime', 'SwVersion', 'Rel', ' Type','Stat','MO']
            table_df = pd.DataFrame(matches, columns=columns)

            print("log5:\n", table_df)
            fourtyeight5Log=table_df.to_string()
            write_data("fourtyeight5Log\n"+fourtyeight5Log)
            
        else:
            print("No matching data found.")


try:
    extract_data42(log42, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")


####==== 49 log 44 #############################################################################

log44="scg"
file_path = 'C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt'
def extract_data44(log44, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # print(content)

    if log44 in content:
        
        # table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+(.+)"
        # table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+ENodeBFunction=\S+,EUtraNetwork=\S+,ExternalENodeBFunction=\S+,TermPointToENB=\S+"
        # table_pattern= r"(\d+)\s+(SystemFunctions=\S+,SwM=\S+,UpgradePackage=\S+)\s"
        table_pattern=r"(\w+)\s+(\d+)\s+(\d+)\s+"
        # table_pattern = r"(\d+)\s+(\d\s\(\w+\))\s+(\d\s\(\w+\))\s+(.+)"
        table_matches = re.findall(table_pattern, content, re.MULTILINE)

        if table_matches:
            columns = ['Namespace','SC ','Value']
            table_df = pd.DataFrame(table_matches, columns=columns)
            
            print("log44:\n", table_df)
            fourtynineLog=table_df.to_string()
            write_data("fourtynineLog\n"+fourtynineLog)
            
        else:
            print("No matching data found.")
    else:
        print("Log not found in the file.")

try:
    extract_data44(log44, file_path)
except FileNotFoundError:
    print(f"File not found at the specified path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

#################### stop ################################################

if __name__ == ("__main__"):
    app.run(debug=True)




