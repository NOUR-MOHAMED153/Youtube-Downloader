from customtkinter import *
import PIL 
#======= main window =========
window = CTk()
set_appearance_mode('system')
window.geometry('960x580+350+100')
window.resizable(False,False)
window.title(' Youtube Downloader   v1.0')
window.iconbitmap(r'icons\\yti.ico')
main_frame = CTkFrame(window,width=870,height=490,corner_radius=20)
main_frame.place(x=45,y=45)
main_img = PIL.Image.open(r'icons\\yt.png')
main_imag = CTkImage(main_img,size=(300,150))
main_image = CTkLabel(main_frame,text='',image=main_imag)
main_image.place(x=285,y=50)
Dev_name = CTkLabel(main_frame,text='Devloped By: Nour M',text_color='#D0D3D4',font=('Rubik',12,'bold'))
Dev_name.place(x=695,y=425)
#================   functions ======================
def change_mode(x):
    if x == 'Dark':
        set_appearance_mode('dark')
        Dev_name.configure(text_color='#D0D3D4')
        path_en.configure(placeholder_text_color='silver')
        url_en.configure(placeholder_text_color='silver')
        type_btn1.configure(text_color='silver')
        type_btn2.configure(text_color='silver')
        type_lbl.configure(text_color='#BDC3C7')


    else:
        set_appearance_mode('light')
        Dev_name.configure(text_color='#17202A')
        path_en.configure(placeholder_text_color='black')
        url_en.configure(placeholder_text_color='black')
        type_btn1.configure(text_color='black')
        type_btn2.configure(text_color='black')
        type_lbl.configure(text_color='black')
     
#===============    Entries   =====================
url_en= CTkEntry(main_frame,
width=500,
height=30,
placeholder_text=' Enter a video url here',
border_width=2,
border_color='black',
corner_radius=10)
url_en.place(x=156,y=232)
path_en= CTkEntry(main_frame,
width=350,
height=30,
placeholder_text=' Download Folder',
border_width=2,
border_color='black',
corner_radius=10)
path_en.place(x=156,y=270)
#=============== buttons =====================
mode_btn = CTkSegmentedButton(window,values=['Light','Dark'],
selected_color='#239B56',
selected_hover_color='#186A3B',
unselected_color='#922B21',
unselected_hover_color='#641E16',
command=change_mode)
mode_btn.place(x=10,y=5)
down_img= PIL.Image.open(r'icons\\down.png')
down_image= CTkImage(down_img)
down_btn= CTkButton(main_frame,
width=20,
height=26,
text='',
image=down_image,
corner_radius=10,
fg_color='red',
cursor="hand2",
hover=True,
hover_color='#641E16')
down_btn.place(x=661,y=233)
path_img= PIL.Image.open(r'icons\\up.png')
path_image= CTkImage(path_img)
path_btn= CTkButton(main_frame,
text='',
image=path_image,
width=20,
height=26,
corner_radius=10,
fg_color='red',
cursor="hand2",
hover=True,
hover_color='#641E16')
path_btn.place(x=511,y=270)
s = IntVar()
type_btn1= CTkRadioButton(main_frame,
text='Mp4',
radiobutton_height=18,
radiobutton_width=18,
border_width_checked=4,
border_width_unchecked=4,
fg_color='red',
hover_color='#641E16',
hover=True,
variable=s,
value=1,)
type_btn1.place(x=205,y=317)
type_btn2= CTkRadioButton(main_frame,
text='Mp3',
radiobutton_height=18,
radiobutton_width=18,
border_width_checked=4,
border_width_unchecked=4,
fg_color='red',
hover_color='#641E16',
hover=True,
variable=s,
value=2,)
type_btn2.place(x=205,y=345)
#==================    labels    ======================
type_lbl = CTkLabel(main_frame
,text='Type : ',
font=('Rubik',15,'bold'),
text_color='#BDC3C7')
type_lbl.place(x=155,y=312)
#======================================================================
window.mainloop()