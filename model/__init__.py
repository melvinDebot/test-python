import os
import shutil

source = "../logo_test.png"
target = "../images/logo_test.png"

#copier coller un fichier
shutil.copy(source, target)

#Supression du fichier
os.remove(source)



