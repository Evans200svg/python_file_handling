def main():
	filename = input("Enter the filename to read: ")
	try:
		with open(filename, 'r') as f:
			content = f.read()
	except FileNotFoundError:
		print(f"Error: File '{filename}' not found.")
		return
	except IOError:
		print(f"Error: Could not read file '{filename}'.")
		return

	# Modify the content (convert to uppercase)
	modified_content = content.upper()
	new_filename = f"modified_{filename}"
	try:
		with open(new_filename, 'w') as f:
			f.write(modified_content)
		print(f"Modified content written to '{new_filename}'.")
	except IOError:
		print(f"Error: Could not write to file '{new_filename}'.")

if __name__ == "__main__":
	main()
