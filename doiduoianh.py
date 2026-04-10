import os
folder_path = r'C:\Users\KhaiTran\Documents\GitHub\CSDL_BAI1\images'
def rename_images(path):
    files = [f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
    print(f"Đang xử lý {len(files)} ảnh...")
    for index, filename in enumerate(files, start=1):
        extension = os.path.splitext(filename)[1]
        new_name = f"{index}{extension}"
        old_file = os.path.join(path, filename)
        new_file = os.path.join(path, new_name)
        try:
            os.rename(old_file, new_file)
            print(f"Đã đổi: {filename} -> {new_name}")
        except Exception as e:
            print(f"Lỗi tại file {filename}: {e}")
if __name__ == "__main__":
    rename_images(folder_path)