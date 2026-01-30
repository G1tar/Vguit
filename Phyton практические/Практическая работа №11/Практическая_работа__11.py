import json
import tkinter as tk
from tkinter import messagebox
import requests

def get_repo_info():
    repo_name = entry.get().strip()
    if not repo_name:
        messagebox.showwarning("Ошибка", "Введите имя репозитория!")
        return
    
    url = f"https://api.github.com/repos/{repo_name}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            filtered_data = {
                "company": data.get("owner", {}).get("company"),
                "created_at": data.get("created_at"),
                "email": data.get("owner", {}).get("email"),
                "id": data.get("id"),
                "name": data.get("name"),
                "url": data.get("html_url")
            }
            
            # Сохраняем в файл
            with open(f"{repo_name.replace('/', '_')}_info.json", "w", encoding="utf-8") as f:
                json.dump(filtered_data, f, indent=4, ensure_ascii=False)
            
            messagebox.showinfo("Успех", f"Данные сохранены в файл: {repo_name.replace('/', '_')}_info.json")
        else:
            messagebox.showerror("Ошибка", f"Репозиторий не найден или ошибка API: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при запросе: {str(e)}")

# Создаем GUI
root = tk.Tk()
root.title("GitHub Repo Info - Вариант 5")
root.geometry("400x200")

label = tk.Label(root, text="Введите имя репозитория (например: kubernetes/kubernetes):")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Получить данные", command=get_repo_info)
button.pack(pady=20)

root.mainloop()