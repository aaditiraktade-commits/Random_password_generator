import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string
import pyperclip


# ==========================================
# 1. PASSWORD GENERATION FUNCTION
# ==========================================

def generate_password(length, selected_types, exclude_similar):
    character_groups = {
        "uppercase": string.ascii_uppercase,
        "lowercase": string.ascii_lowercase,
        "numbers": string.digits,
        "symbols": string.punctuation
    }

    similar_characters = "0O1lI"

    groups = []

    for option in selected_types:
        group = character_groups[option]

        if exclude_similar:
            group = "".join(
                char for char in group
                if char not in similar_characters
            )

        if group:
            groups.append(group)

    if len(groups) < 2:
        raise ValueError("Select at least two character types.")

    if length < 8:
        raise ValueError("Minimum password length is 8.")

    if length < len(groups):
        raise ValueError("Password length is too short.")

    # Guarantee one character from each selected group
    password_list = [
        secrets.choice(group) for group in groups
    ]

    all_characters = "".join(groups)

    # Fill remaining positions
    while len(password_list) < length:
        password_list.append(
            secrets.choice(all_characters)
        )

    # Shuffle characters securely
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)


# ==========================================
# 2. PASSWORD STRENGTH CHECKER
# ==========================================

def check_password_strength(password):
    if not password:
        return "NOT GENERATED", 0

    score = 0

    if len(password) >= 8:
        score += 20

    if len(password) >= 12:
        score += 15

    if len(password) >= 16:
        score += 15

    if any(c.isupper() for c in password):
        score += 15

    if any(c.islower() for c in password):
        score += 15

    if any(c.isdigit() for c in password):
        score += 10

    if any(c in string.punctuation for c in password):
        score += 10

    if score >= 75:
        return "STRONG", 100

    elif score >= 50:
        return "MEDIUM", 65

    else:
        return "WEAK", 30


# ==========================================
# 3. MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("Random Password Generator")
root.geometry("700x900")
root.minsize(450, 550)
root.configure(bg="#202A44")


# ==========================================
# 4. SCROLLABLE WINDOW
# ==========================================

canvas = tk.Canvas(
    root,
    bg="#202A44",
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    root,
    orient="vertical",
    command=canvas.yview
)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

main_frame = tk.Frame(
    canvas,
    bg="#202A44"
)

window_id = canvas.create_window(
    (0, 0),
    window=main_frame,
    anchor="nw"
)


def update_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))


def resize_frame(event):
    canvas.itemconfig(window_id, width=event.width)


main_frame.bind("<Configure>", update_scroll_region)
canvas.bind("<Configure>", resize_frame)


# ==========================================
# 5. TITLE
# ==========================================

title = tk.Label(
    main_frame,
    text="Random Password Generator",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#202A44"
)

title.pack(pady=25)

subtitle = tk.Label(
    main_frame,
    text="Create your secure password!",
    font=("Arial", 13),
    fg="white",
    bg="#202A44"
)

subtitle.pack(pady=10)


# ==========================================
# 6. PASSWORD LENGTH
# ==========================================

tk.Label(
    main_frame,
    text="Enter Password Length:",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#202A44"
).pack(pady=10)

length_var = tk.IntVar(value=12)

length_spinbox = tk.Spinbox(
    main_frame,
    from_=8,
    to=128,
    textvariable=length_var,
    font=("Arial", 13),
    width=12
)

length_spinbox.pack(pady=5)


# ==========================================
# 7. CHARACTER TYPE CHECKBOXES
# ==========================================

tk.Label(
    main_frame,
    text="Select Character Types:",
    font=("Arial", 15, "bold"),
    fg="white",
    bg="#202A44"
).pack(pady=20)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

checkbox_style = {
    "font": ("Arial", 12),
    "fg": "white",
    "bg": "#202A44",
    "activebackground": "#202A44",
    "activeforeground": "white",
    "selectcolor": "#202A44"
}

tk.Checkbutton(
    main_frame,
    text="Uppercase Letters (A-Z)",
    variable=uppercase_var,
    **checkbox_style
).pack(pady=5)

tk.Checkbutton(
    main_frame,
    text="Lowercase Letters (a-z)",
    variable=lowercase_var,
    **checkbox_style
).pack(pady=5)

tk.Checkbutton(
    main_frame,
    text="Numbers (0-9)",
    variable=numbers_var,
    **checkbox_style
).pack(pady=5)

tk.Checkbutton(
    main_frame,
    text="Symbols (!@#$)",
    variable=symbols_var,
    **checkbox_style
).pack(pady=5)


# ==========================================
# 8. EXTRA OPTIONS
# ==========================================

exclude_var = tk.BooleanVar(value=False)

tk.Checkbutton(
    main_frame,
    text="Exclude Similar Characters (0, O, 1, l, I)",
    variable=exclude_var,
    **checkbox_style
).pack(pady=12)


# ==========================================
# 9. PASSWORD OUTPUT
# ==========================================

tk.Label(
    main_frame,
    text="Your Generated Password:",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#202A44"
).pack(pady=15)

password_var = tk.StringVar()

password_output = tk.Entry(
    main_frame,
    textvariable=password_var,
    font=("Arial", 13),
    justify="center",
    width=35,
    show=""
)

password_output.pack(pady=8)

show_var = tk.BooleanVar(value=True)


def toggle_password():
    if show_var.get():
        password_output.config(show="")
    else:
        password_output.config(show="*")


tk.Checkbutton(
    main_frame,
    text="Show Password",
    variable=show_var,
    command=toggle_password,
    **checkbox_style
).pack(pady=8)


# ==========================================
# 10. STATUS MESSAGE
# ==========================================

status_var = tk.StringVar(value="")

status_label = tk.Label(
    main_frame,
    textvariable=status_var,
    font=("Arial", 11, "bold"),
    fg="#4ADE80",
    bg="#202A44"
)

status_label.pack(pady=8)


# ==========================================
# 11. PASSWORD STRENGTH INDICATOR
# ==========================================

strength_var = tk.StringVar(
    value="Password Strength: NOT GENERATED"
)

strength_label = tk.Label(
    main_frame,
    textvariable=strength_var,
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#202A44"
)

strength_label.pack(pady=15)

strength_bar = ttk.Progressbar(
    main_frame,
    orient="horizontal",
    length=350,
    mode="determinate",
    maximum=100
)

strength_bar.pack(pady=8)


# ==========================================
# 12. PASSWORD HISTORY
# ==========================================

password_history = []

tk.Label(
    main_frame,
    text="Password History",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#202A44"
).pack(pady=25)

tk.Label(
    main_frame,
    text="Your last 5 generated passwords:",
    font=("Arial", 11),
    fg="white",
    bg="#202A44"
).pack(pady=5)

history_listbox = tk.Listbox(
    main_frame,
    font=("Arial", 11),
    width=38,
    height=6,
    selectmode=tk.SINGLE
)

history_listbox.pack(pady=10)


# ==========================================
# 13. COPY TO CLIPBOARD FUNCTION
# ==========================================

def copy_to_clipboard(password):
    if not password:
        messagebox.showwarning(
            "Warning",
            "Generate a password first!"
        )
        return False

    try:
        pyperclip.copy(password)
    except Exception:
        try:
            root.clipboard_clear()
            root.clipboard_append(password)
            root.update()
        except Exception:
            messagebox.showerror(
                "Clipboard Error",
                "Unable to copy password."
            )
            return False

    return True


# ==========================================
# 14. GENERATE PASSWORD FUNCTION
# ==========================================

def generate():
    try:
        length = int(length_var.get())

        if length < 8 or length > 128:
            messagebox.showerror(
                "Invalid Length",
                "Enter a length between 8 and 128."
            )
            return

    except (ValueError, tk.TclError):
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid password length."
        )
        return

    selected_types = []

    if uppercase_var.get():
        selected_types.append("uppercase")

    if lowercase_var.get():
        selected_types.append("lowercase")

    if numbers_var.get():
        selected_types.append("numbers")

    if symbols_var.get():
        selected_types.append("symbols")

    if len(selected_types) < 2:
        messagebox.showerror(
            "Selection Error",
            "Please select at least two character types."
        )
        return

    try:
        password = generate_password(
            length,
            selected_types,
            exclude_var.get()
        )

    except ValueError as error:
        messagebox.showerror("Error", str(error))
        return

    # Display password
    password_var.set(password)

    # Automatically copy password
    copied = copy_to_clipboard(password)

    if copied:
        status_var.set(
            "Password generated and copied successfully!"
        )
    else:
        status_var.set(
            "Password generated. Clipboard copy failed."
        )

    # Calculate strength
    strength, score = check_password_strength(password)

    strength_var.set(
        f"Password Strength: {strength}"
    )

    strength_bar["value"] = score

    # Add to history
    password_history.insert(0, password)

    # Keep only last five passwords
    if len(password_history) > 5:
        password_history.pop()

    # Update history listbox
    history_listbox.delete(0, tk.END)

    for item in password_history:
        history_listbox.insert(tk.END, item)


# ==========================================
# 15. GENERATE PASSWORD BUTTON
# ==========================================

generate_button = tk.Button(
    main_frame,
    text="Generate Password",
    command=generate,
    font=("Arial", 14, "bold"),
    bg="#22C55E",
    fg="white",
    activebackground="#16A34A",
    width=22,
    pady=10
)

generate_button.pack(pady=15)


# ==========================================
# 16. COPY PASSWORD BUTTON
# ==========================================

def copy_password():
    password = password_var.get()

    if copy_to_clipboard(password):
        status_var.set("Password copied successfully!")


copy_button = tk.Button(
    main_frame,
    text="Copy Password",
    command=copy_password,
    font=("Arial", 12, "bold"),
    bg="#06B6D4",
    fg="white",
    width=16
)

copy_button.pack(pady=8)


# ==========================================
# 17. CLEAR PASSWORD FUNCTION
# ==========================================

def clear_password():
    password_var.set("")
    strength_var.set("Password Strength: NOT GENERATED")
    strength_bar["value"] = 0
    status_var.set("")

    password_output.config(show="")

    show_var.set(True)


clear_button = tk.Button(
    main_frame,
    text="Clear",
    command=clear_password,
    font=("Arial", 12, "bold"),
    bg="#EF4444",
    fg="white",
    width=12
)

clear_button.pack(pady=8)


# ==========================================
# 18. COPY SELECTED HISTORY PASSWORD
# ==========================================

def copy_selected():
    selection = history_listbox.curselection()

    if not selection:
        messagebox.showwarning(
            "Selection",
            "Please select a password from history."
        )
        return

    password = history_listbox.get(selection[0])

    if copy_to_clipboard(password):
        status_var.set("Selected password copied!")


copy_selected_button = tk.Button(
    main_frame,
    text="Copy Selected",
    command=copy_selected,
    font=("Arial", 11, "bold"),
    bg="#06B6D4",
    fg="white",
    width=16
)

copy_selected_button.pack(pady=8)


# ==========================================
# 19. CLEAR HISTORY FUNCTION
# ==========================================

def clear_history():
    password_history.clear()
    history_listbox.delete(0, tk.END)

    status_var.set("Password history cleared.")


clear_history_button = tk.Button(
    main_frame,
    text="Clear History",
    command=clear_history,
    font=("Arial", 11, "bold"),
    bg="#EF4444",
    fg="white",
    width=16
)

clear_history_button.pack(pady=8)


# ==========================================
# 20. FOOTER
# ==========================================

footer = tk.Label(
    main_frame,
    text="Create Strong Passwords | Stay Secure!",
    font=("Arial", 10, "italic"),
    fg="white",
    bg="#202A44"
)

footer.pack(pady=25)


# ==========================================
# 21. RUN APPLICATION
# ==========================================

root.mainloop()