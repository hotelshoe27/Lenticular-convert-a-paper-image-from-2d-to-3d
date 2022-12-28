import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image
import sys
import os

root = Tk()
root.title("Making Lenticular ver 1.1")

#- File support Function
def add_file():
    files = filedialog.askopenfilenames(title="Select images", \
        filetypes=(("All","*.*"), ("PNG","*.png"), ("JPG","*.jpg"), ("JPEG","*.jpeg")), \
        initialdir=r".\data\.")
    
    for file in files:
        list_file.insert(END, file)

def del_file():
    #print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return 
    #print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

def combo(imgs, out):
    images = map(Image.open, imgs)
    widths, heights = zip(*(i.size for i in images))
    images = map(Image.open, imgs)
    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
    
    dest_path = os.path.join(txt_dest_path.get(), out)
    new_im.save(dest_path)

#- Lenticular Function
def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords) # coords: x, y coordinates tuple (x1, y1, x2, y2)
    cropped_image.save(saved_location)

def strips(image, pieces):
    gen = []
    im = Image.open(image)
    width, height = im.size
    mult = width/pieces #-- width/pieces: Calculate based on width/pieces using x value and height/width
    for i in range(0,pieces):
        if i % 2 == 0: #-- Only extract even number pieces
            continue
        x = 0+(i*mult)
        crop(image, (x, 0, x+mult, height), image.split(".")[0]+'_'+str(i+1)+'.png')
        gen.append(image.split(".")[0]+'_'+str(i+1)+'.png')
    return gen

def merge_image():
    psz = int(piece_txt.get("1.0", "end"))
    image1 = list_file.get(0)
    image2 = list_file.get(1)
    print(image1)
    print(image2)
    im = Image.open(image1)
    w, h = im.size
    im2 = Image.open(image2)
    w2, h2 = im2.size

    print("The sizes of the two images you entered are as follows:")
    print("1st image:", im.size)
    print("2nd image:", im2.size)
    
    if w != w2 or h != h2:
        sys.exit("Both uploaded images must be the same size!")

    if psz > w:
        sys.exit("The number of piece is more than the number of pixels!")

    list1 = strips(image1, psz)
    list2 = strips(image2, psz)
    new = []

    for i in range(0, len(list1)):
        new.append(list1[i])
        new.append(list2[i])
        progress = ((i + 1) / len(list1)) * 100
        p_var.set(progress)
        progress_bar.update()
    file_name = "lenticularImg_sample.png"
    combo(new, file_name)
    msgbox.showinfo("Notice", "Complete")

    for n in new:
        os.remove(n)

def start():

    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Please add image files")
        return

    if len(txt_dest_path.get()) == 0:
       msgbox.showwarning("Warning", "Please select save path")
       return 

    merge_image()


#- UI parts
file_frame = Frame(root)
file_frame.pack(fill="x", padx="5", pady="5" )

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add files", command=add_file)
btn_add_file.pack(side = "left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete", command=del_file)
btn_del_file.pack(side="right")


list_frame = Frame(root)
list_frame.pack(fill="both", padx="5", pady="5")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode = "extended", height=15, yscrollcommand = scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


path_frame = LabelFrame(root, text="Save path")
path_frame.pack(fill="x", padx="5", pady="5", ipady ="5")

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx="5", pady="5", ipady=4)
txt_dest_path.insert(END, "./complete")

btn_dest_path = Button(path_frame, text="Browse", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx="5", pady="5")


piece_frame = LabelFrame(root, text = "number of piece")
piece_frame.pack(fill="x", padx="5", pady="5", ipady ="5")

piece_txt = Text(piece_frame, width = 70, height = 1)
piece_txt.pack()


frame_progress = LabelFrame(root, text="progress")
frame_progress.pack(fill="x", padx="5", pady="5", ipady ="5")

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx="5", pady="5")


frame_run = Frame(root)
frame_run.pack(fill="x", padx="5", pady="5")

btn_closed = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_closed.pack(side="right", padx="5", pady="5")

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12, command = start)
btn_start.pack(side="right", padx="5", pady="5")

root.resizable(False, False)
root = mainloop()