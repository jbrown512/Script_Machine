class Host:
    def __init__(self):
        self.ports = []
        self.ip_address = None
        self.vendor = None

    def add_port(self, port):
        if port:
            self.ports.append(port)
        else:
            raise Exception("Port object cannot be None.")

    def set_ip_address(self, address):
        if address:
            self.ip_address = address
        else:
            raise Exception("ip_address cannot be None.")
        
    def set_vendor(self, vendor):
        self.vendor = vendor

    def get_ports(self):
        return self.ports
    
    def get_ip_address(self):
        if self.ip_address:
            return self.ip_address
        
        return "unknown"
    
    def get_vendor(self):
        if self.vendor:
            return self.vendor
        
        return "unknown"

    def to_string(self):
        return "HOST IP ADDRESS: " + self.get_ip_address() + \
            "\nVENDOR: " + self.get_vendor() + \
            "\n\n"