# import the modules
import shutil
import os
import sys

# to change the directory
os.chdir(sys.path[0])

def takeBackup(src_file_name,
				dst_file_name=None,
				src_dir='',
				dst_dir=''):
	try:
		number = "copy"

		src_dir = src_dir+src_file_name

		if not src_file_name:
			print("Please give the Source File Name")
			exit()

		try:
			
			if src_file_name and dst_file_name and src_dir and dst_dir:
				src_dir = src_dir+src_file_name
				dst_dir = dst_dir+dst_file_name
				
			elif dst_file_name is None or not dst_file_name:
				dst_file_name = src_file_name
				dst_dir = dst_dir+number+ dst_file_name
				
			elif dst_file_name.isspace():
				dst_file_name = src_file_name
				dst_dir = dst_dir+number+dst_file_name
				
			else:
				dst_dir = dst_dir+number+dst_file_name

			shutil.copy2(src_dir, dst_dir)

			print("Backup Successful!")
		except FileNotFoundError:
			print("File does not exists!,\
			please give the complete path")

	except PermissionError:
		dst_dir = dst_dir+number+dst_file_name

		shutil.copytree(src_file_name, dst_dir)

# Call the function
takeBackup()

