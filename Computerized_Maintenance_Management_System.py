"""This Computerized Maintenance Management System (CMMS) will schedule and track maintenance repairs performed by technicians on the conveyor system. 
Scheduling and tracking preventive and corrective maintenance on various equipment using this CMMS software will ensure that the assets are properly maintained to reduce breakdowns.  
Minimizing breakdowns on the conveyor system will decrease the ratio of bags missed or failed to load on the aircraft due to mechanical or electrical breakdowns on the conveyor system.  
This will ultimately enhance the user experience and improve customer satisfaction when booking flights and traveling with southwest airlines 
as they are confident that their luggage will accompany them on their flight to their destination.  """

# tkinter GUI application creation.  PIL to support images for the application
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Exit application variable
def exitApplication():
    root.destroy()  

# Main application window named root.  This window will have an image, header, multiple labels and buttons to simplify the user experience.
root = tk.Tk()
root.title("COMPUTERIZED MAINTENANCE MANAGEMENT SYSTEM (CMMS)")

# Root window image file path
imagePath = r"C:\Users\shoddeji\Documents\ERMC PC\MISC\Deji\Deji\2024\My Ivy\Software Development Technical Certificate\SDEV220\Final Project\CMMS.png"
image = Image.open(imagePath)

maxWidth = 600
width, height = image.size
if width > maxWidth:
    newWidth = maxWidth
    newHeight = int((newWidth / width) * height)
    image = image.resize((newWidth, newHeight))

# Image object converted to a Tkinter PhotoImage object
tkImage = ImageTk.PhotoImage(image)

# Label widget to display the image
imageLabel = ttk.Label(root, image=tkImage)
imageLabel.pack(pady=15)  

titleLabel = tk.Label(root, text="WORK ORDER REQUEST", font=("Helvetica", 20, "bold"))
titleLabel.pack(pady=20)  



# define variables ConveyorID, Reason, Requester, Labor, Labor Hours, Parts and Work Status.
def conveyorId(value):
    selectedLabel1.config(text=f"Selected: {value}")

def reason(value):
    selectedLabel2.config(text=f"Selected: {value}")
    
def requester(value):
    selectedLabel3.config(text=f"Selected: {value}")
    
def labor(value):
    selectedLabel4.config(text=f"Selected: {value}")

def laborHours(value):
    selectedLabel5.config(text=f"Selected: {value}")

def parts(value):
    selectedLabel6.config(text=f"Selected: {value}")

def workStatus(value):
    selectedLabel7.config(text=f"Selected: {value}")    

    
# Variables buttonClick 1-9 to define selections ConveyorID, Reason, Requester, Work order creation, Labor, Labor Hours, Parts and Work Status.
def buttonClick1():
    return

def buttonClick2():
    return

def buttonClick3():
    return

def buttonClick4():
    return

def buttonClick5():
    return

def buttonClick8():
    return

def buttonClick9():
    return

def buttonClick6():
    conveyorIdVal = selectedOption1.get()
    reasonVal = selectedOption2.get()
    requesterVal = selectedOption3.get()
    laborVal = ()
    laborHoursVal = ()
    partsVal = ()
    workStatusVal = ()

    # Desk Checking - Validate inputs before proceeding 
    if not requesterVal or not conveyorIdVal or not reasonVal:
        tk.messagebox.showerror("Error", "Please complete all fields before submitting.")
        return

        
    # Callback to Maintenance Class
    maintenance = Maintenance(conveyorIdVal, reasonVal, requesterVal, laborVal, laborHoursVal, partsVal, workStatusVal)

    # Work Order creation details in a separate window called results window
    displayResults(maintenance)

    # Second window defined to display work order details.  window titled 'WORK ORDER'
def labor(value):
    global selectedLabel4
    selectedLabel4.config(text=f"Selected: {value}")

def laborHours(value):
    global selectedLabel5
    selectedLabel5.config(text=f"Selected: {value}")

def parts(value):
    global selectedLabel6
    selectedLabel6.config(text=f"Selected: {value}")  
    
def workStatus(value):
    global selectedLabel7
    selectedLabel7.config(text=f"Selected: {value}")  
    


# Button for Conveyor Id Selection
button = ttk.Button(root, text="CONVEYOR ID", command=buttonClick1)
button.pack(pady=20)

# Tuples used to create drop down menu options for conveyor Id selection 
conveyorOptions = ("", "Que (Que Conveyor)", "Transport (Transport Conveyor)", 
                    "PowerTurn (PowerTurn Conveyor)", "Merge (Merge Conveyor)", 
                    "HSD (High Speed Diverter Gen. 1)", "Makeup Unit (Carousel)", 
                    "Transnorm (Transnorm Conveyor)", "HSD II (High Speed Diverter Gen. 2)",
                    "VSU (Vertical Sort Unit)")
selectedOption1 = tk.StringVar(root)
selectedOption1.set(conveyorOptions[0]) 

dropdown = ttk.Combobox(root, textvariable=selectedOption1, values=conveyorOptions, state="readonly")
dropdown.pack(pady=10)
dropdown.bind("<<ComboboxSelected>>", lambda event: conveyorId(selectedOption1.get()))

#Label to display final selection
selectedLabel1 = ttk.Label(root, text="Selected: ")
selectedLabel1.pack(pady=10)



# Dictionary used to create drop down menu options for reason selection 

def reason(selectedKey):

    selectedReason = reasonOptions.get(selectedKey, "Unknown Reason")
    selectedLabel2.config(text=f"Selected: {selectedReason}")

button = ttk.Button(root, text="REASON", command=lambda: reason(selectedOption2.get()))
button.pack(pady=20)

reasonOptions = {
"": "Select a Reason",
"Motor Failure": "Motor Failure",
"Belt Repair/Replacement": "Belt Repair/Replacement",
"Gearbox Repair/Replacement": "Gearbox Repair/Replacement",
"Bearing Replacement": "Bearing Replacement",
"Shaft/Roller Replacement": "Shaft/Roller Replacement",
"Electrical Component Repair": "Electrical Component Repair",
"Mechanical Component Repair": "Mechanical Component Repair"
}
dropdownKeys = list(reasonOptions.keys())

selectedOption2 = tk.StringVar(root)
selectedOption2.set("")
dropdown = ttk.Combobox(root, textvariable=selectedOption2, values=dropdownKeys, state="readonly")
dropdown.pack(pady=10)
dropdown.bind("<<ComboboxSelected>>", lambda event: reason(selectedOption2.get()))


# Label to display the selected option
selectedLabel2 = ttk.Label(root, text="Selected: ")
selectedLabel2.pack(pady=10)


# Tuples used to create drop down menu options for requester selection 
button = ttk.Button(root, text="REQUESTER", command=buttonClick3)
button.pack(pady=20)

requesterOptions = ("", "ML (Mathew Lisecki)", "KG (Kenroy Griffith)", "JC (Josh Crockett)", 
                     "OK (Omar Kiettega)", "WC (Warren Chavon)", "LS (Luis Santiago)", 
                     "MC (Malique Carroll)", "CO (Cermy Oneus)", "KA (Kenneth Ajayi)", 
                     "CW (Christopher Williams)")
selectedOption3 = tk.StringVar(root)
selectedOption3.set(requesterOptions[0])  # Set the default option

# Drop down menu that displays all options 
dropdown = ttk.Combobox(root, textvariable=selectedOption3, values=requesterOptions, state="readonly")
dropdown.pack(pady=10)
dropdown.bind("<<ComboboxSelected>>", lambda event: requester(selectedOption3.get()))

selectedLabel3 = ttk.Label(root, text="Selected: ")
selectedLabel3.pack(pady=10)




# Button to Create Work Order
button = ttk.Button(root, text="CREATE WORK ORDER", command=buttonClick6)
button.pack(pady=20)

options8 = [","]
selectedOption8 = tk.StringVar(root)
selectedOption8.set(options8[0])  


# Button for Exit
button = ttk.Button(root, text="EXIT", command=exitApplication)
button.pack(pady=20)



import random
    
def displayResults(details):
    global selectedLabel4, selectedLabel5, selectedLabel6, selectedLabel7  # Declare as global to use in callbacks
    
    # Second application window named resultWindow.  This window will have an image, header, selections from the root window, multiple labels and buttons to simplify the user experience.
    resultWindow = tk.Toplevel(root)
    resultWindow.title("WORK ORDER")
    resultWindow.geometry("450x1000") 
 
    # Introduce canvas for scrolling, as all items do not fit in one fixed window size
    canvas = tk.Canvas(resultWindow)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Introduce a scrollbar
    scrollbar = ttk.Scrollbar(resultWindow, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a frame inside the canvas
    resultWindow = ttk.Frame(canvas)
    resultWindow.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=resultWindow, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    #   Second image for resultWindow
    imagePath1 = r"C:\Users\shoddeji\Documents\ERMC PC\MISC\Deji\Deji\2024\My Ivy\Software Development Technical Certificate\SDEV220\Final Project\workorder.png"
    image = Image.open(imagePath1)

    maxWidth = 600
    width, height = image.size
    if width > maxWidth:
        newWidth = maxWidth
        newHeight = int((newWidth / width) * height)
        image = image.resize((newWidth, newHeight))

    # Image object converted to a Tkinter PhotoImage object
    global tkImageResult
    tkImageResult = ImageTk.PhotoImage(image)

    # Label widget created to display the image
    imageLabel = ttk.Label(resultWindow, image=tkImageResult)
    imageLabel.image = tkImageResult  
    imageLabel.pack(pady=20)  
    
        # Exit application variable
    def exitApplication():
        resultWindow.destroy()  
    
    # Generate a random number called work order ID to identify the work order
    workOrderId = random.randint(1000, 9999)

    # Display the Work Order ID
    ttk.Label(resultWindow, text=f"Work Order ID: {workOrderId}", font=("Helvetica", 20, "bold")).pack(pady=10)



    # Labels created to display results (conveyorId, reason, requester, labor, laborHours, parts and workStatus)
    conveyorIdLabel = tk.Label(resultWindow, text=f"Conveyor ID: {details.conveyorId}")
    conveyorIdLabel.pack()

    reasonLabel = tk.Label(resultWindow, text=f"Reason: {details.reason}")
    reasonLabel.pack()
    
    requesterLabel = tk.Label(resultWindow, text=f"Requester: {details.requester}")
    requesterLabel.pack()
    
    
    # Redefine values
    def buttonClick7():
        conveyorIdVal = selectedOption1.get()
        reasonVal = selectedOption2.get()
        requesterVal = selectedOption3.get() 
        laborVal = selectedOption4.get()
        laborHoursVal = selectedOption5.get()
        partsVal = selectedOption6.get()
        workStatusVal = selectedOption7.get()
        

    # Array used to create drop down menu options for labor selection 
    
    button = ttk.Button(resultWindow, text="LABOR", command=buttonClick4)
    button.pack(pady=20)

    options4 = ["","ML (Mathew Lisecki)", "KG (Kenroy Griffith)", "JC (Josh Crockett)", "OK (Omar Kiettega)", "WC (Warren Chavon)", "LS (Luis Santiago)", "MC (Malique Carroll)", "CO (Cermy Oneus)","KA (Kenneth Ajayi)", "CW (Christopher Williams)"]
    
    selectedOption4 = tk.StringVar(resultWindow)
    selectedOption4.set(options4[0]) 

    dropdown = ttk.Combobox(resultWindow, textvariable=selectedOption4, values=options4, state="readonly")
    dropdown.pack(pady=10)
    dropdown.bind("<<ComboboxSelected>>", lambda event: labor(selectedOption4.get()))

    selectedLabel4 = ttk.Label(resultWindow, text="Selected: ")
    selectedLabel4.pack(pady=10)



    # Lists used to create drop down menu options for labor hours selection 
    button = ttk.Button(resultWindow, text="LABOR HOURS", command=buttonClick5)
    button.pack(pady=20)

    options5 = ["",".5", "1","1.5", "2","2.5", "3","3.5", "4","4.5", "5","5.5", "6","6.5", "7","7.5", "8"]
    selectedOption5 = tk.StringVar(root)
    selectedOption5.set(options5[0]) 

    dropdown = ttk.Combobox(resultWindow, textvariable=selectedOption5, values=options5, state="readonly")
    dropdown.pack(pady=10)
    dropdown.bind("<<ComboboxSelected>>", lambda event: laborHours(selectedOption5.get()))

    selectedLabel5 = ttk.Label(resultWindow, text="Selected: ")
    selectedLabel5.pack(pady=10)
    


# Dictionary used to create drop down menu options for Parts selection 

    def parts(selectedKey):

        selectedParts = partsOptions.get(selectedKey, "Select Parts")
        selectedLabel6.config(text=f"Selected: {selectedParts}")

    button = ttk.Button(resultWindow, text="PARTS", command=buttonClick8)
    button.pack(pady=20)

    partsOptions = {
    "": "Select a Part",
    "ELECTRIC MOTOR": "ELECTRIC MOTOR",
    "GEARBOX ASSEMBLY": "GEARBOX ASSEMBLY",
    "CONVEYOR BELTING": "CONVEYOR BELTING",
    "ROLLER/SHAFT ASSEMBLY": "ROLLER/SHAFT ASSEMBLY",
    "BEARINGS": "BEARINGS"
    }
    dropdownKeys = list(partsOptions.keys())

    selectedOption6 = tk.StringVar(resultWindow)
    selectedOption6.set("")
    dropdown = ttk.Combobox(root, textvariable=selectedOption6, values=dropdownKeys, state="readonly")
    dropdown.pack(pady=10)
    dropdown.bind("<<ComboboxSelected>>", lambda event: parts(selectedOption6.get()))


    # Label to display the selected option
    selectedLabel6 = ttk.Label(resultWindow, text="Selected: ")
    selectedLabel6.pack(pady=10)

    options6 = ["","ELECTRIC MOTOR","GEARBOX ASSEMBLY","CONVEYOR BELTING","ROLLER/SHAFT ASSEMBLY", "BEARINGS"]
    selectedOption6 = tk.StringVar(resultWindow)
    selectedOption6.set(options6[0]) 

    dropdown = ttk.Combobox(resultWindow, textvariable=selectedOption6, values=options6, state="readonly")
    dropdown.pack(pady=10)
    dropdown.bind("<<ComboboxSelected>>", lambda event: parts(selectedOption6.get()))

    selectedLabel6 = ttk.Label(resultWindow, text="Selected: ")
    selectedLabel6.pack(pady=10)



    # Lists used to create drop down menu options for work status selection 
    button = ttk.Button(resultWindow, text="WORK STATUS", command=buttonClick7)
    button.pack(pady=20)

    options7 = ["","ON-HOLD","IN PROGRESS","COMPLETED"]
    selectedOption7 = tk.StringVar(resultWindow)
    selectedOption7.set(options7[0])  

    dropdown = ttk.Combobox(resultWindow, textvariable=selectedOption7, values=options7, state="readonly")
    dropdown.pack(pady=10)
    dropdown.bind("<<ComboboxSelected>>", lambda event: workStatus(selectedOption7.get()))

    selectedLabel7 = ttk.Label(resultWindow, text="Selected: ")
    selectedLabel7.pack(pady=10)
    
    
    
    # Introduce a text window to input detailed reports from assigned maintenance task 
    ttk.Label(resultWindow, text="Add Comments:").pack(pady=10)
    commentText = tk.Text(resultWindow, height=5, width=50)
    commentText.pack(pady=10)
    


    # Redefine values
    def submitComments():
        comments = commentText.get("1.0", tk.END).strip()  
        conveyorIdVal = selectedOption1.get()
        reasonVal = selectedOption2.get()
        requesterVal = selectedOption3.get()
        laborVal = selectedOption4.get()
        laborHoursVal = selectedOption5.get()
        partsVal = selectedOption6.get()
        workStatusVal = selectedOption7.get()
        
        # Desk Checking - Validate inputs before proceeding 
        if not laborVal or not laborHoursVal or not partsVal or not workStatusVal:
            tk.messagebox.showerror("Error", "Please complete all fields before submitting.")
            return
        
        # Third application window named resultSummary.  This window will have an image, header, selections from the root window and result window.
        resultSummary = tk.Toplevel(root)
        resultSummary.title("WORK ORDER SUMMARY")
        resultSummary.geometry("450x1200") 
        
                # Exit application variable
        def exitApplication():
            resultSummary.destroy()  
        

        #   Image for resultSummary
        imagePath2 = r"C:\Users\shoddeji\Documents\ERMC PC\MISC\Deji\Deji\2024\My Ivy\Software Development Technical Certificate\SDEV220\Final Project\workordersummary.png"
        image = Image.open(imagePath2)

        maxWidth = 400
        width, height = image.size
        if width > maxWidth:
            newWidth = maxWidth
            newHeight = int((newWidth / width) * height)
            image = image.resize((newWidth, newHeight))
            
            # Image object converted to a Tkinter PhotoImage object
            global tkImageResult
            tkImageResult = ImageTk.PhotoImage(image)

            # Label widget created to display the image
            imageLabel = ttk.Label(resultSummary, image=tkImageResult)
            imageLabel.image = tkImageResult  
            imageLabel.pack(pady=20)  
            

        #Work order details selected from the root and resultWindow displayed in the resultSummary window
        ttk.Label(resultSummary, text="WORK ORDER SUMMARY", font=("Helvetica", 18, "bold")).pack(pady=20)
        ttk.Label(resultSummary, text=f"Work Order#: {workOrderId}").pack(pady=10)        
        ttk.Label(resultSummary, text=f"Requester: {requesterVal}").pack(pady=10)
        ttk.Label(resultSummary, text=f"Conveyor ID: {conveyorIdVal}").pack(pady=10)
        ttk.Label(resultSummary, text=f"Reason: {reasonVal}").pack(pady=10)
        ttk.Label(resultSummary, text=f"Labor: {laborVal}").pack(pady=10)
        ttk.Label(resultSummary, text=f"Labor Hours: {laborHoursVal}").pack(pady=10)
        ttk.Label(resultSummary, text=f"Parts: {partsVal}").pack(pady=10)
        ttk.Label(resultSummary, text=f"Comments: {comments}").pack(pady=10)
        ttk.Label(resultSummary, text=f"Work Status: {workStatusVal}").pack(pady=10)
        
                # Button for Exit
        button = ttk.Button(resultSummary, text="EXIT", command=exitApplication)
        button.pack(pady=20)


    # Submit work order button to open result summary window
    ttk.Button(resultWindow, text="Submit Work Order", command=submitComments).pack(pady=20)
    
    # Button for Exit
    button = ttk.Button(resultWindow, text="EXIT", command=exitApplication)
    button.pack(pady=20)
    
    






#Maintenance Class created to establish (conveyorId, reason, requester, labor, laborHours, parts, workStatus)
class Maintenance:
    def __init__(self, conveyorId, reason, requester, labor, laborHours, parts, workStatus):
        self.conveyorId = conveyorId
        self.reason = reason
        self.requester = requester
        self.labor = labor
        self.laborHours = laborHours
        self.parts = parts
        self.workStatus = workStatus

    def get_conveyorId(self):
        return self.conveyorId
    
    def get_reason(self):
        return self.reason
    
    def get_requester(self):
        return self.requester
    
    def get_labor(self):
        return self.labor
    
    def get_laborHours(self):
        return self.laborHours
    
    def get_parts(self):
        return self.parts
    
    def get_workStatus(self):
        return self.workStatus

    def set_conveyorId(self, conveyorId):
        self.conveyorId = conveyorId
    
    def set_reason(self, reason):
        self.reason = reason
    
    def set_requester(self, requester):
        self.requester = requester
        
    def set_labor(self, labor):
        self.labor = labor
        
    
    def set_laborHours(self, laborHours):
        self.laborHours = laborHours
        
    def set_workStatus(self, workStatus):
        self.workStatus = workStatus


# Run the main event loop
root.mainloop()