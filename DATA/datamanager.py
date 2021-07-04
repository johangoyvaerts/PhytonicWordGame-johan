from DATA.database import dbconn

class Datamanager :

    #
    # FILMS
    #


    # TONEN

    def alle_woorden(self):
        with dbconn() as cur :
            sql = "SELECT * FROM woorden.woorden_met_B"
            cur.execute (sql)
            rijen = cur.fetchall()
            woorden = [rij for rij in rijen]
            return woorden

    def woord_by_id(self, id):
        with dbconn() as cur :
            sql = "SELECT * FROM woorden WHERE id = ?"
            cur.execute (sql, [id])
            rij = cur.fetchone()
            if rij :
                woord = rij[1]
                return woord
            else :
                return None

    def woord_by_zoekterm(self, zoekterm):
        with dbconn() as cur :
            zkterm =f"%{zoekterm}%"
            sql = "SELECT * FROM woorden WHERE woord LIKE ?"
            cur.execute (sql, [zkterm])
            rij = cur.fetchone()
            if rij :
                woord = rij[1]
                return woord
            else :
                return None




    # toevoegen woord

    def woord_toevoegen (self, woord,toevoegsel):
        
        with dbconn() as cur :
            tabel=f"woorden_met_{toevoegsel}"
            sql = f"INSERT INTO {tabel} (woord) VALUES (?)"
            cur.execute(sql,[woord])
"""
    # verwijderen FILM

    def film_verwijderen_by_id (self,id):
        with dbconn() as cur :
            if id :
                sql = "DELETE FROM films WHERE id = ?"
                cur.execute(sql,[id])
            else :
                raise ValueError

    def film_verwijderen_by_MDB_id (self,MDB_id):
        with dbconn() as cur :
            if id :
                sql = "DELETE FROM films WHERE MDB_id = ?"
                cur.execute(sql,[MDB_id])
            else :
                raise ValueError

    def set_film_KT_by_id(self,id):
        with dbconn() as cur :
            sql = "UPDATE films SET knt = 'KT' WHERE id = ?"
            cur.execute (sql, [id])

    def set_film_KNT_by_id(self,id):
        with dbconn() as cur :
            sql = "UPDATE films SET knt = 'KNT' WHERE id = ?"
            cur.execute (sql, [id])

    #
    # VERTONINGEN
    #

    # TONEN

    def alle_vertoningen(self):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id ORDER BY vertoningen.zaal, vertoningen.uur"
            cur.execute (sql)
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen

    def alle_actieve_vertoningen(self):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.vertoning_actief = 'AC' ORDER BY vertoningen.zaal, vertoningen.uur"
            cur.execute (sql)
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen

    def alle_niet_actieve_vertoningen(self):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.vertoning_actief = 'NA'"
            cur.execute (sql)
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen

    def alle_2D_vertoningen(self):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.drie_d = '2D'"
            cur.execute (sql)
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen

    def alle_3D_vertoningen(self):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.drie_d = '3D'"
            cur.execute (sql)
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen
    
    def alle_vertoningen_by_zaal(self,zaal):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.zaal = ?"
            cur.execute (sql, [zaal])
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen

    def vertoning_by_id(self,id):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.id = ?"
            cur.execute (sql, [id])
            rij = cur.fetchone()
            if rij :
                vertoning = Vertoning.from_dict(rij)
                return vertoning
            else :
                return None

    def vertoning_by_film_id_zaal_uur(self,film_id,zaal,uur):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.films_id = ? AND vertoningen.zaal = ? AND vertoningen.uur = ? "
            cur.execute (sql, [film_id, zaal, uur])
            rij = cur.fetchone()
            if rij :
                vertoning = Vertoning.from_dict(rij)
                return vertoning
            else :
                return None

    def vertoning_by_film_id(self,id):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.films_id = ?"
            cur.execute (sql, [id])
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen

    def vertoning_actief_by_film_id(self,id):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.vertoning_actief = 'AC' and vertoningen.films_id = ?"
            cur.execute (sql, [id])
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen
#            if rij :
#                vertoning = Vertoning.from_dict(rij)
#                return vertoning
#            else :
#                return None    
            
    #
    #  VERTONINGEN bewerken
    #

    def set_vertoning_actief_by_id(self,id):
        with dbconn() as cur :
            sql = "UPDATE vertoningen SET vertoning_actief = 'AC' WHERE id = ?"
            cur.execute (sql, [id])

    def set_vertoning_non_actief_by_id(self,id):
        with dbconn() as cur :
            sql = "UPDATE vertoningen SET vertoning_actief = 'NA' WHERE id = ?"
            cur.execute (sql, [id])

    def vertoning_verwijderen_by_id (self,id):
        with dbconn() as cur :
            if id :
                sql = "DELETE FROM vertoningen WHERE id = ?"
                cur.execute(sql,[id])
            else :
                raise ValueError

    def vertoning_toevoegen (self, vertoning):
        with dbconn() as cur :
            sql = "INSERT INTO vertoningen (zaal, uur, drie_d, vertoning_actief, films_id) VALUES (?,?,?,?,?)"
            cur.execute(sql,[vertoning.zaal, vertoning.uur, vertoning.drie_d, vertoning.vertoning_actief, vertoning.film.id])

    def set_vertoning_3D_by_id(self,id):
        with dbconn() as cur :
            sql = "UPDATE vertoningen SET drie_d = '3D' WHERE id = ?"
            cur.execute (sql, [id])

    def set_vertoning_2D_by_id(self,id):
        with dbconn() as cur :
            sql = "UPDATE vertoningen SET drie_d = '2D' WHERE id = ?"
            cur.execute (sql, [id])


#           
#   TICKETS
#

    # tonen

    def alle_tickets(self):
        with dbconn() as cur :
            sql = "SELECT tickets.*, vertoningen.*, films.* FROM tickets INNER JOIN vertoningen, films ON tickets.vertoningen_id = vertoningen.id AND vertoningen.films_id = films.id"
            cur.execute (sql)
            rijen = cur.fetchall()
            tickets = [Ticket.from_dict(rij) for rij in rijen]
            return tickets

    def tickets_tss_data(self, datumlaag, datumhoog):
        with dbconn() as cur :
            sql = "SELECT tickets.*, vertoningen.*, films.* FROM tickets INNER JOIN vertoningen, films ON tickets.vertoningen_id = vertoningen.id AND vertoningen.films_id = films.id WHERE tickets.datum > ? AND tickets.datum <= ?"
            cur.execute (sql,[datumlaag,datumhoog])
            rijen = cur.fetchall()
            tickets = [Ticket.from_dict(rij) for rij in rijen]
            return tickets

    def tickets_film_tss_data(self, datumlaag, datumhoog, film_id):
        with dbconn() as cur :
            sql = "SELECT tickets.*, vertoningen.*, films.* FROM tickets INNER JOIN vertoningen, films ON tickets.vertoningen_id = vertoningen.id AND vertoningen.films_id = films.id WHERE tickets.datum > ? AND tickets.datum <= ? AND films.id = ?"
            cur.execute (sql,[datumlaag,datumhoog,film_id])
            rijen = cur.fetchall()
            tickets = [Ticket.from_dict(rij) for rij in rijen]
            return tickets

    def tickets_vandaag(self, datum):
        with dbconn() as cur :
            sql = "SELECT tickets.*, vertoningen.*, films.* FROM tickets INNER JOIN vertoningen, films ON tickets.vertoningen_id = vertoningen.id AND vertoningen.films_id = films.id WHERE tickets.datum = ? "
            cur.execute (sql,[datum])
            rijen = cur.fetchall()
            tickets = [Ticket.from_dict(rij) for rij in rijen]
            return tickets

    def tickets_by_film_id(self, id):
        with dbconn() as cur :
            sql = "SELECT tickets.*, vertoningen.*, films.* FROM tickets INNER JOIN vertoningen, films ON tickets.vertoningen_id = vertoningen.id AND vertoningen.films_id = films.id WHERE films.id = ? "
            cur.execute (sql,[id])
            rijen = cur.fetchall()
            tickets = [Ticket.from_dict(rij) for rij in rijen]
            return tickets

    def tickets_by_vertoning_id(self, id):
        with dbconn() as cur :
            sql = "SELECT tickets.*, vertoningen.*, films.* FROM tickets INNER JOIN vertoningen, films ON tickets.vertoningen_id = vertoningen.id AND vertoningen.films_id = films.id WHERE tickets.vertoningen_id = ? "
            cur.execute (sql,[id])
            rijen = cur.fetchall()
            tickets = [Ticket.from_dict(rij) for rij in rijen]
            return tickets

    def ticket_by_id(self,id):
        with dbconn() as cur :
            sql = "SELECT tickets.*, vertoningen.*, films.* FROM tickets INNER JOIN vertoningen, films ON tickets.vertoningen_id = vertoningen.id AND vertoningen.films_id = films.id WHERE tickets.id = ?"
            cur.execute (sql, [id])
            rij = cur.fetchone()
            if rij :
                ticket = Ticket.from_dict(rij)
                return ticket
            else :
                return None

    def ticket_toevoegen (self, ticket):
        with dbconn() as cur :
            sql = "INSERT INTO tickets (datum, prijs_volw, prijs_kind, aant_volw, aant_kind, vertoningen_id) VALUES (?,?,?,?,?,?)"
            cur.execute(sql,[ticket.datum, ticket.prijs_volw, ticket.prijs_kind, ticket.aant_volw, ticket.aant_kind, ticket.vertoning.id])

    def ticket_verwijderen_by_id (self,id):
        with dbconn() as cur :
            if id :
                sql = "DELETE FROM tickets WHERE id = ?"
                cur.execute(sql,[id])
            else :
                raise ValueError 


    """