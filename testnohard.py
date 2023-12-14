import re

# Sample input string

file_path='C:/Users/LENOVO/Desktop/dataframework/find_data/find_data copy.txt'

input_string=""
with open(file_path, 'r') as file:
    input_string = file.read()

# print(input_string)
# input_string = """
# pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'
# This is the data you want to capture.
# More data.
# End of data.
# pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'
# This is another block of data.
# Even more data.
# End of data.
# Some text after the marker.
# """

# Define the start marker as a regular expression

def siteIdGetter(pattern):
        
    # start_marker = re.escape("pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'")

    # pattern = r".*pmr -m 3 -r 206 \| egrep -i '\(Int_RadioRecInterference\)'.*$"


    matches = re.findall(pattern, input_string, re.MULTILINE)
    strid=""

    for i in matches:

        if(i.split(">")[0]!=""):
            strid=i.split(">")[0]

    return strid


pattern = r".*pmr -m 3 -r 206 \| egrep -i '\(Int_RadioRecInterference\)'.*$"

print(siteIdGetter(pattern))




print(input_string.find(marking),input_string.find(marking))

print(input_string[113634:113624])


for i in range(113634,113624,-1):
    print(input_string[i])

dsadsadsadsa


# Define the end marker
end_marker = "pst"

# Use re.findall to find all matches between the markers
data_list = re.findall(f"{start_marker}(.*?){re.escape(end_marker)}", input_string, re.DOTALL)

# Print the found data
f=open("testdel.txt","a+")
for i in data_list:
    
    start_marker = re.escape("pmr -m 3 -r 206 | egrep -i '(Int_RadioRecInterference)'")
    end_marker = "pst"
    data_list = re.findall(f"{start_marker}(.*?){re.escape(end_marker)}", "".join(data_list), re.DOTALL)
    f.write(i[0])
f.close()

# for i, data in enumerate(data_list, start=1):
#     print(f"Data {i}:\n{data.strip()}\n")
