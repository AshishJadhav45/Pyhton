import shutil

def copy_file(source_file, destination_file):
    try:
        shutil.copyfile(source_file, destination_file)
        print("File copied successfully.")
    except FileNotFoundError:
        print("One or both files not found.")
    except Exception as e:
        print("An error occurred:", str(e))


# Example usage
source_file_path = 'C:/Users/SAM/OneDrive/Desktop/Assignment/Python Assignment/Python.txt'
destination_file_path = 'C:/Users/SAM/OneDrive/Desktop/Assignment/Python Assignment/new_file.new_file.txt'
copy_file(source_file_path, destination_file_path)
