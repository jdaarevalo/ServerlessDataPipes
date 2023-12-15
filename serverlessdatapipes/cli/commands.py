import os
import shutil


def init_project(args):    
    project_name = args.name
    base_path = project_name
    base_path_src = base_path + '/src'
    os.makedirs(os.path.join(base_path, 'src'), exist_ok=True)
    os.makedirs(os.path.join(base_path_src, 'queries'), exist_ok=True)

    with open(f'{base_path_src}/queries/example_query.yaml', 'w') as f:
        f.write("title: 'example_query'\n# ...")
    with open(f'{project_name}/template.yaml', 'w') as f:
        f.write("# ServerlessDataPipes Project\nThis is an auto-generated project structure.")

    with open(f'{project_name}/README.md', 'w') as f:
        f.write("# ServerlessDataPipes Project\nThis is an auto-generated project structure.")

    print(f"{project_name} project initialized successfully.")

def delete_project(args):
    # Require user confirmation
    project_name = args.name
    user_confirmation = input(f"Are you sure you want to delete the project '{project_name}'? This action cannot be undone. Type 'yes' to confirm: ").strip().lower()

    if user_confirmation == 'yes':
        try:
            shutil.rmtree(project_name)
            print(f"Project {project_name} has been successfully deleted.")
        except FileNotFoundError:
            print(f"Project {project_name} not found for deletion.")
        except Exception as e:
            print(f"Error deleting project {project_name}: {e}")
    else:
        print("Project deletion cancelled.")