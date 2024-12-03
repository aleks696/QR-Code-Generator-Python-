import customtkinter
import qrcode
import qrcode.image.svg

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def generate_qr(text_entry, filename_entry):
    text = text_entry.get().strip()
    filename = filename_entry.get().strip()

    if not text:
        status_label.configure(text="Please enter text for QR Code!", text_color="red")
        return

    if not filename:
        status_label.configure(text="Please enter a file name!", text_color="red")
        return

    if not filename.endswith(".svg"):
        filename += ".svg"

    try:
        factory = qrcode.image.svg.SvgPathImage
        svg_img = qrcode.make(text, image_factory=factory)
        svg_img.save(filename)
        status_label.configure(text=f"QR Code saved as '{filename}'", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="red")

root = customtkinter.CTk()
root.geometry("400x300")
root.title("QR Code Generator")

text_label = customtkinter.CTkLabel(root, text="Enter text for QR Code:")
text_label.pack(pady=5)
text_entry = customtkinter.CTkEntry(root, width=300)
text_entry.pack(pady=5)

filename_label = customtkinter.CTkLabel(root, text="Enter file name (without .svg):")
filename_label.pack(pady=5)
filename_entry = customtkinter.CTkEntry(root, width=300)
filename_entry.pack(pady=5)

button = customtkinter.CTkButton(root,
                   text="Generate QR Code",
                   text_color="white",
                   command=lambda: generate_qr(text_entry, filename_entry))
button.pack(pady=10)

status_label = customtkinter.CTkLabel(root, text="")
status_label.pack(pady=10)

root.mainloop()
