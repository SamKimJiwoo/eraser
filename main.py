import os
import tkinter as tk
from tkinter import messagebox

def refresh_file_list():
    """현재 폴더의 파일 목록을 리스트박스에 갱신"""
    file_listbox.delete(0, tk.END)
    # 숨김 파일(.)을 제외하고 일반 파일만 깔끔하게 불러오기
    files = [f for f in os.listdir('.') if os.path.isfile(f) and not f.startswith('.')]
    
    if not files:
        file_listbox.insert(tk.END, "현재 폴더에 파일이 없습니다.")
    else:
        for f in files:
            file_listbox.insert(tk.END, f)

def delete_selected_file():
    """선택한 파일 삭제"""
    try:
        selected_indices = file_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("알림", "삭제할 파일을 선택해 주세요.")
            return
        
        filename = file_listbox.get(selected_indices[0])
        
        # 파일이 없을 경우 처리
        if filename == "현재 폴더에 파일이 없습니다.":
            return
            
        # 깔끔하고 직관적인 확인 팝업
        confirm = messagebox.askyesno("삭제 확인", f"'{filename}' 파일을 영구적으로 삭제하시겠습니까?")
        
        if confirm:
            os.remove(filename)
            messagebox.showinfo("완료", "파일이 성공적으로 삭제되었습니다.")
            refresh_file_list()
    except Exception as e:
        messagebox.showerror("오류", f"삭제 중 문제가 발생했습니다:\n{e}")

# --- 메인 창 설정 (모던 스타일) ---
root = tk.Tk()
root.title("File Eraser")
root.geometry("360x520")
root.configure(bg="#f4f6f9") # 부드러운 배경색

# 상단 타이틀 프레임
header_frame = tk.Frame(root, bg="#f4f6f9")
header_frame.pack(fill="x", padx=20, pady=20)

title_label = tk.Label(header_frame, text="파일 삭제 유틸리티", font=("Helvetica", 16, "bold"), bg="#f4f6f9", fg="#2c3e50")
title_label.pack(anchor="w")

sub_label = tk.Label(header_frame, text="삭제할 파일을 선택하고 버튼을 누르세요.", font=("Helvetica", 10), bg="#f4f6f9", fg="#7f8c8d")
sub_label.pack(anchor="w", pady=(2, 0))

# 파일 목록 리스트박스 (여백과 테두리 정리)
list_frame = tk.Frame(root, bg="#ffffff", bd=1, relief="solid")
list_frame.pack(fill="both", expand=True, padx=20, pady=10)

file_listbox = tk.Listbox(
    list_frame, 
    selectmode=tk.SINGLE, 
    font=("Helvetica", 11),
    bg="#ffffff",
    fg="#333333",
    selectbackground="#3498db",
    selectforeground="#ffffff",
    bd=0,
    highlightthickness=0
)
file_listbox.pack(fill="both", expand=True, padx=10, pady=10)

# 하단 버튼 프레임
btn_frame = tk.Frame(root, bg="#f4f6f9")
btn_frame.pack(fill="x", padx=20, pady=20)

# 새로고침 버튼 (회색 계열)
btn_refresh = tk.Button(
    btn_frame, 
    text="목록 새로고침", 
    font=("Helvetica", 11), 
    bg="#95a5a6", 
    fg="#ffffff", 
    activebackground="#7f8c8d",
    activeforeground="#ffffff",
    bd=0, 
    relief="flat",
    command=refresh_file_list
)
btn_refresh.pack(fill="x", pady=(0, 8), ipady=8)

# 삭제 버튼 (눈에 띄는 포인트 컬러 - 코랄 레드)
btn_delete = tk.Button(
    btn_frame, 
    text="선택 파일 삭제", 
    font=("Helvetica", 11, "bold"), 
    bg="#e74c3c", 
    fg="#ffffff", 
    activebackground="#c0392b",
    activeforeground="#ffffff",
    bd=0, 
    relief="flat",
    command=delete_selected_file
)
btn_delete.pack(fill="x", ipady=8)

# 실행 시 최초 목록 불러오기
refresh_file_list()

# 창 실행
root.mainloop()
