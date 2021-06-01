def aslist(data):
    
    """
    convert list of table/view object to lict of dict
    """
    try:
        data = list(data)
        if data == [] or data == None:
            return []
        if hasattr(data[0],"_asdict"):
            return [ i._asdict() for i in data ]
        else:
            return [ dict(i) for i in data ]
    except Exception as e:
        return []