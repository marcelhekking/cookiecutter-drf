import os

file_content = """SQL_DATABASE={{cookiecutter.project_slug}}_local_production
SQL_USER=postgres
SQL_PASSWORD=a_secret_password
SQL_HOST=db
SQL_PORT=5432

POSTGRES_DB={{cookiecutter.project_slug}}_local_production
POSTGRES_USER=postgres
POSTGRES_PASSWORD=a_secret_password

WEB_IMAGE={{cookiecutter.project_slug}}-web:latest
MEDIAFILES_HOST=current_working_dir/public/mediafiles/
STATICFILES_HOST=current_working_dir/public/staticfiles/
"""

# Define the path to the file where the original working directory is stored
original_working_directory_file = "original_working_directory.txt"

# Read the original working directory from the file
with open(original_working_directory_file, "r") as file:
    original_working_directory = file.read().strip()

# Print the original working directory to verify
print(f"Original working directory: {original_working_directory}")

# Define the path to the template file to be created
template_file_path = original_working_directory + "/.env_var"

# Write the content to th `.env_var` file
content = file_content.replace("current_working_dir", original_working_directory)
with open(template_file_path, "w") as file:
    file.write(content)

print(f"Created the file {template_file_path}")
