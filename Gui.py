# Tiearra Mable/Storm Summers
# CMSC 495-6380
# GUI - Phase A
# January 18, 2025

# Latest Update: 01/26/2025

"""
Phase A - GUI Development for Network Vulnerability Scanner

This program sets up the GUI with the following functionality:
1. "Start Scan" button calls the Modules object's `receive()` method with "full scan" as input.
2. Ability to receive a 2-dimensional array via `receive()` and display it in the text box.
3. "Clear" button to reset the display.

Placeholders are included for:
- Dropdown menu to select scan type.
- "Stop Scan" and "Save Results" buttons.
- Progress bar to indicate scan status.
"""

import tkinter as tk
from tkinter import ttk

class NetworkScannerGUI:
    def __init__(self, root):
        """
        Initialize the GUI and create widgets.
        """
        self.root = root
        self.root.title("Network Vulnerability Scanner")
        
        # Variables to store scan results
        self.scan_results = []

        # Create and arrange GUI components
        self.create_widgets()

    def create_widgets(self):
        """
        Create GUI components and arrange them in a grid layout.
        """
        # "Start Scan" Button - Full functionality
        self.start_scan_button = tk.Button(self.root, text="Start Scan", command=self.start_scan)
        self.start_scan_button.grid(row=0, column=0, padx=10, pady=10)
        
        # "Clear" Button - Full functionality
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_results)
        self.clear_button.grid(row=0, column=1, padx=10, pady=10)
        
        # "Stop Scan" Button - Placeholder
        self.stop_scan_button = tk.Button(self.root, text="Stop Scan", state=tk.DISABLED)
        self.stop_scan_button.grid(row=0, column=2, padx=10, pady=10)
        
        # "Save Results" Button - Placeholder
        self.save_button = tk.Button(self.root, text="Save Results", state=tk.DISABLED)
        self.save_button.grid(row=0, column=3, padx=10, pady=10)
        
        # Dropdown menu for scan type selection - Placeholder
        self.scan_type_label = tk.Label(self.root, text="Scan Type:")
        self.scan_type_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.scan_type_menu = ttk.Combobox(self.root, values=["Port Scan", "Vulnerability Check"])
        self.scan_type_menu.grid(row=1, column=1, padx=10, pady=5)
        
        # Progress bar - Placeholder
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        
        # Scrollable text box for displaying scan results - Full functionality
        self.results_text_box = tk.Text(self.root, width=60, height=15)
        self.results_text_box.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    def start_scan(self):
        """
        Calls the Modules object's `receive()` method with "full scan" as input.
        """
        if self.module_obj:
            self.module_obj.receive("full scan")
        else:
            self.results_text_box.insert(tk.END, "Modules object not registered.\n")

    def display_results(self):
        """
        Displays scan results in the scrollable text box.
        """
        for row in self.scan_results:
            self.results_text_box.insert(tk.END, "\t".join(row) + "\n")
        self.results_text_box.insert(tk.END, "Scan completed.\n")

    def clear_results(self):
        """
        Clears the results from the text box and resets stored results.
        """
        self.results_text_box.delete(1.0, tk.END)
        self.scan_results = []

    def receive(self, input_data):
        """
        Receives a 2-dimensional array and displays it in the text box.
        """
        self.scan_results = input_data  # Store the 2D array
        for row in self.scan_results:
            self.results_text_box.insert(tk.END, "\t".join(map(str, row)) + "\n")

    def register(self, module_obj):
        """
        Registers an object of the class Modules.
        """
        self.module_obj = module_obj
