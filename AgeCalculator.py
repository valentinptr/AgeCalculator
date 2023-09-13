def age_calculator(date: str) -> int:
    import datetime

    today = datetime.date.today()

    try:
        if (len(date) != 10) | (date[2] != "/") | (date[5] != "/") | (type(int(date[0:2])) != int) | (
                type(int(date[3:5])) != int) | (type(int(date[6:])) != int) | (
                not ((int(date[0:2]) > 0) & (int(date[0:2]) <= 31))) | (
                not ((int(date[3:5]) > 0) & (int(date[3:5]) <= 12))) | (
                not ((int(date[6:]) > 1900) & (int(date[6:]) < datetime.date.today().year))):
            print('Formats de date non correct')
            return -1
        else:
            mois: int = int(date[3:5])
            annee: int = int(date[6:])

            cal_annee: int = today.year - annee
            cal_mois = today.month - mois

            if cal_mois < 0:
                cal_annee -= 1

            return cal_annee

    except ValueError:
        print('Format de date non correct')
        return -2


calAnnee: int = age_calculator("01/12/1925")
if calAnnee >= 0:
    print(f'{calAnnee} ans')
