from datetime import datetime


def paint(obiekt_funkcyjny):
    def opakowanie():
        przed_wywolaniem = datetime.now()
        wynik = obiekt_funkcyjny()
        po_wywolaniu = datetime.now()
        print(f'wywloanie zajelo mi: {po_wywolaniu - przed_wywolaniem}')
        return wynik

    return opakowanie

@paint
def cos_robie():
    a = [x for x in range(50000)]
    return a


@paint
def jednak_nic_nie_robie():
    print('lazy')


print(cos_robie())
jednak_nic_nie_robie()