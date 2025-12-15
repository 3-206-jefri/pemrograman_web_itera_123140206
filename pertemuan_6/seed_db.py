from database import init_db, DBSession
from models import Matakuliah
import transaction


def seed():
    init_db()
    session = DBSession()

    # Check if table already has data
    existing = session.query(Matakuliah).count()
    if existing > 0:
        print(f"Terdapat {existing} data. Tidak menambahkan seed.")
        DBSession.remove()
        return

    data = [
        {"kode_mk": "IF101", "nama_mk": "Algoritma dan Pemrograman", "sks": 3, "semester": 1},
        {"kode_mk": "IF102", "nama_mk": "Struktur Data", "sks": 3, "semester": 2},
        {"kode_mk": "IF201", "nama_mk": "Basis Data", "sks": 3, "semester": 3},
    ]

    # Use transaction manager so zope.sqlalchemy can join the transaction
    with transaction.manager:
        for item in data:
            mk = Matakuliah(
                kode_mk=item['kode_mk'],
                nama_mk=item['nama_mk'],
                sks=item['sks'],
                semester=item['semester']
            )
            session.add(mk)

    print("Seed data berhasil ditambahkan.")
    DBSession.remove()


if __name__ == '__main__':
    seed()
