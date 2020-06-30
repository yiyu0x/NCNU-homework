try:
	fn = input("Filename? ") 
	infile = open(fn, "r") # 檔名不存在，open 時就會出錯
	s = infile.read() # 若 fd 已經出錯那也無法繼續操作
	print(s)
	infile.close()
	print("Program ends gracefully.")
except FileNotFoundError as e:
	print("File not found. QQ")
except IsADirectoryError as e:
	print("This is a directory, not file. QQ")
except PermissionError as e:
	print("PermissionError. QQ")
except ValueError as e:
	print("ValueError. QQ")
except Exception as e:
	print("Unknown error.", e)