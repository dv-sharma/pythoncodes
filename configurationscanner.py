#def validateconfig(configstr)
    
def validator(configstr):
    configlist=configstr.split('|')
    configdict={}
    barcodes=set()

    for config in configlist:
       cleanconfig=config.strip()
       if not (cleanconfig.isalnum() and len(cleanconfig)==14):
        return "Invalid Configuration"
       ordinal=cleanconfig[0:4]
       barcode=cleanconfig[4::]
       if ordinal=='0000':
           return "Invalid Configuration"
       if ordinal in configdict:
           return "Invalid Configuration"
       
       if barcode in barcodes:
          return "Invalid Configuration"
       configdict[ordinal]=barcode
       barcodes.add(barcode)
       
    finallist=[]
    for finalvals in sorted(configdict):
       finallist.append(configdict[finalvals])
    return finallist
       
        
        
        
if __name__== '__main__':
    str='0002f7c22e7904 | 000176a3a4d214 | 000305d29f4a4b'
    str2="0002f7c22e7904 | 000176a3a4d214 | 000205d29f4a4b"
    print(validator(str))
    #validateconfig(str)
