from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import pyramid_tm
from database import DBSession, init_db

@view_config(route_name='home', renderer='json')
def home(request):
    """Home endpoint"""
    return {
        'message': 'Selamat datang di API Manajemen Matakuliah',
        'endpoints': {
            'GET /api/matakuliah': 'Get all matakuliah',
            'GET /api/matakuliah/{id}': 'Get single matakuliah',
            'POST /api/matakuliah': 'Create matakuliah',
            'PUT /api/matakuliah/{id}': 'Update matakuliah',
            'DELETE /api/matakuliah/{id}': 'Delete matakuliah'
        }
    }

def main():
    """Configure and return WSGI application"""
    
    # Initialize database
    init_db()
    
    # Create configuration
    config = Configurator()
    
    # Add transaction manager
    config.include('pyramid_tm')
    
    # Configure routes
    config.add_route('home', '/')
    config.add_route('get_all_matakuliah', '/api/matakuliah', request_method='GET')
    config.add_route('get_matakuliah', '/api/matakuliah/{id}', request_method='GET')
    config.add_route('create_matakuliah', '/api/matakuliah', request_method='POST')
    config.add_route('update_matakuliah', '/api/matakuliah/{id}', request_method='PUT')
    config.add_route('delete_matakuliah', '/api/matakuliah/{id}', request_method='DELETE')
    
    # Scan for view configurations
    config.scan()
    
    return config.make_wsgi_app()

if __name__ == '__main__':
    from waitress import serve
    app = main()
    print("Server berjalan di http://localhost:6543")
    print("Tekan Ctrl+C untuk stop")
    serve(app, host='0.0.0.0', port=6543)