import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from tkinter import messagebox
import imghdr
import shutil

class NoteInputDialog:
    def __init__(self, base_name):
        self.window = tk.Tk()
        self.window.title("Create Note")
        self.selected_folder = None
        self.note_content = None
        self.base_name = base_name

        # Configure window
        self.window.geometry("300x250")
        
        # Create folder buttons frame
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        # Create folder buttons
        folders = ["Girls", "Medieval", "Random", "Style"]
        for folder in folders:
            btn = tk.Button(button_frame, 
                          text=folder,
                          width=10,
                          command=lambda f=folder: self.complete_task(f))
            btn.pack(pady=2)

        # Create input label
        tk.Label(self.window, 
                text=f"Enter note content for {base_name}:").pack(pady=5)

        # Create text input
        self.text_input = tk.Text(self.window, height=5)
        self.text_input.pack(pady=10, padx=10)

        # Bind Enter key to complete_task
        self.window.bind('<Return>', lambda event: self.complete_task(self.selected_folder))

    def complete_task(self, folder):
        self.selected_folder = folder
        self.note_content = self.text_input.get("1.0", "end-1c")
        if self.note_content.strip():  # Check if there's content
            self.window.quit()
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Please enter some content!")

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        if self.is_image(event.src_path):
            image_name = os.path.basename(event.src_path)
            
            while '.crdownload' in image_name or '.download' in image_name or '.part' in image_name:
                image_name = os.path.splitext(image_name)[0]
            
            image_ext = imghdr.what(event.src_path)
            if image_ext:
                image_name = f"{os.path.splitext(image_name)[0]}.{image_ext}"
            
            base_name = os.path.splitext(image_name)[0]
            
            # Create dialog instance
            dialog = NoteInputDialog(base_name)
            dialog.window.mainloop()
            
            if dialog.note_content and dialog.selected_folder:
                formatted_content = f"{dialog.note_content}\n\n![[{image_name}]]"
                
                current_dir = os.path.dirname(os.path.abspath(__file__))
                prompts_folder = os.path.join(current_dir, "Prompts")
                selected_folder_path = os.path.join(prompts_folder, dialog.selected_folder)
                
                # Create necessary folders
                os.makedirs(selected_folder_path, exist_ok=True)
                
                # Create and move the note file
                temp_md_filename = f"{base_name}.md"
                final_md_path = os.path.join(selected_folder_path, temp_md_filename)
                
                with open(final_md_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(formatted_content)
                
                print(f"Created note in: {final_md_path}")

    def is_image(self, file_path):
        try:
            return imghdr.what(file_path) is not None
        except:
            return False

def monitor_folder():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, current_dir, recursive=False)
    
    print(f"Monitoring folder: {current_dir}")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nMonitoring stopped")
    
    observer.join()

if __name__ == "__main__":
    monitor_folder()