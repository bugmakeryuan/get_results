# coding=UTF-8
import os
import linecache


# Get the current path
filedir = os.getcwd()
# Get the filenames' list in current path
filenames = os.listdir(filedir)
"""
Open 'result.txt' in current path
if it doesn't exist, create one
"""
fo = open("result.txt", "a")
# Tranversing the filenames of all folder
for filename in filenames:
    """
    Exclude 'get_results.py' and 'result.txt'
    tranversing all subfolder in this folder
    """
    if filename != "get_results.py" and filename != "result.txt":
        # Get the path of the subfolder
        filepath = filedir+"\\"+filename
        # Change path to this subfolder
        os.chdir(filepath)
        # Open “w000r000.avg"，read line 32，and write it into 'result.txt'
        if os.path.exists("w000r000.avg"):
            f = open('ww000r000.avg', 'w')
            # Read line 32
            line = linecache.getline("w000r000.avg", 32)
            # Write line 32 to 'result.txt'
            fo.writelines(filename + ' ' + line)
            # write a Enter
            fo.write('\n')
            # close 'w000r000.avg'
            f.close()
        else:
            # write a Enter
            fo.writelines("No result in %s" % filename)
            # close 'w000r000.avg'
            fo.write('\n')
# close 'result.txt'
fo.close()
# print 'Finished'
print("Finished.")