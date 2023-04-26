import os
import shutil


def main():
    folder_to_merge = input("Enter the path to your folder to merge: ").lower()
    output_folder = input("Enter the path to your output folder: ").lower()

    if not os.path.isdir(folder_to_merge):
        print("Error: The folder to merge path is not valid.")
        print("Hint: Make sure to provide a valid folder path.")
        print(
            '       Use double quotes or a backslash to escape spaces, e.g., "/Users/username/My\\ Folder" or "/Users/username/My Folder"'
        )
        return
    if not os.path.isdir(output_folder):
        print("Error: The output folder path is not valid.")
        print("Hint: Make sure to provide a valid folder path.")
        print(
            '       Use double quotes or a backslash to escape spaces, e.g., "/Users/username/Output\\ Folder" or "/Users/username/Output Folder"'
        )
        return

    unique_subfolder_names = set()

    print("Scanning folder to merge for unique subfolder names...")
    for root, dirs, files in os.walk(folder_to_merge):
        for folder in dirs:
            unique_subfolder_names.add(folder.lower())

    total_folders = len(unique_subfolder_names)
    folder_counter = 0
    total_files_moved = 0

    for subfolder_name in unique_subfolder_names:
        folder_counter += 1
        print(
            f"Processing folder {folder_counter} of {total_folders}: {subfolder_name}"
        )

        for root, dirs, files in os.walk(folder_to_merge):
            for folder in dirs:
                if folder.lower() == subfolder_name:
                    source_folder_path = os.path.join(root, folder)

                    for root2, dirs2, files2 in os.walk(source_folder_path):
                        for another_folder in dirs2:
                            another_folder_path = os.path.join(root2, another_folder)
                            master_folder_path = os.path.join(
                                output_folder, subfolder_name, another_folder
                            )

                            if not os.path.exists(master_folder_path):
                                os.makedirs(master_folder_path)

                            for file in os.listdir(another_folder_path):
                                source_file_path = os.path.join(
                                    another_folder_path, file
                                )
                                target_file_path = os.path.join(
                                    master_folder_path, file
                                )

                                try:
                                    if not os.path.exists(target_file_path):
                                        shutil.move(source_file_path, target_file_path)
                                        total_files_moved += 1
                                except Exception as e:
                                    print(
                                        f"Error moving file {source_file_path} to {target_file_path}: {e}"
                                    )

    if total_files_moved == 0:
        print("No files were moved.")
    else:
        print(f"Done! A total of {total_files_moved} files were moved.")


if __name__ == "__main__":
    main()
