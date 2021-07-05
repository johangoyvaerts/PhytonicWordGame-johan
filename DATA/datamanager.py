from DATA.database import dbconn

class Datamanager :



#    def alle_woorden_alle_tabellen(self,toevoegsel):
#        with dbconn() as cur :
#            tabelnaam = f"woorden_met_{toevoegsel.upper()}"
#            sql = f"SELECT * FROM {tabelnaam}"
#            cur.execute(sql)
#            rijen=cur.fetchall()
#            woorden=[rij for rij in rijen]
#            return woorden
#
#
#    def woord_by_zoekterm(self, zoekterm,toevoegsel):
#        with dbconn() as cur :
#            tabelnaam = f"woorden_met_{toevoegsel.upper()}"
#            zkterm =f"{zoekterm}"
#            sql = f"SELECT * FROM {tabelnaam} WHERE woord LIKE ?"
#            cur.execute (sql, [zkterm])
#            rij = cur.fetchone()
#            if rij :
#                woord = rij[1]
#                return woord
#            else :
#                return None
#
#    def check_by_zoekterm(self, zoekterm,toevoegsel):
#        with dbconn() as cur :
#            tabelnaam = f"woorden_met_{toevoegsel.upper()}"
#            zkterm =f"{zoekterm}"
#            sql = f"SELECT * FROM {tabelnaam} WHERE woord LIKE ?"
#            cur.execute (sql, [zkterm])
#            rij = cur.fetchone()
#            if rij :
#                return True
#            else :
#                return False

    def check_by_zoekterm_alle_woorden(self, zoekterm):
        with dbconn() as cur :
            sql = f"SELECT * FROM woorden WHERE woord LIKE ?"
            cur.execute (sql, [zoekterm])
            rij = cur.fetchone()
            if rij :
                return True
            else :
                return False


    # toevoegen woord

#    def woord_toevoegen (self, woord, toevoegsel):
#        
#        with dbconn() as cur :
#            tabel=f"woorden_met_{toevoegsel}"
#            sql = f"INSERT INTO {tabel} (woord) VALUES (?)"
#            cur.execute(sql,[woord])
#
    def woord_toevoegen_aan_woorden_met_id (self, woord):
        with dbconn() as cur :
            #tabel=f"woorden_met_{toevoegsel}"
            sql = f"INSERT INTO woorden_met_id (woord) VALUES (?)"
            cur.execute(sql,[woord])
    
    def woord_toevoegen_aan_woorden (self, woord):
        with dbconn() as cur :
            sql = f"INSERT INTO woorden (woord) VALUES (?)"
            cur.execute(sql,[woord])
