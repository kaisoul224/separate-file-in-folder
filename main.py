import os
import shutil

# Đường dẫn đến thư mục chứa các tệp
src_folder = 'D:\source'

# Thư mục đích mà các tệp được chia sẽ được lưu trữ
dst_folder = 'D:\destination'

# Duyệt qua tất cả các tệp trong thư mục nguồn
for filename in os.listdir(src_folder):
    # Tách tên tệp và phần mở rộng
    name, ext = os.path.splitext(filename)

    # Tách phần trước và sau ký tự "_" trong tên tệp
    prefix, suffix = name.split("_")

    # Tạo một thư mục cho mỗi prefix duy nhất
    folder_path = os.path.join(dst_folder, suffix)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Di chuyển tệp đến thư mục
    src_path = os.path.join(src_folder, filename)
    dst_path = os.path.join(folder_path, filename)
    shutil.move(src_path, dst_path)
