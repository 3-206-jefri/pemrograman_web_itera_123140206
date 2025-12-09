from pyramid.view import view_config
from pyramid.response import Response
from .models import Matakuliah
import json

@view_config(route_name='get_all_matakuliah', renderer='json')
def get_all_matakuliah(request):
    """Get all matakuliah"""
    try:
        matakuliahs = request.db.query(Matakuliah).all()
        return {
            'status': 'success',
            'matakuliahs': [mk.to_dict() for mk in matakuliahs]
        }
    except Exception as e:
        request.response.status = 500
        return {
            'status': 'error',
            'message': str(e)
        }

@view_config(route_name='get_matakuliah', renderer='json')
def get_matakuliah(request):
    """Get single matakuliah by id"""
    try:
        mk_id = int(request.matchdict['id'])
        matakuliah = request.db.query(Matakuliah).filter(Matakuliah.id == mk_id).first()
        
        if not matakuliah:
            request.response.status = 404
            return {
                'status': 'error',
                'message': 'Matakuliah tidak ditemukan'
            }
        
        return {
            'status': 'success',
            'matakuliah': matakuliah.to_dict()
        }
    except ValueError:
        request.response.status = 400
        return {
            'status': 'error',
            'message': 'ID harus berupa angka'
        }
    except Exception as e:
        request.response.status = 500
        return {
            'status': 'error',
            'message': str(e)
        }

@view_config(route_name='create_matakuliah', renderer='json')
def create_matakuliah(request):
    """Create new matakuliah"""
    try:
        data = request.json_body
        
        # Validasi input
        required_fields = ['kode_mk', 'nama_mk', 'sks', 'semester']
        for field in required_fields:
            if field not in data:
                request.response.status = 400
                return {
                    'status': 'error',
                    'message': f'Field {field} harus diisi'
                }
        
        # Cek apakah kode_mk sudah ada
        existing = request.db.query(Matakuliah).filter(
            Matakuliah.kode_mk == data['kode_mk']
        ).first()
        
        if existing:
            request.response.status = 400
            return {
                'status': 'error',
                'message': 'Kode matakuliah sudah ada'
            }
        
        # Buat matakuliah baru
        matakuliah = Matakuliah(
            kode_mk=data['kode_mk'],
            nama_mk=data['nama_mk'],
            sks=int(data['sks']),
            semester=int(data['semester'])
        )
        
        request.db.add(matakuliah)
        request.db.commit()
        request.db.refresh(matakuliah)
        
        request.response.status = 201
        return {
            'status': 'success',
            'message': 'Matakuliah berhasil ditambahkan',
            'matakuliah': matakuliah.to_dict()
        }
    except KeyError as e:
        request.response.status = 400
        return {
            'status': 'error',
            'message': f'Field tidak valid: {str(e)}'
        }
    except Exception as e:
        request.db.rollback()
        request.response.status = 500
        return {
            'status': 'error',
            'message': str(e)
        }

@view_config(route_name='update_matakuliah', renderer='json')
def update_matakuliah(request):
    """Update existing matakuliah"""
    try:
        mk_id = int(request.matchdict['id'])
        data = request.json_body
        
        matakuliah = request.db.query(Matakuliah).filter(Matakuliah.id == mk_id).first()
        
        if not matakuliah:
            request.response.status = 404
            return {
                'status': 'error',
                'message': 'Matakuliah tidak ditemukan'
            }
        
        # Update fields jika ada dalam request
        if 'kode_mk' in data:
            # Cek apakah kode_mk baru sudah dipakai oleh matakuliah lain
            existing = request.db.query(Matakuliah).filter(
                Matakuliah.kode_mk == data['kode_mk'],
                Matakuliah.id != mk_id
            ).first()
            
            if existing:
                request.response.status = 400
                return {
                    'status': 'error',
                    'message': 'Kode matakuliah sudah digunakan'
                }
            
            matakuliah.kode_mk = data['kode_mk']
        
        if 'nama_mk' in data:
            matakuliah.nama_mk = data['nama_mk']
        
        if 'sks' in data:
            matakuliah.sks = int(data['sks'])
        
        if 'semester' in data:
            matakuliah.semester = int(data['semester'])
        
        request.db.commit()
        request.db.refresh(matakuliah)
        
        return {
            'status': 'success',
            'message': 'Matakuliah berhasil diupdate',
            'matakuliah': matakuliah.to_dict()
        }
    except ValueError:
        request.response.status = 400
        return {
            'status': 'error',
            'message': 'ID atau nilai numerik tidak valid'
        }
    except Exception as e:
        request.db.rollback()
        request.response.status = 500
        return {
            'status': 'error',
            'message': str(e)
        }

@view_config(route_name='delete_matakuliah', renderer='json')
def delete_matakuliah(request):
    """Delete matakuliah"""
    try:
        mk_id = int(request.matchdict['id'])
        
        matakuliah = request.db.query(Matakuliah).filter(Matakuliah.id == mk_id).first()
        
        if not matakuliah:
            request.response.status = 404
            return {
                'status': 'error',
                'message': 'Matakuliah tidak ditemukan'
            }
        
        request.db.delete(matakuliah)
        request.db.commit()
        
        return {
            'status': 'success',
            'message': 'Matakuliah berhasil dihapus'
        }
    except ValueError:
        request.response.status = 400
        return {
            'status': 'error',
            'message': 'ID harus berupa angka'
        }
    except Exception as e:
        request.db.rollback()
        request.response.status = 500
        return {
            'status': 'error',
            'message': str(e)
        }