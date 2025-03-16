import os
import random

# Banner ASCII
banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠚⣷⠀⠀⣀⣤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⣟⢀⡴⠋⠀⠀⣿⠖⠋⢀⡏⠀⠀⠀⡀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡀⡼⠀⢸⡟⡸⠀⠀⠀⠃⠀⠀⢸⡧⠜⠛⠛⣻⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢺⢾⡃⠀⠈⣴⠁⢻⡀⠀⠀⢀⡠⠀⠀⠀⠀⢸⣇⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⡜⠂⠀⠀⣟⠀⢸⠑⠀⠰⠁⠀⠀⠀⠀⠀⠛⠉⡼⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣷⣾⣿⣿⣿⣿⣾⣶⣶⣤⣀⡀⢰⠕⠋⠀⠀⠸⠧⣤⡄
⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣔⠈⣤⣶⡚⠁⠀
⠀⠀⠀⠀⣠⣶⡀⢸⡟⠿⡿⠿⡟⠻⠿⣿⣿⣿⣿⣿⣿⣿⠿⣿⠋⠁⠀⠀⠀
⠀⠀⠀⢰⢧⡷⡿⢘⡎⠀⠀⠐⣶⢶⣲⠈⠙⠋⠉⠉⠁⡘⡯⣿⡶⣆⡀⠀⠀
⠀⠀⠀⢾⢈⣼⣿⣤⣿⣶⣶⣶⣿⣿⣧⣤⣄⣀⣀⣤⣾⣿⣿⢯⢇⣿⢳⠀⠀
⠀⠀⠀⠈⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⣷⣬⠏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠻⠟⠋⠁⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣀⡀⣰⣿⣿⣿⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣤⣶⣴⣿⣿⣿⡧⠀⠉⠙⢿⣿⣿⣿⣿⣾⣶⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠛⠛⠿⣿⣿⡇⠀⠀⠀⠀⠻⣿⣿⣿⡿⠿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀"""
info = "Telegram: HgAnh_7"

# Danh sách màu chữ ANSI
colors = [
    "\033[1;31m",  # Đỏ
    "\033[1;32m",  # Xanh lá
    "\033[1;33m",  # Vàng
    "\033[1;34m",  # Xanh dương
    "\033[1;35m",  # Tím
    "\033[1;36m",  # Xanh ngọc
    "\033[1;37m",  # Trắng

    "\033[1;91m",  # Đỏ nhạt
    "\033[1;92m",  # Xanh lá nhạt
    "\033[1;93m",  # Vàng nhạt
    "\033[1;94m",  # Xanh dương nhạt
    "\033[1;95m",  # Tím nhạt
    "\033[1;96m",  # Xanh ngọc nhạt
    "\033[1;97m",  # Trắng đậm
]

# Chọn màu chữ ngẫu nhiên
random_color = random.choice(colors)

# Chọn màu thứ hai khác với màu thứ nhất
random_color1 = random.choice(colors)
while random_color1 == random_color:
    random_color1 = random.choice(colors)

# Xóa màn hình trước khi in banner
os.system("cls" if os.name == "nt" else "clear")

# In banner với màu chữ ngẫu nhiên
print(random_color + banner + "\033[0m")  # Reset màu về mặc định
print("╔═══════════════════╗")
print("║ " + random_color1 + info + "\033[0m" + " ║")
print("╚═══════════════════╝")
