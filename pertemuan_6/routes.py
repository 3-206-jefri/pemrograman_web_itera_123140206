def includeme(config):
    """Configure routes"""
    # GET all matakuliah
    config.add_route('get_all_matakuliah', '/api/matakuliah', request_method='GET')
    
    # GET single matakuliah
    config.add_route('get_matakuliah', '/api/matakuliah/{id}', request_method='GET')
    
    # POST new matakuliah
    config.add_route('create_matakuliah', '/api/matakuliah', request_method='POST')
    
    # PUT update matakuliah
    config.add_route('update_matakuliah', '/api/matakuliah/{id}', request_method='PUT')
    
    # DELETE matakuliah
    config.add_route('delete_matakuliah', '/api/matakuliah/{id}', request_method='DELETE')