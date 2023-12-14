import pandas as pd 
import re
file_path = "C:/Users/LENOVO/Desktop/dataframework/find_data/find_data.txt"
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
                # table_df['operationalState'] = table_df['operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                # table_df['Site Id'] = globalSiteId
                # table_df = table_df[[ 'Site Id','MO ','electricalAntennaTilt','iuantAntennaModelNumber','iuantBaseStationId','maxTilt','minTilt','operationalState','tiltChangeStatus',' userLabel']]
######################################################################################################################################\

    file_path3 = "C:/Users/LENOVO/Desktop/dataframework/find_data/third_data.txt"
    with open(file_path3, 'r') as file:
        content2 = file.read()

        start_marker2 = """hget SectorCarrier= administrativeState$|operationalState$|arfcn|configuredMaxTxPower|bSChannelBw|reservedBy"""
        end_marker2 = """hget ^SectorEquipmentFunction= administrativeState|operationalState|availableHwOutputPower|reservedBy"""

        start_index2 = content2.find(start_marker2)
        end_index2 = content2.find(end_marker2)
        extracted_data2 = content2[start_index2:end_index2]
        print(extracted_data2,'22222')

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
                # table_df['operationalState'] = table_df['operationalState'].str.replace(r'(', '').str.replace(')', '').str.replace('1', '').str.replace('0', '')
                # table_df['Site Id'] = globalSiteId
         #         table_df = table_df[[ 'Site Id','MO ','electricalAntennaTilt','iuantAntennaModelNumber','iuantBaseStationId','maxTilt','minTilt','operationalState','tiltChangeStatus',' userLabel']]
##################################################################################################################################################


        #         def apply_color(val):

        #             if val.strip() == 'DISABLED':
        #                 return 'background-color: rgb(250, 9, 9);color:white; '
        #             else:
        #                 return ''
        #         table_df['operationalState'] = table_df['operationalState'].apply(lambda x: f'<span class="shobhit" style="{apply_color(x)}">{x}</span>')
        #         html_table = global_style + table_df.to_html(escape=False, index=False,
        #                                                   table_id='styled_table',
        #                                                   classes='table table-striped table-bordered')

        #         write_html_table("<h2>-----: RET Status:-----:</h2>\n"+html_table)

        #         # # print("RetSubUnit:\n", table_df)

        #     else:
        #         print("No matching table data found.")
        # else:
        #     print("No extracted data found.")

LTE_SECTOR(file_path)