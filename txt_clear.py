import os

# Path to your folder
folder_path = "txt_file"

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):  # Check if it's a .txt file
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'w') as file:  # Open the file in write mode
            pass  # Write nothing to clear the file
        #print(f"Cleared content of: {filename}")

print("All text files have been cleared.")
