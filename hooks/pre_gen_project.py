from pathlib import Path

# Capture the current working directory before the project generation
original_working_directory = Path.cwd().resolve() / Path("backend")

# Write it to a file
with open('original_working_directory.txt', 'w') as f:
    f.write(str(original_working_directory))
