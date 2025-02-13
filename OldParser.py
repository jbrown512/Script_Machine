# Jeffrey Brown
# CMSC 495-6380
# Parser - Phase A
# January 27, 2025

# Latest Update: 01/27/2025


import xmltodict
import Port as Pt
import os


# Parses an .xml file created by NMap and creats a list of Port objects
class Parser:
    def __init__(self):
        self._ports_list = []
        self._modules = None
        self._net_address = None

    def _parse(self, file_name):
        self._ports_list = []
        try:
            with open(file_name, "rb") as file:
                dict_ = xmltodict.parse(file)
                print(dict_)
        except:
            raise Exception("Parse function failed to load file.")
            
        try:
            for item in dict_["address"][1]:
                port = Pt.Port(item["@protocol"], item["@portid"], item["state"]["@state"])

                if "service" in item:
                    port.set_service(item["service"]["@name"])

                self._ports_list.append(port)
        except:
            raise Exception("Parser failed to parse file. Please verify file is correctly formatted.")
        
        try:
            os.remove(file_name)
        except:
            raise Exception("Parser failed to remove file " + file_name + ". Please remove file manually.")

        if not self._is_validated():
            raise Exception("Parser failed to parse file. Please verify file is correctly formatted.")
        
    
    def get_ports_list(self):
        return self._ports_list
    
    
    def get_ports_table(self):
        table = []

        table.append(Pt.Port.HEADERS)

        for item in self._ports_list:    
            table.append(item.get_table())

        return table
    
    
    def _is_validated(self):
        for item in self._ports_list:
            if not item.is_validated():
                return False
        
        return True
    

    def register(self, modules):
        self._modules = modules
    

    def receive(self, file_name, process):
        self._parse(file_name)

        self._modules.receive(self.get_ports_table())