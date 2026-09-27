import tkinter as tk
from tkinter import ttk, messagebox
from src.config import APP_NAME, DEFAULT_LENGTH, MIN_LENGTH, MAX_LENGTH
from src.generator import generate_password
from src.strength import password_strength

class PasswordGeneratorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_NAME)
        self.root.geometry("680x520")
        self.root.minsize(620, 470)
        self.length=tk.IntVar(value=DEFAULT_LENGTH); self.upper=tk.BooleanVar(value=True)
        self.lower=tk.BooleanVar(value=True); self.digits=tk.BooleanVar(value=True)
        self.special=tk.BooleanVar(value=True); self.show_password=tk.BooleanVar(value=True)
        self.password=tk.StringVar(); self.status=tk.StringVar(value="Ready")
        self._build()

    def _build(self):
        r=self.root; r.configure(padx=24,pady=20)
        ttk.Label(r,text="🔐 Secure Password Generator",font=("Segoe UI",22,"bold")).pack(anchor="w")
        ttk.Label(r,text="Create strong passwords locally. Nothing is uploaded.").pack(anchor="w",pady=(2,18))
        card=ttk.LabelFrame(r,text="Generated Password",padding=16); card.pack(fill="x")
        self.entry=ttk.Entry(card,textvariable=self.password,font=("Consolas",18)); self.entry.pack(side="left",fill="x",expand=True,padx=(0,10))
        ttk.Button(card,text="📋 Copy",command=self.copy_password).pack(side="right")
        sf=ttk.Frame(r); sf.pack(fill="x",pady=12)
        self.strength_label=ttk.Label(sf,text="Strength: —",font=("Segoe UI",11,"bold")); self.strength_label.pack(side="left")
        self.progress=ttk.Progressbar(sf,maximum=100,length=220); self.progress.pack(side="right")
        opt=ttk.LabelFrame(r,text="Password Options",padding=16); opt.pack(fill="x",pady=4)
        row=ttk.Frame(opt); row.pack(fill="x"); ttk.Label(row,text="Length:").pack(side="left")
        ttk.Spinbox(row,from_=MIN_LENGTH,to=MAX_LENGTH,textvariable=self.length,width=7).pack(side="left",padx=8)
        ttk.Label(row,text=f"({MIN_LENGTH}-{MAX_LENGTH})").pack(side="left")
        checks=ttk.Frame(opt); checks.pack(fill="x",pady=(14,0))
        for text,var in [("Uppercase (A-Z)",self.upper),("Lowercase (a-z)",self.lower),("Numbers (0-9)",self.digits),("Special characters",self.special)]:
            ttk.Checkbutton(checks,text=text,variable=var).pack(anchor="w")
        actions=ttk.Frame(r); actions.pack(fill="x",pady=18)
        ttk.Button(actions,text="🔄 Generate Password",command=self.generate).pack(side="left",ipadx=12,ipady=5)
        ttk.Checkbutton(actions,text="Show password",variable=self.show_password,command=self.toggle_visibility).pack(side="right")
        ttk.Separator(r).pack(fill="x",pady=(2,10)); ttk.Label(r,textvariable=self.status).pack(anchor="w")
        ttk.Label(r,text="Security: generated with Python's secrets module.").pack(anchor="w",pady=(8,0))
        self.generate()

    def generate(self):
        try:
            p=generate_password(int(self.length.get()),self.upper.get(),self.lower.get(),self.digits.get(),self.special.get())
            self.password.set(p); label,score=password_strength(p)
            self.strength_label.config(text=f"Strength: {label}"); self.progress["value"]=score; self.status.set("Password generated locally.")
        except (ValueError,tk.TclError) as e: messagebox.showerror("Invalid options",str(e))

    def copy_password(self):
        if self.password.get():
            self.root.clipboard_clear(); self.root.clipboard_append(self.password.get()); self.root.update()
            self.status.set("Password copied to clipboard.")

    def toggle_visibility(self):
        self.entry.config(show="" if self.show_password.get() else "•")

    def run(self): self.root.mainloop()
