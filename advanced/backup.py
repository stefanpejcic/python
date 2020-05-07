import os
import zipfile
import shutil

#copy files and folder and compress into a zip file
def	doprocess(source_folder, target_zip):
	zipf = zipfile.ZipFile(target_zip, "w")
	for subdir, dirs, files in os.walk(source_folder):
		for file in files:
			print (os.path.join(subdir, file))
			zipf.write(os.path.join(subdir, file))
	
	print ("Created ", target_zip)
	

#copy files to a target folder	
def	docopy(source_folder, target_folder):
	for subdir, dirs, files in os.walk(source_folder):
		for file in files:
			print (os.path.join(subdir, file))
			shutil.copy2(os.path.join(subdir, file), target_folder)
	
		

if __name__ =='__main__':
	print ('Starting execution')
	
	#compress to zip
	source_folder = (r'C:\Users\Stefan\Desktop\screen')
	target_zip = (r'C:\Users\Stefan\Desktop\screen\screen.zip')
	doprocess(source_folder, target_zip)	
			
	#copy to backup folder
	source_folder = (r'C:\Users\Stefan\Desktop\screen\1')
	target_folder = (r'C:\Users\Stefan\Desktop\screen\2')
	docopy(source_folder, target_folder)
	
	
	print ('Ending execution')
