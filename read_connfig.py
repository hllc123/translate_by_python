class data_config():
    config_dict={}
    @classmethod     
    def get_data_config(cls):    
        with open("config.txt","r",encoding="utf-8") as f:
            config_data = f.read()
       
        for line in config_data.split("\n"):
            if line.strip() and not line.startswith("#"): 
                key,value = line.split("=")
                cls.config_dict[key.strip()] = value.strip()  
        