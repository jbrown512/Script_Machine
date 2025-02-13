import Parser as Ps
import Modules as Mods
import Script_Machine as Sm
import Gui
import tkinter as tk


def main():
    parser = Ps.Parser()
    gui = Gui.NetworkScannerGUI(tk.Tk())
    script_machine = Sm.Script_Machine()
    
    modules = Mods.Modules(gui, script_machine, parser)

    parser.register(modules)
    gui.register(modules)
    script_machine.register(modules)

    gui.root.mainloop()
    

if __name__ == "__main__":
    main()