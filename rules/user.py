def check_accronym(accronym: str, name: str) -> bool:
    accronym = accronym.lower()
    it = iter(name.lower())
    
    if all(a in it for a in accronym):
        return True
    else:
        return False

def check_email(email:str) -> bool:
    if email.lower().endswith("@labmetro.ufsc.br"):
        return True
    else:
        return False