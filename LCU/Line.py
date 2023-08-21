import win32api
import win32con
import win32gui


def draw_line_on_game_window(x1, y1, x2, y2):
    game_window_title = "Plants vs. Zombies"
    game_hwnd = win32gui.FindWindow(None, game_window_title)
    if game_hwnd == 0:
        print("Không tìm thấy cửa sổ trò chơi.")
        return

    hdc = win32gui.GetDC(game_hwnd)
    pen = win32gui.CreatePen(win32con.PS_SOLID, 2, win32api.RGB(255, 0, 0))

    while True:
        win32gui.SelectObject(hdc, pen)
        win32gui.MoveToEx(hdc, x1, y1)
        win32gui.LineTo(hdc, x2, y2)

    win32gui.ReleaseDC(game_hwnd, hdc)
    win32gui.DeleteObject(pen)


if __name__ == "__main__":
    x1, y1, x2, y2 = 100, 100, 300, 300
    draw_line_on_game_window(x1, y1, x2, y2)
