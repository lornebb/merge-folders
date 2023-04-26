import os
import subprocess


def unarchive(input_file, output_folder):
    try:
        subprocess.run(["unzip", "-o", "-d", output_folder, input_file], check=True)
        print(f"Unarchived {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error unarchiving {input_file}: {e}")


def main():
    folder_to_scan = input("Enter the path to the folder you want to scan: ").lower()

    if not os.path.isdir(folder_to_scan):
        print("Error: The folder path is not valid.")
        print("Hint: Make sure to provide a valid folder path.")
        print(
            '       Use double quotes or a backslash to escape spaces, e.g., "/Users/username/My\\ Folder" or "/Users/username/My Folder"'
        )
        return

    for root, _, files in os.walk(folder_to_scan):
        for file in files:
            if file.endswith(".zip"):
                file_path = os.path.join(root, file)
                unarchive(file_path, root)


if __name__ == "__main__":
    main()
