def creeazaRezervare(id, nume, clasa, pret, checkin):
    '''
    Creeaza o noua rezervare
    :param id: id-ul pe care s-a facut rezervarea
    :param nume: numele persoanei care a facut rezervarea
    :param clasa: clasa la care este facuta rezervarea
    :param pret: pretul rezervarii
    :param checkin: checkin
    :return: o noua rezervare
    '''
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin
    }
    def get_id(rezervare):
    return rezervare['id']

def get_nume(rezervare):
    return rezervare['nume']

def get_clasa(rezervare):
    return rezervare['clasa']

def get_pret(rezervare):
    return rezervare['pret']

def get_checkin(rezervare):
    return rezervare['checkin']

def get_id(rezervare):
    return rezervare[0]

def get_nume(rezervare):
    return rezervare[1]

def get_clasa(rezervare):
    return rezervare[2]

def get_pret(rezervare):
    return rezervare[3]

def get_checkin(rezervare):
    return rezervare[4]

def toString(rezervare):
    return "Id {}, Nume {}, Clasa {}, Pret {}, Check-in {}".format(
        get_id(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare),
    )

def set_pret(rezervare,pret):
    rezervare[3]=pret