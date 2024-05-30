import os
import shutil
import argparse

def copy_and_sort_files(src_dir, dst_dir):
    try:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            if os.path.isdir(item_path):
                # Recursively process subdirectories
                new_dst_dir = os.path.join(dst_dir, os.path.basename(item_path))
                copy_and_sort_files(item_path, new_dst_dir)
            else:
                # Process files
                file_ext = os.path.splitext(item)[1][1:].lower()  # Get the file extension without the dot
                ext_dir = os.path.join(dst_dir, file_ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                shutil.copy2(item_path, ext_dir)
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursively copy files and sort them into subdirectories based on file extensions.")
    parser.add_argument("src_dir", help="Path to the source directory")
    parser.add_argument("dst_dir", nargs='?', default="dist", help="Path to the destination directory (default is 'dist')")
    args = parser.parse_args()
    
    src_dir = args.src_dir
    dst_dir = args.dst_dir
    
    if not os.path.exists(src_dir):
        print(f"Error: Source directory '{src_dir}' does not exist.")
        return
    
    copy_and_sort_files(src_dir, dst_dir)
    print("Files copied and sorted successfully.")

if __name__ == "__main__":
    main()
