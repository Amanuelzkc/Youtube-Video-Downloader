import customtkinter as ctk 
from tkinter import ttk
from pytube import YouTube
import os

def download_video():
    url = entry_url.get()
    res= reso_var.get()
    
    progress_label.pack(pady=(10,5))
    progress_bar.pack(pady=(10,5))
    stat_label.pack(pady=(10,5))
    
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=reso).first()
        
        #for the path
        #use ur on directory instead and don't forget to use "\\" instead  of a single backslash like"\"
        os.path.join("C:\\Users\\peni\\Downloads\\New folder (2)", f"{yt.title}.mp4")
        stream.download(output_path="C:\\Users\\peni\\Downloads\\New folder (2)")
        
        stat_label.configure(text="Downloaded!", text_color = "red", fg_color="green")
    except Exception as e:
        stat_label.configure(text=f"Error {str(e)}", text_color = "green", fg_color="red")
       
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize 
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100
    
    progress_label.configure(text= str(int(percentage_completed)) + "%")
    progress_label.update()
    
    progress_bar.set(float(percentage_completed / 100))
#create root window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#title on the window
root.title("Yt vid Downloader")

#min n max width n height

root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

#for the frame
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10 )

#label n text field 
url_label = ctk.CTkLabel(content_frame, text="Url here :")
entry_url = ctk.CTkEntry(content_frame, width=400 , height=40)
url_label.pack(pady=(10,5))
entry_url.pack(pady=(10,5))

#button
download_button = ctk.CTkButton(content_frame, text="Download" ,command=download_video)
download_button.pack(pady=(10,5))

#combo box
reso = ["1080p","720p","480p","240p"]
reso_var = ctk.StringVar()
reso_combobox = ttk.Combobox(content_frame, values=reso, textvariable=reso_var)
reso_combobox.pack(pady=(10,5))
reso_combobox.set("720p")

#progress bar n it's label
progress_label = ctk.CTkLabel(content_frame, text="0%")


progress_bar = ctk.CTkProgressBar(content_frame,width=400)
progress_bar.set(0)
#status
stat_label = ctk.CTkLabel(content_frame, text="")

#to start the app
root.mainloop()