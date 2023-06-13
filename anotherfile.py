source_file = 'C:/Users/SAM/OneDrive/Desktop'
destination_file = 'new_file'

with open(source_file, 'r') as source:
    with open(destination_file, 'w') as destination:
        destination.write(source.read())

print("Contents copied from", source_file, "to", destination_file)
