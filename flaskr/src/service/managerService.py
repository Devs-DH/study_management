def get_manager(mgr_id:int,managers:list ):
    return next((mgr for mgr in managers if mgr['mgr_id'] == mgr_id), None )