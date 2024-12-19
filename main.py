import os
import sys
import subprocess


def detect_project_type(path):
    files = os.listdir(path)
    for entry in os.scandir(path):
        if entry.is_dir():
            files.extend(os.listdir(entry.path))

    if "CMakeLists.txt" in files or any(f.endswith(".cpp") or f.endswith(".h") or f.endswith(".uproject") for f in files):
        return "C++"
    elif "requirements.txt" in files or any(f.endswith(".py") for f in files):
        return "Python"
    elif any(f.endswith(".java") for f in files):
        return "Java"
    elif "symfony.lock" in files or any(f.endswith(".php") for f in files):
        return "PHP"
    elif "package.json" in files or any(f.endswith(".html") or f.endswith(".css") or f.endswith(".js")for f in files):
        return "Web"
    elif any(f.endswith(".cs") or f.endswith(".csproj")for f in files):
        return "C#"
    elif "Cargo.toml" in files or any(f.endswith(".rs") for f in files):
        return "Rust"
    elif any(f.endswith(".go") for f in files):
        return "Go"
    elif any(f.endswith(".rb") for f in files):
        return "Ruby"
    else:
        return "Other"


def open_ide(project_type, path):
    ide_commands = {
        "C++": f"clion {path}",
        "Python": f"pycharm {path}",
        "Java": f"intellij-idea {path}",
        "PHP": f"phpstorm {path}",
        "Web": f"webstorm {path}",
        "C#": f"rider {path}",
        "Rust": f"rustrover {path}",
        "Go": f"goland {path}",
        "Ruby": f"rubymine {path}",
        "Other": f"code {path}"
    }

    command = ide_commands.get(project_type, f"code {path}")
    try:
        print(f"Opening {project_type} project in {path} with command: {command}")
        subprocess.run(command, shell=True)
    except FileNotFoundError:
        print(f"IDE for {project_type} not found. Please install the appropriate IDE.")


if __name__ == "__main__":
    if not len(sys.argv) < 2:
        repository_path = sys.argv[1]
    else:
        repository_path = "."

    if not os.path.exists(repository_path):
        print(f"Error: Path '{repository_path}' does not exist.")
        sys.exit(1)

    project_type = detect_project_type(repository_path)
    open_ide(project_type, repository_path)